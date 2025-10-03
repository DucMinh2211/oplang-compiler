"""
AST Generation module for OPLang programming language.
This module contains the ASTGeneration class that converts parse trees
into Abstract Syntax Trees using the visitor pattern.
"""

from functools import reduce
from build.OPLangVisitor import OPLangVisitor
from build.OPLangParser import OPLangParser
from src.utils.nodes import *


class ASTGeneration(OPLangVisitor):

    def visitProgram(self, ctx:OPLangParser.ProgramContext) -> Program:
        self._classes: list[str] = []
        return Program(self.visit(ctx.classDeclList()))

    def visitClassDeclList(self, ctx: OPLangParser.ClassDeclListContext) -> list[ClassDecl]:
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.classDecl())] 
        return [self.visit(ctx.classDecl())] + self.visit(ctx.classDeclList())

    def visitClassDecl(self, ctx: OPLangParser.ClassDeclContext) -> ClassDecl:
        self._classes.append(ctx.ID().getText())
        return ClassDecl(
            name=ctx.ID().getText(),
            superclass = self.visit(ctx.classExtends()),
            members = self.visit(ctx.memberNulist()),
        )

    def visitClassExtends(self, ctx: OPLangParser.ClassExtendsContext) -> Optional[Identifier]:
        if ctx.getChildCount() == 0:
            return None
        return ctx.ID().getText()

    def visitMemberNulist(self, ctx: OPLangParser.MemberNulistContext) -> list[AttributeDecl | MethodDecl]:
        if ctx.getChildCount() == 0:
            return []
        return [self.visit(ctx.member())] + self.visit(ctx.memberNulist())

    def visitMember(self, ctx: OPLangParser.MemberContext) -> ConstructorDecl | AttributeDecl | MethodDecl:
        if ctx.constructor():
            return self.visit(ctx.constructor())
        elif ctx.attributeDecl():
            return self.visit(ctx.attributeDecl())
        else:
            return self.visit(ctx.methodDecl())

    def visitAttributeDecl(self, ctx: OPLangParser.AttributeDeclContext) -> AttributeDecl:
        return AttributeDecl(
            is_static=True if ctx.STATIC() else False,
            is_final=True if ctx.FINAL() else False,
            attr_type=self.visit(ctx.typeRef()),
            attributes=self.visit(ctx.attributeNameList())
        )

    def visitAttributeNameList(self, ctx: OPLangParser.AttributeNameListContext) -> list[Attribute]:
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.attributeName())]
        return [self.visit(ctx.attributeName())] + self.visit(ctx.attributeNameList())

    def visitAttributeName(self, ctx: OPLangParser.AttributeNameContext) -> Attribute:
        if ctx.getChildCount() == 1:
            return Attribute( name=ctx.ID().getText() )
        return Attribute(
            name=ctx.ID().getText(),
            init_value=self.visit(ctx.expr0())
        )

    def visitMethodDecl(self, ctx: OPLangParser.MethodDeclContext) -> MethodDecl:
        return MethodDecl(
            is_static=True if ctx.STATIC() else False,
            name=ctx.ID().getText(),
            return_type=self.visit(ctx.typeRef()),
            params=self.visit(ctx.paramNulist()),
            body=self.visit(ctx.blockStatement())
        )

    def visitParamNulist(self, ctx: OPLangParser.ParamNulistContext) -> list[Parameter]:
        if ctx.paramPrime():
            return self.visit(ctx.paramPrime())
        return []

    def visitParamPrime(self, ctx: OPLangParser.ParamPrimeContext) -> list[Parameter]:
        if not ctx.paramPrime():
            return self.visit(ctx.param())
        return self.visit(ctx.param()) + self.visit(ctx.paramPrime())

    def visitParam(self, ctx: OPLangParser.ParamContext) -> list[Parameter]:
        return list(map(lambda id: Parameter(self.visit(ctx.typeRef()), id.name), self.visit(ctx.idList())))

    def visitIsFinal(self, ctx: OPLangParser.IsFinalContext) -> bool:
        return ctx.FINAL()



    def visitConstructor(self, ctx: OPLangParser.ConstructorContext) -> ConstructorDecl | DestructorDecl:
        if ctx.destructor():
            destructor_ctx = ctx.destructor()
            return DestructorDecl(
                name=destructor_ctx.ID().getText(),
                body=self.visit(destructor_ctx.blockStatement())
            )
        
        params = []
        body = None
        name = None
        constructor_ctx = None

        if ctx.defConstructor():
            constructor_ctx = ctx.defConstructor()
            name = constructor_ctx.ID().getText()
        elif ctx.copyConstructor():
            constructor_ctx = ctx.copyConstructor()
            name = constructor_ctx.ID(0).getText()
            param_type = ClassType(constructor_ctx.ID(1).getText())
            params = [Parameter(param_type, 'other')]
        elif ctx.customConstructor():
            constructor_ctx = ctx.customConstructor()
            name = constructor_ctx.ID().getText()
            params = self.visit(constructor_ctx.paramNulist())

        body = self.visit(constructor_ctx.blockStatement())

        return ConstructorDecl(
            name=name,
            params=params,
            body=body
        )

    def visitBlockStatement(self, ctx: OPLangParser.BlockStatementContext) -> BlockStatement:
        return BlockStatement(
                var_decls=self.visit(ctx.varDeclNulist()),
                statements=self.visit(ctx.stmtNulist())
        )

    def visitVarDeclNulist(self, ctx: OPLangParser.VarDeclNulistContext) -> list[VariableDecl]:
        if ctx.varDecl():
            return [self.visit(ctx.varDecl())] + self.visit(ctx.varDeclNulist())
        return []

    def visitVarDecl(self, ctx: OPLangParser.VarDeclContext) -> VariableDecl:
        return VariableDecl(
                    is_final=self.visit(ctx.isFinal()),
                    var_type=self.visit(ctx.typeRef()),
                    variables=self.visit(ctx.variableNameList()),
                )

    def visitVariableNameList(self, ctx: OPLangParser.VariableNameListContext) -> list[Variable]:
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.variableName())]
        return [self.visit(ctx.variableName())] + self.visit(ctx.variableNameList())

    def visitVariableName(self, ctx: OPLangParser.VariableNameContext):
        return Variable(
            name=ctx.ID().getText(),
            init_value=self.visit(ctx.expr0()) if ctx.expr0() else None
        )

    def visitStmtNulist(self, ctx: OPLangParser.StmtNulistContext) -> list[Statement]:
        if not ctx.stmt(): return []
        return [self.visit(ctx.stmt())] + self.visit(ctx.stmtNulist())

    def visitStmt(self, ctx: OPLangParser.StmtContext) -> Statement:
        if ctx.ifStmt():
            return self.visit(ctx.ifStmt())
        elif ctx.forStmt():
            return self.visit(ctx.forStmt())
        elif ctx.breakStmt():
            return self.visit(ctx.breakStmt())
        elif ctx.continueStmt():
            return self.visit(ctx.continueStmt())
        elif ctx.returnStmt():
            return self.visit(ctx.returnStmt())
        elif ctx.methodInvoStmt():
            return self.visit(ctx.methodInvoStmt())
        elif ctx.blockStatement():
            return self.visit(ctx.blockStatement())
        assert ctx.assignStmt()
        return self.visit(ctx.assignStmt())

    def visitAssignStmt(self, ctx: OPLangParser.AssignStmtContext) -> AssignmentStatement:
        return AssignmentStatement(
            lhs=self.visit(ctx.lhs()),
            rhs=self.visit(ctx.expr0())
        )

    def visitLhs(self, ctx: OPLangParser.LhsContext) -> LHS:
        if not ctx.arrayAccessExpr():
            return IdLHS(name=ctx.ID().getText())
        return PostfixLHS(postfix_expr=self.visit(ctx.arrayAccessExpr()))

    def visitIfStmt(self, ctx: OPLangParser.IfStmtContext) -> IfStatement:
        then_stmt = self.visit(ctx.stmt(0))
        else_stmt = self.visit(ctx.stmt(1)) if len(ctx.stmt()) > 1 else None
        return IfStatement(
            condition=self.visit(ctx.expr0()),
            then_stmt=then_stmt,
            else_stmt=else_stmt
        )

    def visitForStmt(self, ctx: OPLangParser.ForStmtContext) -> ForStatement:
        dir = None
        if ctx.TO():
            dir = ctx.TO().getText()
        else: dir = ctx.DOWNTO().getText()
        return ForStatement(
            variable=ctx.ID().getText(),
            start_expr=self.visit(ctx.expr0()[0]),
            direction=dir,
            end_expr=self.visit(ctx.expr0()[1]),
            body=self.visit(ctx.stmt())
        )

    def visitBreakStmt(self, ctx: OPLangParser.BreakStmtContext) -> BreakStatement:
        return BreakStatement()

    def visitContinueStmt(self, ctx: OPLangParser.ContinueStmtContext) -> ContinueStatement:
        return ContinueStatement()

    def visitReturnStmt(self, ctx: OPLangParser.ReturnStmtContext) -> ReturnStatement:
        return ReturnStatement(value=self.visit(ctx.expr0()))

    def visitMethodInvoStmt(self, ctx: OPLangParser.MethodInvoStmtContext) -> MethodInvocationStatement:
        method_call = self.visit(ctx.methodInvocation()) # This is a MethodCall node

        if ctx.ID(): # e.g., ID.methodInvocation()
            lhs_name = ctx.ID().getText()
            if lhs_name == "io" or lhs_name in self._classes: # All io methods are static
                return MethodInvocationStatement(
                    method_invocation=StaticMethodInvocation(
                        class_name=lhs_name,
                        method_name=method_call.method_name,
                        args=method_call.args
                    )
                )
            else: # General case for ID.methodInvocation() (instance method call)
                lhs = Identifier(lhs_name)
                expr = PostfixExpression(primary=lhs, postfix_ops=[method_call])
                return MethodInvocationStatement(method_invocation=MethodInvocation(postfix_expr=expr))
        elif ctx.THIS(): # e.g., this.methodInvocation()
            lhs = ThisExpression()
            expr = PostfixExpression(primary=lhs, postfix_ops=[method_call])
            return MethodInvocationStatement(method_invocation=MethodInvocation(postfix_expr=expr))
        else: # e.g., methodInvocation() (direct method call)
            implicit_this = ThisExpression()
            expr = PostfixExpression(primary=implicit_this, postfix_ops=[method_call])
            return MethodInvocationStatement(method_invocation=MethodInvocation(postfix_expr=expr))

    def visitMethodInvocation(self, ctx: OPLangParser.MethodInvocationContext) -> MethodCall:
        return MethodCall(
            method_name=ctx.ID().getText(),
            args=self.visitExprNulist(ctx.exprNulist())
        )

    def visitExprNulist(self, ctx: OPLangParser.ExprNulistContext) -> list[Expr]:
        if not ctx.exprPrime():
            return []
        return self.visitExprPrime(ctx.exprPrime())

    def visitExprPrime(self, ctx: OPLangParser.ExprPrimeContext):
        if not ctx.exprPrime():
            return [self.visit(ctx.expr0())]
        return [self.visit(ctx.expr0())] + self.visit(ctx.exprPrime())

    def visitExpr0(self, ctx: OPLangParser.Expr0Context) -> Expr:
        if ctx.getChildCount() == 1:
            return self.visit(ctx.relationalExpr()[0])
        return BinaryOp(
            left=self.visit(ctx.relationalExpr()[0]),
            operator=ctx.CMP_WITH_OP().getText(),
            right=self.visit(ctx.relationalExpr()[1])
        )

    def visitRelationalExpr(self, ctx: OPLangParser.RelationalExprContext) -> Expr:
        if ctx.getChildCount() == 1:
            return self.visit(ctx.logicalExpr()[0])
        return BinaryOp(
            left=self.visit(ctx.logicalExpr()[0]),
            operator=ctx.CMP_OP().getText(),
            right=self.visit(ctx.logicalExpr()[1])
        )

    def visitLogicalExpr(self, ctx: OPLangParser.LogicalExprContext) -> Expr:
        if ctx.getChildCount() == 1:
            return self.visit(ctx.addSubExpr())
        return BinaryOp(
            left=self.visit(ctx.logicalExpr()),
            operator=ctx.AND_OR_OP().getText(),
            right=self.visit(ctx.addSubExpr())
        )

    def visitAddSubExpr(self, ctx: OPLangParser.AddSubExprContext) -> Expr:
        if ctx.getChildCount() == 1:
            return self.visit(ctx.mulDivModExpr())
        return BinaryOp(
            left=self.visit(ctx.addSubExpr()),
            operator=ctx.ADD_SUB_OP().getText(),
            right=self.visit(ctx.mulDivModExpr())
        )

    def visitMulDivModExpr(self, ctx: OPLangParser.MulDivModExprContext) -> Expr:
        if ctx.getChildCount() == 1:
            return self.visit(ctx.strConcatExpr())
        return BinaryOp(
            left=self.visit(ctx.mulDivModExpr()),
            operator=ctx.MUL_DIV_MOD_OP().getText(),
            right=self.visit(ctx.strConcatExpr())
        )

    def visitStrConcatExpr(self, ctx: OPLangParser.StrConcatExprContext) -> Expr:
        if ctx.getChildCount() == 1:
            return self.visit(ctx.logicalNotExpr())
        return BinaryOp(
            left=self.visit(ctx.strConcatExpr()),
            operator=ctx.STR_CONCAT_OP().getText(),
            right=self.visit(ctx.logicalNotExpr())
        )

    def visitLogicalNotExpr(self, ctx: OPLangParser.LogicalNotExprContext) -> Expr:
        if ctx.getChildCount() == 1:
            return self.visit(ctx.unaryAddSubExpr())
        return UnaryOp(
            operator=ctx.NOT().getText(),
            operand=self.visit(ctx.logicalNotExpr())
        )

    def visitUnaryAddSubExpr(self, ctx: OPLangParser.UnaryAddSubExprContext) -> Expr:
        if ctx.getChildCount() == 1:
            return self.visit(ctx.arrayAccessExpr())
        return UnaryOp(
            operator=ctx.ADD_SUB_OP().getText(),
            operand=self.visit(ctx.unaryAddSubExpr())
        )

    def visitArrayAccessExpr(self, ctx: OPLangParser.ArrayAccessExprContext) -> Expr:
        if ctx.getChildCount() == 1:
            return self.visit(ctx.memberAccessExpr())

        lhs = self.visit(ctx.arrayAccessExpr())
        op = ArrayAccess(index=self.visit(ctx.arrayAccess()))

        if isinstance(lhs, PostfixExpression):
            lhs.postfix_ops.insert(0, op)
            return lhs
        
        return PostfixExpression(primary=lhs, postfix_ops=[op])

    def visitMemberAccessExpr(self, ctx: OPLangParser.MemberAccessExprContext) -> Expr:
        if ctx.getChildCount() == 1:
            return self.visit(ctx.fact())

        lhs = self.visit(ctx.memberAccessExpr())

        if ctx.methodInvocation():
            op = self.visit(ctx.methodInvocation())
        else:
            op = MemberAccess(member_name=ctx.ID().getText())

        if isinstance(lhs, PostfixExpression):
            lhs.postfix_ops.append(op)
            return lhs
        
        return PostfixExpression(primary=lhs, postfix_ops=[op])

    def visitFact(self, ctx: OPLangParser.FactContext)-> Expr:
        if ctx.ID():
            return Identifier(name=ctx.ID().getText())
        elif ctx.THIS():
            return ThisExpression()
        elif ctx.methodInvocation():
            return self.visit(ctx.methodInvocation())
        elif ctx.objCreation():
            return self.visit(ctx.objCreation())
        elif ctx.expr0():
            return ParenthesizedExpression(expr=self.visit(ctx.expr0()))
        elif ctx.literals():
            return (self.visit(ctx.literals()))

        assert ctx.NIL(), "ctx not NIL"
        return NilLiteral()

    def visitObjCreation(self, ctx: OPLangParser.ObjCreationContext):
        return ObjectCreation(
            class_name=ctx.ID().getText(),
            args=self.visit(ctx.exprNulist())
        )

    def visitLiterals(self, ctx:OPLangParser.LiteralsContext):
        if ctx.INTEGER_LITERAL():
            return IntLiteral(value=int(ctx.INTEGER_LITERAL().getText()))
        elif ctx.FLOAT_LITERAL():
            return FloatLiteral(value=float(ctx.FLOAT_LITERAL().getText()))
        elif ctx.BOOLEAN_LITERAL():
            return BoolLiteral(value=True if ctx.BOOLEAN_LITERAL().getText() == "true" else False)
        elif ctx.STRING_LITERAL():
            return StringLiteral(value=ctx.STRING_LITERAL().getText())
        else:
            return self.visit(ctx.arrayLiteral())

    def visitArrayLiteral(self, ctx: OPLangParser.ArrayLiteralContext) -> ArrayLiteral:
        if ctx.floatArray():
            return self.visit(ctx.floatArray())
        elif ctx.intArray():
            return self.visit(ctx.intArray())
        elif ctx.boolArray():
            return self.visit(ctx.boolArray())
        elif ctx.strArray():
            return self.visit(ctx.strArray())
        elif ctx.idArray():
            return self.visit(ctx.idArray())
        else:
            # Empty array literal
            return ArrayLiteral([])

    def visitFloatArray(self, ctx: OPLangParser.FloatArrayContext) -> ArrayLiteral:
        elements = self.visit(ctx.floatNulist()) if ctx.floatNulist() else []
        return ArrayLiteral(elements)

    def visitIntArray(self, ctx: OPLangParser.IntArrayContext) -> ArrayLiteral:
        elements = self.visit(ctx.intNulist()) if ctx.intNulist() else []
        return ArrayLiteral(elements)

    def visitBoolArray(self, ctx: OPLangParser.BoolArrayContext) -> ArrayLiteral:
        elements = self.visit(ctx.boolNulist()) if ctx.boolNulist() else []
        return ArrayLiteral(elements)

    def visitStrArray(self, ctx: OPLangParser.StrArrayContext) -> ArrayLiteral:
        elements = self.visit(ctx.strNulist()) if ctx.strNulist() else []
        return ArrayLiteral(elements)

    def visitIdArray(self, ctx: OPLangParser.IdArrayContext) -> ArrayLiteral:
        elements = self.visit(ctx.idNulist()) if ctx.idNulist() else []
        return ArrayLiteral(elements)

    def visitFloatNulist(self, ctx: OPLangParser.FloatNulistContext) -> List[FloatLiteral]:
        if ctx.floatPrime():
            return self.visit(ctx.floatPrime())
        return []

    def visitIntNulist(self, ctx: OPLangParser.IntNulistContext) -> List[IntLiteral]:
        if ctx.intPrime():
            return self.visit(ctx.intPrime())
        return []

    def visitBoolNulist(self, ctx: OPLangParser.BoolNulistContext) -> List[BoolLiteral]:
        if ctx.boolPrime():
            return self.visit(ctx.boolPrime())
        return []

    def visitStrNulist(self, ctx: OPLangParser.StrNulistContext) -> List[StringLiteral]:
        if ctx.strPrime():
            return self.visit(ctx.strPrime())
        return []

    def visitIdNulist(self, ctx: OPLangParser.IdNulistContext) -> List[Identifier]:
        if ctx.idPrime():
            return self.visit(ctx.idPrime())
        return []

    def visitFloatPrime(self, ctx: OPLangParser.FloatPrimeContext) -> List[FloatLiteral]:
        if ctx.floatPrime():
            return [FloatLiteral(float(ctx.FLOAT_LITERAL().getText()))] + self.visit(ctx.floatPrime())
        return [FloatLiteral(float(ctx.FLOAT_LITERAL().getText()))]

    def visitIntPrime(self, ctx: OPLangParser.IntPrimeContext) -> List[IntLiteral]:
        if ctx.intPrime():
            return [IntLiteral(int(ctx.INTEGER_LITERAL().getText()))] + self.visit(ctx.intPrime())
        return [IntLiteral(int(ctx.INTEGER_LITERAL().getText()))]

    def visitBoolPrime(self, ctx: OPLangParser.BoolPrimeContext) -> List[BoolLiteral]:
        if ctx.boolPrime():
            return [BoolLiteral(ctx.BOOLEAN_LITERAL().getText() == "true")] + self.visit(ctx.boolPrime())
        return [BoolLiteral(ctx.BOOLEAN_LITERAL().getText() == "true")]

    def visitStrPrime(self, ctx: OPLangParser.StrPrimeContext) -> List[StringLiteral]:
        if ctx.strPrime():
            return [StringLiteral(ctx.STRING_LITERAL().getText())] + self.visit(ctx.strPrime())
        return [StringLiteral(ctx.STRING_LITERAL().getText())]

    def visitIdPrime(self, ctx: OPLangParser.IdPrimeContext) -> List[Identifier]:
        if ctx.idPrime():
            return [Identifier(ctx.ID().getText())] + self.visit(ctx.idPrime())
        return [Identifier(ctx.ID().getText())]

    def visitArrayAccess(self, ctx: OPLangParser.ArrayAccessContext) -> Expr:
        return self.visit(ctx.expr0())

    def visitTypeRef(self, ctx: OPLangParser.TypeRefContext) -> ReferenceType:
        return ReferenceType(self.visit(ctx.type_())) if ctx.AMPERSAND() else self.visit(ctx.type_())

    def visitType(self, ctx: OPLangParser.TypeContext) -> Type:
        if ctx.VOID():
            return PrimitiveType(ctx.VOID().getText())

        type_name = ""
        is_class_type = False
        if ctx.INT():
            type_name = ctx.INT().getText()
        elif ctx.FLOAT():
            type_name = ctx.FLOAT().getText()
        elif ctx.BOOLEAN():
            type_name = ctx.BOOLEAN().getText()
        elif ctx.STRING():
            type_name = ctx.STRING().getText()
        elif ctx.ID():
            type_name = ctx.ID().getText()
            is_class_type = True
        
        element_type = ClassType(type_name) if is_class_type else PrimitiveType(type_name)

        if is_class_type: self._classes.append(type_name)

        arr_decl: OPLangParser.ArrayDeclContext = ctx.arrayDecl()
        if arr_decl.getChildCount() == 0:
            return element_type

        return ArrayType(
            element_type=element_type,
            size=int(arr_decl.INTEGER_LITERAL().getText())
        )

    def visitIdList(self, ctx: OPLangParser.IdListContext) -> list[Identifier]:
        if not ctx.idList():
            return [Identifier(ctx.ID().getText())]
        return [Identifier(ctx.ID().getText())] + self.visit(ctx.idList())
