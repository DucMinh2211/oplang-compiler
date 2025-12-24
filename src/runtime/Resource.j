.source Resource.java
.class public Resource
.super java/lang/Object

.method public finalize()V
.var 0 is this LResource; from Label0 to Label1
Label0:
	ldc "Destructor called"
	invokestatic io/writeStrLn(Ljava/lang/String;)V
	aload_0
	invokespecial java/lang/Object/finalize()V
	return
Label1:
.limit stack 1
.limit locals 1
.end method
