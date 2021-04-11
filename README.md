# JBReactGraph by Agroskin Alexander
Task done for the JetBrains summer internship program application. Visualization of the React project contributor network.

The overall goal of the project is to visualize top 50 of [React](https://github.com/facebook/react) contributors as a network graph. For each two contributos, the more time they have spent together on the project, and the more the files they have worked on overlap, the closer are they going to be in the network.

The solution with detailed step-by-step explanations can be found in the [`task.ipynb`](task.ipynb) file. Additional utils for data preparation can be found in the ['preparation.py'](preparation.py) file, which can be executed through the notebook.

Data preparation itself has been done in advance, and is encoded as JSON in the ['authors.json'](authors.json) file. A cell in the notebook can be uncommented to update the contributor data. A GitHub OAuth token is recommended to get around the rate limiter. Unfortunately, limitations of GitHub API prevent us from updating all the commit info in real time. Because of this, the only way to update commit data is as follows:

1. Clone the [React](https://github.com/facebook/react) repository to your machine
2. Run the following command inside of it: `git log --name-only --oneline --pretty=format:'$ %at %an' > ../git_log.txt`
3. Replace the old [`git_log.txt`](git_log.txt) file with the new one
4. Run the preparation cell in the notebook

To view the resulting network, Jupyter notebook generates an embedded `.html` file ([`react_graph.html`](react_graph.html)). Not all Jupyter viewers allow for embedding of `.html` files. You can use the standard Jupyter Notebook or JupyterLab, or you can change the `notebook` parameter to `False`, and the file will be opened in your browser. You can also open the file manually after running the cell.

That is all, hope I didn't miss anything!
