
# adding a member to a club
from pyscript import display, document

grade7 = {'John Doe', 'Jane Doe'}
grade8 = {'Two Time', 'Azure'}
grade9 = {'Chance', 'Mafioso'}
grade10 = {'Noob', 'Sixer'}

grade7to8 = grade7.union(grade8)
grade9to10 = grade9.union(grade10)

members = grade7to8.union(grade9to10)


def update_output():

    display(members, target='output')
    display(len(members), target='output')

def add_member(event):

    global members

    fname = document.getElementById("fname").value.strip()
    lname = document.getElementById("lname").value.strip()

    new_member = fname + " " + lname

    members = members.union({new_member})

    document.getElementById("fname").value = ""
    document.getElementById("lname").value = ""

    update_output()


update_output()