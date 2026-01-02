.source Main.java
.class public Main
.super java/lang/Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is fact [I from Label0 to Label1
	iconst_5
	newarray int
	astore_1
.var 2 is i I from Label0 to Label1
	aload_1
	iconst_0
	iconst_1
	iastore
	iconst_1
	istore_2
Label4:
	iload_2
	iconst_4
	if_icmpgt Label3
	aload_1
	iload_2
	aload_1
	iload_2
	iconst_1
	isub
	iaload
	iload_2
	iconst_1
	iadd
	imul
	iastore
Label2:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label4
Label3:
	aload_1
	iconst_4
	iaload
	invokestatic io/writeIntLn(I)V
	return
Label1:
.limit stack 6
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
