import re
points = []
scores = []
a = "[BodyPart:1-(0.51, 0.28) score=0.82 BodyPart:2-(0.60, 0.29) score=0.82 BodyPart:3-(0.62, 0.38) score=0.84 BodyPart:4-(0.60, 0.30) score=0.10 BodyPart:5-(0.42, 0.29) score=0.72 BodyPart:6-(0.38, 0.39) score=0.81 BodyPart:8-(0.55, 0.49) score=0.53 BodyPart:9-(0.68, 0.64) score=0.84 BodyPart:10-(0.59, 0.80) score=0.67 BodyPart:11-(0.44, 0.50) score=0.51 BodyPart:12-(0.29, 0.64) score=0.80 BodyPart:13-(0.37, 0.81) score=0.76 BodyPart:16-(0.55, 0.18) score=0.81 BodyPart:17-(0.47, 0.18) score=0.91]"
b = "[BodyPart:0-(0.56, 0.23) score=0.80 BodyPart:1-(0.57, 0.33) score=0.79 BodyPart:2-(0.52, 0.35) score=0.70 BodyPart:3-(0.46, 0.40) score=0.69 BodyPart:4-(0.36, 0.41) score=0.84 BodyPart:5-(0.61, 0.32) score=0.72 BodyPart:6-(0.61, 0.21) score=0.58 BodyPart:7-(0.59, 0.11) score=0.80 BodyPart:8-(0.56, 0.52) score=0.43 BodyPart:9-(0.61, 0.65) score=0.36 BodyPart:10-(0.60, 0.80) score=0.63 BodyPart:11-(0.59, 0.51) score=0.50 BodyPart:12-(0.56, 0.65) score=0.50 BodyPart:13-(0.53, 0.80) score=0.69 BodyPart:14-(0.55, 0.22) score=0.64 BodyPart:15-(0.57, 0.22) score=0.67 BodyPart:17-(0.60, 0.24) score=0.33]"
c = "[BodyPart:0-(0.56, 0.23) score=0.80 BodyPart:1-(0.57, 0.33) score=0.79 BodyPart:2-(0.52, 0.35) score=0.70 BodyPart:3-(0.46, 0.40) score=0.69 BodyPart:4-(0.36, 0.41) score=0.84 BodyPart:5-(0.61, 0.32) score=0.72 BodyPart:6-(0.61, 0.21) score=0.58 BodyPart:7-(0.59, 0.11) score=0.80 BodyPart:8-(0.56, 0.52) score=0.43 BodyPart:9-(0.61, 0.65) score=0.36 BodyPart:10-(0.60, 0.80) score=0.63 BodyPart:11-(0.59, 0.51) score=0.50 BodyPart:12-(0.56, 0.65) score=0.50 BodyPart:13-(0.53, 0.80) score=0.69 BodyPart:14-(0.55, 0.22) score=0.64 BodyPart:15-(0.57, 0.22) score=0.67 BodyPart:17-(0.60, 0.24) score=0.33]"
d = "[BodyPart:0-(0.48, 0.16) score=0.91 BodyPart:1-(0.50, 0.27) score=0.85 BodyPart:2-(0.44, 0.27) score=0.74 BodyPart:3-(0.37, 0.26) score=0.71 BodyPart:4-(0.30, 0.23) score=0.79 BodyPart:5-(0.56, 0.28) score=0.76 BodyPart:6-(0.66, 0.29) score=0.82 BodyPart:7-(0.76, 0.29) score=0.74 BodyPart:8-(0.45, 0.42) score=0.68 BodyPart:11-(0.51, 0.45) score=0.70 BodyPart:12-(0.49, 0.59) score=0.86 BodyPart:13-(0.47, 0.74) score=0.88 BodyPart:14-(0.47, 0.15) score=0.67 BodyPart:15-(0.49, 0.16) score=0.94 BodyPart:17-(0.52, 0.18) score=0.96]"
e = "[BodyPart:1-(0.50, 0.30) score=0.50 BodyPart:2-(0.45, 0.28) score=0.48 BodyPart:3-(0.39, 0.30) score=0.26 BodyPart:4-(0.54, 0.26) score=0.12 BodyPart:5-(0.56, 0.30) score=0.39 BodyPart:6-(0.62, 0.30) score=0.60 BodyPart:7-(0.59, 0.31) score=0.56 BodyPart:8-(0.44, 0.44) score=0.44 BodyPart:9-(0.45, 0.64) score=0.66 BodyPart:10-(0.45, 0.82) score=0.82 BodyPart:11-(0.54, 0.45) score=0.47 BodyPart:12-(0.52, 0.63) score=0.66 BodyPart:13-(0.52, 0.81) score=0.83 BodyPart:16-(0.52, 0.28) score=0.09]"
pose_estimation = "[BodyPart:0-(0.55, 0.17) score=0.81 BodyPart:1-(0.49, 0.27) score=0.85 BodyPart:2-(0.41, 0.26) score=0.67 BodyPart:3-(0.33, 0.37) score=0.72 BodyPart:4-(0.36, 0.48) score=0.78 BodyPart:5-(0.58, 0.27) score=0.81 BodyPart:6-(0.65, 0.38) score=0.88 BodyPart:7-(0.62, 0.48) score=0.86 BodyPart:8-(0.43, 0.48) score=0.60 BodyPart:9-(0.43, 0.66) score=0.67 BodyPart:10-(0.53, 0.79) score=0.56 BodyPart:11-(0.53, 0.48) score=0.56 BodyPart:12-(0.59, 0.66) score=0.75 BodyPart:13-(0.49, 0.80) score=0.50 BodyPart:14-(0.54, 0.15) score=0.73 BodyPart:15-(0.56, 0.15) score=0.85 BodyPart:16-(0.48, 0.16) score=0.81 BodyPart:17-(0.83, 0.18) score=0.79]"

findable = "0.[0-9][0-9]"
compilable = re.compile(findable)
res = re.findall(compilable, a) #there are other examples except 'a' in strings 5 - 9 so you can change some variables and get another result


for z in range(2, len(res), 3):
    scores.append(res[0+z])

for w in range(0, len(res), 3):
    points.append(res[0+w])    
    points.append(res[1+w])

print(points)
print(scores)