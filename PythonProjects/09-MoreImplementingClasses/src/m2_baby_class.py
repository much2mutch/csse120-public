"""
A   Baby   class and functions that use/test it.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Derek Whitley, their colleagues,
         and PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """
    After you have written the code for the Baby class, run this module.
    If your Baby class is correct, running this module should display (print)
    EXACTLY this:
        Hello baby McKinley!
        Hello baby Keegan!
        - - - - -
        Baby Keegan is sleeping.
        Thank you for feeding baby McKinley.
        Baby McKinley is sleeping.
        Baby McKinley is awake.  Time for food.
        Baby McKinley is CRYING uncontrollably!  Feed the Baby!
        Baby McKinley is CRYING uncontrollably!  Feed the Baby!
        - - - - -
        Baby Keegan is awake.  Time for food.
        Thank you for feeding baby McKinley.
        Baby McKinley is sleeping.
        Baby McKinley is awake.  Time for food.
        Baby McKinley is CRYING uncontrollably!  Feed the Baby!
        Baby McKinley is CRYING uncontrollably!  Feed the Baby!
    """
    mckinley = Baby('McKinley')
    keegan = Baby('Keegan')

    for k in range(2):
        print('- - - - -')
        keegan.hour_passes()
        mckinley.feed_baby()

        for j in range(4):
            mckinley.hour_passes()


###############################################################################
# TODO: 2.
#
#  Step 2a:  Implement a class called   Baby   that has a constructor method
#            (__init__) and two other methods, as described below.
#
#  Step 2b:  Test your finished   Baby   class by running this module.
#            Your code passes the test if it displays (prints)
#            EXACTLY the output shown in the doc_string for main.
#
# -----------------------------------------------------------------------------
# Here (below) are the methods that you must implement in your Baby class:
# -----------------------------------------------------------------------------
#
# Constructor method (__init__)
#     What comes in:
#        -- self
#        -- a string for the name of the baby
#     What goes out:  Nothing (i.e., None).
#     Side effects:
#        -- Sets instance variables as needed [YOU FIGURE OUT WHAT IS NEEDED!]
#        -- Prints 'Hello baby <your baby's name>!'
#     Example:
#         b = Baby('McKinley')   causes the following to be printed:
#               Hello baby McKinley!
#
# feed_baby
#     What comes in:
#        -- self
#     What goes out:  Nothing (i.e., None).
#     Side effects:
#        -- Prints 'Thank you for feeding baby <your baby's name>.'
#        -- Modifies instance variables as needed.
#     Example:
#         b = Baby('Joshua')
#         b.feed_baby()         causes the following to be printed:
#               Hello baby Joshua!
#               Thank you for feeding baby Joshua.
#
# hour_passes
#     What comes in:
#        -- self
#     What goes out:  Nothing (i.e., None).
#     Side effects:
#      -- If this is the FIRST time this method has been called
#         since this Baby was created or last fed, then this method prints:
# 	             'Baby <your baby's name> is sleeping.'
#
#      -- If this is the SECOND time this method has been called
#         since baby was created or last fed, then this method prints:
# 	             'Baby <your baby's name> is awake.  Time for food.'
#
#      -- If this is the THIRD (OR MORE) time this method has been called
#           since baby was created or last fed, then this method prints:
#         'Baby <your baby's name> is CRYING uncontrollably!  Feed the Baby!'
#      -- Modifies instance variables as needed.
#     Example:
#       Read the code in main (above).
#       Then read what the doc-string for  main  says should get printed.
#       Make sure that you understand WHY that output should be produced
#       by that code.  ASK QUESTIONS AS NEEDED to clarify this specification.
###############################################################################

###############################################################################
# The   Baby   class (and its methods) should begin here.
# Here is a reminder for the syntax (notation) to define a new class.
#
#      class NameOfClass(object):
#          """ Brief description of what an object of the class 'is'. """
#
###############################################################################


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
