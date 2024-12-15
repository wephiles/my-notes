在机器学习领域中，可视化是十分重要的。在开始一项新任务时，通过可视化手段探索数据能更好地帮助人们把握数据的要点。在分析模型表现和模型报告的结果时，可视化能使分析显得更加生动鲜明。有时候，为了理解复杂的模型，我们还可以将高维空间映射为视觉上更直观的二维或三维图形。

总而言之，可视化是一个相对快捷的从数据中挖掘信息的手段。本文将使用 Pandas、Matplotlib、seaborn 等流行的库

# 1、 单变量可视化

单变量（univariate）分析一次只关注一个变量。当我们独立地分析一个特征时，通常最关心的是该特征值的分布情况。下面考虑不同统计类型的变量，以及相应的可视化工具。

-   数量特征：数量特征（quantitative feature）的值为有序数值。这些值可能是离散的，例如整数，也可能是连续的，例如实数。

## 1.1 直方图和密度图

直方图依照相等的间隔将值分组为柱，它的形状可能包含了数据分布的一些信息，如高斯分布、指数分布等。当分布总体呈现规律性，但有个别异常值时，你可以通过直方图辨认出来。当你使用的机器学习方法预设了某一特定分布类型（通常是高斯分布）时，知道特征值的分布是非常重要的。最简单的查看数值变量分布的方法是使用 `DataFrame `的 [ *`hist()`*](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.hist.html) 方法绘制直方图。密度图（density plots），也叫核密度图（kernel density estimate，KDE）是理解数值变量分布的另一个方法。它可以看成是直方图平滑（smoothed）的版本。相比直方图，它的主要优势是不依赖于柱的尺寸，更加清晰。

```python
features = ['Total day minutes', 'Total intl calls']
df[features].hist(figsize=(10, 4))
```

![image-20241113200615055](./assets/image-20241113200615055.png)

为上面两个变量建立密度图：

```python
df[features].plot(
    kind="density",
    subplots=True,
    layout=(1, 2),
    sharex=True,
    figsize=(10, 4),
    legend=False,
    title=features,
)
```

![image-20241113201739067](./assets/image-20241113201739067.png)
当然，还可以使用 seaborn 的 [ *`distplot()`*](https://seaborn.pydata.org/generated/seaborn.distplot.html) 方法观测数值变量的分布。例如，Total day minutes 每日通话时长 的分布。默认情况下，该方法将同时显示直方图和密度图。

```python
sns.distplot(df['Total intl calls'])
```

![image-20241113202059009](./assets/image-20241113202059009.png)

上图中直方图的柱形高度已进行归一化处理，表示的是密度而不是样本数。

## 1.2 箱型图

箱形图的主要组成部分是箱子（box），须（whisker）和一些单独的数据点（离群值），分别简单介绍如下：

-   箱子显示了分布的四分位距，它的长度由 25th,（Q1，下四分位数）25*t**h*,（Q1，下四分位数） 和 75th,（Q3，上四分位数）75*t**h*,（Q3，上四分位数） 决定，箱中的水平线表示中位数 （5050）。
-   须是从箱子处延伸出来的线，它们表示数据点的总体散布，具体而言，是位于区间 （Q1−1.5⋅IQR,Q3+1.5⋅IQR）（Q1−1.5⋅IQR,Q3+1.5⋅IQR）的数据点，其中 IQR=Q3−Q1IQR=Q3−Q1，也就是四分位距。
-   离群值是须之外的数据点，它们作为单独的数据点，沿着中轴绘制。

使用 `seaborn `的 `boxplot()` 方法绘制箱形图。

```python
sns.boxplot(x='Total intl calls', data=df)
```

![image-20241113202416966](./assets/image-20241113202416966.png)

上图表明，在该数据集中，大量的国际呼叫是相当少见的。

## 1.3 提琴型图

提琴形图和箱形图的区别是，提琴形图聚焦于平滑后的整体分布，而箱形图显示了单独样本的特定统计数据。

使用 `violinplot()` 方法绘制提琴形图。下图左侧是箱形图，右侧是提琴形图。

```python
_, axes = plt.subplots(1, 2, sharey=True, figsize=(6, 4))
sns.boxplot(data=df['Total intl calls'], ax=axes[0])
sns.violinplot(data=df['Total intl calls'], ax=axes[1])
```

![image-20241113203024364](./assets/image-20241113203024364.png)

## 1.4 数据描述

除图形工具外，还可以使用 DataFrame 的 [ *`describe()`*](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.describe.html) 方法来获取分布的精确数值统计。

```python
df[features].describe()
```

`describe()` 的输出基本上是自解释性的，25%，50% 和 75% 是相应的百分数。

## 1.5 类别特征和二元特征

类别特征（categorical features take）反映了样本的某个定性属性，它具有固定数目的值，每个值将一个观测数据分配到相应的组，这些组称为类别（category）。如果类别变量的值具有顺序，称为有序（ordinal）类别变量。

二元（binary）特征是类别特征的特例，其可能值有 2 个。

### 1.5.1 频率表

使用 [ *`value_counts()`*](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.value_counts.html) 方法得到一张频率表。

```python
df['Churn'].value_counts()
```

上表显示，该数据集的 Churn 有 2850 个属于 False（Churn==0），有 483 个属于 True（Churn==1），数据集中忠实客户（Churn==0）和不忠实客户（Churn==1）的比例并不相等。我们将在以后的文章中看到，这种数据不平衡的情况会导致建立的分类模型存在一定的问题。在这种情况下，构建分类模型可能需要加重对「少数数据（在这里是 Churn==1）分类错误」这一情况的惩罚。

### 1.5.2 条形图

频率表的图形化表示是条形图。创建条形图最简单的方法是使用 seaborn 的 [ *`countplot()`*](https://seaborn.pydata.org/generated/seaborn.countplot.html) 函数。

```python
_, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 4))

sns.countplot(x='Churn', data=df, ax=axes[0])
sns.countplot(x='Customer service calls', data=df, ax=axes[1])
```

![image-20241113203730461](./assets/image-20241113203730461.png)

条形图和直方图的区别如下：

-   直方图适合查看数值变量的分布，而条形图用于查看类别特征。
-   直方图的 X 轴是数值；条形图的 X 轴可能是任何类型，如数字、字符串、布尔值。
-   直方图的 X 轴是一个笛卡尔坐标轴；条形图的顺序则没有事先定义。

上左图清晰地表明了目标变量的失衡性。上右图则表明大部分客户最多打了 2-3 个客服电话就解决了他们的问题。不过，既然想要预测少数数据的分类（Churn==1），我们可能对少数不满意的客户的表现更感兴趣。所以让我们尝试一下更有趣的可视化方法：多变量可视化，看能否对预测有所帮助。

# 2、 多变量可视化

多变量（multivariate）图形可以在单张图像中查看两个以上变量的联系，和单变量图形一样，可视化的类型取决于将要分析的变量的类型。

## 2.1 相关矩阵

相关矩阵可揭示数据集中的数值变量的相关性。这一信息很重要，因为有一些机器学习算法（比如，线性回归和逻辑回归）不能很好地处理高度相关的输入变量。

首先，我们使用 DataFrame 的 [ *`corr()`*](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.corr.html) 方法计算出每对特征间的相关性。接着，我们将所得的相关矩阵（correlation matrix）传给 seaborn 的 [ *`heatmap()`*](https://seaborn.pydata.org/generated/seaborn.heatmap.html)方法，该方法根据提供的数值，渲染出一个基于色彩编码的矩阵。

```python
# 丢弃非数值列
numerical = list(
    set(df.columns)
    - set(
        [
            "State",
            "International plan",
            "Voice mail plan",
            "Area code",
            "Churn",
            "Customer service calls",
        ]
    )
)

# 计算和绘图
correct_matrix = df[numerical].corr()
sns.heatmap(correct_matrix)
```

![image-20241114192540205](./assets/image-20241114192540205.png)

上图中，Total day charge 日话费总额 是直接基于 Total day minutes 电话的分钟数 计算得到，它被称为因变量。除了 Total day charge 外，还有 3 个因变量：Total eve charge，Total night charge，Total intl charge。这 4 个因变量并不贡献任何额外信息，我们直接去除。

![image-20241114192929282](./assets/image-20241114192929282.png)

```python
numerical = list(
    set(numerical)
    - set(
        [
            "Total day charge",
            "Total eve charge",
            "Total night charge",
            "Total intl charge",
        ]
    )
)
corr_matrix = df[numerical].corr()
sns.heatmap(corr_matrix)
```

![image-20241114193457965](./assets/image-20241114193457965.png)

## 2.2 散点图

散点图（scatter plot）将两个数值变量的值显示为二维空间中的笛卡尔坐标（Cartesian coordinate）。通过 matplotlib 库的 [ *`scatter()`*](https://matplotlib.org/devdocs/api/_as_gen/matplotlib.pyplot.scatter.html) 方法可以绘制散点图。

```python
plt.scatter(df['Total day minutes'], df['Total night minutes'])
```

![image-20241114193713165](./assets/image-20241114193713165.png)

我们得到了两个正态分布变量的散点图，看起来这两个变量并不相关，因为上图的形状和轴是对齐的。

seaborn 库的 [ *`jointplot()`*](https://seaborn.pydata.org/generated/seaborn.jointplot.html) 方法在绘制散点图的同时会绘制两张直方图，某些情形下它们可能会更有用。

```python
sns.jointplot(x='Total day minutes', y='Total night minutes', data=df, kind='scatter')
```

![image-20241114193854330](./assets/image-20241114193854330.png)

`jointplot()` 方法还可以绘制平滑过的散点直方图。

```python
sns.jointplot(
    x="Total day minutes", y="Total night minutes", data=df, kind="kde", color="g"
)
```

![image-20241114194112366](./assets/image-20241114194112366.png)

## 2.3 散点图矩阵

在某些情形下，我们可能想要绘制如下所示的散点图矩阵（scatterplot matrix）。它的对角线包含变量的分布，并且每对变量的散点图填充了矩阵的其余部分。

```python
%config InlineBackend.figure_format = 'png'
sns.pairplot(df[numerical])
```

![output](./assets/output.png)

## 2.4 数量和类别

为了让图形更有趣一点，可以尝试从数值和类别特征的相互作用中得到预测 Churn 的新信息，更具体地，让我们看看输入变量和目标变量 Churn 的关系。使用 [ *`lmplot()`*](https://seaborn.pydata.org/generated/seaborn.lmplot.html) 方法的 hue 参数来指定感兴趣的类别特征。

```python
sns.lmplot(
    x="Total day minutes", y="Total night minutes", data=df, hue="Churn", fit_reg=False
)
```

![image-20241114195442233](./assets/image-20241114195442233.png)

看起来不忠实客户偏向右上角，也就是倾向于在白天和夜间打更多电话的客户。当然，这不是非常明显，我们也不会基于这一图形下任何确定性的结论。

现在，创建箱形图，以可视化忠实客户（Churn=0）和离网客户（Churn=1）这两个互斥分组中数值变量分布的统计数据。

```python
# 有时我们可以将有序变量作为数值变量分析
numerical.append('Customer service calls')

fig, axes = plt.subplots(nrows=3, ncols=4, figsize=(10, 7))
for idx, feat in enumerate(numerical):
    ax =axes[int(idx/4), idx%4]
    sns.boxplot(x='Churn', y=feat, data=df, ax=ax)
    ax.set_xlabel('')
    ax.set_ylabel(feat)
fig.tight_layout()
```

![image-20241114200117832](./assets/image-20241114200117832.png)

上面的图表表明，两组之间分歧最大的分布是这三个变量：Total day minutes 日通话分钟数、Customer service calls 客服呼叫数、Number vmail messages 语音邮件数。在后续的课程中，我们将学习如何使用随机森林（Random Forest）或梯度提升（Gradient Boosting）来判定特征对分类的重要性，届时可以清晰地看到，前两个特征对于离网预测模型而言确实非常重要。

创建箱型图和提琴形图，查看忠实客户和不忠实客户的日通话分钟数。

```python
_, axes = plt.subplots(1, 2, sharey=True, figsize=(10, 4))

sns.boxplot(x="Churn", y="Total day minutes", data=df, ax=axes[0])
sns.violinplot(x="Churn", y="Total day minutes", data=df, ax=axes[1])
```

![image-20241114201343570](./assets/image-20241114201343570.png)

上图表明，不忠实客户倾向于打更多的电话。

我们还可以发现一个有趣的信息：平均而言，离网客户是通讯服务更活跃的用户。或许是他们对话费不满意，所以预防离网的一个可能措施是降低通话费。当然，公司需要进行额外的经济分析，以查明这样做是否真的有利。

当想要一次性分析两个类别维度下的数量变量时，可以用 seaborn 库的 [ *`catplot()`*](https://seaborn.pydata.org/generated/seaborn.factorplot.html) 函数。例如，在同一图形中可视化 Total day minutes 日通话分钟数 和两个类别变量（Churn 和 Customer service calls）的相互作用。

```python
sns.catplot(
    x="Churn",
    y="Total day minutes",
    col="Customer service calls",
    data=df[df["Customer service calls"] < 8],
    kind="box",
    col_wrap=4,
    height=3,
    aspect=0.8,
)
```

![image-20241114202104918](./assets/image-20241114202104918.png)

上图表明，从第 4 次客服呼叫开始，Total day minutes 日通话分钟数 可能不再是客户离网（Churn==1）的主要因素。也许，除了我们之前猜测的话费原因，还有其他问题导致客户对服务不满意，这可能会导致日通话分钟数更少。

## 2.5 类别与类别

正如之前提到的，变量 Customer service calls 客服呼叫数 的重复值很多，因此，既可以看成数值变量，也可以看成有序类别变量。之前已通过计数图（count plot）查看过它的分布了，现在我们感兴趣的是这一有序特征和目标变量 Churn 离网率 之间的关系。使用 `countplot()` 方法查看客服呼叫数的分布，这次传入 `hue=Churn` 参数，以便在图形中加入类别维度。

```python
sns.countplot(x="Customer service calls", hue="Churn", data=df)
```

![image-20241114202357441](./assets/image-20241114202357441.png)

## 2.6 交叉表

除了使用图形进行类别分析之外，还可以使用统计学的传统工具：交叉表（cross tabulation），即使用表格形式表示多个类别变量的频率分布。通过它可以查看某一列或某一行以了解某个变量在另一变量的作用下的分布情况。

通过交叉表查看 Churn 离网率 和类别变量 State 州 的关系。

```python
pd.crosstab(df['State'], df['Churn']).T
```

上表显示，State 州 有 51 个不同的值，并且每个州只有 3 到 17 个客户抛弃了运营商。通过 `groupby()` 方法计算每个州的离网率，由高到低排列。

```python
df.groupby(['State'])['Churn'].agg([np.mean]).sort_values(by='mean', ascending=False).T
```

上表显示，新泽西和加利福尼亚的离网率超过了 25%，夏威夷和阿拉斯加的离网率则不到 6%。然而，这些结论是基于极少的样本得出的，可能仅适用于这一特定数据集，不太具有泛用性。

# 3、 全局数据集可视化

上面我们一直在研究数据集的不同方面（facet），通过猜测有趣的特征并一次选择少量特征进行可视化。如果我们想一次性显示所有特征并仍然能够解释生成的可视化，该怎么办？

## 3.1 降维

大多数现实世界的数据集有很多特征，每一个特征都可以被看成数据空间的一个维度。因此，我们经常需要处理高维数据集，然而可视化整个高维数据集相当难。为了从整体上查看一个数据集，需要在不损失很多数据信息的前提下，降低用于可视化的维度。这一任务被称为降维（dimensionality reduction）。降维是一个无监督学习（unsupervised learning）问题，因为它需要在不借助任何监督输入（如标签）的前提下，从数据自身得到新的低维特征。

**主成分分析（Principal Component Analysis, PCA）**是一个著名的降维方法，我们会在之后的课程中讨论它。但主成分分析的局限性在于，它是线性（linear）算法，这意味着对数据有某些特定的限制。

与线性方法相对的，有许多**非线性方法**，统称流形学习（Manifold Learning）。著名的流形学习方法之一是 t-SNE。

## 3.2 `t-SNE`

它的基本思路很简单：为高维特征空间在二维平面（或三维平面）上寻找一个投影，使得在原本的 n 维空间中相距很远的数据点在二维平面上同样相距较远，而原本相近的点在平面上仍然相近。

该数据库创建一个 t-SNE 表示，首先加载依赖。

```python
# pip install scikit-learn
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler
```

去除 State 州 和 Churn 离网率 变量，然后用 [ *`pandas.Series.map()`*](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.map.html) 方法将二元特征的「Yes」/「No」转换成数值。 

```python
X = df.drop(["Churn", "State"], axis=1)
X['International plan'] = X['International plan'].map({'Yes': 1, 'No': 0})
X['Voice mail plan'] = X['Voice mail plan'].map({'Yes': 1, 'No': 0})
```

使用 `StandardScaler()` 方法来完成归一化数据，即从每个变量中减去均值，然后除以标准差。

```python
scaler = StandardScaler()
X_scaler = scaler.fit_transform(X)
```

现在可以构建 t-SNE 表示了。

```python
tsne = TSNE(random_state=17)
tsne_repr = tsne.fit_transform(X_scaler)
```

然后以图形的方式可视化。

```python
plt.scatter(tsne_repr[:, 0], tsne_repr[:, 1], alpha=.5)
```

![image-20241114210122087](./assets/image-20241114210122087-1731589283710-1.png)

根据离网情况给 t-SNE 表示加上色彩（蓝色表示忠实用户，黄色表示不忠实用户），形成离网情况散点图。

```python
plt.scatter(
    tsne_repr[:, 0],
    tsne_repr[:, 1],
    c=df["Churn"].map({False: "blue", True: "orange"}),
    alpha=0.5,
)
```

![image-20241114210215374](./assets/image-20241114210215374.png)

可以看到，离网客户集中在低维特征空间的一小部分区域。为了更好地理解这一图像，可以使用剩下的两个二元特征，即 International plan 国际套餐 和 Voice mail plan 语音邮件套餐 给图像着色，蓝色代表二元特征的值为 Yes，黄色代表二元特征的值为 No。

```python
_, axes = plt.subplots(1, 2, sharey=True, figsize=(12, 5))

for i, name in enumerate(['International plan', 'Voice mail plan']):
    axes[i].scatter(tsne_repr[:, 0], tsne_repr[:, 1],
                    c=df[name].map({'Yes': 'orange', 'No': 'blue'}), alpha=.5)
    axes[i].set_title(name)
```

![image-20241114210328792](./assets/image-20241114210328792.png)

通过上面 3 张图，我们就可以更直观的分析客户的离网原因了。

最后，了解下 t-SNE 的缺陷。

-   计算复杂度高。如果你有大量样本，你应该使用 [ *Multicore-TSNE*](https://github.com/DmitryUlyanov/Multicore-TSNE)。
-   随机数种子的不同会导致图形大不相同，这给解释带来了困难。通常而言，你不应该基于这些图像做出任何决定性的结论，因为它可能和单纯的猜测差不多。当然，t-SNE 图像中的某些发现可能会启发一个想法，这个想法可以通过更全面深入的研究得到确认。

# 4、 练习-心血管疾病数据探索分析

### 初步数据分析

首先，导入挑战所需模块：

```python
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker
from matplotlib import rcParams
import warnings
warnings.filterwarnings('ignore')
```

本次挑战将优先选择 `Seaborn `用于绘图，下面我们定义 `Seaborn` 全局绘图参数，保证后续图像更加整洁美观。

```python
sns.set()
sns.set_context(
    "notebook",
    font_scale=1.5,
    rc={
        "figure.figsize": (11, 8),
        "axes.titlesize": 18
    }
)

rcParams['figure.figsize'] = 11, 8
```

接下来，读取并预览数据集。

```python
df = pd.read_csv(
    'https://labfile.oss.aliyuncs.com/courses/1283/mlbootcamp5_train.csv', sep=';')
print('Dataset size: ', df.shape)
df.head()
```

数据集特征表示如下：

| Feature                                       | Variable Type       | Variable    | Value Type                                       |
| --------------------------------------------- | ------------------- | ----------- | ------------------------------------------------ |
| Age                                           | Objective Feature   | age         | int (days)                                       |
| Height                                        | Objective Feature   | height      | int (cm)                                         |
| Weight                                        | Objective Feature   | weight      | float (kg)                                       |
| Gender                                        | Objective Feature   | gender      | categorical code                                 |
| Systolic blood pressure                       | Examination Feature | ap_hi       | int                                              |
| Diastolic blood pressure                      | Examination Feature | ap_lo       | int                                              |
| Cholesterol                                   | Examination Feature | cholesterol | 1: normal, 2: above normal, 3: well above normal |
| Glucose                                       | Examination Feature | gluc        | 1: normal, 2: above normal, 3: well above normal |
| Smoking                                       | Subjective Feature  | smoke       | binary                                           |
| Alcohol intake                                | Subjective Feature  | alco        | binary                                           |
| Physical activity                             | Subjective Feature  | active      | binary                                           |
| Presence or absence of cardiovascular disease | Target Variable     | cardio      | binary                                           |

所以数据均为医学检查时收集，主要包含 3 种类别的特征：

-   Objective Feature: 基础事实数据。
-   Examination Feature: 体检结果。
-   Subjective Feature: 患者给出的主观信息。

接下来，我们探索数据值分布情况。这里使用 [`catplot()`](https://seaborn.pydata.org/generated/seaborn.catplot.html) 绘制出变量特征的计数条形图。

```python
df_uniques = pd.melt(frame=df, value_vars=['gender', 'cholesterol',
                                           'gluc', 'smoke', 'alco',
                                           'active', 'cardio'])
df_uniques = pd.DataFrame(df_uniques.groupby(['variable',
                                              'value'])['value'].count()) \
    .sort_index(level=[0, 1]) \
    .rename(columns={'value': 'count'}) \
    .reset_index()

sns.catplot(x='variable', y='count', hue='value',
            data=df_uniques, kind='bar', height=12)
```

接下来，让我们按目标值分割数据集，这样往往可以通过绘图结果快速找出相对重要的特征。

```python
df_uniques = pd.melt(frame=df, value_vars=['gender', 'cholesterol',
                                           'gluc', 'smoke', 'alco',
                                           'active'], id_vars=['cardio'])
df_uniques = pd.DataFrame(df_uniques.groupby(['variable', 'value',
                                              'cardio'])['value'].count()) \
    .sort_index(level=[0, 1]) \
    .rename(columns={'value': 'count'}) \
    .reset_index()

sns.catplot(x='variable', y='count', hue='value',
            col='cardio', data=df_uniques, kind='bar', height=9)
```

您可以看到胆固醇和葡萄糖水平对目标变量影响明显较大。这是巧合吗？

接下来，你需要自行补充必要的代码来回答相应的挑战问题。

------

### 进一步观察

 *问题：*数据集中有多少男性和女性？由于 `gender` 特征没有说明男女，你需要通过分析身高计算得出。

-   [ A ] 45530 女性 和 24470 男性
-   [ B ] 45530 男性 和 24470 女性
-   [ C ] 45470 女性 和 24530 男性
-   [ D ] 45470 男性 和 24530 女性

```python

```

 *问题：*数据集中男性和女性，哪个群体饮酒的频次更高？

-   [ A ] 女性
-   [ B ] 男性

```python

```

 *问题：*数据集中男性和女性吸烟者所占百分比的差值是多少？

-   [ A ] 4
-   [ B ] 16
-   [ C ] 20
-   [ D ] 24

```python

```

 *问题：*数据集中吸烟者和非吸烟者的年龄中位数之间的差值（以月计）近似是多少？你需要尝试确定出数据集中 `age` 合理的表示单位。

-   [ A ] 5
-   [ B ] 10
-   [ C ] 15
-   [ D ] 20

本次挑战规定 1 年为 365.25 天。

```python

```

### 风险量表图

欧洲心脏病学会的网站上给出了 [ *SCORE scale*](https://www.escardio.org/Education/Practice-Tools/CVD-prevention-toolbox/SCORE-Risk-Charts) 量表。它可以用于计算未来 10 年心血管疾病死亡的风险。

![img](./assets/uid214893-20190505-1557034697564.png)

让我们来看看最右上角的矩形，也就是 60 到 65 岁的吸烟男性的子集。其中，矩形的左下角看到一个值 9，在右上角看到 47。量表意味着对于收缩压（纵坐标）低于 120 （正常血压）的性别年龄组的人来说，心血管疾病的风险估计比收缩压为 [160,180)[160,180) 的患者（高血压）低 5 倍（47/9）。

接下来，让我们结合量表，并利用挑战数据集进行计算。这里需要注意的是，量表中胆固醇（Cholesterol）水平和挑战数据单位不太一样，我们使用对应关系为：`4 mmol/l` →→ `1`, `5-7 mmol/l` →→ `2`, `8 mmol/l` →→ `3`。

 *问题：*计算 [60,65)[60,65) 年龄区间下，较健康人群（胆固醇类别 1，收缩压低于 120）与高风险人群（胆固醇类别为 3，收缩压 [160,180)[160,180)）各自心血管病患所占比例。并最终求得二者比例的近似倍数。

-   [ A ] 1
-   [ B ] 2
-   [ C ] 3
-   [ D ] 4

```python

```

选择 [60,65)[60,65) 年龄区间：

```python
smoking_old_men = df[(df['gender'] == 2) & (df['age_years'] >= 60)
                     & (df['age_years'] < 65) & (df['smoke'] == 1)]
smoking_old_men[(smoking_old_men['cholesterol'] == 1) &
                (smoking_old_men['ap_hi'] < 120)]['cardio'].mean()
```

胆固醇类别为 1，收缩压低于 120，心血管疾病患者的比例为 26%。

```python
smoking_old_men[(smoking_old_men['cholesterol'] == 3) &
                (smoking_old_men['ap_hi'] >= 160) &
                (smoking_old_men['ap_hi'] < 180)]['cardio'].mean()
```

胆固醇类别为 3，收缩压 [160,180)[160,180)，心血管疾病患者的比例为 86%。

所以，挑战数据给出的比例大约是 0.860.26≈30.260.86≈3 倍，而量表给出的是 5 倍。当然，这依赖与给定年龄组中的病人比例。

### BMI 指数分析

挑战将需要创建一个新的特征 BMI，BMI 为身高体重指数，其可以反映体重的标准情况，计算公式为：

BMI=weight(kg)height2(m)*B**M**I*=*h**e**i**g**h**t*2(*m*)*w**e**i**g**h**t*(*k**g*)

正常 BMI 指数一般在 18.5 到 25 之间。

 *问题：*请选择下面叙述正确的有：

-   [ A ] 数据集样本中 BMI 中位数在正常范围内。
-   [ B ] 女性的平均 BMI 指数高于男性。
-   [ C ] 健康人群的 BMI 平均高于患病人群。
-   [ D ] 健康和不饮酒男性中，BMI 比健康不饮酒女性更接近正常值。

```python

```

### 数据清洗

你可能会注意到给出的数据并不够完美，在进一步可视化之前，我们需要对数据进行清洗。

 *问题：*请按照以下列举的项目，过滤掉数据中统计有误的部分：

-   血压特征中，舒张压高于收缩压的样本。
-   身高特征中，低于 2.5％ 分位数的样本。
-   身高特征中，高于 97.5％ 分位数的样本。
-   体重特征中，低于 2.5％ 分位数的样本。
-   体重特征中，高于 97.5％ 分位数的样本。

百分位数请使用 `pd.Series.quantile` 方法进行确定，不熟悉可以阅读 [ *官方文档*](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.quantile.html)

```python

```

 *问题：*清洗掉的数据占原数据总量的近似百分比？

-   [ A ] 8%
-   [ B ] 9%
-   [ C ] 10%
-   [ D ] 11%

```python

```

### 数据可视化分析

要更好地理解数据集特征，接下来使用过滤之后的数据创建特征之间相关系数的矩阵。

 *问题：*使用 [`heatmap()`](http://seaborn.pydata.org/generated/seaborn.heatmap.html) 绘制特征之间的皮尔逊相关性系数矩阵。

```python

```

 *问题：*以下哪组特征与性别的相关性更强？

-   [ A ] Cardio, Cholesterol
-   [ B ] Height, Smoke
-   [ C ] Smoke, Alco
-   [ D ] Height, Weight

### 男女身高分布

前面的探索中，我们知道性别对应 1 和 2，虽然不知道不同性别对应哪个值，但可以通过平均身高和体重来确定。

 *问题：*绘制身高和性别之间的小提琴图 [`violinplot()`](https://seaborn.pydata.org/generated/seaborn.violinplot.html)。

这里建议通过 `hue` 参数按性别划分，并通过 `scale` 参数来计算性别对应的具体数量。为了便于你能正确绘制，这里给出一个 [ *参考示例*](https://stackoverflow.com/questions/41573283/seaborn-violin-plot-with-one-data-per-column/41575149#41575149)。

```python

```

 *问题：*绘制身高和性别之间的核密度图 [`kdeplot`](https://seaborn.pydata.org/generated/seaborn.kdeplot.html)。

通过核密度图可以更清楚地看到性别之间的差异，但却无法得到每个性别对应的具体人数。

```python

```

大多数情况下，皮尔逊相关性指数可以看出特征之间的相关程度。不过，这里我们进一步绘制 [ *Spearman's rank correlation coefficient*](https://en.wikipedia.org/wiki/Spearman's_rank_correlation_coefficient) 斯皮尔曼等级相关系数对应的图像。它利用单调方程评价两个统计变量的相关性，是用于衡量两个变量的依赖性的非参数指标。

 *问题：*使用 [`heatmap()`](http://seaborn.pydata.org/generated/seaborn.heatmap.html) 绘制特征之间的斯皮尔曼等级相关系数矩阵。

```python

```

 *问题：*下列那一组特征具有最强的 Spearman 相关性？

-   [ A ] Height, Weight
-   [ B ] Age, Weight
-   [ C ] Cholesterol, Gluc
-   [ D ] Cardio, Cholesterol
-   [ E ] Ap_hi, Ap_lo
-   [ F ] Smoke, Alco

### 年龄可视化

上面，我们已经计算过受访者的年龄。接下来，我们对其进行可视化。

 *问题：*请使用 [`countplot()`](http://seaborn.pydata.org/generated/seaborn.countplot.html) 绘制年龄分布计数图，横坐标为年龄，纵坐标为对应的人群数量。

```python

```

 *问题：*在哪个年龄下，心血管疾病患者人数首次超过无心血管疾病患者人数？

-   [ A ] 44
-   [ B ] 55
-   [ C ] 64
-   [ D ] 70

















































































































































































































































































































