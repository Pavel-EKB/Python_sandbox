from string import Template
name = 'Bob'
t = Template('Hey, $name!')

print(t.substitute(name=name))
# Вывод: 'Hey, Bob!'


templ_string = 'Hey $name, there is a $error error!'
errno = 50159747054
name = 'Bob'
print(
    Template(templ_string).substitute(
        name=name, error=hex(errno)
    )
)

# Вывод: 'Hey Bob, there is a 0xbadc0ffee error!'
