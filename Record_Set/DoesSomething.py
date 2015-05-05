import Record_Set

# Play with the data as if it were real data

recordSet = Record_Set.Record_Set()

print("Initial table")
print(recordSet.getTable())

print("")

print("Append new row")
print("[10, 11, 12]")
recordSet.setTable(recordSet.getTable() + [[10,11,12]])

print("New Table")
print(recordSet.getTable())

print("")

print("Remove row")
print("[7, 8, 9]")
table = recordSet.getTable()
table.remove([7,8,9])
recordSet.setTable(table)

print("New Table")
print(recordSet.getTable())