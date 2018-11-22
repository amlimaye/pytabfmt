# pytabfmt

A simple formatter for LaTeX tables. Example of use:

```python
import pytabfmt as ptf
tbl = ptf.LatexTable(['Teacher', 'Student 1', 'Student 2', 'Student 3'], ['%s', '%0.2f', '%0.2f', '%0.2f'])
tbl.add_row(['Alex', 3.0, 3.0, 4.0])
tbl.add_row(['Bertha', 2.0, 5.0, 3.0])
tbl.write('my_table.txt')
tbl.print_out()
```

This produces:

```
\begin{tabular}{l|l|l|l}
Teacher & Student 1 & Student 2 & Student 3 \\ \hline
Alex & $3.00$ & $3.00$ & $4.00$  \\
Bertha & $2.00$ & $5.00$ & $3.00$
\end{tabular}
```
