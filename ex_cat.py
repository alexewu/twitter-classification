import spacy
nlp = spacy.load('en')

train_data = [
    (u"[ #COSTARICA #TSUNAMI ADVISORY ]: NO TSUNAMI WAVES REPORTED YET--BE ON ALERT! PRECAUTIONARY EVACUATION RECOMMENDED! #Earthquake #PTWC",
     {"cats": {"LOW": 0, "MEDIUM": 0, "HIGH": 1}}),
    (u"Sott - Costa Rican Officials: A Strong Earthquake Could Still Occur in Guanacaste http://t.co/Y6s3nUc9", {"cats": {"LOW": 0, "MEDIUM": 1, "HIGH": 0}}),
    (u"Bummer for Caribbean locals &amp; vacationers. Major quake hits near Costa Rica coast: http://t.co/6sL4AtOj Hope all is well down there!", {"cats": {"LOW": 1, "MEDIUM": 0, "HIGH": 0}}),
    (u"@TheNextCorner you missed our earthquake 7.6 in Costa Rica", {"cats": {"LOW": 1, "MEDIUM": 0, "HIGH": 0}}),
    (u"Two dead, 20 injured as major earthquake  at magnitude 7.6 damages Costa Rica coast, Red Cross says.", {"cats": {"LOW": 0, "MEDIUM": 0, "HIGH": 1}}),
    (u"The High Park fire west of Fort Collins, #CO has consumed 36,930 acres so far, is 0% contained and continues to grow. #NWS #cowx #cofire", {"cats": {"LOW": 1, "MEDIUM": 0, "HIGH": 0}}),
    (u"RT @ColoradoRapids: Photo of #FlagStaffFire in Boulder as seen from @DSGPark at 4pm MT. So many wildfires throughout Colorado rt now,  h ...", {"cats": {"LOW": 0, "MEDIUM": 1, "HIGH": 0}}),
    (u"RT @LarimerSheriff: #HighParkFire Another evacuation area notice has been lifted. Please check out link http://t.co/KXPBivpb", {"cats": {"LOW": 0, "MEDIUM": 0, "HIGH": 1}}),
    (u"RT @Kswan11: Pic of #highparkfire from Estes park high school http://t.co/hTVMKlk6", {"cats": {"LOW": 0, "MEDIUM": 1, "HIGH": 0}}),
    (u"Unprecedented Colorado Wildfires Continue, As Strong Winds and Looting Add to the Problem http://t.co/HwKpHLBt", {"cats": {"LOW": 0, "MEDIUM": 0, "HIGH": 1}}),
]

textcat = nlp.create_pipe('textcat')
nlp.add_pipe(textcat, last=True)
textcat.add_label('LOW')
textcat.add_label('MEDIUM')
textcat.add_label('HIGH')
optimizer = nlp.begin_training()
for itn in range(10):
    for doc, gold in train_data:
        nlp.update([doc], [gold], sgd=optimizer)

#low
doc = nlp(u"Sott - Costa Rican Officials: A Strong Earthquake Could Still Occur in Guanacaste http://t.co/Y6s3nUc9")
print(doc.cats)

#medium
doc = nlp(u"RT @ColoradoRapids: Photo of #FlagStaffFire in Boulder as seen from @DSGPark at 4pm MT. So many wildfires throughout Colorado rt now,  h ...")
print(doc.cats)

#high
doc = nlp(u"Unprecedented Colorado Wildfires Continue, As Strong Winds and Looting Add to the Problem http://t.co/HwKpHLBt")
print(doc.cats)
