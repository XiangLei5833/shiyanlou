try:
    raise KeyboardInterrupt
finally:    # 不管是否发生异常，都会在 try 之后执行，当 try 语句中发生了未被 except 捕获的异常，在 finally 子句完成后会被重新抛出。
    print('Goodbye, world!')
