This repo is for chatglm3-6b language filter. Chatglm3-6b generates mixed languages in generation, so filter out words from another language to keep the generation clean. 

Usage: Replace .py files in chatglm-6b using files in this repo, and move chinese-150000 and english-150000 to that repo too.

``CUDA_VISIBLE_DEVICES=* python test.py``

First lines of test.py contains params for chat generation.  

Example:

输入(chat模式）：
``Indonesia Geography  ``

添加filter前：
>Indonesia is a country located in Southeast Asia, bordered by the Pacific Ocean to the northwest, the Indian Ocean to the southwest, and the Java Sea to the east.
It is the world's fourth most populous country, with a population of over 273 million people.

The geography of Indonesia is diverse, with a range of landscapes, including rainforests, savannas, beaches, mountains, and plateaus. The country is home to more th
an 17,500 islands, with the largest island being Sumatra and the smallest being Bintan.

The capital city of Indonesia is Jakarta, located on the island of Java. Other major cities in the country include Bali, Surabaya, and雅加达。

添加filter后：
 >Indonesia is a country located in Southeast Asia, bordered by the Pacific Ocean to the east and the Indian Ocean to the west. It is the world's fourth moss country, with a population of over 273 million people.

The geography of Indonesia is diverse, with a range of mountains, forests, islands, and coastal regions. The country's highest peak is Mount Bromo, an active volcan
o located in the east of the island of Java. The coastline of Indonesia is long and varied, with stretches of sandy beaches, rocky cliffs, and Exclusive Economic Zo
nes (EEZs) that protect the country's marine resources.

Indonesia is made up of more than 19,000 islands, with the largest ones being Sumatra and Borneo. The country is home to a rich and diverse array of flora and fauna
, including orangutans, tigers, elephants, and the world's largest mammal, the Javan rhinoceros.``

添加中文filter:

> |梗概 |                                                                                                                                                  

* 印度尼西亚位于亚洲东南部，拥有丰富的自然资源和生物多样性
* 印度尼西亚是世界上面积最大的岛屿国家，拥有超过1900个岛屿，其中最大的岛屿是巴厘岛
* 该国拥有多样化的地形，包括热带雨林、草原、沼泽、山脉、沙漠和海滩
* 印度尼西亚的气候分为热带雨林气候、热带草原气候、热带沙漠气候和亚热带海洋性气候

|主要岛屿和地区 |

* 巴厘岛：印度尼西亚最著名的岛屿，以其美丽的海滩、寺庙和热带雨林而闻名
* 千岛湖：位于爪哇岛北部，是一个受欢迎的旅游胜地，有许多岛屿和海滩
* 加里曼岛：位于苏门答腊岛，是印度尼西亚最大的岛屿之一，以其美丽的海滩和热带雨林而闻名
* 伊尔内岛：位于苏门答腊岛东南部，是一个未被开发的岛屿，据说有许多野生动物和美丽的海滩
* 东加里曼岛：位于东苏门答腊岛，是一个较小的岛屿，以其美丽的海滩和珊瑚礁而闻名

|地理特征 |

* 河流：印度尼西亚有许多河流，其中最长的河流是伊洛河
* 山脉：印度尼西亚有许多山脉，其中最高的山脉是巴厘岛山脉
* 沙漠：印度尼西亚的沙漠主要位于西部和北部，包括爪哇岛和苏门答腊岛
* 海岸线：印度尼西亚拥有丰富的海岸线，包括沙滩、珊瑚礁、海峡和海岛。

