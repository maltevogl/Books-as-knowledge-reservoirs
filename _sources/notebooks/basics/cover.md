# Tools for the book

To follow the book on your own computer, you will need to install some tools. Additionally, if you want to share your code or work in collaboration with others, e.g. during a code-sprint, consider some of the other tools below. 

## Tools

  - __Python__ (because it is nice to us!)
  - __Jupyter Notebooks__, the swiss-army-knive of DH

If you want to use this book in a collaborative setting, consider also

  - __Cloud services__ (e.g. Nextcloud or Seafile) to share files
  - __Slack__ to chat while solving problems

## Python

  - Install Python using Anaconda: [URL](https://www.anaconda.com/distribution/)

  ```python
  import pandas as pd
  import numpy as np

  df = pd.DataFrame(
      np.random.randn(1000, 4),
      columns=['A', 'B', 'C', 'D']
      )

  df.plot()
  ```

## JupyterLab

  - To edit Jupyter Notebooks, use JupyterLab (comes bundled with Anaconda, or install standalone)

  ![JupyterLab](assets/JupyterLab.png)

## Cloud Services

  - Based on open source software, e.g Seafile or Nextcloud, often found at universities
  - For sharing files between project partners
  - Login e.g. with your institutions account

  ![HU Box](assets/hubox.png)


## Slack/RocketChat/...

  - Chat-App with rooms for different topics
  - Join with your email (invitation mail necessary)

  ![Slack](assets/slack.png)
