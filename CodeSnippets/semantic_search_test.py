
import test_embedding as t
text1 = "Python is a programming language  "
text2 = "Python is used to write ai related code"
text3 = "My name is aakash malviya and i am from india and i am a software developer  "

emd1 = t.get_embedding(text=text1)
emd2 = t.get_embedding(text=text2)
emd3 = t.get_embedding(text=text3)

print( "simpilirity " ,  f"{t.cosine_similarity(emd1 , emd3) :.2f}")