# TOC-project-2017

TOC-finalproject
 Code for TOC Project 2017

A telegram bot based on a finite state machine


## Finite State Machine
![fsm](/show-fsm.png)

## Usage
 一開始先將initial state 命名為 `me`. 當 `me` state is triggered to `gogo` 時,需要輸入指令,輸入後，bot會回應你並進去 `user` state,如下列指令所示:

* me state:
	* Input: "hi,我最近想出國玩"
		* Reply: "Hello,你最近想去哪裡玩?"

 接著 `user` state is triggered to `advance`時,依據三個不同的輸入指令,會各自進入3個state,分別為 `europe` state,`asia` state,`northamerica` state,如下列指令所示:

* user state:
	* Input: "歐洲?"
		* Reply: "那英國是個不錯的選擇!"
	* Input: "亞洲?"
		* Reply: "那台灣是個不錯的選擇!"
	* Input: "美洲?"
		* Reply: "那美國是個不錯的選擇!"

  在輸入"歐洲?"後會進入 `europe` state,之後在 `europe` state is triggered to `country_1`時,會請你輸入指令然後進入 `england` state.而在 `england` state時,又is triggered to `scene_1`時,再次輸入指令會在進去下一個  `bigben` state,如下列指令所示:

* europe state:
	* Input: "那就去英國玩吧?"
		* Reply: "有心目中必去的英國景點嗎?"
* england state:
	* Input: "倫敦的大笨鐘!"
		* Reply: "ok,馬上為你安排去英國的行程"
* bigben state:end.

  在輸入"亞洲?"後會進入 `asia` state,之後在 `asia` state is triggered to `country_2`時,會請你輸入指令然後進入 `taiwan` state.而在 `taiwan` state時,又is triggered to `scene_2`時,再次輸入指令會在進去下一個  `mount_ali` state,如下列指令所示:

* asia state:
	* Input: "那就去台灣玩吧?"
		* Reply: "有心目中必去的台灣景點嗎?"
* taiwan state:
	* Input: "阿里山"
		* Reply: "ok,馬上為你安排去台灣的行程"
* mount_ali state:end.	

  在輸入"美洲?"後會進入 `northamerica` state,在 `northamerica` state is triggered to `country_3`時,會請你輸入指令然後進入 `usa` state.而在 `usa` state時,又is triggered to `scene_3`時,再次輸入指令會在進去下一個  `statue_of_liberty` state,如下列指令所示:

* northamerica state:
	* Input: "那就去英國玩吧?"
		* Reply: "有心目中必去的美國景點嗎?"
* usa state:
	* Input: "倫敦的大笨鐘!"
		* Reply: "ok,馬上為你安排去美國的行程"
* statue_ of _liberty state:end.

## 作者
[林軒毅](https://github.com/we999750)
