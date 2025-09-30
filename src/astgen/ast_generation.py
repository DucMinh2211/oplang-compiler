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
        return Program(self.visit(ctx.classDeclList()))

    def visitClassDeclList(self, ctx: OPLangParser.ClassDeclListContext) -> list[ClassDecl]:
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.classDecl())] 
        return [self.visit(ctx.classDecl())] + self.visit(ctx.classDeclList())

    def visitClassDecl(self, ctx: OPLangParser.ClassDeclContext) -> ClassDecl:
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
        if ctx.getChildCount() == 1:
            return self.visit(ctx.constructor())

        is_static = True if self.visit(ctx.isStatic()) else False
        if ctx.attributeDecl():
            att_decl: AttributeDecl = self.visit(ctx.attributeDecl())
            att_decl.is_static = is_static
            return att_decl

        method_decl: MethodDecl = self.visit(ctx.methodDecl())
        method_decl.is_static = is_static
        return method_decl

    def visitAttributeDecl(self, ctx: OPLangParser.AttributeDeclContext) -> AttributeDecl:
        return AttributeDecl(
            is_static=False,
            is_final=self.visit(ctx.isFinal()),
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
            is_static=False,
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

    def visitIsStatic(self, ctx: OPLangParser.IsStaticContext) -> bool:
        return ctx.STATIC()

    def visitConstructor(self, ctx: OPLangParser.ConstructorContext) -> ConstructorDecl | DestructorDecl:
        child: OPLangParser.DefConstructorContext = ctx.defConstructor()
        params: list[Parameter] = []
        if ctx.copyConstructor():
            child = ctx.copyConstructor()
            params = [Parameter(child.ID().getText(), "other")]
        elif ctx.customConstructor():
            child = ctx.customConstructor()
            assert type(child) == OPLangParser.CustomConstructorContext
            params = self.visit(child.paramNulist())
        elif ctx.destructor():
            child = ctx.destructor()
        body: BlockStatement = self.visit(child.blockStatement())

        assert child
        return ConstructorDecl(
            name=child.ID().getText(),
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

    def visitMethodInvoStmt(self, ctx: OPLangParser.MethodInvoStmtContext):
        return MethodInvocationStatement(
            method_invocation=self.visit(ctx.methodInvocation())
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

    def visitArrayAccessExpr(self, ctx: OPLangParser.ArrayAccessExprContext) -> PostfixExpression | Expr:
        if ctx.getChildCount() == 1:
            return self.visit(ctx.memberAccessExpr())

        child = ArrayAccess(index=self.visit(ctx.arrayAccess()))
        primary = self.visit(ctx.arrayAccessExpr())
        if type(primary) == PostfixExpression:
            return PostfixExpression(
                primary=primary.primary,
                postfix_ops=[child] + primary.postfix_ops
            )
        return PostfixExpression(
            primary=primary,
            postfix_ops=[child]
        )

    def visitMemberAccessExpr(self, ctx: OPLangParser.MemberAccessExprContext) -> PostfixExpression | Expr | list[PostfixOp]:
        if ctx.getChildCount() == 1:
            return self.visit(ctx.fact())

        child = self.visit(ctx.methodInvocation()) if ctx.methodInvocation() else MemberAccess(member_name=ctx.ID().getText())
        primary = self.visit(ctx.memberAccessExpr())
        if type(primary) == PostfixExpression:
            assert isinstance(child, PostfixOp), "child not PostfixOp but: " + str(type(child))
            return PostfixExpression(
                primary=primary.primary,
                postfix_ops=[child] + primary.postfix_ops
            )
        return PostfixExpression(
            primary=primary,
            postfix_ops=[child]
        )

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
            return self.visit(ctx.expr0())
        elif ctx.literals():
            return (self.visit(ctx.literals()))

        assert ctx.NIL(), "ctx not NIL"
        return NilLiteral()

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


    def visitArrayAccess(self, ctx: OPLangParser.ArrayAccessContext) -> Expr:
        return self.visit(ctx.expr0())

    def visitTypeRef(self, ctx: OPLangParser.TypeRefContext) -> ReferenceType:
        return ReferenceType(self.visit(ctx.type_())) if ctx.AMPERSAND() else self.visit(ctx.type_())

    def visitType(self, ctx: OPLangParser.TypeContext) -> PrimitiveType | ArrayType:
        child = ctx.VOID()

        if ctx.INT():
            child = ctx.INT()
        elif ctx.FLOAT():
            child = ctx.FLOAT()
        elif ctx.BOOLEAN():
            child = ctx.BOOLEAN()
        elif ctx.STRING():
            child = ctx.STRING()
        elif ctx.ID():
            child = ctx.ID()
        elif ctx.VOID():
            return PrimitiveType(ctx.VOID().getText())

        arr_decl: OPLangParser.ArrayDeclContext = ctx.arrayDecl()
        # handle PrimitiveType
        if arr_decl.getChildCount() == 0:
            return PrimitiveType(child.getText())

        # handle ArrayType
        assert type(child) != ctx.VOID()
        return ArrayType(
            element_type=PrimitiveType(child.getText()),
            size=int(arr_decl
                     .INTEGER_LITERAL().getText())
        )

    def visitIdList(self, ctx: OPLangParser.IdListContext) -> list[Identifier]:
        if not ctx.idList():
            return [Identifier(ctx.ID().getText())]
        return [Identifier(ctx.ID().getText())] + self.visit(ctx.idList())
