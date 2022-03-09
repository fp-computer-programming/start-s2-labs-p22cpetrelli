#author CJP 03/07/2022
#define initials and names seperately
last_initials = ["B.", "D.", "H.", "E.", "G.", "G.", "H.", "R.", "M.", "L.", "I.", "I.", "N.", "N.", "O.", "P.", "P.", "X.", "T.", "S.", "S.", "P."]

rows = [["Mateo", "Jason", "Jordan", "Mohamed", "Michael", "Charlie", "Declan"], ["Sean", "Luis", "Ryan", "James", "Jack"], ["Aiden", "Ian", "Colin", "Tim", "Cam"], ["Larry", "Spencer", "Chris", "Ryan", "Nolan"]]

#create index
index = 0

#for each name in each row it will set to position 0
for row in rows:
    for name in (row):
        print("{0} {1}".format(name, last_initials[index]))
        index += 1