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
    # def visit(self, tree, o:Any=None) -> Any:
    #     if o:
    #         match type(tree):
    #             case OPLangParser.AttributeDeclContext:
    #                 self.visitAttributeDecl(tree, o)
    #             case OPLangParser.MethodDeclContext:
    #                 self.visitMethodDecl(tree, o)
        # match type(tree):
            # case OPLangParser.ProgramContext: 
            #     return self.visitProgram(tree)
            # case OPLangParser.ClassDeclListContext: 
            #     return self.visitClassDeclList(tree)
            # case OPLangParser.ClassDeclContext:
            #     return self.visitClassDecl(tree)
            # case OPLangParser.ClassExtendsContext:
            #     return self.visitClassExtends(tree)
            # case OPLangParser.MemberNulistContext:
            #     return self.visitMemberNulist(tree)
            # case OPLangParser.MemberContext:
            #     return self.visitMember(tree)
            # case OPLangParser.AttributeDeclContext:
            #     return self.visitAttributeDecl(tree, o)
            # case OPLangParser.MethodDeclContext:
            #     return self.visitMethodDecl(tree)
            # case OPLangParser.IsStaticContext:
            #     return self.visitIsStatic(tree)
            # case OPLangParser.IsFinalContext:
            #     return self.visitIsFinal(tree)
            # case OPLangParser.AttributeNameListContext:
            #     return self.visitAttributeNameList(tree)
            # case OPLangParser.AttributeNameContext:
            #     return self.visitAttributeName(tree)
        # return super().visit(tree)

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
        return self.visit(ctx.ID())

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
            attr_type=self.visit(ctx.type_()),
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
            return_type=self.visit(ctx.type_()),
            params=self.visit(ctx.paramNulist()),
            body=self.visit(ctx.blockStatement())
        )

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

    def visitVarDecl(self, ctx: OPLangParser.VarDeclContext):
        return VariableDecl(
            is_final=self.visit(ctx.isFinal()),
            var_type=self.visit(ctx.type_()),
            variables=self.visit(ctx.attributeNameList()),
        )

    def visitStmtNulist(self, ctx: OPLangParser.StmtNulistContext) -> list[Statement]:
        if not ctx.stmt(): return []
        return [self.visit(ctx.stmt())] + self.visit(ctx.stmtNulist())

    def visitStmt(self, ctx: OPLangParser.StmtContext) -> AssignmentStatement | IfStatement | ForStatement | BreakStatement | ContinueStatement | ReturnStatement | MethodInvocationStatement | BlockStatement:
        # TODO: finish method
        return self.visit(ctx.assignStmt())

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

        arr_decl: OPLangParser.ArrayDeclContext = ctx.arrayDecl()
        # handle PrimitiveType
        if arr_decl.getChildCount() == 0:
            return PrimitiveType(child.getText())

        # handle ArrayType
        assert type(child) != ctx.VOID()
        return ArrayType(
            element_type=child.getText(),
            size=int(arr_decl
                     .INTEGER_LITERAL().getText())
        )

