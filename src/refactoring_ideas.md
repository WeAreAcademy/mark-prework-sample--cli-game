### prompt_user_for_action

prompt_user_for_action - be explicit about lockdown has been used

don't overload the lockdown_answers array with more meaning

### repeated print and time could be combined

```python
print("\nHello " + username + "!\nWelcome to the Coronavirus Simulator.")
time.sleep(1)
```

### data-drive stat reporting

this is a long line!

```python
print("\nThese are the current stats for China:\nPopulation: "+ str(f'{china["population"]:,}') + "\nInfected: " + str(f'{china["infected"]:,}')+ "\nDead: " + str(f'{china["dead"]:,}'))
```

### if x is true...

```python
if lockdown is true:
```

can become:

```python
if lockdown:
```
