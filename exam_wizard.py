# Sample Question and Evaluation Criteria:
# Question: Explain the process of photosynthesis.

# Ideal Answer: Photosynthesis is a process used by plants and other organisms to convert light energy into chemical energy. It occurs in the chloroplasts of plant cells. The process involves the absorption of light by chlorophyll, the conversion of carbon dioxide and water into glucose and oxygen, and the storage of energy in the form of ATP.

# Keywords and Weights:
# Photosynthesis (2 points)
# Light energy (1 point)
# Chemical energy (1 point)
# Chloroplasts (2 points)
# Chlorophyll (1 point)
# Carbon dioxide (1 point)
# Water (1 point)
# Glucose (1 point)
# Oxygen (1 point)
# ATP (1 point)

# Photosynthesis is a process in which plants use sunlight to make 
# food. It happens in the chloroplasts where chlorophyll absorbs light.
# The plants take in carbon dioxide and water, and produce glucose and oxygen.

score = 0
question = input("What is photosynthesis? :").lower()
if  "photosynthesis" in question:
    score+=2
if "light energy" in question:
    score+=1
if "chemical energy" in question:
    score+=1
if "chloroplasts" in question:
    score+=2
if "chlorophyll" in question:
    score+=1
if "carbon dioxide" or "carbondioxide" in question:
    score+=1
if "water" in question:
    score+=1
if "glucose" in question:
    score+=1
if "oxygen" in question:
    score+=1
if "atp" in question:
    score+=1
print( f" You scored {score} out of 12")

i="photosynthesis,chlorophyll,chloroplasts,oxygen,water,carbon dioxide,glucose,atp,chemical energy,light energy"
for i in question:
    print(i)