print("===== Identitas Teman =====")

#membuat list teman
list_teman = ['erika','sekar','hana','rafli','bonang','ano','yola','maurich','vizal','rio']
print("list_teman[4]: ", list_teman[4])
print("list_teman[6]: ", list_teman[6])
print("list_teman[7]: ", list_teman[7])

#mengganti list teman
list_teman[3] = 'densur'
list_teman[5] = 'titus'
list_teman[9] = 'truely'

#menambah list teman
list_teman.extend(['riri','zafira'])

#menampilkan list nama perulangan
urutan = 0
for list in range(0,12):
    print(list_teman[urutan])
    urutan = urutan + 1

#menampilkan list
print(len(list_teman))