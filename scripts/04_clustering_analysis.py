from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

df = pd.read_csv("data/match_history.csv")
df["Move_Num"] = df["P1_Move"].map({"Rock": 0, "Paper": 1, "Scissors": 2})
X = df[["Move_Num"]].values

kmeans = KMeans(n_clusters=3)
df["Cluster"] = kmeans.fit_predict(X)

plt.scatter(df.index, df["Move_Num"], c=df["Cluster"])
plt.title("Clustering of Player Behavior")
plt.savefig("outputs/clustering_results.png")