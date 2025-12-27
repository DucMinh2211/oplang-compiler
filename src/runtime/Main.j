.source Main.java
.class public Main
.super java/lang/Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
.var 2 is j I from Label0 to Label1
	iconst_1
	istore_1
Label4:
	iload_1
	iconst_2
	if_icmpgt Label3
	iconst_1
	istore_2
Label7:
	iload_2
	iconst_2
	if_icmpgt Label6
	iload_1
	bipush 10
	imul
	iload_2
	iadd
	invokestatic io/writeIntLn(I)V
Label5:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label7
Label6:
Label2:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label4
Label3:
	return
Label1:
.limit stack 4
.limit locals 3
.end method

.method public <init>()V
.var 0 is this LMain; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	return
Label1:
.limit stack 1
.limit locals 1
.end method
