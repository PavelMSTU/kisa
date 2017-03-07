# kisa
"Keyboard Interrupt System Exit"

## Introduction

Sometimes you run you **python** code
in [tmux](https://en.wikipedia.org/wiki/Tmux)
like this:
  1. ~$ ssh user@host.yy
  1. (insert password)
  1. ~# tmux attach
  1. (select some tmux window)
  1. ~# python3 your_script.py

More useful example is
[Machine Learning using python](https://github.com/rasbt/python-machine-learning-book)

You have many little works in
your **data processing**.
For each little work you have some *.py file.
It is useful, really?

Of cause in production you write
"big-big system"...
But in R&D tmux using is more useful...

Most useful method of stop python
script is send CTRL+C signal.

But in this case you
have problems in
[data integrity](https://en.wikipedia.org/wiki/Data_integrity)...

For example you whant do this:
```python
sql="""
insert into mytable values ('bat', 'lala')
"""
engine.execute(sql)
channel.basic_ack(delivery_tag=method.delivery_tag)
```
First two lines is [SQLAlchemy](http://www.sqlalchemy.org)
[execute command](http://docs.sqlalchemy.org/en/latest/core/connections.html).
Second is command for [ack](https://en.wikipedia.org/wiki/Acknowledgement_(data_networks))
in [RabbitMQ](http://www.rabbitmq.com).

Of course you want to run both commands or not to run both.
If your code insert information to database
but not **ack** in **RabbitMQ**,
**data integrity** will be breaked!

There are four type solutions of this problem:
  1. don't stop by Ctrl+C
  1. use [atexit](https://docs.python.org/2/library/atexit.html)
  1. use some BIG-BI-I-IG framework for solving ALL 
  problems in **data integrity**... 
  Including "Ctrl+C" problem...
  1. became humility...

Therefore I spend a lot of time and make 
vary simple *.py code.
I call it **kisa**.
This means Keyboard Interrupt and System Exit.

(I use name **"kisA"** not **"kisE"**, 
becouse **"kisa"** is nickname
of Ippolit Vorobianinov (see russian novel ["The Twelve Chairs"](https://en.wikipedia.org/wiki/The_Twelve_Chairs) )
but **kise** means nothing.
<s>ATTANTION: Don't speak **kisKa**,
becouse this is mean "pussy"</s>)

**Kisa** allows do this:
```
with Kisa():
    sql="""
    insert into mytable values ('bat', 'lala')
    """
    engine.execute(sql)
    channel.basic_ack(delivery_tag=method.delivery_tag)
```

If you send Ctrl+C, all code in with statement
will be done!

**ATTANTIONS**
  1. I dont know is Kisa work in multithreads...
  But in in simple *.py data science workers
  is is not actual problem
  1. Kisa DOES NOT except some program, logic or
  environment errors! Kisa is solutions for 
  simple using python code in console (ssh + tmux).
  Kisa allows you send some "close-program SIGNALS" without
  **data integrity** break

## How to use

### quick start
you can dump git solution:
```bash
git clone https://github.com/PavelMSTU/kisa
```

but project is vary tiny and have only one *.py file.
This is **kisa.py**.

You can download this file only. ;)

After you can do this:
```python
from kisa import Kisa
...
...
with Kisa():
    # some data integrity critical code
    ...
# another code
```

If user send Ctrl+C before or after with
statement, script is interrupt.
If user send Ctrl+C in with statement,
all code will be done and after
KeyboardInterrupt will be send.

###cookbook

TODO

## License

Kisa is
[LGPL](https://en.wikipedia.org/wiki/GNU_Lesser_General_Public_License).

It will be boorish in another case...

You can copy, fork, use all in kisa.

## Disclaimer
This code will be write in Russia.
Therefore NOTHING disclaimer.
If you are stupied -- this is YOUR problem.
In Russia, I dont need write some bullshit text for 
protect my liability... Ha-ha-ha!...
