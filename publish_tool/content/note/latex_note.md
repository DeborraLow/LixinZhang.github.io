Title: 一些Latex备忘
Date: 2015-06-27 13:20
Category: Note

最近在公司要写一些技术文档，选来选取还是觉得用<code>latex</code>或是<code>markdown</code>写最好，因为排版清晰漂亮，又容易编写公式，不会出现格式错乱的情况。对于程序员来说，还有一点好处，就是你可以通过脚本的形式，用程序写文档，比如我就就用python自动把很多字段自动生成了markdown格式的表格，不需要手动去搞了。我个人认为，平常写一些小的tech report用markdown写就很好，如果要写一些正式一点的，需要有目录的长篇文档，还是用latex比较合适，至于office那一套，能抛弃就抛弃吧，太重了。

我不懂latex复杂的东西，这里主要是我平常使用的比较常用的latex笔记，我觉得这些就够了。

###基本latex框架
<pre>
% !Mode:: "TeX:UTF-8"
\documentclass[a4paper,11pt]{article}
\usepackage{CJKutf8}
\usepackage{amsmath}
\usepackage{algorithm}
\usepackage{algorithmic}

\usepackage{listings} %插入代码
\usepackage{xcolor} %代码高亮

%下面一段可以解决mac下中文乱码的问题
\XeTeXlinebreaklocale "zh"
\XeTeXlinebreakskip = 0pt plus 1pt minus 0.1pt
\usepackage[top=1in,bottom=1in,left=1.25in,right=1.25in]{geometry}
\usepackage{float}
\usepackage{fontspec}
\newfontfamily\zhfont[BoldFont=Adobe Heiti Std]{Adobe Song Std}
\newfontfamily\zhpunctfont{Adobe Song Std}
\setmainfont{Times New Roman}
\usepackage{zhspacing}
\zhspacing

\usepackage{graphicx}
\usepackage[unicode]{hyperref} %目录、引用等的跳转
\usepackage{xcolor}
\usepackage{cite}
\usepackage{indentfirst}

\begin{document}
\renewcommand{\contentsname}{目录}  % 将Contents改为目录
\renewcommand{\abstractname}{摘要}  % 将Abstract改为摘要
\renewcommand{\refname}{参考文献}   % 将References改为参考文献
\renewcommand{\indexname}{索引}
\renewcommand{\figurename}{图}
\renewcommand{\tablename}{表}
\renewcommand{\appendixname}{附录}
\renewcommand{\algorithm}{算法}

\title{文档标题}
\author{lixinzhang}
\maketitle
\tableofcontents

\newpage
\section{AAA}
\subsection{aaa}
\subsubsection{bbb}
\section{附录}
\end{document}
</pre>

###常用命令备忘
* 段落，分4个层级，前三个会在目录中显示
    <pre>
\section{AAA}
\subsection{aaa}
\subsubsection{bbb}
\paragraph{ccc}
</pre>
* 脚注
    <pre>
\footnote{}
</pre>
* 引用表格或图片或章节
    <pre>
\ref{}
</pre>
* 引入其他tex文件，比如把section_one.tex文件中的内容导入进来
    <pre>
\input{section_one}
</pre>
* 数学公式
    <pre>
\begin{equation}
\label{binomial}
p(h) = \mu^h(1-\mu)^{(1-h)}
\end{equation}
</pre>
* 图片
    <pre>
\begin{figure}[H]
    \centering
    \includegraphics[width=1.0\textwidth]{figure/log_merge.png}
    \caption{日志拼接示意图}
    \label{fig-log-merge}
\end{figure}
</pre>
* 表格
    <pre>
\begin{table}[H] \normal
    \centering
    \caption{朋友圈Feed属性特征}
    \label{feed-feature}
    \begin{tabular}{c|l|l}
        \hline
        序号 & 特征符号 & 特征描述 \\ \hline \hline
        1 & title category1 & URL Title的分类类目1（取分类结果的Top3） \\ \hline
        2 & title category2 & URL Title的分类类目2 \\ \hline
\hline
    \end{tabular}
\end{table}
</pre>
* 列表，可嵌套
    <pre>
\begin{enumerate}
\item 性别 cross
\item 国家 cross
\item 城市 cross
\item 省份 cross
\item 阅读兴趣cross
    \begin{enumerate}
    \item 主类目，top2阅读兴趣cross
    \item 子类目，top2阅读兴趣cross
    \end{enumerate}
\end{enumerate}
</pre>
* 算法
    <pre>
\begin{lstlisting}[language=SQL]
CREATE TABLE sns_daily_feature_string(
     ds STRING,
     expose INT,
     click INT,
     featurestring STRING
)
\end{lstlisting}
</pre>


