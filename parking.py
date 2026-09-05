class parking:
    def __init__(self,slot_num,status):
        self.slot_num=slot_num
        self.status=status
    def display(self):
        print("Slot Number: ",self.slot_num)
        print("Status: ",self.status)
    def update_status(self,new_status):
        self.status=new_status
        print(self.slot_num," status has been updated to " ,self.status)

p1=parking(1111,"occupied")
p2=parking(1112,"vacant")
p1.display()
p2.display()
p1.update_status("vacant")
p1.display()