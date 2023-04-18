with open ("24/MailMergeProjectStart/Input/Names/invited_names.txt", "r") as dosya:
 isimler = dosya.read().split("\n")
 
print(isimler)

with open ("24/MailMergeProjectStart/Input/Letters/starting_letter.txt", "r") as dosya:
 mektup = dosya.read()

print(mektup)
 
for isim in isimler:
 with open (f"24/MailMergeProjectStart/Output/ReadyToSend/{isim}.txt", "w") as dosya:
  dosya.write(mektup.replace("[name]", f"{isim}"))