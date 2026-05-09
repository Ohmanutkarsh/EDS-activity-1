courses = int(input())
Tmarks=[]

def result():
	agg = sum(Tmarks)/len(Tmarks)
	print(f"Aggregate Percentage: {agg:.2f}")
	print("Grade:",end =" ")

	if agg >= 75 :
		print("Distinction")
	elif agg >= 60:
		print("First Division")
	elif agg >= 50:
		print("Second Division")
	else:
		print("Third Division")
		
Tmarks = list(map(int,input().split()))

if any(mark < 40 for mark in Tmarks):
	print ('Fail')
	
else:
	result()
