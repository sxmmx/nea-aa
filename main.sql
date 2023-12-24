CREATE TABLE Users(
  User_ID int(4) NOT NULL,
  User_email varchar(50)NOT NULL,
  User_password varchar(10)NOT NULL,
  PRIMARY KEY (User_ID)
);

--table to make translation and transcription quiz
CREATE TABLE TranslationQuiz(
  TranslationQuiz_ID int(4) NOT NULL,
  User_ID int(4) NOT NULL,
  TL_text varchar(100) NOT NULL,
  max_score int(2) NOT NULL,
  PRIMARY KEY (TranslationQuiz_ID),
  FOREIGN KEY (User_ID) REFERENCES Users(User_ID)
);

CREATE TABLE TranscriptionQuiz(
  TranscriptionQuiz_ID int(4) NOT NULL,
  User_ID int(4) NOT NULL,
  TC_text varchar(100) NOT NULL,
  max_score int(2) NOT NULL,
  PRIMARY KEY (TranscriptionQuiz_ID),
  FOREIGN KEY (User_ID) REFERENCES Users(User_ID)
);

--translation and transcription questions 
CREATE TABLE TranslationQ_Questions(
  TranslationQuestions_ID int(4) NOT NULL,
  TranslationQuiz_ID int(4) NOT NULL,
  TLQ_Questions varchar(30) NOT NULL,
  score int(2) NOT NULL,
  PRIMARY KEY (TranslationQuestions_ID),
  FOREIGN KEY (TranslationQuiz_ID) REFERENCES TranslationQuiz(TranslationQuiz_ID)
);

CREATE TABLE TranscriptionQ_Questions(
  TranscriptionQuestions_ID int(4) NOT NULL,
  TranscriptionQuiz_ID int(4) NOT NULL,
  TLQ_Questions varchar(30) NOT NULL,
  score int(2) NOT NULL,
  PRIMARY KEY (TranscriptionQuestions_ID),
  FOREIGN KEY (TranscriptionQuiz_ID) REFERENCES TranscriptionQuiz(TranscriptionQuiz_ID)
);

--answers to each question translation and transcription
CREATE TABLE TranslationQ_Answers(
  TranslationAnswers_ID int(4) NOT NULL,
  TranslationQuestions_ID int(4) NOT NULL,
  TL_answercorrect varchar(50) NOT NULL,
  PRIMARY KEY (TranslationAnswers_ID),
  FOREIGN KEY (TranslationQuestions_ID) REFERENCES TranslationQ_Questions(TranslationQuestions_ID)
);

CREATE TABLE TranscriptionQ_Answers(
  TranscriptionAnswers_ID int(5) NOT NULL,
  TranscriptionQuestions_ID int(5) NOT NULL,
  TC_answercorrect varchar(50) NOT NULL,
  PRIMARY KEY (TranscriptionAnswers_ID),
  FOREIGN KEY (TranscriptionQuestions_ID) REFERENCES TranscriptionQ_Questions(TranscriptionQuestions_ID)
);

--what the user will fill in as their answer for the question in each quiz
CREATE TABLE User_AnswerTL(
  UserAnswerTL_ID int(5) NOT NULL,
  UserAnswerTL varchar(50) NOT NULL,
  overall_mark int(2) NOT NULL,
  TranslationQuiz_ID int(5) NOT NULL,
  TranslationQuestions_ID int(5) NOT NULL,
  TranslationAnswers_ID int(5) NOT NULL,
  User_ID int(5) NOT NULL,
  PRIMARY KEY (UserAnswerTL_ID),
  FOREIGN KEY (TranslationQuiz_ID) REFERENCES TranslationQuiz(TranslationQuiz_ID),
  FOREIGN KEY (TranslationQuestions_ID) REFERENCES TranslationQ_Questions(TranslationQuestions_ID),
  FOREIGN KEY (TranslationAnswers_ID) REFERENCES TranslationQ_Answers(TranslationAnswers_ID),
  FOREIGN KEY (User_ID) REFERENCES Users(User_ID)
);

CREATE TABLE User_AnswerTC(
  UserAnswerTC_ID int(5) NOT NULL,
  UserAnswerTC varchar(50) NOT NULL,
  overall_mark int(2) NOT NULL,
  TranscriptionQuiz_ID int(5) NOT NULL,
  TranscriptionQuestions_ID int(5) NOT NULL,
  TranscriptionAnswers_ID int(5) NOT NULL,
  User_ID int(5) NOT NULL,
  PRIMARY KEY (UserAnswerTC_ID),
  FOREIGN KEY (TranscriptionQuiz_ID) REFERENCES TranscriptionQuiz(TranscriptionQuiz_ID),
  FOREIGN KEY (TranscriptionQuestions_ID) REFERENCES TranscriptionQ_Questions(TranscriptionQuestions_ID),
  FOREIGN KEY (TranscriptionAnswers_ID) REFERENCES TranscriptionQ_Answers(TranscriptionAnswers_ID),
  FOREIGN KEY (User_ID) REFERENCES Users(User_ID)
);

 --title of quizzes
INSERT INTO TranslationQuiz(2001 ,"During transcription, a molecule of mRNA is made in the nucleus: 1. The hydrogen bonds between the complementary bases break and DNA uncoils , thus separang the two strands. 2. One of the DNA strands is used as a template to make the mRNA molecule. The template is called the antisense strand. Free nucleodes line up by complementary base pairing and adjacent nucleodes are joined by phosphodiester bonds, thus forming a molecule of mRNA. This is catalysed by RNA polymerase. 3. mRNA then moves out of the nucleus through a pore and aaches to a ribosome in the cytoplasm which is the site of the next stage of protein synthesis." , 15)

INSERT INTO TranscriptionQuiz(3001 ,"During translaon amino acids join together to form a polypeptide chain: 1.mRNA aaches to a ribosome tRNA is a single stranded molecule with an amino acid binding site. 2.tRNA binds to specific amino acids from the cytoplasm depending on its anticodon, this is known as activation. Complementary ancodons of tRNA bind to mRNA codons and are held in place by hydrogen bonds. The ribosome joins the amino acids aached to two tRNA molecules by a pepde bond and then tRNA molecules detach from the amino acids. This process is repeated thus leading to the formaon of a polypepde chain unl a stop codon is reached on mRNA.", 15) 

INSERT INTO TranslationQ_Questions(4001, 2001, "Describe the role of translation in the synthesis of a globular protein by a muscle cell.", 3)
INSERT INTO TranslationQ_Questions(4002, 2001, "Leptin is a protein hormone with a role in the control of appetite in humans. Describe the role of tRNA in the production of leptin.", 3)
INSERT INTO TranslationQ_Questions(4003, 2001, "Many of the proteins synthesised become extracellular enzymes. Describe what happens to these proteins following the process of translation until they are released from the cell.", 3)
INSERT INTO TranslationQ_Questions(4004, 2001, "If the DNA code reads CCAATTGG then the tRNA code would read...", 3)
INSERT INTO TranslationQ_Questions(4005, 2001, "Summarise translation in three steps.", 3)
  
INSERT INTO TranscriptionQ_Question(5001, 3001, "Where does transcription take place?" ,3)
INSERT INTO TranscriptionQ_Question(5002, 3001, "Describe the role of transcription in protein synthesis" ,3)
INSERT INTO TranscriptionQ_Question(5003, 3001, "What does mRNA do?" ,3)
INSERT INTO TranscriptionQ_Question(5004, 3001, "Compare and contrast DNA replication and DNA transcription?", 3)
INSERT INTO TranscriptionQ_Question(5005, 3001, "Define RNA Polymerase, sense strand, and Which way is the template strand read?", 3)

INSERT INTO TranslationQ_Answers(6001, 4001, "1. the { gene / sequence of DNA } for the (globular) protein is transcribed (1) 2.complementary base pairing between RNA nucleotides and DNA (to produce mRNA) (1) 3. mRNA leaves the nucleus and attaches to a ribosome (1) 4. pairing between codons on mRNA and anticodons on tRNA (1) 4. tRNA provides specific amino acids (1) 6. the sequence of { bases / codons } determines the {sequence of amino acids / primary structure of the protein } (1)")
INSERT INTO TranslationQ_Answers(6002, 4002, "1. tRNA molecules {transport amino acids to ribosomes} 2. tRNA molecule has an anticodon that binds to a codon on the mRNA 3. each tRNA carries a  particular amino acids")
INSERT INTO TranslationQ_Answers(6003, 4003, "  proteins are folded on RER  packages into/tranported in vesicles modified in the golgi apparatus exocytosis")
INSERT INTO TranslationQ_Answers(6004, 4004, "GGTTAACC")
INSERT INTO TranslationQ_Answers(6005, 4005, "1. mRNA ataches to a ribosome tRNA is a single stranded molecule with an amino acid binding site . tRNA binds to specific amino acids from the cytoplasm depending on its an-codon, this is known as acvaon. 2. Complementary ancodons of tRNA bind to mRNA codons and are held in place by hydrogenbonds. 3. The ribosome joins the amino acids aached to two tRNA molecules by a pepde bond and then tRNA molecules detach from the amino acids")

INSERT INTO TranscriptionQ_Answers(7001,5001,"nucleus")
INSERT INTO TranscriptionQ_Answers(7002,5002,"RNA polymerase breaks hydrogen bonds between complentary bases and DNA uncoils. The antisense stand is used as a template for DNA. ")
INSERT INTO TranscriptionQ_Answers(7003,5003,"mRNA has complementary bases to the template strand due to RNA polymerase catalysing the joining of adjacent nucleotides with phosphodiester.  ")
INSERT INTO TranscriptionQ_Answers(7004,5004,"Simlarities: DNA is uncoiled. Differences: DNA helicase is used to uncoil DNA in replication wherease RNA Polymerase is used in transcription, transcription is used to make proteins whereas replication makes copies of DNA")
INSERT INTO TranscriptionQ_Answers(7005,5005,"The enzyme that joins nucleotides together, strand not used for mRNA, 5'to3'")
