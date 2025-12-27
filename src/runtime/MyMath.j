.source MyMath.java
.class public MyMath
.super java/lang/Object

.method public static fact(I)I
.var 0 is n I from Label0 to Label1
Label0:
	iload_0
	iconst_1
	if_icmpgt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	iconst_1
	ireturn
	goto Label5
Label4:
	iload_0
	iload_0
	iconst_1
	isub
	invokestatic MyMath/fact(I)I
	imul
	ireturn
Label5:
Label1:
.limit stack 7
.limit locals 1
.end method

.method public <init>()V
.var 0 is this LMyMath; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	return
Label1:
.limit stack 1
.limit locals 1
.end method
