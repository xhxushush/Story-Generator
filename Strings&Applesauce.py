import random

When = ['A few years ago', 'Yesteerday', 'Last Night', 'A long time ago','On 20th January']
Who = ['A young man', 'A little girl', 'A powerful king', 'A cute rabbit', 'A sly cat']
Name = ['John', 'Sally', 'Christopher', 'Pum-Pum']
Residence = ['United Kingdom', 'India', 'Portuagal', 'Nepal']
Went = ['Hunting', 'Sking', 'Diving', 'To an amusmentpark']
Happen = ['Saw a pretty, large bird', 'Got stuck', 'Died', 'Had fun']
print(random.choice(When) + ', ' + random.choice(Who) + ' named ' + random.choice(Name)' that lived in ' +  random.choice(Residence) +
', went to the ' + random.choice(Went) + ' and ' + random.choice(Happen))

