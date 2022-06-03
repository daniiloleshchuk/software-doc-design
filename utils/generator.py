from string import Template

section_templates = {'User': Template('username$i,name$i,email$i@gmail.com,surname$i\n'),
                     'Story': Template('path$i\n'),
                     'Message': Template('$i,$j,text$i\n'),
                     'StoryReaction': Template('$i,$j,text$i\n')}


def generate_csv(filename):
    with open(filename, 'w+') as file:
        for section, template in section_templates.items():
            file.write(section + '\n')
            for i in range(1, 250):
                if section in ('User', 'Story'):
                    file.write(template.substitute(i=i))
                elif section in ('Message', 'StoryReaction'):
                    file.write(template.substitute(i=i, j=i + 1 if i + 1 != 250 else 1))
            file.write('\n')
