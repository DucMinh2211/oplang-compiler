.source Main.java
.class public Main
.super java/lang/Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is a [I from Label0 to Label1
	iconst_2
	newarray int
	astore_1
.var 2 is h LHelper; from Label0 to Label1
	new Helper
	dup
	invokespecial Helper/<init>()V
	astore_2
	aload_1
	iconst_0
	bipush 10
	iastore
	aload_2
	aload_1
	iconst_0
	iaload
	invokevirtual Helper/set(I)LHelper;
	pop
	aload_2
	getfield Helper/val I
	invokestatic io/writeIntLn(I)V
	return
Label1:
.limit stack 3
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
