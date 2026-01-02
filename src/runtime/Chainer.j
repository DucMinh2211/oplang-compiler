.source Chainer.java
.class public Chainer
.super java/lang/Object
.field val I

.method public inc()LChainer;
.var 0 is this LChainer; from Label0 to Label1
Label0:
	aload_0
	aload_0
	getfield Chainer/val I
	iconst_1
	iadd
	putfield Chainer/val I
	aload_0
	areturn
Label1:
.limit stack 3
.limit locals 1
.end method

.method public <init>()V
.var 0 is this LChainer; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	iconst_0
	putfield Chainer/val I
	return
Label1:
.limit stack 2
.limit locals 1
.end method
