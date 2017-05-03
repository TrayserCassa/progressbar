# ProgressBar

Small Progressbar in Python.

```python
def example():
    import time

    bar = Progressbar()
    for i in range(0, 100):
        time.sleep(0.02)
        bar.update()

    bar.step_to(0)
    time.sleep(2)

    bar.step_to(40)
    time.sleep(2)

    bar.set_message('This is a message')
    time.sleep(3)
    bar.set_message('New Message arrived')
    time.sleep(3)

    bar.step_to(80)
    time.sleep(4)

    bar.step_to(100)
```
