WARNING
Be careful about how you are getting your translations. If you rely on Google
Translate to populate EXPECTED values for Unit Tests, there is a chance that it
will be wrong.
Examples (IBM_Watson / Google Translate)
A) "Joy To the World" = joy au monde / joie au monde
B) "Peace to the Earth" = Paix sur Terre / paix sur la terre

WARNING
Watson IBM translate API can only handle 1 line at a time. It will remove '\n'
new line characters from translated strings.