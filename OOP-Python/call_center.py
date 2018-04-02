# import time

class Call(object):
    def __init__(self, uid, name, number, time, reason):
        self.uid = uid
        self.name = name
        self.number = number
        self.time = time
        self.reason = reason

    def display_info(self):
        print 'Unique ID:\t{}\nCaller Name:\t{}\nPhone Number:\t{}\nTime of Call:\t{}\nReason for call:\t{}'.format(self.uid, self.name, self.number, self.time, self.reason)
        return self

# call1.display_info()

class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue_size = len(self.calls)

    def add(self, call):
        self.calls.append(call)
        self.queue_size += 1

    def remove(self): 
        self.calls.pop(0)
        self.queue_size -= 1

    def removeNumber(self, userNumber):
        for i in range (len(self.calls)):
            if self.calls[i].number == userNumber: 
                self.calls.pop(i)
                self.queue_size -= 1
        return self
    
    def sortByTime(self):
        self.calls = sorted(self.calls, key=lambda call: call.time)

    def info(self):
        for callz in self.calls:
            print(">>\n{} {} {} {}\n>>".format(callz.name, callz.number, callz.time, self.queue_size)) 
            #when you are adding self.queue_size here it prints of the queue after every phone-number! If you don't want to print the number after every phone-number you have to create a seperat for loop with size.queue 
    

cc_munich = CallCenter()
cc_us = CallCenter()

cc_munich.add(Call(111, "Isabell", 12345, "3.33pm", "Internet window couldn't be refreshed"))
cc_us.add(Call(645, "Manuel", 937930, "06:45am", "No wlan connnection"))
cc_munich.add(Call(929, "Hannah", 72047, "1.58pm", "missing adapter"))
cc_us.add(Call(647, "Ashley", 7463869, "1.37pm", "general question"))


# cc_munich.info()
# cc_munich.removeNumber(72047)
# cc_us.info()
cc_munich.sortByTime()
cc_munich.info()
