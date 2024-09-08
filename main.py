import gspread
gc = gspread.oauth()
spread = gc.open("Processadores e Benchmarks")
sheet = spread.worksheet("i7 x r7")
data = sheet.get('B2:L19')

# Print each row in the data
cpus = []
for row in data:
    cpu = (row[0],row[1],row[9],row[10])
    cpus.append(cpu)

sheet = spread.worksheet("i5 x r5")
data = sheet.get('B2:L15')
for row in data:
    cpu = (row[0],row[1],row[9],row[10])
    cpus.append(cpu)

sheet = spread.worksheet("i3 x r3")
data = sheet.get('B2:L12')
for row in data:
    cpu = (row[0],row[1],row[9],row[10])
    cpus.append(cpu)


##analysis
###cpu[2] = single_core
###cpu[3] = multi_core
similar_cpus_list_single_core = []
for cpu in cpus:
    single_core = int(cpu[2])
    output = ""
    output+=(f"Main [{cpu[1]}]: ") #name
    for cpu2 in cpus:
        if single_core != int(cpu2[2]): #not the same cpu
            dif = abs(single_core - int(cpu2[2]))
            ##dif is what percentage of single_core?
            percentage = dif*100/single_core
            ##proximity margin
            if percentage >= 5 and percentage <= 7:
                ##this cpu is proximal
                output+=(f"{cpu2[1]} ({round(percentage,2)}%),")
    similar_cpus_list_single_core.append(output)

print("Single Core Similarity comparison: ")
for line in similar_cpus_list_single_core:
    print(line)

similar_cpus_list_multi_core = []
print("\n\nMulti Core Similarity comparison: ")
for cpu in cpus:
    multi_core = int(cpu[3])
    output = ""
    output+=(f"Main [{cpu[1]}]: ") #name
    for cpu2 in cpus:
        if multi_core != int(cpu2[3]): #not the same cpu
            dif = abs(multi_core - int(cpu2[3]))
            ##dif is what percentage of single_core?
            percentage = dif*100/single_core
            ##proximity margin
            if percentage >= 5 and percentage <= 15:
                ##this cpu is proximal
                output+=(f"{cpu2[1]} ({round(percentage,2)}%),")
    similar_cpus_list_multi_core.append(output)

for line in similar_cpus_list_multi_core:
    print(line)






