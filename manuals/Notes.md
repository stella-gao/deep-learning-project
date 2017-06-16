```
score = model.evaluate(X_test, y_test, batch_size=batch_size,
                                show_accuracy=True)
return {'loss': -score[1], 'status': STATUS_OK}
```




