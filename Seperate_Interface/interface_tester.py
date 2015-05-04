import important_broadcaster
import general_broadcaster

#Simple script using both interfaces

ib = important_broadcaster.ImportantBroadcast()
gb = general_broadcaster.GeneralBroadcaster()

ib.say("This is the Important broadcaster. I am important.\n")

print(ib.get_feedback())

ib.ammend_message("What's that? I couldn't hear you.\n")

ib.take_it_back("Nevermind.")

gb.say_something("We heard you.")