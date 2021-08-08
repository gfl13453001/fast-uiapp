#!/usr/bin/env python
#-*- coding:utf-8 -*-

# authors:guanfl
# 2021/8/5

KEYCODE_SOFT_LEFT = 1

"""

 public static final int KEYCODE_UNKNOWN         = 0;
83    /** Key code constant: Soft Left key.
84     * Usually situated below the display on phones and used as a multi-function
85     * feature key for selecting a software defined function shown on the bottom left
86     * of the display. */
87    public static final int KEYCODE_SOFT_LEFT       = 1;
88    /** Key code constant: Soft Right key.
89     * Usually situated below the display on phones and used as a multi-function
90     * feature key for selecting a software defined function shown on the bottom right
91     * of the display. */
92    public static final int KEYCODE_SOFT_RIGHT      = 2;
93    /** Key code constant: Home key.
94     * This key is handled by the framework and is never delivered to applications. */
95    public static final int KEYCODE_HOME            = 3;
96    /** Key code constant: Back key. */
97    public static final int KEYCODE_BACK            = 4;
98    /** Key code constant: Call key. */
99    public static final int KEYCODE_CALL            = 5;
100    /** Key code constant: End Call key. */
101    public static final int KEYCODE_ENDCALL         = 6;
102    /** Key code constant: '0' key. */
103    public static final int KEYCODE_0               = 7;
104    /** Key code constant: '1' key. */
105    public static final int KEYCODE_1               = 8;
106    /** Key code constant: '2' key. */
107    public static final int KEYCODE_2               = 9;
108    /** Key code constant: '3' key. */
109    public static final int KEYCODE_3               = 10;
110    /** Key code constant: '4' key. */
111    public static final int KEYCODE_4               = 11;
112    /** Key code constant: '5' key. */
113    public static final int KEYCODE_5               = 12;
114    /** Key code constant: '6' key. */
115    public static final int KEYCODE_6               = 13;
116    /** Key code constant: '7' key. */
117    public static final int KEYCODE_7               = 14;
118    /** Key code constant: '8' key. */
119    public static final int KEYCODE_8               = 15;
120    /** Key code constant: '9' key. */
121    public static final int KEYCODE_9               = 16;
122    /** Key code constant: '*' key. */
123    public static final int KEYCODE_STAR            = 17;
124    /** Key code constant: '#' key. */
125    public static final int KEYCODE_POUND           = 18;
126    /** Key code constant: Directional Pad Up key.
127     * May also be synthesized from trackball motions. */
128    public static final int KEYCODE_DPAD_UP         = 19;
129    /** Key code constant: Directional Pad Down key.
130     * May also be synthesized from trackball motions. */
131    public static final int KEYCODE_DPAD_DOWN       = 20;
132    /** Key code constant: Directional Pad Left key.
133     * May also be synthesized from trackball motions. */
134    public static final int KEYCODE_DPAD_LEFT       = 21;
135    /** Key code constant: Directional Pad Right key.
136     * May also be synthesized from trackball motions. */
137    public static final int KEYCODE_DPAD_RIGHT      = 22;
138    /** Key code constant: Directional Pad Center key.
139     * May also be synthesized from trackball motions. */
140    public static final int KEYCODE_DPAD_CENTER     = 23;
141    /** Key code constant: Volume Up key.
142     * Adjusts the speaker volume up. */
143    public static final int KEYCODE_VOLUME_UP       = 24;
144    /** Key code constant: Volume Down key.
145     * Adjusts the speaker volume down. */
146    public static final int KEYCODE_VOLUME_DOWN     = 25;
147    /** Key code constant: Power key. */
148    public static final int KEYCODE_POWER           = 26;
149    /** Key code constant: Camera key.
150     * Used to launch a camera application or take pictures. */
151    public static final int KEYCODE_CAMERA          = 27;
152    /** Key code constant: Clear key. */
153    public static final int KEYCODE_CLEAR           = 28;
154    /** Key code constant: 'A' key. */
155    public static final int KEYCODE_A               = 29;
156    /** Key code constant: 'B' key. */
157    public static final int KEYCODE_B               = 30;
158    /** Key code constant: 'C' key. */
159    public static final int KEYCODE_C               = 31;
160    /** Key code constant: 'D' key. */
161    public static final int KEYCODE_D               = 32;
162    /** Key code constant: 'E' key. */
163    public static final int KEYCODE_E               = 33;
164    /** Key code constant: 'F' key. */
165    public static final int KEYCODE_F               = 34;
166    /** Key code constant: 'G' key. */
167    public static final int KEYCODE_G               = 35;
168    /** Key code constant: 'H' key. */
169    public static final int KEYCODE_H               = 36;
170    /** Key code constant: 'I' key. */
171    public static final int KEYCODE_I               = 37;
172    /** Key code constant: 'J' key. */
173    public static final int KEYCODE_J               = 38;
174    /** Key code constant: 'K' key. */
175    public static final int KEYCODE_K               = 39;
176    /** Key code constant: 'L' key. */
177    public static final int KEYCODE_L               = 40;
178    /** Key code constant: 'M' key. */
179    public static final int KEYCODE_M               = 41;
180    /** Key code constant: 'N' key. */
181    public static final int KEYCODE_N               = 42;
182    /** Key code constant: 'O' key. */
183    public static final int KEYCODE_O               = 43;
184    /** Key code constant: 'P' key. */
185    public static final int KEYCODE_P               = 44;
186    /** Key code constant: 'Q' key. */
187    public static final int KEYCODE_Q               = 45;
188    /** Key code constant: 'R' key. */
189    public static final int KEYCODE_R               = 46;
190    /** Key code constant: 'S' key. */
191    public static final int KEYCODE_S               = 47;
192    /** Key code constant: 'T' key. */
193    public static final int KEYCODE_T               = 48;
194    /** Key code constant: 'U' key. */
195    public static final int KEYCODE_U               = 49;
196    /** Key code constant: 'V' key. */
197    public static final int KEYCODE_V               = 50;
198    /** Key code constant: 'W' key. */
199    public static final int KEYCODE_W               = 51;
200    /** Key code constant: 'X' key. */
201    public static final int KEYCODE_X               = 52;
202    /** Key code constant: 'Y' key. */
203    public static final int KEYCODE_Y               = 53;
204    /** Key code constant: 'Z' key. */
205    public static final int KEYCODE_Z               = 54;
206    /** Key code constant: ',' key. */
207    public static final int KEYCODE_COMMA           = 55;
208    /** Key code constant: '.' key. */
209    public static final int KEYCODE_PERIOD          = 56;
210    /** Key code constant: Left Alt modifier key. */
211    public static final int KEYCODE_ALT_LEFT        = 57;
212    /** Key code constant: Right Alt modifier key. */
213    public static final int KEYCODE_ALT_RIGHT       = 58;
214    /** Key code constant: Left Shift modifier key. */
215    public static final int KEYCODE_SHIFT_LEFT      = 59;
216    /** Key code constant: Right Shift modifier key. */
217    public static final int KEYCODE_SHIFT_RIGHT     = 60;
218    /** Key code constant: Tab key. */
219    public static final int KEYCODE_TAB             = 61;
220    /** Key code constant: Space key. */
221    public static final int KEYCODE_SPACE           = 62;
222    /** Key code constant: Symbol modifier key.
223     * Used to enter alternate symbols. */
224    public static final int KEYCODE_SYM             = 63;
225    /** Key code constant: Explorer special function key.
226     * Used to launch a browser application. */
227    public static final int KEYCODE_EXPLORER        = 64;
228    /** Key code constant: Envelope special function key.
229     * Used to launch a mail application. */
230    public static final int KEYCODE_ENVELOPE        = 65;
231    /** Key code constant: Enter key. */
232    public static final int KEYCODE_ENTER           = 66;
233    /** Key code constant: Backspace key.
234     * Deletes characters before the insertion point, unlike {@link #KEYCODE_FORWARD_DEL}. */
235    public static final int KEYCODE_DEL             = 67;
236    /** Key code constant: '`' (backtick) key. */
237    public static final int KEYCODE_GRAVE           = 68;
238    /** Key code constant: '-'. */
239    public static final int KEYCODE_MINUS           = 69;
240    /** Key code constant: '=' key. */
241    public static final int KEYCODE_EQUALS          = 70;
242    /** Key code constant: '[' key. */
243    public static final int KEYCODE_LEFT_BRACKET    = 71;
244    /** Key code constant: ']' key. */
245    public static final int KEYCODE_RIGHT_BRACKET   = 72;
246    /** Key code constant: '\' key. */
247    public static final int KEYCODE_BACKSLASH       = 73;
248    /** Key code constant: ';' key. */
249    public static final int KEYCODE_SEMICOLON       = 74;
250    /** Key code constant: ''' (apostrophe) key. **/
251    public static final int KEYCODE_APOSTROPHE      = 75;
252    /** Key code constant: '/' key. */
253    public static final int KEYCODE_SLASH           = 76;
254    /** Key code constant: '@' key. */
255    public static final int KEYCODE_AT              = 77;
256    /** Key code constant: Number modifier key.
257     * Used to enter numeric symbols.
258     * This key is not Num Lock; it is more like {@link #KEYCODE_ALT_LEFT} and is
259     * interpreted as an ALT key by {@link android.text.method.MetaKeyKeyListener}. */
260    public static final int KEYCODE_NUM             = 78;
261    /** Key code constant: Headset Hook key.
262     * Used to hang up calls and stop media. */
263    public static final int KEYCODE_HEADSETHOOK     = 79;
264    /** Key code constant: Camera Focus key.
265     * Used to focus the camera. */
266    public static final int KEYCODE_FOCUS           = 80;   // *Camera* focus
267    /** Key code constant: '+' key. */
268    public static final int KEYCODE_PLUS            = 81;
269    /** Key code constant: Menu key. */
270    public static final int KEYCODE_MENU            = 82;
271    /** Key code constant: Notification key. */
272    public static final int KEYCODE_NOTIFICATION    = 83;
273    /** Key code constant: Search key. */
274    public static final int KEYCODE_SEARCH          = 84;
275    /** Key code constant: Play/Pause media key. */
276    public static final int KEYCODE_MEDIA_PLAY_PAUSE= 85;
277    /** Key code constant: Stop media key. */
278    public static final int KEYCODE_MEDIA_STOP      = 86;
279    /** Key code constant: Play Next media key. */
280    public static final int KEYCODE_MEDIA_NEXT      = 87;
281    /** Key code constant: Play Previous media key. */
282    public static final int KEYCODE_MEDIA_PREVIOUS  = 88;
283    /** Key code constant: Rewind media key. */
284    public static final int KEYCODE_MEDIA_REWIND    = 89;
285    /** Key code constant: Fast Forward media key. */
286    public static final int KEYCODE_MEDIA_FAST_FORWARD = 90;
287    /** Key code constant: Mute key.
288     * Mutes the microphone, unlike {@link #KEYCODE_VOLUME_MUTE}. */
289    public static final int KEYCODE_MUTE            = 91;
290    /** Key code constant: Page Up key. */
291    public static final int KEYCODE_PAGE_UP         = 92;
292    /** Key code constant: Page Down key. */
293    public static final int KEYCODE_PAGE_DOWN       = 93;
294    /** Key code constant: Picture Symbols modifier key.
295     * Used to switch symbol sets (Emoji, Kao-moji). */
296    public static final int KEYCODE_PICTSYMBOLS     = 94;   // switch symbol-sets (Emoji,Kao-moji)
297    /** Key code constant: Switch Charset modifier key.
298     * Used to switch character sets (Kanji, Katakana). */
299    public static final int KEYCODE_SWITCH_CHARSET  = 95;   // switch char-sets (Kanji,Katakana)
300    /** Key code constant: A Button key.
301     * On a game controller, the A button should be either the button labeled A
302     * or the first button on the bottom row of controller buttons. */
303    public static final int KEYCODE_BUTTON_A        = 96;
304    /** Key code constant: B Button key.
305     * On a game controller, the B button should be either the button labeled B
306     * or the second button on the bottom row of controller buttons. */
307    public static final int KEYCODE_BUTTON_B        = 97;
308    /** Key code constant: C Button key.
309     * On a game controller, the C button should be either the button labeled C
310     * or the third button on the bottom row of controller buttons. */
311    public static final int KEYCODE_BUTTON_C        = 98;
312    /** Key code constant: X Button key.
313     * On a game controller, the X button should be either the button labeled X
314     * or the first button on the upper row of controller buttons. */
315    public static final int KEYCODE_BUTTON_X        = 99;
316    /** Key code constant: Y Button key.
317     * On a game controller, the Y button should be either the button labeled Y
318     * or the second button on the upper row of controller buttons. */
319    public static final int KEYCODE_BUTTON_Y        = 100;
320    /** Key code constant: Z Button key.
321     * On a game controller, the Z button should be either the button labeled Z
322     * or the third button on the upper row of controller buttons. */
323    public static final int KEYCODE_BUTTON_Z        = 101;
324    /** Key code constant: L1 Button key.
325     * On a game controller, the L1 button should be either the button labeled L1 (or L)
326     * or the top left trigger button. */
327    public static final int KEYCODE_BUTTON_L1       = 102;
328    /** Key code constant: R1 Button key.
329     * On a game controller, the R1 button should be either the button labeled R1 (or R)
330     * or the top right trigger button. */
331    public static final int KEYCODE_BUTTON_R1       = 103;
332    /** Key code constant: L2 Button key.
333     * On a game controller, the L2 button should be either the button labeled L2
334     * or the bottom left trigger button. */
335    public static final int KEYCODE_BUTTON_L2       = 104;
336    /** Key code constant: R2 Button key.
337     * On a game controller, the R2 button should be either the button labeled R2
338     * or the bottom right trigger button. */
339    public static final int KEYCODE_BUTTON_R2       = 105;
340    /** Key code constant: Left Thumb Button key.
341     * On a game controller, the left thumb button indicates that the left (or only)
342     * joystick is pressed. */
343    public static final int KEYCODE_BUTTON_THUMBL   = 106;
344    /** Key code constant: Right Thumb Button key.
345     * On a game controller, the right thumb button indicates that the right
346     * joystick is pressed. */
347    public static final int KEYCODE_BUTTON_THUMBR   = 107;
348    /** Key code constant: Start Button key.
349     * On a game controller, the button labeled Start. */
350    public static final int KEYCODE_BUTTON_START    = 108;
351    /** Key code constant: Select Button key.
352     * On a game controller, the button labeled Select. */
353    public static final int KEYCODE_BUTTON_SELECT   = 109;
354    /** Key code constant: Mode Button key.
355     * On a game controller, the button labeled Mode. */
356    public static final int KEYCODE_BUTTON_MODE     = 110;
357    /** Key code constant: Escape key. */
358    public static final int KEYCODE_ESCAPE          = 111;
359    /** Key code constant: Forward Delete key.
360     * Deletes characters ahead of the insertion point, unlike {@link #KEYCODE_DEL}. */
361    public static final int KEYCODE_FORWARD_DEL     = 112;
362    /** Key code constant: Left Control modifier key. */
363    public static final int KEYCODE_CTRL_LEFT       = 113;
364    /** Key code constant: Right Control modifier key. */
365    public static final int KEYCODE_CTRL_RIGHT      = 114;
366    /** Key code constant: Caps Lock key. */
367    public static final int KEYCODE_CAPS_LOCK       = 115;
368    /** Key code constant: Scroll Lock key. */
369    public static final int KEYCODE_SCROLL_LOCK     = 116;
370    /** Key code constant: Left Meta modifier key. */
371    public static final int KEYCODE_META_LEFT       = 117;
372    /** Key code constant: Right Meta modifier key. */
373    public static final int KEYCODE_META_RIGHT      = 118;
374    /** Key code constant: Function modifier key. */
375    public static final int KEYCODE_FUNCTION        = 119;
376    /** Key code constant: System Request / Print Screen key. */
377    public static final int KEYCODE_SYSRQ           = 120;
378    /** Key code constant: Break / Pause key. */
379    public static final int KEYCODE_BREAK           = 121;
380    /** Key code constant: Home Movement key.
381     * Used for scrolling or moving the cursor around to the start of a line
382     * or to the top of a list. */
383    public static final int KEYCODE_MOVE_HOME       = 122;
384    /** Key code constant: End Movement key.
385     * Used for scrolling or moving the cursor around to the end of a line
386     * or to the bottom of a list. */
387    public static final int KEYCODE_MOVE_END        = 123;
388    /** Key code constant: Insert key.
389     * Toggles insert / overwrite edit mode. */
390    public static final int KEYCODE_INSERT          = 124;
391    /** Key code constant: Forward key.
392     * Navigates forward in the history stack.  Complement of {@link #KEYCODE_BACK}. */
393    public static final int KEYCODE_FORWARD         = 125;
394    /** Key code constant: Play media key. */
395    public static final int KEYCODE_MEDIA_PLAY      = 126;
396    /** Key code constant: Pause media key. */
397    public static final int KEYCODE_MEDIA_PAUSE     = 127;
398    /** Key code constant: Close media key.
399     * May be used to close a CD tray, for example. */
400    public static final int KEYCODE_MEDIA_CLOSE     = 128;
401    /** Key code constant: Eject media key.
402     * May be used to eject a CD tray, for example. */
403    public static final int KEYCODE_MEDIA_EJECT     = 129;
404    /** Key code constant: Record media key. */
405    public static final int KEYCODE_MEDIA_RECORD    = 130;
406    /** Key code constant: F1 key. */
407    public static final int KEYCODE_F1              = 131;
408    /** Key code constant: F2 key. */
409    public static final int KEYCODE_F2              = 132;
410    /** Key code constant: F3 key. */
411    public static final int KEYCODE_F3              = 133;
412    /** Key code constant: F4 key. */
413    public static final int KEYCODE_F4              = 134;
414    /** Key code constant: F5 key. */
415    public static final int KEYCODE_F5              = 135;
416    /** Key code constant: F6 key. */
417    public static final int KEYCODE_F6              = 136;
418    /** Key code constant: F7 key. */
419    public static final int KEYCODE_F7              = 137;
420    /** Key code constant: F8 key. */
421    public static final int KEYCODE_F8              = 138;
422    /** Key code constant: F9 key. */
423    public static final int KEYCODE_F9              = 139;
424    /** Key code constant: F10 key. */
425    public static final int KEYCODE_F10             = 140;
426    /** Key code constant: F11 key. */
427    public static final int KEYCODE_F11             = 141;
428    /** Key code constant: F12 key. */
429    public static final int KEYCODE_F12             = 142;
430    /** Key code constant: Num Lock key.
431     * This is the Num Lock key; it is different from {@link #KEYCODE_NUM}.
432     * This key alters the behavior of other keys on the numeric keypad. */
433    public static final int KEYCODE_NUM_LOCK        = 143;
434    /** Key code constant: Numeric keypad '0' key. */
435    public static final int KEYCODE_NUMPAD_0        = 144;
436    /** Key code constant: Numeric keypad '1' key. */
437    public static final int KEYCODE_NUMPAD_1        = 145;
438    /** Key code constant: Numeric keypad '2' key. */
439    public static final int KEYCODE_NUMPAD_2        = 146;
440    /** Key code constant: Numeric keypad '3' key. */
441    public static final int KEYCODE_NUMPAD_3        = 147;
442    /** Key code constant: Numeric keypad '4' key. */
443    public static final int KEYCODE_NUMPAD_4        = 148;
444    /** Key code constant: Numeric keypad '5' key. */
445    public static final int KEYCODE_NUMPAD_5        = 149;
446    /** Key code constant: Numeric keypad '6' key. */
447    public static final int KEYCODE_NUMPAD_6        = 150;
448    /** Key code constant: Numeric keypad '7' key. */
449    public static final int KEYCODE_NUMPAD_7        = 151;
450    /** Key code constant: Numeric keypad '8' key. */
451    public static final int KEYCODE_NUMPAD_8        = 152;
452    /** Key code constant: Numeric keypad '9' key. */
453    public static final int KEYCODE_NUMPAD_9        = 153;
454    /** Key code constant: Numeric keypad '/' key (for division). */
455    public static final int KEYCODE_NUMPAD_DIVIDE   = 154;
456    /** Key code constant: Numeric keypad '*' key (for multiplication). */
457    public static final int KEYCODE_NUMPAD_MULTIPLY = 155;
458    /** Key code constant: Numeric keypad '-' key (for subtraction). */
459    public static final int KEYCODE_NUMPAD_SUBTRACT = 156;
460    /** Key code constant: Numeric keypad '+' key (for addition). */
461    public static final int KEYCODE_NUMPAD_ADD      = 157;
462    /** Key code constant: Numeric keypad '.' key (for decimals or digit grouping). */
463    public static final int KEYCODE_NUMPAD_DOT      = 158;
464    /** Key code constant: Numeric keypad ',' key (for decimals or digit grouping). */
465    public static final int KEYCODE_NUMPAD_COMMA    = 159;
466    /** Key code constant: Numeric keypad Enter key. */
467    public static final int KEYCODE_NUMPAD_ENTER    = 160;
468    /** Key code constant: Numeric keypad '=' key. */
469    public static final int KEYCODE_NUMPAD_EQUALS   = 161;
470    /** Key code constant: Numeric keypad '(' key. */
471    public static final int KEYCODE_NUMPAD_LEFT_PAREN = 162;
472    /** Key code constant: Numeric keypad ')' key. */
473    public static final int KEYCODE_NUMPAD_RIGHT_PAREN = 163;
474    /** Key code constant: Volume Mute key.
475     * Mutes the speaker, unlike {@link #KEYCODE_MUTE}.
476     * This key should normally be implemented as a toggle such that the first press
477     * mutes the speaker and the second press restores the original volume. */
478    public static final int KEYCODE_VOLUME_MUTE     = 164;
479    /** Key code constant: Info key.
480     * Common on TV remotes to show additional information related to what is
481     * currently being viewed. */
482    public static final int KEYCODE_INFO            = 165;
483    /** Key code constant: Channel up key.
484     * On TV remotes, increments the television channel. */
485    public static final int KEYCODE_CHANNEL_UP      = 166;
486    /** Key code constant: Channel down key.
487     * On TV remotes, decrements the television channel. */
488    public static final int KEYCODE_CHANNEL_DOWN    = 167;
489    /** Key code constant: Zoom in key. */
490    public static final int KEYCODE_ZOOM_IN         = 168;
491    /** Key code constant: Zoom out key. */
492    public static final int KEYCODE_ZOOM_OUT        = 169;
493    /** Key code constant: TV key.
494     * On TV remotes, switches to viewing live TV. */
495    public static final int KEYCODE_TV              = 170;
496    /** Key code constant: Window key.
497     * On TV remotes, toggles picture-in-picture mode or other windowing functions.
498     * On Android Wear devices, triggers a display offset. */
499    public static final int KEYCODE_WINDOW          = 171;
500    /** Key code constant: Guide key.
501     * On TV remotes, shows a programming guide. */
502    public static final int KEYCODE_GUIDE           = 172;
503    /** Key code constant: DVR key.
504     * On some TV remotes, switches to a DVR mode for recorded shows. */
505    public static final int KEYCODE_DVR             = 173;
506    /** Key code constant: Bookmark key.
507     * On some TV remotes, bookmarks content or web pages. */
508    public static final int KEYCODE_BOOKMARK        = 174;
509    /** Key code constant: Toggle captions key.
510     * Switches the mode for closed-captioning text, for example during television shows. */
511    public static final int KEYCODE_CAPTIONS        = 175;
512    /** Key code constant: Settings key.
513     * Starts the system settings activity. */
514    public static final int KEYCODE_SETTINGS        = 176;
515    /** Key code constant: TV power key.
516     * On TV remotes, toggles the power on a television screen. */
517    public static final int KEYCODE_TV_POWER        = 177;
518    /** Key code constant: TV input key.
519     * On TV remotes, switches the input on a television screen. */
520    public static final int KEYCODE_TV_INPUT        = 178;
521    /** Key code constant: Set-top-box power key.
522     * On TV remotes, toggles the power on an external Set-top-box. */
523    public static final int KEYCODE_STB_POWER       = 179;
524    /** Key code constant: Set-top-box input key.
525     * On TV remotes, switches the input mode on an external Set-top-box. */
526    public static final int KEYCODE_STB_INPUT       = 180;
527    /** Key code constant: A/V Receiver power key.
528     * On TV remotes, toggles the power on an external A/V Receiver. */
529    public static final int KEYCODE_AVR_POWER       = 181;
530    /** Key code constant: A/V Receiver input key.
531     * On TV remotes, switches the input mode on an external A/V Receiver. */
532    public static final int KEYCODE_AVR_INPUT       = 182;
533    /** Key code constant: Red "programmable" key.
534     * On TV remotes, acts as a contextual/programmable key. */
535    public static final int KEYCODE_PROG_RED        = 183;
536    /** Key code constant: Green "programmable" key.
537     * On TV remotes, actsas a contextual/programmable key. */
538    public static final int KEYCODE_PROG_GREEN      = 184;
539    /** Key code constant: Yellow "programmable" key.
540     * On TV remotes, acts as a contextual/programmable key. */
541    public static final int KEYCODE_PROG_YELLOW     = 185;
542    /** Key code constant: Blue "programmable" key.
543     * On TV remotes, acts as a contextual/programmable key. */
544    public static final int KEYCODE_PROG_BLUE       = 186;
545    /** Key code constant: App switch key.
546     * Should bring up the application switcher dialog. */
547    public static final int KEYCODE_APP_SWITCH      = 187;
548    /** Key code constant: Generic Game Pad Button #1.*/
549    public static final int KEYCODE_BUTTON_1        = 188;
550    /** Key code constant: Generic Game Pad Button #2.*/
551    public static final int KEYCODE_BUTTON_2        = 189;
552    /** Key code constant: Generic Game Pad Button #3.*/
553    public static final int KEYCODE_BUTTON_3        = 190;
554    /** Key code constant: Generic Game Pad Button #4.*/
555    public static final int KEYCODE_BUTTON_4        = 191;
556    /** Key code constant: Generic Game Pad Button #5.*/
557    public static final int KEYCODE_BUTTON_5        = 192;
558    /** Key code constant: Generic Game Pad Button #6.*/
559    public static final int KEYCODE_BUTTON_6        = 193;
560    /** Key code constant: Generic Game Pad Button #7.*/
561    public static final int KEYCODE_BUTTON_7        = 194;
562    /** Key code constant: Generic Game Pad Button #8.*/
563    public static final int KEYCODE_BUTTON_8        = 195;
564    /** Key code constant: Generic Game Pad Button #9.*/
565    public static final int KEYCODE_BUTTON_9        = 196;
566    /** Key code constant: Generic Game Pad Button #10.*/
567    public static final int KEYCODE_BUTTON_10       = 197;
568    /** Key code constant: Generic Game Pad Button #11.*/
569    public static final int KEYCODE_BUTTON_11       = 198;
570    /** Key code constant: Generic Game Pad Button #12.*/
571    public static final int KEYCODE_BUTTON_12       = 199;
572    /** Key code constant: Generic Game Pad Button #13.*/
573    public static final int KEYCODE_BUTTON_13       = 200;
574    /** Key code constant: Generic Game Pad Button #14.*/
575    public static final int KEYCODE_BUTTON_14       = 201;
576    /** Key code constant: Generic Game Pad Button #15.*/
577    public static final int KEYCODE_BUTTON_15       = 202;
578    /** Key code constant: Generic Game Pad Button #16.*/
579    public static final int KEYCODE_BUTTON_16       = 203;
580    /** Key code constant: Language Switch key.
581     * Toggles the current input language such as switching between English and Japanese on
582     * a QWERTY keyboard.  On some devices, the same function may be performed by
583     * pressing Shift+Spacebar. */
584    public static final int KEYCODE_LANGUAGE_SWITCH = 204;
585    /** Key code constant: Manner Mode key.
586     * Toggles silent or vibrate mode on and off to make the device behave more politely
587     * in certain settings such as on a crowded train.  On some devices, the key may only
588     * operate when long-pressed. */
589    public static final int KEYCODE_MANNER_MODE     = 205;
590    /** Key code constant: 3D Mode key.
591     * Toggles the display between 2D and 3D mode. */
592    public static final int KEYCODE_3D_MODE         = 206;
593    /** Key code constant: Contacts special function key.
594     * Used to launch an address book application. */
595    public static final int KEYCODE_CONTACTS        = 207;
596    /** Key code constant: Calendar special function key.
597     * Used to launch a calendar application. */
598    public static final int KEYCODE_CALENDAR        = 208;
599    /** Key code constant: Music special function key.
600     * Used to launch a music player application. */
601    public static final int KEYCODE_MUSIC           = 209;
602    /** Key code constant: Calculator special function key.
603     * Used to launch a calculator application. */
604    public static final int KEYCODE_CALCULATOR      = 210;
605    /** Key code constant: Japanese full-width / half-width key. */
606    public static final int KEYCODE_ZENKAKU_HANKAKU = 211;
607    /** Key code constant: Japanese alphanumeric key. */
608    public static final int KEYCODE_EISU            = 212;
609    /** Key code constant: Japanese non-conversion key. */
610    public static final int KEYCODE_MUHENKAN        = 213;
611    /** Key code constant: Japanese conversion key. */
612    public static final int KEYCODE_HENKAN          = 214;
613    /** Key code constant: Japanese katakana / hiragana key. */
614    public static final int KEYCODE_KATAKANA_HIRAGANA = 215;
615    /** Key code constant: Japanese Yen key. */
616    public static final int KEYCODE_YEN             = 216;
617    /** Key code constant: Japanese Ro key. */
618    public static final int KEYCODE_RO              = 217;
619    /** Key code constant: Japanese kana key. */
620    public static final int KEYCODE_KANA            = 218;
621    /** Key code constant: Assist key.
622     * Launches the global assist activity.  Not delivered to applications. */
623    public static final int KEYCODE_ASSIST          = 219;
624    /** Key code constant: Brightness Down key.
625     * Adjusts the screen brightness down. */
626    public static final int KEYCODE_BRIGHTNESS_DOWN = 220;
627    /** Key code constant: Brightness Up key.
628     * Adjusts the screen brightness up. */
629    public static final int KEYCODE_BRIGHTNESS_UP   = 221;
630    /** Key code constant: Audio Track key.
631     * Switches the audio tracks. */
632    public static final int KEYCODE_MEDIA_AUDIO_TRACK = 222;
633    /** Key code constant: Sleep key.
634     * Puts the device to sleep.  Behaves somewhat like {@link #KEYCODE_POWER} but it
635     * has no effect if the device is already asleep. */
636    public static final int KEYCODE_SLEEP           = 223;
637    /** Key code constant: Wakeup key.
638     * Wakes up the device.  Behaves somewhat like {@link #KEYCODE_POWER} but it
639     * has no effect if the device is already awake. */
640    public static final int KEYCODE_WAKEUP          = 224;
641    /** Key code constant: Pairing key.
642     * Initiates peripheral pairing mode. Useful for pairing remote control
643     * devices or game controllers, especially if no other input mode is
644     * available. */
645    public static final int KEYCODE_PAIRING         = 225;
646    /** Key code constant: Media Top Menu key.
647     * Goes to the top of media menu. */
648    public static final int KEYCODE_MEDIA_TOP_MENU  = 226;
649    /** Key code constant: '11' key. */
650    public static final int KEYCODE_11              = 227;
651    /** Key code constant: '12' key. */
652    public static final int KEYCODE_12              = 228;
653    /** Key code constant: Last Channel key.
654     * Goes to the last viewed channel. */
655    public static final int KEYCODE_LAST_CHANNEL    = 229;
656    /** Key code constant: TV data service key.
657     * Displays data services like weather, sports. */
658    public static final int KEYCODE_TV_DATA_SERVICE = 230;
659    /** Key code constant: Voice Assist key.
660     * Launches the global voice assist activity. Not delivered to applications. */
661    public static final int KEYCODE_VOICE_ASSIST = 231;
662    /** Key code constant: Radio key.
663     * Toggles TV service / Radio service. */
664    public static final int KEYCODE_TV_RADIO_SERVICE = 232;
665    /** Key code constant: Teletext key.
666     * Displays Teletext service. */
667    public static final int KEYCODE_TV_TELETEXT = 233;
668    /** Key code constant: Number entry key.
669     * Initiates to enter multi-digit channel nubmber when each digit key is assigned
670     * for selecting separate channel. Corresponds to Number Entry Mode (0x1D) of CEC
671     * User Control Code. */
672    public static final int KEYCODE_TV_NUMBER_ENTRY = 234;
673    /** Key code constant: Analog Terrestrial key.
674     * Switches to analog terrestrial broadcast service. */
675    public static final int KEYCODE_TV_TERRESTRIAL_ANALOG = 235;
676    /** Key code constant: Digital Terrestrial key.
677     * Switches to digital terrestrial broadcast service. */
678    public static final int KEYCODE_TV_TERRESTRIAL_DIGITAL = 236;
679    /** Key code constant: Satellite key.
680     * Switches to digital satellite broadcast service. */
681    public static final int KEYCODE_TV_SATELLITE = 237;
682    /** Key code constant: BS key.
683     * Switches to BS digital satellite broadcasting service available in Japan. */
684    public static final int KEYCODE_TV_SATELLITE_BS = 238;
685    /** Key code constant: CS key.
686     * Switches to CS digital satellite broadcasting service available in Japan. */
687    public static final int KEYCODE_TV_SATELLITE_CS = 239;
688    /** Key code constant: BS/CS key.
689     * Toggles between BS and CS digital satellite services. */
690    public static final int KEYCODE_TV_SATELLITE_SERVICE = 240;
691    /** Key code constant: Toggle Network key.
692     * Toggles selecting broacast services. */
693    public static final int KEYCODE_TV_NETWORK = 241;
694    /** Key code constant: Antenna/Cable key.
695     * Toggles broadcast input source between antenna and cable. */
696    public static final int KEYCODE_TV_ANTENNA_CABLE = 242;
697    /** Key code constant: HDMI #1 key.
698     * Switches to HDMI input #1. */
699    public static final int KEYCODE_TV_INPUT_HDMI_1 = 243;
700    /** Key code constant: HDMI #2 key.
701     * Switches to HDMI input #2. */
702    public static final int KEYCODE_TV_INPUT_HDMI_2 = 244;
703    /** Key code constant: HDMI #3 key.
704     * Switches to HDMI input #3. */
705    public static final int KEYCODE_TV_INPUT_HDMI_3 = 245;
706    /** Key code constant: HDMI #4 key.
707     * Switches to HDMI input #4. */
708    public static final int KEYCODE_TV_INPUT_HDMI_4 = 246;
709    /** Key code constant: Composite #1 key.
710     * Switches to composite video input #1. */
711    public static final int KEYCODE_TV_INPUT_COMPOSITE_1 = 247;
712    /** Key code constant: Composite #2 key.
713     * Switches to composite video input #2. */
714    public static final int KEYCODE_TV_INPUT_COMPOSITE_2 = 248;
715    /** Key code constant: Component #1 key.
716     * Switches to component video input #1. */
717    public static final int KEYCODE_TV_INPUT_COMPONENT_1 = 249;
718    /** Key code constant: Component #2 key.
719     * Switches to component video input #2. */
720    public static final int KEYCODE_TV_INPUT_COMPONENT_2 = 250;
721    /** Key code constant: VGA #1 key.
722     * Switches to VGA (analog RGB) input #1. */
723    public static final int KEYCODE_TV_INPUT_VGA_1 = 251;
724    /** Key code constant: Audio description key.
725     * Toggles audio description off / on. */
726    public static final int KEYCODE_TV_AUDIO_DESCRIPTION = 252;
727    /** Key code constant: Audio description mixing volume up key.
728     * Louden audio description volume as compared with normal audio volume. */
729    public static final int KEYCODE_TV_AUDIO_DESCRIPTION_MIX_UP = 253;
730    /** Key code constant: Audio description mixing volume down key.
731     * Lessen audio description volume as compared with normal audio volume. */
732    public static final int KEYCODE_TV_AUDIO_DESCRIPTION_MIX_DOWN = 254;
733    /** Key code constant: Zoom mode key.
734     * Changes Zoom mode (Normal, Full, Zoom, Wide-zoom, etc.) */
735    public static final int KEYCODE_TV_ZOOM_MODE = 255;
736    /** Key code constant: Contents menu key.
737     * Goes to the title list. Corresponds to Contents Menu (0x0B) of CEC User Control
738     * Code */
739    public static final int KEYCODE_TV_CONTENTS_MENU = 256;
740    /** Key code constant: Media context menu key.
741     * Goes to the context menu of media contents. Corresponds to Media Context-sensitive
742     * Menu (0x11) of CEC User Control Code. */
743    public static final int KEYCODE_TV_MEDIA_CONTEXT_MENU = 257;
744    /** Key code constant: Timer programming key.
745     * Goes to the timer recording menu. Corresponds to Timer Programming (0x54) of
746     * CEC User Control Code. */
747    public static final int KEYCODE_TV_TIMER_PROGRAMMING = 258;
748    /** Key code constant: Help key. */
749    public static final int KEYCODE_HELP = 259;
750    /** Key code constant: Navigate to previous key.
751     * Goes backward by one item in an ordered collection of items. */
752    public static final int KEYCODE_NAVIGATE_PREVIOUS = 260;
753    /** Key code constant: Navigate to next key.
754     * Advances to the next item in an ordered collection of items. */
755    public static final int KEYCODE_NAVIGATE_NEXT   = 261;
756    /** Key code constant: Navigate in key.
757     * Activates the item that currently has focus or expands to the next level of a navigation
758     * hierarchy. */
759    public static final int KEYCODE_NAVIGATE_IN     = 262;
760    /** Key code constant: Navigate out key.
761     * Backs out one level of a navigation hierarchy or collapses the item that currently has
762     * focus. */
763    public static final int KEYCODE_NAVIGATE_OUT    = 263;
764    /** Key code constant: Primary stem key for Wear
765     * Main power/reset button on watch. */
766    public static final int KEYCODE_STEM_PRIMARY = 264;
767    /** Key code constant: Generic stem key 1 for Wear */
768    public static final int KEYCODE_STEM_1 = 265;
769    /** Key code constant: Generic stem key 2 for Wear */
770    public static final int KEYCODE_STEM_2 = 266;
771    /** Key code constant: Generic stem key 3 for Wear */
772    public static final int KEYCODE_STEM_3 = 267;
773    /** Key code constant: Directional Pad Up-Left */
774    public static final int KEYCODE_DPAD_UP_LEFT    = 268;
775    /** Key code constant: Directional Pad Down-Left */
776    public static final int KEYCODE_DPAD_DOWN_LEFT  = 269;
777    /** Key code constant: Directional Pad Up-Right */
778    public static final int KEYCODE_DPAD_UP_RIGHT   = 270;
779    /** Key code constant: Directional Pad Down-Right */
780    public static final int KEYCODE_DPAD_DOWN_RIGHT = 271;
781    /** Key code constant: Skip forward media key. */
782    public static final int KEYCODE_MEDIA_SKIP_FORWARD = 272;
783    /** Key code constant: Skip backward media key. */
784    public static final int KEYCODE_MEDIA_SKIP_BACKWARD = 273;
785    /** Key code constant: Step forward media key.
786     * Steps media forward, one frame at a time. */
787    public static final int KEYCODE_MEDIA_STEP_FORWARD = 274;
788    /** Key code constant: Step backward media key.
789     * Steps media backward, one frame at a time. */
790    public static final int KEYCODE_MEDIA_STEP_BACKWARD = 275;
791    /** Key code constant: put device to sleep unless a wakelock is held. */
792    public static final int KEYCODE_SOFT_SLEEP = 276;
793    /** Key code constant: Cut key. */
794    public static final int KEYCODE_CUT = 277;
795    /** Key code constant: Copy key. */
796    public static final int KEYCODE_COPY = 278;
797    /** Key code constant: Paste key. */
798    public static final int KEYCODE_PASTE = 279;
799    /** Key code constant: Consumed by the system for navigation up */
800    public static final int KEYCODE_SYSTEM_NAVIGATION_UP = 280;
801    /** Key code constant: Consumed by the system for navigation down */
802    public static final int KEYCODE_SYSTEM_NAVIGATION_DOWN = 281;
803    /** Key code constant: Consumed by the system for navigation left*/
804    public static final int KEYCODE_SYSTEM_NAVIGATION_LEFT = 282;
805    /** Key code constant: Consumed by the system for navigation right */
806    public static final int KEYCODE_SYSTEM_NAVIGATION_RIGHT = 283;
807    /** Key code constant: Show all apps
808     * @hide */
809    public static final int KEYCODE_ALL_APPS = 284;

"""
