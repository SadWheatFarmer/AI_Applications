IBM Watson Language Translator
Des: The 'translator.py' is a python module that defines two functions that will
        allow a user to convert text from English to French or German using the
        IBM Watson Language Translator API.
     All needed information needed to connect/run the API is provided in the
        'IBM_Watson_APIs.txt' file.
     Google Translate was used to verify the operation of the IBM Watson API.
        Unfortunately, there are differences between these two services. Please
        see below for more information regarding the performance of the Watson
        API.



WARNING
Be careful about how you are getting your translations. If you rely on Google
Translate to populate EXPECTED values for Unit Tests, there is a chance that it
will be wrong.
Examples (IBM_Watson / Google Translate)
A) "Joy To the World" = joy au monde / joie au monde
B) "Peace to the Earth" = Paix sur Terre / paix sur la terre
C) "Blue Square\nRed Circle" = cercle rouge bleu carre / carre bleu cercle rouge
    - 3 Errors...
        1) For IBM translation, the new line char is gone.
        2) For IBM translation, the words are flipped from order given
                (red circle blue square) vs (blue square red circle)
        3) For IBM translation, the 'red circle' french words are flipped.
                The IBM version is saying 'circle red'

WARNING
Watson IBM translate API can only handle 1 line at a time. It will remove '\n'
new line characters from translated strings.