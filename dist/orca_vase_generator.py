# /// script
# requires-python = ">=3.12"
# dependencies = ["numpy>=1.26"]
#
# [tool.orcaslicer.plugin]
# id = "orca-vase-studio"
# name = "Orca Vase Studio"
# description = "Parametric 3D Vase & Planter Studio with X-Ray Wall Calipers & 1-Click Plater | Estudio 3D de Vasos e Cachepos"
# author = "Orca Vase Studio"
# version = "1.3.3"
# ///

from __future__ import annotations

import sys as _orca_init_sys
import types as _orca_init_types
if __name__ not in _orca_init_sys.modules:
    _orca_init_sys.modules[__name__] = _orca_init_types.ModuleType(__name__)

# ===========================================================================
# MODULE: vase_studio.language_packs
# ===========================================================================

"""Discover data-only offline language packs in source, wheels and standalone bundles.

This module is self-contained so future Studio plugins can use the same format
without importing another plugin. Catalogs never contain executable code.
"""
pass  # [bundled] hoisted __future__ import

import base64
import json
from pathlib import Path
import re
import zlib

_BUNDLED_LANGUAGE_PACKS = json.loads(zlib.decompress(base64.b85decode('c-qvxYm?MQwl4fvWJl~{90TpyGkd>pgdO`tG!4ca17>K(GvhBO)K#i(nJTG9Dm52}BWT(eFkpPY--ofmjBRW#ZgY*;73X{N7pC3a@M+FZc-OO5rj(LWs%qQ?ej{c~mz2uO%9ZPu`Q&=;!EW!tN1uBzZp?Tc_kYiNQS67ogOC3E#s?c=(|hnyyx;g>;P(7k?|%nw2ak4#Q7@TJ`d`QNs_92wqsJdT*zQI2B#fF~^x&hv-S}WHa)Y?-;%$spCX=We`LXBhL^b@&^Ma<kiK^ZB;N*<k#q-C*sN>S_z21Rd5_$Bc`qM>we{$Px=YKf6BR`;?Ke)X^b;NQ1Zy~+gO@Dele4zi*&zx=anHL?TSM-+``L5HXZqN|hAxizmnRI8-IR0qQx)_IglKviVx6zfb$zMDbO}l~LpeOWK{|ow)A8+%*j@OI$1^(`z#Seb9yX^)&A~3y~aEadC{>4}|)1+rRy@Y@I?U^v~dOeRu`MWL7L=s6i=s7)h=_ww$^bV!lep9N{e{Fp5aUyDqXlQ;dpX~5wBQN)%^Us&w$eJiT!z65p+-YaV4VrB)c4V&G2c0l*dNZiWiL>s8k<;=6Z&NP`JSSFlO%Z|jk5T305zQZ!a%0DB_rIcl0++w$K~YU%;<(QyC=$j_BMf>`h&J6R*FO-B>8|Vx!d~qB_m9p*+i&c18tA&y3mv!F<ac<rB}}H;-lhghJQDfSGd=m+@j-u|`pG5ftH|qwv!2<#E;StL2L76O=w*Y6*L{Q<@f*a;Zp5u5-FAqIsnjD=VUJjl3FK3~R932v(D9vKJmc)~;;@~lg(5%tU-37tv(s(QxXe=x*V)?fBDdXiXu|hlQamcKHI|32gCe{(sK1S{N2Hr*yI|`HFY15M@u>p+4&`>bn3+G#`1D^Y;dYoYX#qDp;zrlmOe?g34)m}BC&F&mi|An(90EhgAI?NLMQpP*ZiKUL6YK2%e)`rwoIh{c;~sP#ad<&)*vm^jX?Q{JVfvCw>~Z~Y)1RrxZa4C1xv4_^D-FLHK8*1afrz)JohLlE*KxbfhW|c~uXnm#UZ3fEer{>Eq9rc+<|(JsaVFfh-<1`@k0yvNF};x5{+>1=H5tD*KKRcQ?>c{?32j9p_V8QJ)c^hT<aLr1G~S56q+h!u5_G`~=(EcsR>GRzO2qXK2+<~KL2Q~jxC#H#s~z;zp(QCVS)933e%tRIWbvhcHeDVL6ZsM6@pc%ZK}Aq{kOcgF|2-0BNpHs497d>}em|Z>A^l`_+2VJ+0Fpg+Hgq~5u{`Nt^3)Ts$^nxaDeZUmKR-aPx5m9O=W)MHv|z!j{|p_x0ZWol4W`>7uOpvC;&dXy^{IrGou03)2k1wDPEEM8G+L5pdQ^CT@#2vh*W<*2+*(9Ufe?GcE(_r<-fpG^5O%<*Zj6_Y`#tAr-`mfW|7+qlBNp8M{OE`?5ruKQX;M@bNjFr=&q<eg4l^c{pW9aDpZ202Ev7b#IvaLJVasoO&R-tReU=v5u-l8M0N#T)-ni*J5k~$Y>N~xB#v#GlAohm>aQ^e({(1P#fB)@o|4o(&6@8re#?61gMQLptg=q$YSrVpQkY`&voT7qz_xo{=2b;dx8%82lqzEtS&XgaxBoQ5pMs?(M|MOYT$6W34r>49nvsxlNJmCf;D~MU?87Xg5`O%!ta&1qM5|16N2wf@SPm{QDw)k!*44SMbvnQ_1=7iU7CvB3akAR{yqTg>}QC510jy0#LWAfx_&xb|vApJ|i+M{JoJtKN;;MWglX2MflFYqBigzMG1`5(^s6ipqCUo-#Sh(!GpVVjhd^E5FNo-@bdD|!$*Pc=f4;XKz;3AHNUPIi6t3C4u8;onKg1|ADBG8AZS$V+)X<37xG#D4c+?CkTru0xX+I2~TO#Fk@|dv`eAfi5u@OF^hBXNs0EX+i2Q{S&I!L>&|^v_6&i?Ix*AhqQ~|bfz$nsdh-3Z~sgfLr-=cKUS)V-XCNw9)mk0XT#X<cRv2`nDZq1h3CC+nwGO@aEI)b#y<LnC}H$6c8KZ+c@z&|hMnA?r%B;BNr$@-N^cs;vmv?>I{mZK4^jnAmzr=|SO(27>j=@=%@5a!J(zn!jc}vGY(!M05qG1o=LzSF#o)kXbsxx6=+QD|$Wn69ptC{IL8ud>mk&eFbHiMHgBFCd{}E;?5x0eDew2Dd`a!BE8$jw!2PQQ;LV!Zu)1X7+5f<3Ooi1~61onN@ndEM(k!<FU|MT!$^8J3FSY7DkOze1Sa_bfvJI^)7roMp)qM9&E<3uy2)T3NeHeVgL;rG7^xn?!ZvFk_u&&eF?sBSxtZ=HBze9Kc#7qi1d(^`Nl0m1)y?5Oix@VrA}y&F4W%XzN7|9L258Zq>fL)z&%zllc>r>gX9*oJB*Ha3d05;Kac$~zq{(1PM{HgH?+!7(Q3uJF(y;@ane@X+&AWCLki8rpOFJAUvy2~+yRJ@C9E;=rtn+HFDUNOcXjBh_st<9(RQHa@7N2YvJ0el;}6jO=&HiDnT^d$SmgmsRGY&U3S>7(Eij8Kw`p9LSk328tPFAj6CTBD*Ty)6n(63?k(}v6az^*l36Kx6uqMI;{x*%X#jQs;k@RJzvy>&sYj5fnFF#R=;$h(0++hB|>E-)YMGC2xa*L9qD$uZYILzG0E?wM|OW0wESsOrfiW<is&E_9(%0oxD2~9B)W_e5a7YAFaBjG3`y>*mjC=0XVP;!>=%<Abcnv22xHb!x(9#$i*B84{!TYDk0+u0VN?1YpBvOKP`Km5M(HT~X`4&lxyTgqr^qgthB{0w+5bha`C$j|J^qWmZMT;hT-ldTgktZ3mb`S+Z{S;qQ8w9eNia>d{h&$9icCHq!gVGJlj#{Pj-^^!!(@UzN^+70+th8$up7AF?~$KL_0Y?G(CD!bV-xex3zJmLL3cl3n3Cj4deiJ{##qxX%#^r)0d{o^&kK_JQCj%uKGjUhkyMOB9^Dj~jwJH9dRlc({|Y>OhnUI~_zy5+_Fx8*m+3SPVw4e^glYfD9VP<`nv$NNlpZ^D?2HJFF1e#D%;1XdrMAcza~giT{|#41opb4H(n_%lz7CbBg7Bt6bV>2KETcvJ{B9E|M!yx36G@JUOO~()1ATkYXeWqzxV^><NSMw#zwx8gg(1#E5GN4dgzcf<sM4?sJnA{Ia>`rn_CY7632My1r)KS_gduyrYE?WUDr!s{RKF3fa-L1t<0eWI*Y=3|Zk}mH)1)>S>&6iL)$w9iRqC=n8xx0@y1`vm)-KvlN4m%BdOaGcGJi3jTr<tE=J84DD~}^vwPcO=`17s2cBMxyM#nW|C1ItDB8ISFZ%3Oi_?^9l?Pk7Jwwy?W2|sGIIch_Hz!Iicq?9&o<JbYz6THS)o;q#=u{rgEjh+oLy9);zo=4VTH}b`fgmDNhn{>!deQxT&^Zj?9n>xt<Woi5H1Kgzs1Z$`Z5_|a)Vhdp{+dmV}s~1XCjwv;+WMBU?CKGIZ4#7~N_+Zdby*7#5O}|x<7p5{T^9K2VEDw#2@Hk7fpQM_}L{oLE3P}qgZuvZQzUg=3=O50ZhFMKnGflVrLC%40`90Wyy-*i33Hw0awH6HkS>t9D_0)%;+wMKvckLbDykjeL(wlp??|cdpWqi-B?Yp*tihH;2>c8Bd$J2>D+xKpt7zf`>?CGDRzn|iGV?b6mI@Fbz0ogvY;C_;Q{xn<VyTaKJ&q5}k-|2rt-Xa_4&G3ONLK-6u`9K;wrQhw@kflmYi-(By06UYiN}Fkb53@e;#P;1z8g}GxA`4+D%oaZ8(hNfKHxIBw5101|526txZu7e2r%*T;3LHjHSYwOd{{rz<mU~LUZ1y04?1c~kc{WT7Ni)tKgru{^vQmE{4bZD>Z-NL+<<oK%wV4HXk=In&wcTFa2+81<um%yPOJ29j@tf2?#V|=0yQ<6{zvFE7X#PN6Qt_=Qd_=$B9kvfnL)iJydmDcHUm`~yR>7v2n+!>(P@z!2f7tkNPe@uNpsChI2nS>E<%A0v4eJ9z9a@T&(M(kUYC{J{D$D8;nPH(t_Tz5T%Pb)&ommthL~Y5?Q2`<qCwanab5C@<Bn^`Ai;%|Ime7Z@#p|+Hhky?eLsLK^AF9j*k*Viw*aCsjI|%arAtCxmS$T{<A6CWx<TpvCKjLgjdIz0}gCf~?xY0DGcQ%G8LH!ml3M-6OU(cDGaigx9id|$fHN8X3SRCe16<3Z5GnR&G^o;GE0rALG!-~pg2@#xh)Z?9Q+wZ|fK%_Zfu1cp7CEH#w%_S#77A5TY8Plj6+YwH&UAUuvVG2P&Oy1M*?^uK+5X+mm<(>Wkwm;}W%ZvJ72Mr&iOdyAK?<V(gL~lHfecoDejoxvA+|aUjkGl;LV|r|RsPnTz8y$d(RRk(_#v`yk#??QI*i)Q^<2Wjo5@D||vE*@Tf+k9joeR;-p#$dBJxyu_4Te*Z(%5^*Dw^!M)6*gjyqG+2<w0*y&mT4eV}<Uk(3nALlyoMkZ=TtGgWg#rlS}#>+20z|6W5%&Egp@vO(s@P#q{u?O(yDwr^u%u^}&(?+X)eg7>`4Plb%>;8}Qo*g&_ncd~dKiaTSNawC$X&dI@gqVC$c4cd^qaQ#;+$E1#Xfy)$G;C<0Sm^oJ6ZY4Bgw%W>tZ;$a$NM&NtWZFy$&n>{Jd+=Gw}sLbsVF@WXSztZs_&^>l3V+jR#l~Nytcm<OMzQ=9)Nt|jBY-6CvI5`X~pgrt@F=55{-cGIrO?lgMv2P=rrR{0g;RO`%s8TalzJS6gDpy0Ns8S`mD*w7%Uzw)jY8xe`lPR%CRB<sDNUEpeEMi9~m3!k+1G`iW^ssG2pGjN5c~enn4lT35BNGGy5aQzr;(EjtsJ?_p2;TZj7|-|}47WNGot80I9EXs3#WnnvXRNrLe&CaX1<k)VY5Tknfq%&nNZ+`^eF%=zDAbN`>O2`czcd3q*)>*<klH$Wf}GiDTEQ{P+f6DQ|HQ$m$Zv{-PH0i~M99V1Dba#{N4S3zG`W**L6aao825NEqBw}IkckN9>(Xe_?GOV~E6<SQmTeMd8;W?olbm>-0N%*<*y7ynVz+Pyk1^ntuGnxlks_9|JG~~&YDDbnxq(C7pCR(X*gX=oV1DcOL<^6FHo1*h84aZ+W|WeP{B9R<06&2Akl;0O4-cxD1hBQqZ3`P{rIAF~E{exwXM(1W^dii0-c@#`PH25{vRmZ%f{;=#%N=q-o6K__eZV!*ryVzf@QTM+(ED-MnbmUD&2erEoGbAPhing*J(3nVkmNYD+g?vPN>%`MG@hZU*zdGSTykfb$$3|1R_hfi+5en0UjqRQl4+h{El|sUO{nEw{~|L|o9z3LdL4%y(l_XGg9d~iPww};F376M*`o21QO=a)u42!i)gxyDL?k^F22`rSn`W_WnvJnOCyoGVOcH{s{cnOqdWgNIrs{00BJxyYC^g1nr%A8Ilim!CgBUdy%}0$lWsy3eTB0p5tRiQF>7Fg@F7sc5)h^SI^(>-K)9J|zm#0%Je8+7whr$XVGs|y>Ms?`%tSD^q4jWijystS!j?Jc~b^w_dc`Irbn@~B1ga-tk0aI|aE5bGl`F#!EEsJ|$z=sWF+bT@YjX2cPtN}mcM%mm#jlO0<JaVG2L5g%XX*XoU4gK5=bC?W)00F#NAMBN#&Cqj9G$z%&pWPR9ahm8)BBKSjgM3<uGa6oJ%sg;HUW%%eNDe}IQjbuK*mH`s7A96%1F}2gumjH<Wvq0C4{41w4-(&#u%-5N^h=3J?qojrr-NtcYe&benj{R!J%vO~qe(QIQ6ei4Q8DyPHQ!9A{*5Zehu=CxDe*qU2~^apL2A1f@{x@#iQC>Z#XjRqDv`Tt7ntLe=m?IxI6b9}BGPjXj(iAFJ%{W-Vr825{jjLU(o;BYD#KOpLT8HHPrZ1cO-bxV;ii_TOzIL2OvJQ8r#PI&LCi!dMFgO;sgd+(Np`b!%W_{Y9tj0V%p#r%_cvgs5_9ZhvNkbP8af}}kv)Cx>~3nk<C@jB-7Y*Ep)S{rz=qhNw6+klX}DcX0*Kpcdk2K#u_x=Dt%gneU7q{>?v%eNrvEqyYm&XgvkxIegi{KM)&vWESf(K!U_-0JM_O`SWe&(HY!+FMI~<7x-BF56v8*FoIvk(ay<?nOAfseVPNPL#$8FH!YvRa27fLS{ktnM@PNsO8vyFQ&ML|W)gy306I6P2<<&bnt-g_vr(w$DU$aI7LS>no>%>AHtdVWzssrvAdw7_}^T*~5o8_BP5)1Hu|9=H}!Mvh%6G0=nHWO9bRjm}gQx=k=f(r$XuMrI1;Y*Jce|AVik+o(rr(rIoWLIdbfOiQJwM$jd~GxsrlH#$&8#0SJ9(=5BNQhgV3v_RD9q&LkoNo~X)?CjJNAkRoUjPxrBaI7HpPe`e-+XCKpcF7T)U15ifRvPoO9-Earz@N0-;bqc1^1;GC!tQ71tK}Zzz~LT`pX~9n2eH?aa7E8e<QNG*BSRENvE)_u6F~{yE#EuiaZkoY(L_$q<2HHQW)E40J-prKlP|z=?*8Yb|K!Zje(hH63K5a?^p*_=)VHercCz=I5@02Z5RvFu<cJvuXR?qe^CX^&(0&%?L+EjAY%E7CyudR#fu`cIq-n6-0$u0exE!hZK(@f)sFDzBlQtvM)tmLb{SULPb@v}r%dM7jh)MA`WehEs?0J4Ff5~2iTJWh)!n`T2$DjY=G>xN9&$-V#2b|}oI803>LO@)FYr6>PQ;7zb;LT+og9L9wVsWa=Qb7|N6uk9N`j{+f2?+9MS&LZ+{u!8PJ_<~w4Jw~3_YDW&+v0*gQx3tW?U5lWCTOTP{IJ>XKL6k6x!AwqC&aDuKb`;l&;LIE@R+kz4gx)7*+qQF;Ufx7A}KMgMAw>#K8%^C!5Z8od%I>s*o6|2n>IDhLHLIT?MXg_gP&;jkUGX;#N9|r^wc>e-rEVA9P6$e?*DZDLk}}X_es)(RH};&$VM2Fojsi!OouCMmPV7-^G6&L3CYrenc8+6E*F)JMAp47%%vD7OU)ffuGrZ?W<i$?0?h|9$87JDC~o#<sEO@?7_g4o<jr1gbjUcOui4xnJq+I3h)K%!+9s7DrMBD9EC#s8k7bHl2qq#Nq_!<tQKlQ(Bs}OR?`^r@k#-iTX>+7T@g&V<qD;H2jBDsvRJSpmL=|Mvbi(|0lBU|vQGo><o)wF*IO_81`P~8PKOgF7s*p-<0qOXXr-!A#cN^rCqaRcOnONXjbMbJ@qo)HI*=Ig>r)fT6Yrr-lg@#BcPHyMg&4r#6Ez(Ll3623n#mTT$9c+Ta;)`=#*^92kZ7*nIUzO@@^c)zaaukPTXN<iT$HU@<-HCI%eg{lvh+OoS77I0oh=JRj@nYq*iRK3L(%iU81$(qAbJcss@n)_*$nAm3o+rw2jFwv(OLsJ}A(S+*P1H)rXx3Y3e6X5))Y<ghS~It$l$PUd*PeCTRSx8YQ_m7rHpCAL?XeH5x0RGQ&TR%}AN4}{NcWTs4_2YnbeHU#=Q-GAQKISljSo5-aKLR7AJe0O>Jvlk#UT9eY%tI0;ZIfMVg5MVGo#`0fj{N<a0P6XbNFgj_Sxh7KKq!oP~1x^?uTc`u_D>)`wjawdV78BVH2C+>>>BvYh_{O%wN_gm04}5a4(an8L7kSN?!1$sQBs}RN@$)@(Cb7Lb7kCB{1c=Es0RaD)QWsGBgo0u0+mxqB$0CMzP`h@+*!EVcMF`ZiJ;dL`fZXQL4$&b*?BoAjijoABR)pb+l;Us4K!q4uY=|#%F6g<RFm*=;eUv4jQ@70oJ|b&4@G$RTWG-hzZs!q=H~2gI;6mFs<?s;o+0Wido}^d}c!F)tDEntD-<%p)zYG?WK?%%GG<BaLH=d2U$q4HrZYx$BTF~GSsE;LjosQCXQo6V_EmBHoByJBh-%oY=;lq>QF4RAlGUX+Y|1O<y5%mM^%L^J5`oa`RyFDgo^8{Axx4GQ`=F9DywZbY<*10Zoy8!*~Dbm7blm{^YtF=z_LBrSVUZwoWehlevlLU{8wtVv`DzdvSZL<H^Pk@iNXc|-PC6DoBzPsiGYXe^QrjpCb`gZpo9P9^9j6hMAM`tM<eN~kQl8qgzQK*kax}@zKFXP6T9HZZg#@ANpl;M6+Nac6*f{hYMSRw;x;Eiw1+GnV%^li_9b)=Js%=S;iZul9<I~!8Z&ah3UP{V2+IRZ8?>l7CsfTtY^xKoW6o3PM3|~>Mh6u+xdls+8mE=i4Feor@YxzvQ&8Gwa=ANMfy(Woe6finYU>b9&syRsAu>W^YJh%<;K`Q+`;djk4fgy<MQbg^^gf_?i~TQHwVDj1JEvS=W1|`JGhb*2j@x3g)Ir)}a~&MUf^`#yY{rp9*(2t@u#CjqA+#DZA&!f?$^ccb|0>MRPK!EemUb1#xy9z0j)<jH)ojxLwcKY&E}VTp6-mdHnz;l~N&;}?M>ChJ{*qA=5#K{>`UnTJv`tNC@VE}nr8Z*b&Fs%vdLn0MO^&9{E0ZWSDYVShmM^ef#wK1@@E)e?;+5?|gH7oLB4*AE!aayI5+`Bhk~55O;bUZ4;jECh{2RoL7(tlw+&EQ%R{P&Hd{0j<q6<txRSify%_oAI?qeEGr%d*Zf@5Rerhdmc9!@)|wkL@45Cf)MQKE)VY{nqI*r`N&KO%X77?~fK;-)L!{TQRmBA?c`IsxU&LBv>B&r>q4If)OSVRiuOREIS~EnPxGx`c*wanS>HN~9b0&ysnlq>KwGlO4V4=)Q0#e8&)1zQnfJu_p3MNS8@6gFqpX5`YcmJLV}+7&6mPO(<q^qxL@8drP`vhr%x-2ghsXhaW^CZ*)4n{@0zXJ#uGgf)kLy9Cl%_5TP>b>14w(i(8RCr;n*m*ktFO8=Tl8#pb~r?|&ZoY$Iqrn@KZ^GR)R~S>q1-VP5wR|5aWKKi-DrfJ4n7B(X^^mAIKC-7LXb82_>GGHh&~JgrS}z8J0_BZgGyQ&j0>e(s5ju-Vgb{opY{#@P5Cogt}o0A8pzQ`s;Q?nWR94kA20=_N@UQgbw?P|V=D$U6Ox@w{25e~fofH8mVsx70fb93{dr`c&$-vVz2xseI%RgRe!a`jEwvNKV%va6=sfqLtM_s2ZY($EgKWst3Z{cfk5)0&^q(wuKnDiU*&6e&d5)P!Ci0f)Y%9YcSpR<C!{)`o9l_QCGh*gu47|L8yBcgnI7hkQnvCg91K%)-%!R{7bOu_-_H3&VQ9*>GF3Dlb-&WLDJ>ldQ5ux`S7Up^0VQ9>E3z*)7Pn@5#!TGSh)?LUVLK5rk9`Dkm<!IRj72^(=sMK|9faGdQFLH9J>8^4Gul`tQv%FKDs*`diL9jMOVKJB)a;e1VhjLtihr84wg~qxt~@Hy79Xjgq}SqfzWe5%NX?h?-B%E{apZ{8$T*A=*9yRfgVa58i1a|pUWRP1bX`C004UF`A`7#%GYbhpAS=XNc4H`O%?Rq_S6PEFFvur&U3#9Vb1ZS268?u=G^kI3T|$DIsj{4^Rg0YZhbsF&V0CXzb>Ttuct4g#+Q$>_7MThM^NeAg35;}JvvPJFRRN6DK9;;qRJ<S1(oL?RY1yfPfC#T+|OYE<%3FC;N*n|!{W)S3l#C>=C3lEJpbDcCpRD1;pF9KYrvA%mZ`y#Tc6jX$gAHCgpb$0u7;1>pWi3w_<d+}1R(Ntu5ciF-125b$nkZpaUfv4_H{j2y!xFTC0>USuR@6De-~il{Fe<RE<b(=M0~AZSrFod2Wtd~4^?svi0~l`-VG9bn6h~!c=opm2G@TTpy2Ayp`hRci`1aO`S;x+z=tVZLW1XhmXYB3-xd^j;Xwri-15)@11~(N0DxN_mJ#6j-(}=?{&yMmo&Q~n`mTIshkTcxRp7lX53Atbwx?BSZ`)HV*t_(o66kGxoJV?Re^;TqZBJ{U-4!ov$nN43JFdI@tc>c;|1Q9~jUQEbZrjr`oIC&93gs?6%7eJGzYExH<3|y>ZT>0)w#}awpmyPb6{THzRD@}pzbx47!h;HIw&h_3INS2D0-tR>D1ozcKkd-$^0O*Tw(Y3}j$L?AgT$_QVMk+^pH+deZBNU1?ELQvEOzNx4GO#Bg&l=mepZdcwm+{yV^_SWLS@^YR${TOkIQiE{O@`scJ(_8BD?UwipVZK8i2>Hc{vb_UHf_fAiL&eB_iAUxEhXae_jpAwm)BgNcQ^HH%d76XewSmIQII~GXfy?I#)On5caxPx&9FB^{sD2@aqv&Ix772C~6%Y0DCm`ju3`DqKZd}#U547qXuJ-vi2MzJN?suWvBMPwz{>QojE6&SCR*4o4<14?DWqRp8ZF;ohgN8t6wQD+v}|rlb!ongk+n)@@Q=RXB86L_S8UNt3NCN?81ZlkG{r#2jQ+g6L+0j%D)_V{Yz`OJM{J1zqyyF>wDGG`a!GLr=DLeu=-cot@Qv=|I!+MIh^{JeLr#x^+>B9jH0f8zee=*8Vc8-rYl|y1DCFQzut)HyRXCwm@YlC!lg@(EMV!vgCb7a{8dIsn?K9Y==|>zEIRkIgo)1mEaRc`zefv)9$nof9CYrd4gFkvQi49`ewH!M`QK%<bN+V?*16(E4cxinMHS-N_SAxSE<DJ<&hl?P(%G{ho#jlzeZ@K7$Hq&5=G;#!nz{6-2xc~aSzyeC2Nw8p;eiFYTzF7IEa!ffpvt+QqW~(eca5V4CXcfA^}`~sPd)b?a(rK#zaJpud);CUlDOhU4TQMjMHP0~_SB9TE<d|ZXyN<N=&0esqpY1_!SMiCa9oB3;|AsL!*(4m_;&+w!C?gGHF<+~pSqf_LUTNIxu4&^5ai&&oI%H{PGQ~uhOZ^+*m78JOWdewCb7;Q)Mc^$d~I2*cfxb=<jQ*u8J32m@*3DMUo3o3WmYa^vgSJ=4<TcsSD((B9<=?bs0uY~)-%eS))9;aa#19Y74E*`#MWtEYn26v3uSq&{h-BgT-igq2f3}Wt(q9gts9Pq9Sfb^ny)?SfA11Kq#d|YsQMB7$HB#KWE)924?$6~P3n?cH^9(x;|AFUb;+&0!O5-1qlQnlIK6?Xt#NDp=X`7ZRGU*<cdAocH*l%f6!vx2lGFMiQ7}z4?QG~}Ij!Aca$3*gb`NSY9wMoAuBm}Zt%2OD%xnF$ZngqYJl=LYvXpG8t=n?FYA&z!vvp~$+t#$!+xfN#U*)x~NNbJXVP#fpofxSePh6SRT9d))^gln~cf#7l*0>?QBLgWWxBlFo+**nB1F{rra$J+_YlXEbt|xKZk5rPvjJGS9QA~B+SVOAo-rc3TPEWyX=>CFK*HYI^F4gt$DC4j_%U6UP#Fgl*FrDckvs^dQ*LJM&R=$*)lU$EC+`v`*YtM5XDpgsL=Q>R<gypVIyR1vDYjw4v97Lhj9wA6G>(ytwCTh8BPIf($c(^UKE9@K$k?7jX5?v!}rMLD>*8y*R=ycb<<hySFs`FiMZRhW=ldHGLHAF9P9lpA~>M_!oG&bl=<bhV|6Qh+o9%HrE(>{$iI4faW<+W~zGVPWVVhf?dv5~`&(+t;YWZV~3p_h(`hS`Iekkv>APi{&_nbex8l=e_hia7^dHI-~4sdbtB6I=J}8Q(HKcGqy@F3fU$&u=b~b(+xco+YymjbzqcH<oPHL>V@u?izl~f?<7gS`+05A&|ERrE<2!)@#pez1FnW;oYRQ7OgjQTI-su*5Sac)|yg-GFx|z3$xb(MxIcw3u&#}Ye;L|P-(5bwWhVs5+<n3z+O8wr-w~#&3^Nvk_6^im=fJ~eQImc?=4)5o#l>s_ScZr+UFc1?7_vdz^Q+2S@qfQs5&PKJMetyWht4pm)BooBg<yp_Du5SGh0JLu#f08;N3NGtsRnG_s<$b;=gcj-f)Smc~YsKXA^IFgej~Q_oOMT$%VopU000<R#e`W;WeUjR!2j?kH@<>*sb@CxDw5<L*%Ju3qmeO_ePkdy8jK*RO60m&dQNbRo%9ws!r{4e&WVB$?*JL1CrTQa+Nf|HG&v!7FDx<I98Xnnh7U02nJ$!Z1SX$u-dFd4Yf2AYs^_4Mx#hpEiSW>tvW|a`E;xRQr^Cke(l^|L@6U>^~Co6o4bBV%IZl^Z0Y_57}G}XYG3V@7E#JOIST4btLWp{FGy9bBVrs{ln=%#^Hle$^HhJXE(_*(;8b<0>a-jQ=){Y<gR)hV*Qc_dn_t*6S7$wF43)XssM+|!lEOOQWfGIN4Axzp!J0}<A+ByuVclwzFP$qiIFB_I?wX0L8%hFIA)EK`jpbgL|FS-vwYXgFQ0c6t?ChX))?2)I)(yM{u`$P&{4AVfK{*#o$5}wAI<2(`yfiywI}4ChWVhzD7o^O|DvB!+&_;?|UDnyqR9ExXf}zKQ#*E4aqrOBqQ}U6h9gmuX*B&51wF$3F<INApn*7?eC%-NbC9F$-y(0{!ktkaiH0QoD2X>k%&yJkl=^bjcU0oyjoZW<z_mt9Lb0QhF`x92C!A{@h!PJFOsw{q1T(u|y++*GhBOA7Qmp{vvogTbbfv+~^lgt@!I`OQTuv@C%fPTa_oVD5aMtve|mET&C+$e1YT<>)|*b>ZwoLTu2?3(|QKwJ~&>lnse&Wp`nHj5jVCW{%}hQKz~hlI_HTqRZ6v0>}SIyZK<jZ~Q)8%N_*M#O=+vAJwJjZNFY*u@Y!S;o_n(t2Qi>`?ns_8i%UTG1t|z}cj!^afMgA*aEY&)mQlZB&WWre^ta>2$k{=cqk6XSP;Qwhso<-S*KCGm!ht4&dIZ<*^=+S8!Bo@@jViw!kIaU7J}u@+1kVyB>+PC9K^Tm{%KiL1*~P+Ilw{ez)voBL|Wq-T)*w@l*IL=;o@twt*7D2Tg4<REBLMm6DRKypn2?Y|D1#A%w?Wl0WSMS+*Z{qp&TU)n)eZRKCQ@RNHfsYP+LTZGS$pRNH1|XjGwfST1{Mpwep}<n-FUkzaen>9y0fk|`{mLc7r;VWN_32P(S<z4Z_-^`|5g^FftZJLY6czPqka?(sHn@8qZ_`F@F3Bx2PTz`e?(ZDjJ&$+Oek*_ud7l~WlSGw0|?D;!zgY_-p=cD|h7Zz*t=RB{jrvR$q~HtHNGYDKFN<jF3j$p(Ft2c^;sA567}d=24dZr+RnnVm{R+0Ki?De~__?wpRqais_I@v_n3uXoGVaTD#91a9hCaAM$loa|alZ=+r<yj5yFeJUW$XpJfLxvKk;+Zs8TY4xeaC=`Meg$&E|$cW+7yE7R;^@G77q|hO;#3Xrjrc5NGeL%F8Ls0iPd38hLT%5c*(#fk?mia0vCUs~dkwH>cyEH?7Xc__5q}A%rFo%(5Gu?zpt0Y)ul(ZY$(pXPL%F>L&gQO(}r?Q@L8~Ie$*#je$^;Fw4p5}nl`lUlMlNiW?pPu0O_T8nlPCUtJ?W@CJH94(G{CB-vLQWkj$g*0i185a#tu^uFY~(s%t9K_Vxt1C84Oo=YhY%7QW+6c2U@g3hrbi=evT>77Z!KZqLW1kvSkbhq<b*&?p6m8{<+<Jg<!;1&%h|3u-sA@97Q*@fu6Lvfg4569G<;7ku*!LTfAH3+YuljJZcTHo{kbg5wM6xe&Kqa^IO!ob#b+0J&tpB&)|o3lD3SFzJLxVPlT!&)E{^~CWGTwx`c)^h_Tp(C8JjVzKRhFawVA=1+<}>}n6{cXb0oS#`oevde`Cv(rY9lB<}FaJdwsCfTidE1rHs^y)9HIY=%mhKtS5?khe|zYbUHTDP(%HiXH@PXfSQlSO9JYHTGzUdruE9HDQzOlhp;6)v-;tY(voL7!qILyEAUG*O;>ECnt7(<dc5?6U9GJNI4yIlca*W%N115aRgQ!5Q-p=&7@JBmo!<bjNixme+7MZ$IaWGkifJ<7rs@++&xFrf^Gi!?o1L_XtQ9th?CGVkUL?R$nO-`mOD`=(@UJGnG>IndI=6T|svOgvIt=GEbsMfaR06@PY!+(6l43g05pIc!49GDp@!Is<sy)dx$0hTz^KzQ$$|9xRA$zgHZi!iBh&0m*J28BsY336|J%RriBH6TRAb&v72E(3^)VVT;F-IM8si!xGI8?*m{{KAnv@ez$2gVO7(WC<{7`dDtiiKJ#@W|}kB}aM6HP7IZVO2P~d(aV%BJagu@qj@9yg|*`r*ZtimVDaW#&M-XcF6WN(z>!QP%c-_Ky52!W}&8kU9~%GEnCV%U0XJvjM|l4)CI08pu3H|onnzR8+GEfmB21Hx{gTi9s1N&uFDR`CP*Ey5;t>GH?XXnKn(!9SZxGZ!$6GWhFVtlC?WOMwvmw<jGpVa4o!&2rEV)xt?gUl>}GEJOsA*T4br1&lk?>Jbwq^ka8-J0pR-eEbM5qeL{dT0>KxT<T)DD_a%rk@k}~D-`wtl3k@3|*M;%C{#)2$MwFsfm6hdK62(=|swOF?FL&641F1ak1^vNsk!a<L5gC-sB6L{PhJm;uZNvbiufq`lxwht1>4o+0Phgyr>@<4$~NoU?jRoyN+ro;m>ewDJC{Mh~#oW^t|X|+3i%IczIuxao$eO}V%Yi+zryXO;HV;3MNx(#`Jf3jK=mp2sXRR@4wy&7nJxg>(7T{!@$`#R?APKc8rvb`qU2P?xo=0pXCQ3184sk}#yT89U3QazXET10Y^Zh)mtd4;dSOzdt13OEzi5*{$5q=4D|UOkxI@0Gyp+sQ}qT|UcJ31<KOP+)dMD;cLY5X<h_q3k%1kL|}!*Da>GCdVM8H;1TszXH$RhV+$yZQCy<yl%4@nr6I~p9;vHkRxSFdhJ(bz4r4UcCs&h=u6@wSMZlv_G@a0D<2~NwP(k&Q%RbBe+U@6+*oSEv8y^p17RokGj71$^BEoPlQe1zeqDdh5cbHM4sn_pqvX!Skhdd8u9teJq3hC11zktHYI@pF0&ILsQ)CW=IrKUrsE*(uWb2?J@%0`bKftLTTc?%4by~>^w;tBv)~9p0^?KmCE4X!^aqD5%<w|Y9^+QA>w<B8tL*v$oLMfOWTLN(AaddScY@KoI(`}mbDYt#d9|E_YZ>k2k{)Z&&!Pcq)u1|8K6{z(+UXQn6E3#mNM`vXVC55g}hO-fkiR6(5y*}P*G4*?X8N5EpqK$v{KeJ=kX)N{N_3kj>b-x0;&XfpAOULmb<T?Y_d!aQYcF6Lz1Y7U%4k#SI%Cy-1&m7MJTMtdxIysM_30c?FF!1WzgTFFfeE?j2(vwvPJ{7#WHymJHf0&-~aW;rA7Tz6bUDt;%<P&cVxb^M9tlx$~?RWxPM^$nv+Z%ve_fpup&vRCWt?%++IRmvmDaZJF6{vOeo*&M5b(nR37`!?^_4H$+Y8_@haAk|lm-uEIE-u+y2mpq)z;)KCZg;K7^@cmEfa_YY)FanjUe0R2ieF;qXU*t!viN+b{ZQK9fXMWa7ju|jxaU_0U*Ew7SAhaK411#yO6S7I$lTXWlPR1~kIEj5m-Z^93F6!al3i%QdRT}Pc?!r5%K2mWD4n+Vs2&}<BK4KW=L5}7axANtdl^dgy<RvvFgv*{Osce>dV2J1_zKMK&PFtOmYJA%V*4K_e;JgWfd;-q-nt27@7_}&yKe&70XpsZT;U(5fjcTx=nW5KpMabgDvP!^433>OXE+p$Jy*<vV()othOuX#j1<SN72&W*_MZ34q3l6ek7S>i@spU3S!xM>S7`P;n7#dwPg*;y&8wZn5~hIPA!N}#7!uEJppOO3o|)J~B--{F%??Xj!@cn*JaEJ4t-`cF4iAo&R`wnFQ>kTl-=OVKLk-^}-9`G7sln^L1Z<ZclY~?-4nerHyiOtRiAK1$Q`Q&>yq!te@Ksghrjm8ehEzjuZ#2N6Y!MWo>};zHlUm!)Ce?ALU=a332x>Q2NR1{eu_|x0$mnp~nbo43Eu2S8%V!vrI}a*5B!vcYj9iCxhk-4?c%O`o5PV$+b(fx1Al>!L3ZT0OC<5c$1)5Yuy0hD80lIr)26^iObNACd3NQvcrE5XBH{G60m8(7$@9i!C?uU5B(n_?cSET>&DY(;`;;f0@`XSuO80En;{~9#3!`mnKj_=$(zIl5I-oAJ1u4lGCwQH*_5BF1RO2Zwd;PzO@7Odd*d<2!q!+}Znu0ie$J<d?>V5%CJyN8KpoV#ZQy1TONSdDO31-iVWTmx?BhEfcATHJzcS2dExsDrfU>r;ixXm(W@Ha%@P_DPx`*^R{Mw9o=#XImglU)RFdNilRugQmcBktkKT^>I>dJwPBNs-wTG1g;ygOAho%2Js5yx=}cdlvG03*&|65|7jteVo&V=cI!8(gE9cdj&Cw7lo2o~;@F8i;=if@i0n^P;Mf!1><>KIZ}b$1oj$JxvF~uB=^5rG{UuQBdtBZn4eKE6^vPfZdts<)?`rVtdTL7mc1?|X^m-Dg@iZUGq1Qbdd_A1<b(4Mta-H;{*LKzAwwrL(f(5kB&ZJw7Sg(Yur!(Ag8}zQHiDStGE}?~KpSNU7c=a8?tGE4hxPC2MoygPmz3CaRgjJtxx$Ri3No-_zRbX}9^M($ZRl(IKHCmk~mdjUW2hVP7F(RD$i!xljhrig^2kFSF4y|}~4VWNV8CGD`vt_^`GHq5@BGo6wdS{QpPlbhV!>Lbp>0kJNUA<#a2~$st)?w81p>nb(8np;@5eu!NS7b%0D|JDIE5YeXFgTHTDsJEn0Hts9!-hKh6NGug*N#Z%Szv`@D?Nz3wr>UzI`@qoioPoqt1=R=NX%*|IsiDS1otdJ^sSJawAgx~+#$I>AoO;aTbflsba+5(0HU)OH6<m0K{qKk0EbRYK^#losD_{;2yQBbVIb(Z2T8vT4XIfVLw9p1bokA^IuyG4i_QIp3#UnhB^q*T!06+7EV?@~D7v9jeJA7%KVnRlS#SXObH@{q0Q_|ZpnD_5pHF5cimsJ7gEwU|og{cf-mmgA{5f@yG$aGt0_@7KH}t%hBUhX#)VbRD>ZxzhZDo=6MuR(_G<7^?NrTU0*10`T!!?Q3jCxX<j0AM9_OJjp&-h2SvoI~x8vtHr6Zw+pM!rPX?~Mv=uD>qe&EepX0*|JA+^Mg$gDYP{g2n8}j1Fy{ZNHg7^O92Kn*CgqNyoHC2s~H&zYK{mBy8phpf|p-K8syd#f*0kQ0LUKv|`T`*lf+}FQ{*P&45Ood-oD{E=PvZ2UrEN3We9?rbV0q$P|Y+V$``Te}M91HBYVrowI$f=Tfa!AJHyP*Wlf2&^e!a6U_N0#+;`z3~bhFB{<vL3pWyJxu0%_(dec_i^_dF>fAR$=VEaisPjK0h(*hJm7-5zL!GCX^J%rcX=dp5@n?oP9}j{=z}y;g?sq+IJw=@RIAqupa7htxp1zZVo>gdbJJ=k5s5nO&nJxm(!&z(+aC)8!w0SoY+l4m?jF7c&ftpt!%@NSd1?ScQY)<wtAZOxV=J4i$e2r++25>VDrOG~1KtwQc=Cm+48r!qr%)v~(8j!hpY-$~V=3Z8VUkx)45!Y4`{B=T_KjbP$sffSz+fw}g0nL?v+TaFx%Oa05Z!3%jbumMlOL#r&ygH7D7zDNA8`~%Ai80r%v{YB>tAQ|QFI!HIB*dx_$u=6l3SR!I0p>Ap>)@;btu1k2v;Ac3fu$I8%tt$ogJeMSHXaJl+-ID*o|8~EF++tl_Z93+Z~gspwD}I#=up~e3*!8tM2<|10B+thTI`=u`d4Cc&BQZ~lH4D>IrBCwsz;q!m;5*3(Q;+zZ~GzKudeqk2ZGJb6JC*@#0@{&uv#nBoHsIYXgU>yC7k&*^s+w?XI|E5Yet#(JiV)n<3A%qnX9cRcn$h&6}X|*!gNKR?2ehf0@;Q>DfLRIxtuIC0w8vz`A!aWrmMOFY2IKz%VngwUjmxbAJfzt?9h<@aIHY|Hv5YF*t4O`@rTb2t%4d9Am)6Q%Z#;_Am(iH3c_63etCeoJ|k_M!5lHle0y7;@Fe#rg_vhLEyI`_hde@VM4cAo%jTj?ae^t5K!vAqwgVfRUIo-#N8K4}o}M(dLd`kum<xOtfaZG;-nW-1?crEUm0;#+i9slH41u@lhXk2R`5_VJC=8@l+kjOXpmO<(Y3P%|i{w~2NIB`6GM?NUkm0-c>w=R92vqbqw(W@o;)nnbRu1jJlhj}VA56=+8{4eK$&R5OKwNWlUmYDCbF61-y)s9`n2)gwtbygks1{&(w&w!g;m(D2WO*8{w-vNN%gcpKWVsr)e<<bbV(AQ9PR36XXn)0Cv<NNd@fe&{gq6#NOtV}<qsq7Wk#B8loe|}zE$b<a8)^-Q`BNyl*m=YeL7~$?FE{uY8)B({)hjC9G#@>ve7gxMN7|RP_hJu;vNgoA#*^cYM!nIc0s<U93r(}u;J2)b5kkuKTvLs9IC;-~Oyks2i@1m;&++yB2bAv;PVrJCd8oHb>je=07e=A<z+(~g&%^I$A%SKpli<ZU+l#$$_$0YW4FCRs%D3yqLY(h68a^M8L7auyFyLKQjyZ<3kb^^Bjs(>Mc0A1o2C_Wwjyj?45W=bgB_A3~o>z=kB|Y?~Ln6ov-<4E%0Wr@0gRdpBAx7^HUVL`eXB21K(_1$wT%1qw!o#Ni!ia|Rt-3qr><(jI6PV(_<E`i%KRl-MDVO=dPq}~OXz?9rIY;soFRsKb#1)(PslI5Jz6njCx)D2;yaQ(3U}rG}1UKG_>T%<(sDvAToYYtUE7y<ffaCu$5ICMNaNIjY-eeIv?pdMZ_B7}riNKypmBgLT<H!4F>3`F0ce*AUy4*TKrdR)r<e@MC<XZz02R?M3kr6%rP-jI?Vhfi1uadALhbHfzRd<=Gmj<GI!ljwm)D3%PUi7rN{@Hj)L^;B6Ni^lzFy$WozY0{YKdMcRt}Bs;{K<O4%D42-cH5->4>_o*8~W2h|17TWNFt{UFHht$5LLRNyVmeGHL)I&(Wgi+^*2bHp$R@jPpISWvmv8q^KB@EIWcihib1hp^;e}wCk{}*oMu8o6bSKYuL@`$5@+|%;$fn09;`;1dki#(DEIjkO$E}N))W1S9I2cmea5Rxl75J*n<c(oTaxr3O<hi_TV+WH+T5!{n@^}%0W(Us9d@RMOOtLkR-Y%`8;~b`Qny=yI0wesuga4?878!3yIw9;dS@!^f7@g770~7r{fjhOoDakwRq4_d<ov7^a!#}r#JL@C{!}u{Xg#kUabA@zT@!=&<A5(W##Ld?C0RQ6vJ5#FiCl!7L+T%(fsyQ12RiMj^Rp0zEg55qI;XXoV$Qc9Y9E`Z^DQDa^0@N}w<*HDK1n*wpP3}x8#YTizAHh_?>0?3D$Dl81#j-Ca?apP>3Gv+6`~;L!y?WHXG))NaTJ7$;taGOD6MV-oyQ7wu5@H2>^vS8cJ8ORbH6@SI*wfFOEvv0S$eAuaxPX#sF%#Jm~&22mK@-)IjR_pIrs8#^Xb4_3*4NMf!L_XdI|*aL!JR;`jz3#)fS%~b%T_NrxE5j7eek#lNcTT0ahMWnjoyv!*sV<AJF<vd%^@blqE;!6|CV!P{7g&(1@6TyCtNG?-{(@5!|+_O7))yMAEE_i?NK6X7x%pxq32qmB=3zzMRRX`l)9|=HfAQk1LL`dHDF&Jv;ly$Q42U8?u0Z0j3<nzSBR`Q(3BvkDkhy`5q=nSNYLNZIe$Z8PbzDS6%<?TGFFWuq0SNSb3@*ogtv*mZD{NIZ3Fs!pn_M)&MVe?jlV(v|b5Z?%2`g)T>%>`9N&BCRZ)ITuh5!1}^t<snSJO2eaZZSHR16_;D<uS>jDOpSUJ)xd8(v-OKh_+cc_&&6bXbk7ma}0ZPnF+$wbW-iS;uNkXUIkej3IxBG}KKO5sr>@*t&WZj9YDJx%h&>U-wGC-D#4$@U8Y|W^<`$h>Y->W{*wZVqsyy&n>MOSi{sq4JcPA?j%GwHOvh>Y<ez~zw)M9nHk;%FG&sNm%}9%6Voc(cf>Zsry%<4S49Z1JSk4hEOYkRlUa-pq}9a5DAqAdg%QxzWD^bE$i^xzxR=4q}e8s#yOefH~Ym2_M-o<|>&w{rk&c<_LvgUcg}*B>hkpn_C;!yxY?vPx5!K9c@kpW`G4}d1%y9{%Wns)Kxuk+5)W7bwiuSK$~}a9Q7iO(Uh#urar#e1~=ck{i$6RwD}+YxOF(V`A&(7a%LL5QA9*ZGBN`WuiA0vS>zRW{^|hcT>{UUdpJiQ2Po_Ft3N?90ou71c+Qq2hE)eXSA`PNBtfgq0;URtt{YXL@$y$zEPC2NBWybng2Mf?4ZjMQZf!$<6vw(H8&2J9$bwYwAH(dj0Hrd(f7mmw2d#)buCz=IVtqnH4hnarl&5j)ZLbct9su)^eN+iqH-e#(tl6)_tQ)0=!mJZ_C$2<Vv!fTpf>V<1){0rL`eueEZXjsgnc<ANVgI|quyt?&2;N8|D%HSsozu)HoPyWS4g{}DOWC&>dfg6QM_?XtH||~3|GJlUt!mh%aTJm3{BLfGbJ+E9q}uBxO$q*jIB{+A^@NA?5JPnapx3=PYql!&I!zi*6Q~+v!3#okmvHO{W!ER)&m5RtMryvcLfZB0Gk{14Yyq?<yd8m@dn7b%nD+j$9`?mF5t0KHn09kYiPV+^>?D6&mh>nR5joWOtB~y&KqC#yRUzB^#~L$o3R2I3@QNB+bw+leDUEn);Ujxmc9r`YnS1<p8RotX#yAU59KvhWz}(e>;n>_jocn}wBG`S&oCzDwy??ChLdYjNH8^{Ll~{MPcv`6y?_LPhJ8}PNRE>8}rAe>os#QSVwW5vXi+bQYYcy=i&~k!EaFaUh`~UJ1Y|LqI9AQGkEVsblwF0%49ERfdFNdLi;Y&LVUdP0ZQF%og*CXMzC{+uvDk(cc`z|rNw_bR7znx#uRd{&MK*M{3(D1v-sTD9h{N~@7^cw(%pTxm`aUVn~V@KT7F~j9!H+SllwB^WZ6%;<(9nHY-LgWEhc(xL{ZWn!qh>f|KN+3M{MWpPX)di@PfK8<lz~K{hh$C;H7@AI1%72O!3lzy|mUxeb5%QzW&~9ul<tp{^Iop#1>PTYj^v^1YJgih~-$1m*0tjE<1noY<<VysMIVgmb(6SMcW@twiL*jMc8(o6-o(Pt97{hvrq4{Wp%H=%3OlZ{6L9Tlu)5vi0yy=#1wPnfKg{P8qGp?tz5czysK~+U7?p^`raiXG|@Gg`qZX3<i0dx!=5xpcw3fs<sROO8fGY{b?0WQJJt1w<xM;7lh<7PTaH)_B<>pLZdJN>UQR<0>#;5;wWR0+xIV>u1Bzdz~PVd3%?U|O1pcF<FEt8nx2sDbmIQ6Yk9zAQ(XXsu9U;kiO@slw5xY>#1>an+<71CU0{v;zPmP%nF#G7w#$q4P-C{(ny1OYpqZGmYSgpy!$Uc#!}=?|3buUH|MxrgOp^AIV0A@F~ubdKC%V^ZDAvh&QnFVkMXJwR_fl?Hufg!e_l+0X2_5y#i`Jm#7`y3N5i*s`ma_V6=T$Sk`Rqx%ZqbDe)`_dUyw(Y&OsI&+w7VGLBwiFIfb>fTKs`9j@3kJ5QBh`lpgv<Zg$jMl1?}(NrfAOfdbVJ{ng6rxz+_QOEU2-Hupx#6z%Q=^Kd9Ivc>D{jU;@rO)MTr&YiKWj5ywEInDzw18R?7Rs>nULH%ITD$83rH{=j%2@iQ3f;^0klw6Vx5Vu;%JWLUYo=QT?tMqpYY&()^=gZ*oVuO7zkKR;IY`2tmz5B5IJTM4$~rVENPX(9hfU`7nzZex=aA&a4mdSl=r?tk_}7i8S98z;Mu*Kp6HyOg4@ax5@btV9uhI1VV|av7s>vY(VPk$)WaAc-mEfuueyRq|YIa?*_2^s)S)cO0%I1!9BkK>X$JyB|lY0-2cSD_WYQmbxov69T=z32C0+cQM>k!NTQK}IM{HB>{<rXSlrw`HB)K?GP=k52q$?6UsNJzUlzaX1?c#zhcbt~7%<vt*l`<8-=bJhy4r)iZPZEv(m+<Cjr+(2i}Q76wLsl#+ENVRw!AZ6<^xwrB$m1=-}D_!N4ncS6VP#$avV&6a3;6QLJk|g23?Kpdml=E<@%`<keJ*RY+0Jwr-6cf5*sb`|f2DcYOnep~gM>(OpN8R*|<EJBr+wbtS$K7&)L2%(3W{G}7KW*Yr?$8Sf&!)C*)GJ!g?9}NNyK>}3;^jl&?p3TbJ!@MDx{u8$d=Yc6_8x3SO8ZXbB87dJtiWKv{aHtH=?smyXGzk*9RtZ=#Qj-g7qJR)FB>#bGDRZNMBGOqc%P9`Yed~k8h7tkfV=n1I6roXIl9QwNunO<$kp*BokbY|O6twi__pPXs)ujN0DL9Q`e(<S;yGilXJzUbM~(fUKBIfO3zSHo?4bMn7D1t)2HoShL!yo#<V$3Td!qELi)E>|?+Ya}w0-{=jzw1%D<yIF@*Gt}+NWDV#S$86znP>(TNY!XvGs)7d)a|6gAHKu075Bfd#XM&0YUOWI!|(p8t`K=7-4n%RWBw#Xz4AO(ZlU`=;JjRm!|_z29g4ZrE+;Z;YftAbkjWIq2MEVZ{(kc-<Noj-p@)U{CeZ=r4Bvk?32d~wg-7L<UOBKmjgte^H_%Blf|=9j`}2ejtmz6736X^*o@s}o;#KeO=B~6pd?CkXXH>R<9a2QkP}R1S41r3=yAVtx@Sb-slrIpxz?0Ok$AY~GYlF<5?F@JF-1Q8r@b|1gN-b?^G+;SL-tXmgTn#vO+9H>+CzR@(%(aVS5oDrobA1IggF6xUl91%nU6wv%*y<Y({sao&Ka528@>Q$q^DzK+L?2YJ1(Oh?*n!{@+D|kaWWNSLm{G-KWk+Nmw4%nY)g@Qfq33M0^^(1&w=q(-u9d-DSZKs%!%5K3{lQxbru%T5>kNpI6_tj#OJ&ic_984FX_<-buj$@90bGfe>8>tW3(F-Q2165eozMC{|T}K=HZqoY3$44@1G7M=;go$z2C|C+NTA8U&z|t^>BT16d0M?jYk5wAD65ZMZmof#Fo8X-WXu}-NYrqp=qzxKi&V-%-+7ui&b;I;qdkt{qMGHdXnFmc>Br5jPDVJy=e*D+d%j9%=avx=P>tsxCVZti>({res>b=!}cML;zj6)F|tFxN1WjxdP!}-q2YeuY(d~)zZdrfdcnv+_NtGnJ5&i%f%?1;U(%yPNymA@4-O@*{<Uc-f>iEan+rU$$7{^=V*Z<pZVh@ZY)b`pp#3hdcgRgz?f&IBA*pP~*W=kHpi<oFX6*S*&x)?+C;Mvix69N0o=<G(JjsvuSs?XKCSB_Dl>8hXP~X2C^gt050&K0BM2#6Nc;bklSqG_S;eZ$W7+XIOO`mV6228)x#Yk&&w@cgo(-PXT!Rd+LW_r^&R3F(P^?&4rPBX~`QdIr+fJTlRxS}$weitoP^K}7L&k}CRjrMtduZ*c@@;>5hro|H2G4=g-TCG4Bstl<gpXvZH2K%@IQ%^s~oODtwh<XxSWI~<p9YSm@eV&KaZ-Ka>B~wJzk0&%I!G4*z5}f{taHbu(v~VEm^awSgp2U2RLF%8H;+H9)9@7xy;q>D)a$1kHd}YsR0I>cK3C&|;CZM?<4pGmq_qlELkuGs}i2AH3wzoD->N<x^;{HVcTD#3MAEcuhayvbm(q`n%2q)M<^-uCspVm8^8$<h+VfEWQ9PaATqbK<clrMU#gsRv2kpvJ6Z7Zx^J)z~D$h6r(_0MEae@~i=?*{d%F!fuBU$L$nRW5LwqRH)e`qZG%%Vj7yJvh`;kGY0H8QkS@Cu{;A&X4^yf$7uUO?iHY-)&M`4PmRrHhx<u_-n$`Z}Bw5Q3mcshrDFE=ddzxo+jGv>tBvYRzJqZfZE;gL|gXQ1fcazQWY9Z_lK55(mUk1`^Y+V+PtDSl240mV8Ny{J&3{msop(I({7B$A*(>wS{&0BA{%M?(?mZ5PS0JQW_fyz<mt%Z^dtrou9RPGGW$&8MOPX%ou@W$-Q{fCIyvzKRXa(4ODkCH58O4XezQA+dB;o{<x|eSCwO|+CQ=v7Wg>_daD`j?*W#h-v*PI?57rM(FWPZ1l0L{4Dq!d#mez!zH$NB>KhM-$Gk!i(YlG9Xvv94%&&zBM0MG|!5gT@1tp;Oht_?qLJY?w%jBd_hsmssK4+1hS@o<`&?};3*gU+W`8Cj3hSUUPt6bTUO!gPc?2ZJG!v%}I3jCat3c|*1eJ3l_vYA10_J_~Qq`kmBHyD!N3Nw=|2_k~>!Rvz4?STA#9oFNG!87S4?fN3NONEqQsY9on80+xS9)xw4mXh>3rH~+ZH3{0PCPcc_ROtMO7<0xg|bsYGK^+<U>L&nT!%px-)RpWb*Dx(9;7np}!O!EA^c3>`wN0iY5ub8!-8gih9HUJ`z7lG`LQFmLp=K9xYQP4a{1gH)tKW?5K*~D&EmqU1t5U&K4XH}kRz+3@A%Nr(;E>Hx_Z{rps=SlL2;v!;x(^igU<<Ro{14hnW1LRpu(9B1$pL)z*o85#RtBP-I*!Vy~ZD5ehff^ncKaL@IWr|aw4A7nuZCF^mwTj*^#l)LVF$btJg3S^es;{uA1VXSSWJ2S&?D^xwlbgr)<bd(`>yPwT4i^6;{v_jSI9R+61Sp4t<`im0nlB*XRSXn@LkATfSStvAd*HM<O2`EyQ0OF`X%FtYC+!wM@ZxCB^e@lY5b*Tdk6FZlyrNc$0Qk+=VX~DepwjnfG&+BvTP(rd1(q4)E40Gg(+brmy2>K1{RwjL^VJn$?R#*nH)-vs)h51n5z>wVE!q63L9(k??DPb9#S)_m!mgf0^h6r9qSycA2m5H8W{lAeT-UJ-Qch-JJ8oTms_?9v#8Yi8J}rQCRXCg~maV|4%VQvHW@rJ@SGh2TiBiYOCqS0GR&_#kDRamrD}BQjHV104=u&)&1t+~5rxEh$s4@h75}{36jvNY$(jF8?BNgU`Pz0XK9Cc@eL2{sTiJ<5a+QH`8%t`6Cj%F5-=F$!}uSJrVQRdrlPyK$br2|Vv`fI|=r3qM8(xn`(Twdyd<T2&yEL}R50+Re0{uI{aA3H5K&!-wlo(*&>!aRW;NB%g+L(EypfynoG{tVAY?Dh`Xu;b{7?xYnjE@a$<a??@&vh3+tA>vtw^My;$aCs2!!|$Ms3g3w{3(+PTMAX}_c8e^qaAm}Dgh{b*B_ez$fHAX0L)iuhhaVRAh?x6olb%aOX*nANoa4$d>n2!jMu6E40w0%Un|C-Y@b4XAQGr;Y-%8v^d{Q#vmvyLbenKMJur%YY@3kv1-$pT<1k%c+3iNFh-=8CJCDz;cVk%E-JIGu5pFWO!wd^Z^-Rki^WP4^G<w*^64J-ifZ63rKiAZ@+kM2(2ZF;JFhpI+*V}<NX<GU7IclJp7N6)*1q20Xq+6%iadYbod2SU3^ug*m5jEP)hH)oF~V=b~<gdGf1w)-W8ZZ)8Ln@7S5Z-7qmf=$`pTos;so7aMvqw>2M&CL!DZ;n)fxsB)Q=_p{_tUyQsB`tqi>mw&{*~RTRPa_>K+uZ@8Zh@ldP7ezW_cmSbun9g=0QZw^&f1oW=8VsIuE|0ndpDeB2X(TC@o*<e-Sb(GHcQv_gl+R~+I}9mT2Hc8+0TvLpoM4v%siUzj)O=p8K@&cY(Fi_qvtvK?HMM_KF}@5KHnsYc0^EZY#$mG63=2UM_5U3@9?}#c{6UpL6WDF_C5xglgSp01gE`ESH%LzIKBY-@Jtas)x9w28;hub4~C8ko;}Ii#tb{0!9Rw;L#I4e>sh=>Xx3H1qK+vNM~Bo_qEww1MYmeA4>YZ`NT9^3L~;}*10_C23DTbQc_Y5D57J7@X?5LEAe%XpIB^kdV!Ay;9$w3hrgR;n&2LWL%0AczKJHEU6Dpp>f40d%B7^4wNAwCpef`tZy5~~m<7Qt+huIdXDk8z0V(h7-2CW7r6gqp;4$)Zm0H(by@@W}h&2EB*k;R)~w^e`XDWD2u+9v%^QMbo;)MC#O=hS)r)tL79nlH<UZ7-MX+_0<jMr|Imo!b3*%=T`8wfFV-7+wysJ=u+rz$Jrh@9AG_?3;$)=TB$2?LQ%ZdxWTZU?8`jNg|ZyMIV%b+fVWz&Y?o70&ZJ%R0n!XsO@oMTLNpG>o76fUIOA84vihNEf0uWVd3^Kw_1UslR|6n=wH@n3d>+^mv6I-92FW{2c)(U$|PMm<#Xu83HXo+`6jG;$a{1)kXIlUIxk=JfV$}>24;IaiE~(OX^}5GtN?1~&DUR!)&BEeHs#I&<*Q&(tV75FZ>pH_^7TP%KLIbvNX&dKAGW48pV_pH_q6U4X8TFB6!Yd%>aP|s+mW1iOPks(yKuZYhX^=FxaDM{M8Y_@00WfeVic?=ZhI$GgFju_-L#r*fW>Zxbw@g~e{BZ&F_mv_oVEOwLboToq-UmS>CEu{WA20vqNi;h2L}+b*Ze<q$IQqGW=f)bIR8g%7;Mz%0<amhPtO_lsHE!s{nImA?*C%kw$#uzI#js~s3tz5V8*o96~}Evc+8KnSLZazO;h&7A+mn-NsfDn<E9C~F@LgcT$+{Gkptb2S}Q>}r<g$GNx3aV<7s;Lvr#k@hC6D7ZCbv>1;)9TyM=OB?>0_*Y=8IUtEZ-*=Dm7Ax2Xx&gyojaR)^0Ail?&vVD863_-Qf?$V?<k#ro(Gd-~QbVw$*o$Bb>JDrmQH!k(JgqY=CoX!j&5EmYUx(5VgFEv~IL_Di_#&6p{Kz;(1dkLP}pe;(3@Jc>B(EIzZD951SWO3rsgWkk39oZ@0-G`ILbtSKx&ZtV%D$CF11;@;wFqO)+=>+$VdqW;EINZ#3}&y#BT$w!>Clclmoak(?c6KFZ}1W`qqvb2D=<);qImoeK?OWf6GAq#kIc^z@+-vZT^*SS5KB2-(7=&g-PoVGmC!ZcAwk}FZ#`QpAHBX(jkE3w-7Pr@lLuwk_~6WJBS^mNZaX>SdB`;(|u#%LQ5ZJHblM4L||+*f?|o`kP%<3L9&r@N*NU)Ve`qaq2i)y13nu*AW~S~6|YCON=_*GLeJ<;(~Sv&gwI&NYdxPa_5XW6F&zxNOiq-F>kjvNz}A{dpud-tD6fbvo&8XC8%(0_oUtWitFV$~3*1pzvDnfZ=tv|5ZR+<E5)z)FRFr9VZ%le#;vT$QmLBt>93Qwm_z%u>a|plXZ-Z^+Se;fmcow<255#zMfhJ#Q3JkHd<gcI-cW5be=_B%)Mh5fd(T{hA~Hg0;WNytxy?~X_95bT~7@47Mzl!R!D+G`t0M3D<`yZXc-3tdpH{*K<dYowY<@JQnRP@l>H3FjOIC^`;47d3toXCWKMVin_?m_C7dVaK=c@J9Yh8>V5x+1wb;Pa>n=%;kV2w2(?8wr<*1`#UH2S8jhQCf3eq#kM4`i23G5tz#|#)$wTNV5rqfTHp#4T>gvlOGuzP&ykDTD98?{n?s6|X0^01^aYYW@-W$g!fZJCEdPqo@^b{<p_>3)Hsxlsv#sE}$vl8mh>KAXm;A=UZ)jdG@yPra(CWv7k)J%l7h2#<|%s4YLw4t>ujq^Wm|neeDndZs6RsZn{vvx*Z&4~_=2nsdQXNF|jv^C_w}@R^A)F8vWB^d0b;Rq>Rx^F}?)p$MpZ@+Xa19mg=rXNp^}($Bi}Sm|fo5>|TU-M_DV^pD$Le^Q5*{(lCcrI+SjS(>}CG<SSy?!(o$K3zHbnt_>KzW&APE0^=A>81IXmX3V4bmXU{`MIU}zm>t$%YU0&nme<6^8E7AA9K*@rTKT4=D%J#a&>8berf)w4MDv$|Hab$%S-d;mX3T&l`qYo#TWC}OfdDot{wmR=Euw5yq7_#)8B%lUYdJ<Y3`?`xi52I>Xna<t(^UI^@A4*VCv<cZv1@x?d5O2lvf6tdgb)Vm5<KcIrfDCq?V>u7LG2>-K;@U-@f+so%wHw4!_&7^5GAwKYozIP&4(;E*&|&G=Eq|XG2lne);Rwx4vJR`?_354oF?7jo+motQ(~IcU$zBXl70=&0koWKgJXF2LEvulX~PlNPpxw*y-@x&kM&<IN!Uaxv!RQe0%%rn=5Z$T$+2AdGGzD!$(GqwqB)f6uLTpRj7pL#L-~1dHjK1eR=!l_2pMSqcY1cy?AH-3=KrrK%;nv2X1~sqxf`b?z`nv7s^#FAA9A_`=@1$WnA{s{O4Tw$EEqd-~Q@v%k!s}uY6ep&t5umhCexrKG1ORAv$A4YGbj2_!qc|o0V|w)%UM2&AqTR|A{QkJMUj!e*cUGuYKp07jGZ?feG*pSm4N&;ZfUvCQ|?F+9?tb|GIW``Q$5i4xd_i@6~@@J5~eNUOIx+zcl|E|ChP$2+5U~mKWx!lK(z0UsuAnvnFeh+sofAtXz1Ts_S&p>dN44Yfma*+)MM{F~6VYvTrZV|AYVd%#P_^K1EFO`sxQaO+@#dmrpLueFHxH{LJd<D`i;s%9*c!Uiflp?m`*TEu#0%+}V}GUzH)<On>6Bw=H<?JMSD{KJ_=^_~jcfIQ{pmnC=p}3W)BNj}9-N{;G;xMR@nht7n$K{QyKdBGUeImMll_ynLzv^8R_@*zK?0AdR&0_W2^vd-?P`GRGy5_v+azD;Gb3KH>puc=yUTf4lSX7b(8`=Y?0~XNvHq;_}3RcrU+r=I85grV~;J?_PQ58~Qv~bO644`I957A6}I2h`4`QdFQ9)*Iw5Qxi)zB%K3}SKV5hxt?WPl?O)eFK?$j@8rUr(6s=D*V-9?8>BxynNcZZc7f25-zjk!#$SE=)mQQ_md!8i8*JUH2jPYhE`3~{o%9W2T*zQzaQ*|pBzOW*@S6-psy|Q}oedw9FA4uF%-zx#$s~6ATp8tdz{QZ`tBbS&ZFIM5Z(*jJ1Z|{8Y((Ow>R>Hf*<dM~5tc+T4_s<L85OY%9w_o{w_07wWiGQ10e)R+WaRtPiY5F>g7tsJ;@CrLd-~apa>u2QKVe#JhwesP@(%i}Am#Hi7uDpL_Y3`higLK{M<!@F_%>ByX-c<x3?Yng3x>CK+i*JZI3mtrTF0(=~v1EmukTp-mNH;IPdNs90h>++c5t1}Ex`FA>Q$!m%=crAx2XBA#BfTPiU4G>!eh8(%G)D{Kv!%JWp;uY;j}{_cAj`k5eSq3l-#TLwg~q0aJ@;LSB3}t1F!1@SGVt$Y;4;Qh;l)=joLPC{6m_^TghJnG8dRtB5Ki2A=NRPE+^4iiS6-wE`O08s(kLfP>vC;q^3{tkP+?k7PXAq9Qj9@SjUxh)liEScQX9<{`tbc}nUbaXSIOQY!l;_)HMHm7&q!4y;?t@`3Rn>2O6bgAt%H!4R@l`#Bsp|1lZ0ll21=e%&MZ~{lZybXDqzQx7rp__G&OR>D51)U)P=@|#FdL$O$(q!E+OsYf#uS>YG}E1q6S-TFkBtDyf9_5LNZA<B*gp<`D`~o7bTDtAlXKq=<@NmZ=d;wY_%Ggd7&47{>$oR(#)@}e)uiq<5hZdi~|kl1|ZL^#v_csD_^FaSw4FC&ik(oMxQT#^v3O17HFDRUVVe?B3Ocky<G)77xRxqj(oLx_Tv4*oKsKOiOvKe2?QeH$~Rv?x{>vB_977lc5zPE8S8iM+vSt*{k(8k`R|z)gPzi4$$8@Ijz|}|bLSXHiV@K){&4Qj;SWTUF2D5B>Njsdh-+$7H%z~nRq(Mpuf9VbO}_tGpR4ie%irBtzWI@AN>4tzz%Kqspz31NnaqYcdhLWVuy~zu{2^6W?=OFL5q9+9Ic02Mbf0Q@ZIa@gUH~tze0Z}!gaOEQ-K}p6_BlG2c9blbBS*-4B>g)8;%>+YRQaxUbdN60Eyx(HAa@7@W8hYtd$~*z>TbxBuZe+*V0ZBqEpYdruU-~Y?XD5;cMg9B7wNkfmOuOfY;^g>rMaVQ^1YCnkd|-7qO_ska}~~=OWi5r*EONwS5Mto{s^HeV`3!c3JH1>b0b{%(Wh&H!B^D*-N}V9UM?-FW-VZNd5ra4MFUV2OF?L7BH<;@AwFjg4KEgD9t?ly<&(>&zZwn-Z&pm)rB;pUP!u{<z{eK?-SnkIjmuxI2{O;mB`B-{mqe%2$5u{#SgyDLohQfs&bjw2sCiLzs~=t@E5nAEzde8P&it9e`vSOK%3u!9(GcHW`R*+nSe_jsVxbdhWmcqoTC7lC5h;J?%XiF<6=CvZ0j(~~v9_5fPl5EL1uCBwA`&d0dPfS?faaG^e;{H7Ui*zJD{r4C&j0Oyk@OM9w?XIW11kOV!h-A<Sb_6Y0eKn{@j=x_6xa@+*TEvo2X+uWrkSRwAoa<-S@`hw=jZKMdKi(l-&A1gC5Xfk85KSv8Whm<68k}AKYmYBT#2Zcazg0k?_Q!I3Z*MC_42{;PcI^_^xa#lufA*r)GvSkJ*NHmH(BGwVWeFw45Nss7rXT5>nB$~Tqr{7S1x>Ej?s>(FH9zVbLZ_JEs**Gmryy0gj%rmcMiW~mg7GBNFr6pVPfp%?VXQ5AtPz^tMfWyYyj=0L^{4a(q0+KdVmF>eWAxJ5YI`cOMv?#6~4WsMps7NtEeA&73LJ?koUJgKfyEifeKz0f%noCv+Gv)y>$Q*0I$N~7sgTeq=d%5efGlY#q-S9N8$Ehsj-qpWb{}Wp1*SD^OdjO<BETjxK{;0zw88%!k~3giPE<^8ZrkZM7g-Nbr5}VY%9R|%ikU&A%VDV?OuT$sh{}>G<)2=B1T`{rK-UO(5E7IUOc&a{abd9UZH}bWhxQ+hI#xgeDb-AYM<}O7ffL4@=q0Lee+XNH=@*P;QG0yG@&b@`nl4Y=ysI8>bG`kMZi^~^p~$*S^e&q1mIT}zLY3^5uBe2M_3*($H{1Ya{xwv`L$y!AHUArDXe}0ebS+P8(?1|_Xx!saeE7He`)^HrTOE$jd_lDA?DyQp$TE>cL!nk(;fdpoL~TepJn8kRAa1uc7z<g+h>k0e{y^fe4lIz5~5I;il2UBs+_Av@UMJzLS*0SmoKIpwN>DKQ&uj`9U+fm<<x7dbKljV_m@99Pj2VRr5{-we8Ky1<gpWzpB({;pJ?^-0<DNM)Zoe`GRDrWetdWZbNt5g4Y6nE40U!6Wr*9398bATc4#mKVp5L^%)k8c%Y0_xTQ(KJ@Ukk<_xE01{et||ukXBne);<Ma9$CgIBhN=ad6aDz&gSCS3Z3!^MPMHml~%Mq6AAGo-+tWPU=fo7J16)&DRUkw{=JQr^KmS_YxvxqT%GomD4|8c_Wq3>DC?wCGO4o-vW^B_?_nSOV`gWAHAx#5k6fdSL^%lmwz~mZXW(P_0OrZtLKi>@>P?}`-DnKi*LBj7Xz%GJ+*Y?1(|ZgS2|Ocbuznfa8h<W@$Sk$zPj@Td^Hse6m}fNZ2`;QetPGF56uuNs9F(<TR!qW$51}yV?#%mPeXjCJEWOZmUBWQxjA6<$FnJ6mCd{G3dGUH^BmaGdQOD=kvH@S4es)l6JT7T>Pu&Mb=^$Gt*Hy7`=h#GAUz30!=MiFIi2FM3NXZtS2<9CAnfwBx6=^Y&kOUZ{8+v8+RFQvjny`yYX{N;N35*NojrGF?yQb#z!0K|kgax8@TL0j=NqI)E-Zg{g#If`PP$QX_{c6J5Or!-TkuU@xc%YFw_p4zC+X(Stp4;0^VQdKR6~c?&MOr*(mM)-p>MzN0ceWo$P2egxsx2zeOfwl5|ZV}NhQaO<+*(7^zw@fBJ22w=GV-1f8*`RZ&><#qDY_Wy6oNp9NaqggL!KKxfsTM1<Qwz=PoNKI7FpO3x2--(ej&f%defxUs-Vb%wahdt8Oe<esLa#1El%;*^LEQ?3j*=`l(!5uzd96m5)AMK72a=N$%c)+h4vThXGaL6YrF7E#Q-PAcw^1OScxNApVD++`jrn{=R~hcg{1<zhJs}_A3j_vm4q-JEzWBl7xDPmd7dc3IjQbXuH6m5V9niuIm*Be3*zd!QWRee}HftM5CNLh8@D^0pD9a{tvx}@TRD;G-58-7_guCcJ3yFl{4?JTzMzE$3Q~0=1m5s6~7+$7^KJF%&*Z=8kMmFf&#|JC}7(ukm23Ubq3-_s($DmJcF3s`>*l-!{BD`-PHyXd}o<qarLE5IRHgmf~ILKXp(v^JYeqm=Fi&b<HqGMB}aBpc;Q3V74}m(>vbCfjFmITu|o~7scw{NeE(sNZ~5dL2}i{9U;1(R<i)Da{z~siD8-u2-TC1CJMX+nqg;LKQ?{FqGtPkQ<`X!!a^~waK(_kTRhrp5FP}nTj!;RjQ_{#o2wUi?H)Og=Z(so&d4tcGtA~2CG(8YT7W~U3XLy_RXx*8tUvRlX@z4_Ywy-SIlRFZV$}P{iZ-2LZ_+-s0{iQc9=mRpj9{q0l^)tk9`JV7`wuO_oFJI97m+Q!g?_MC=<IdYZ!opL>Prs6up)|;};*Ecv^EsaFPw9`s{_{I*Mtz1QfBK`_XI`yZMT2f;$Z1u*t(I<fuJvXHvy*C9JYO#kd9lPGuVP{8$X6T)I-2Uf%3B(0ls`H<?5z#d0rSLxuuFOZ?bv!<+(6CLABr%}BmShtIwsk29HL^|Q+jK;%ppbiuzD8R{I>lzhvm78aC?jxh3!6vG$0{+houW0Zohtv9l)2^lzy{(r323~n+j@6{i=lgig!DR&p?D@KmS<yMu#+(BL|7gmpYIuyL$0>>R?zdc1QysE1z9k{^qq2-|S#c0RS_9o0C1HpBE1ECbC-fD3(Gfj=WJgXP!ZfuD)YE%_62^b{N-;IguFo;KS8(%wFnzfs$~Aiy-n{&9;ilS3(qGTFXb@m7R&g)ewbZw?99TFP3dR=E|AJ@QZgv6pE(Xbd|S8sGVTy<h37V$GGyw2wH8+r@t+fw%-(?_KJ;irE4OXlpiSqy*YRL!q>)K5gM2Ew%`KO3nNndUR@YL3Sjkz8>A}ow??S*i3}>c-&aTQR{slW>`FFWmcRW8u?XTvobOVnmJN!W;Aqm<+9~1{V8}znV?Ox^>)?wkx4%AVRczJg;?LMu2`T&QH*v@sYwl#~jH#uNzh@#hdAx~exojd=2*H}SOLtD>iu_34^-0-2w_QJBmQBfHyMw|k`17>|!9<m=qR5pp;>+cGDa?{9AN@ntXyJYevkX(4Nd0cE<T_qek#EdA3wVOvs*?<OeKlnr>9pbcyf4yHmR)8w+l-^p-d&Mj4JX9dfIk0D)cBVifyxagMV*TA43puDcR5n4M<taEa`e{gGK+LFZhwA8pAr5$AI3Uy=kVd>6YrFbXZSDFPlMkf2GSKzwtohPt?c=IyWYa!zB78}zEi!QBQf%6CeU(ljjzgbOaO88iUb-f^E!dH^6_gc@4Sz#m9r<sIWdIfiRIVM@%iT*#^c^!c)^qULSC4ot1E~9UKQ@h$G<8_WKxD$=jMyIzr@}sZ=SpdOmUu>RM-G#zsZ>USe?Qh#8{QrWTZwyI;xVjQ2NHS7RsO5FU&~IhVloti!<_C=)&^HUrOlpzTBHp)^>8vQ`Q8}?G1BtQ+q$>Zr^-;X^yz#^-NyZGRw-h$FW-`$HNuxDBma#Z2M{X#tGvfwhE%wFS3zevXRacyLd+tj>+~xWY_Gnxr&YQ8dI-{ThL|&n<R@6l?RC%Hln2dh7EdOykTSUvs?4G=5Ea`URhjN{HgAmjsJJhH5-e6Tf9h>{IIy-EM8l@w0Qm2DdV1v#nX#7ZXKo<=ks@MEPg>nuTU3`P)82mI$pkPWAXD_M^GJg@w|h|Z!TWC_449*`r<_H@{Pq$sewy0mP_>Nxb5zZ#WxqvFJ7hhD0hl#%05`UvG{{|1;=lk#m}k7FH(u~)b@gEO}(|glbbmf-#~@AYdID_p^_I=*_XLRko!{MmJaIOCF;gC?*HLZQRCK*#SdusM~M(OjB7j0KHYkq+PZ%0IDc4mfd_rCuy~coe)8545cYRlHqlHR<~ckslb2rSvG^(V?CRo=x8`{w7Ao%Zpelc$g5T5sFH%9OrMlMK1s}!w`DNj|b-U+-8WR>cLNyD4sg1>-z-Qpy^YroxirhNxU=$bwl}m|*QuG77xIoWuqU*O#aOYJWHw&Y|%r9QXn~PNRlmmXF>Ag<He&Qy00UX9plph=QRUx$$pkDt-y*!S}7eA)Qmx(3|GB8j>PYV&_)s4=rmwEAg4_aO1xjzpXfHfgCU0S@#HNC~G@sk?#tz&pWG`O*NC8g#~=3bs}YK2SQlx0r@b?C))Y7=yVIJi##y>@F}cbEUTi1mHz)U8*+(U)k=-59gpNV51D75tGYaFi=sz_>*a2zT4=CRu!sr}P>z2Aab9qJbQx#dehjfiJ8#lt9GMCm7llnsyd7GQ<lQHfUOTYsunA5OmoW--BwJK9{&onj6r_a+L{vd?{UrG(+I8>qM;c!{2B^gn}eLLS3bQsVEpVmBt$s@6Yqh-C&BIXTGKuAFjFdgaz1Pa38Z2Gt8U_NFpg0s=4!|wo^6Npe&w2i&TuiyY&(^N(-HOPpfw$7XG!Wt5J9vn4P>-aW9Gt4E?w@XTJ-DCEZ0{D%Z{HP!`{yiM;_KkrUmy8&ODGpW-jCm9Io$?Y97y=PAFz66J&zIGNI1Tqs|dl2fsdI8uS-@)Y`w2B@K{Oz85}DYCFwhe3L708t+<-=G4vhSsMJU*jcvf*1RxGB;eZ+^B*^Xm~GTsLrhySbCgSHpdY$FpOJO7Qf(iKF_3)mKO9PH*Z+M9P`S)tX52ct4bHID4ms3dLbj6zJ!JJ;Z2dWu#M8oSXfPhLNDH$H?L%&=jhyz{M5LXg<HD9lszwk^(B@A7>6)J-Ayh0wdw{Ir--e?S^_TqINbFu#GsdW&9b-=N|vgENPsAiS)rc(<>9-y-GwZn8_dl=VwLcsHJY1KO+CZ%2UCCDtfTJsm&H$r3l^ZGNJShIxk%Fn^#y&zI^YVJfaoMDQS+evau{0fFxb9lDZaqm1Eq8vH61A#w&e?AXhFZuf|-}y6>jf3E5=vVH^n<+s%%Mzwd+;T$a;?qtr_VlRLO!cD!#g*qz3De%6nxNze8JMoJdb^@T^}Y-A)B6ZkS;?jfuNN?7$)|_a(X_4@G-i=7oGE6Hui~XiBbt7DhKRNmF|xjasri??1?TayH~t+Tst6uBqaB8eY>2G6-`GT;c&-Ls6yH7eomTdsU5i4m75V=m(1x7KSirSioeXWitYddK|6}HOeGhaBiJssd^Iy*<fS5@vrN4n?dxW{*xsEBHVhN%s3tnr0h|}vOHPzV56gjsH5#FW+S2!KDx^GEKIt?hGhr~FC7G}B}L;~C&aw{foj6qdpUKWt~sd$SFc!!GGC`=ea;HzksH&8cIUuwg*kg*<QL`)p!B2FwAE&Vv|dk5JquZnSWO+HmXCpq7G_NunRVAluG}GQbzNB(EW%5J{Yf4a$wLzID*Gg9%QUGNFos%KUJJ}`tR<*2XYt*|*GM6Jws?*#{&R~TrIf)qQ_ru^XqjOb*g!r1z?v`g(WTiaxGs7J{S)trKZR&xXY3Q|zVvR6HTtErDrE+*=aoNcUEI9r9;pt)miiFAkol21rR)Yg<PI8UVyP7^ur0R%83JEDR^zi=3RGM!mai<A1JNTI#r4#7T#$F!2ZdXLU_;-?Q~%bf+&6_QgG{AYS<ZfQkp0tQSxvsu{Xyii6S;G34tIeNwX01uDWjTIrHWSw<<z>-Sn(<$>5qlH1E_0$VY^z$I`I%<aL{QL9TjI+iVt_s5J`d`SR)i;JLk>vN^5hEb?oDcIDQrP4^dYyu%yWR#0o)1y~f)A^IrzsM3nZF1W_8$d^rn>%u9nM&x}KI18ydw31gXeScsr1{pnGX0V;??15q(u(<!dHvuN?H>@#gpmS-Ch4>IP`{kqU-@o&Uzs(ZpgFN%qNGjkX*=pS-AiPYnZ+M)n`UlgTqgRH+7A5DXV{QH<xcX23ce9tRUODG-h!W(u<Qx%j`8|Q6`>L+D1-#Y%lC~i<f{F}E3E^*giPTg=7mOBr(cR|_K7xNKvkgh-uu?x@hgR7zkud8V14;-r^H~M8|+Wn}tlAa<>5fx@1tG#`R*gPNi6n2&Xg_^FPiafslH!_jQBOVQG5u-6NKhCRVeocZv8R=33H|_5cUP7kTHh=3?N5}f;Pdz2K=Bq@Q4(S#hlCi-zII+t9L7DR^j-2<U=TkmZ0cmrvmj>ME#HNq#shY0qOf)9XRpX=5)lQ4wn4^)W#jBl)Wt0O}xY~($9a8+F?7KM<bXdGlyy9t7F>F=5?TMuK6}FFlP^vn3{;n^5lKnII<RT;_u=73dRB$KZ-@HO5y>>S_G{Zq?OQmd8JYc&EN<~1i#;&V)mds$G+BIDaRotjZt!-5Iq6&R4uxA1xvcQYvd`3LOi%y4yb(7<Uq3@I8t+jl+rn69J_@_d{<r>#^<5VFCtCokNH(J#6uAX42`GLZ9R5Wv+Ext#*`w5A>j~73|rp||p-yy>I_TpE>i(f3hm%FBlMAFCf!AJB8|Gu5Su!^0f_wW&YOw|o{brpLG93N1NKNt6A)2$ry20NmF^4kqHR=nBD+(qVCgt@2sz*;Y~BFdasyEMG3%e3cZc0=NR9OC>zPYYWF#ty0oUSq#a8hW67{S{5g_d2496+Fih`Ml*mESj^0tV0~BU>)&;Vb_%|$trxLEV`r2)t3sN6|TEtfy)~bvNlZ{+vsUkouym0ie2I8FqU-HeOp6!z^tiw8CQ{N<~B(2W-hfqVT?p#OA-t~d{-nsYvU_=Um$mH7cn_vT5|(FtGUUGohpflF>77ZhF)nWgrxUx$xqWd=;4ZMzR)Epfg==pR5jIB-33PG@ddHSB<6Iuycb(}EtqW+qOKPEU15vwvfhDReqQ@Ig>bz%^?EPHa(CE}b(s4+6}O40rK`3dibi+Mo`iYb7z_%U0@;bcV#3CP(xUc@$9V7Js<s5#Z@6K6_y0BbZNF_K+1>vNUjpm^UIob0_hp|pJNdpO&W?q#S4jLuS=^OON)&hlC}06ew(gQCk8ir#rY&2RXCzT~iWdoptas19kg%KN)BFoLm#XUO?rKW5#q~U7R&G{TSDiX_?&lYgTse_<2lezft#HXczN3|Uzc14Tb3fn5q!4LeO4PB3&GvRxyYPM}vybZ-3FZqSBH?tgcKA{Rpqu%;`e0hR$>oJV)A*JAk^5|Bdy&vQCm{1NfuLyU9DBwJ%`7jy;&Qs{Ua&N0S?v0eC_~l*1v6s?O#_lt=z{2bhZi|OA(DgWH#uw9k<?_>h$EU@qZGZ?gdd^}aAT@@NhJdhe3%}HHIaKdz&a5k&WVsihmtXgJU+O!fP5t!c8)k;gsJ2QU-PjW`AKZ9pO6XeMq(3GopNF(!y-+;YXWBT-qf7jUJyi^OI{vxff8sJQdc|f_l<aMx;dx~Z^3Fl3^x!_C6OtiGM@vbE0sa*2Xe#z;p!Yp`30c3xy6Pt=peFbAB%y=ZgkgG9EIx$L>z@LJ(90z!g&Mh6P4DKT7U{g7F&V8d0u1FGXM)t7CUr^SPTWa3&QFOD0wgg!x=@kDemD31JSkeV#xXJKu_o>09ej!PC1nT`|$W4iiZ-L1Hc}IR=9JRsd1Hckt=e<rZFx|_wEY;2y`ER&<r_pX%tTfPVgzb5ID&tS;POn8Nkj!3}c{=6_&VG0qAxg=gDv^3bTX*dnyg@FE#K2-=T%0v?Z^m;LBiL0EBm`vV+ja5iSMd(4z?+Pbh&RNo4YvwL$_jQXX8pqRIi5`Be@pGOv#Q{D4^Z6iIOrYMxVZYl^O244+4;bA*dN`2Z(KiqHI`OZgYw2ip=>4?JcRza<hUBo@d3ue#Hjdx15@!kH+FL^abf0FaLa51S0a!N$7I>TeB2h(R!YRMT^xKBxjAD(8w-m5RHM(Zo6t0qfZoFn%J<v`=(65Uxmt?*0hHZgUuEso-papjQp;2gh0_>0OmJn9GzhSoC6?JaQ^x*vBA)@WIPY>9!1Q?1+>-#i*#t3^=zcuMUSc#FmTnjG{;r(xk>m9qmL7RQ8hQ=K8HJI?c;UBfMmSP1LSkQEF%RXvqtyAoor)?aKF5Esi9_RY4Pa4&Qjv&UGfaQGr$L@i`F_z`|!KW~n*P6p5txlgh$<taP*kwon?b8q103f+nv;8cU`Iy`mcrYC@eqKT+0l$td4D+JkOLZZt(NoxS+V&pef8Ew3NRs{6vhqHXBKYYqca0!c=Ycd?vUFtjdhD<MIRsyxoChE4pquBk^BfS4y^GXy1*kotNjgHUFIjkzjDTJ{ufDmpxSA|iC|Ql1hK<N#ULrBL~p+XA~t5n9<k;bc{XAknn6H)Se>r`whi2P^Z0j#TyM@G3sV-_bU#MzKj*MoZF9*$<c-Ci{WXnz+?{V!VozY<GoGaZlGmq8>rsQ!=q#=A9IwN@i)aa3o!Y3oi?lsy*?tIpwuQOs60vZoBXxL4X~Q=^@3F)F*Dc##<??gxNKD$|%8xWg85Y29w_?T05K=OHokz=P~eVcF7GEvcgk^{_{*nJ5eQtkHO3>-4s;}f{*TDI&GKIJH_9UYq=wmUYZUPGEL?m`1J2_%>os|Y5b$IDizt0!hGm0zlR?>+6qVMGB;exM(0Z^+F|wNVf($n+Hyq?;kEL$X{8|?J2fY)4_X_D+>W+`T!KwrrmH?;;%^Gl{gyUbaeiU-$GK^W+F)5Eh0+}Vj`n$oBJo;Ch>;WZK6Ot{2*u|R_CR#BA#FT%Plp>IldkNZb4_%pO!!U4X<9`*TmYJSWXgx0NlD=&J=UqRfb<m&QS;+ACIl&nCNMQA&QTFpfIB<|uBN|2K||MsO;D#5hew>B9BfTzgtQ3`qzCQ>*kt=mexFU-3S|=9K%1(BYnO!ol$QU{KsSLHEXR()tbiv$h?}%;spCoWV3ZzfJv_x61s!*jx_{Zv*86fb{7wI1=<T<KD*)rfwi>vIRM|7)s<S(RMU7Bgg?I?tG_Vd_6~(aQsO93(t2`CQSfSU4zv)mgofvIGxzpi7>O{5(ktcgXosDb)K5(ErWr2<k-sx!v`*QqFPx2ooq*?I)$7i>w%8*;+N{<3{ORDl0nh{5fT437t=fHQmLUQz`>Em2NE=i8PqPLCJCE8;CcA%agm-vEf0@fU{b$#9yH&knY!<P*NqC}<8vhdPhZ>egk?g{ZZOX7J{l^JqQ0WYd25!rEtD4<l_c%b5wm!OB57(Fy1BNb+do(tiQsDKsLKJ3F@c3pXfj$bb{C|o$)c}cW1v){C9N@Y~E<_p;QZ%DT2i6g_+5E_`z)yaf})O`Z7zD84&wWK7f{?-Lam1{<ZQiTyb0o9?ZK5f(@lr5E`ozg&2yHX}s1(Zg|l|YbwN|NXTS@RDe@`+XAgD2$P1Fxj{Qee_n2?c$X9HA~K6I=KgGUioOYejd@y~H*{mP#Qm!>L71=#^w9Twr?8$DHmd$rfnc98;4%eH0e2D`l}+<eLd9+TcbQ>TNxBoDVu4rJtnNeG$Ux$Jav6P`6Ku&K<6r{2bU*S0yPg_av~ElqcW{I}U(iZ_DmC-*mJBK*jPg0fFE(zSO9T@lUCZM!S{RWue+}&<btUp!LmF!K1<|UYIN2C=K1R;MglwwE9k*qavJx;BG3dV%VF@>-feDsoDaL<=7QlG{dZdR2KQm9lAa;eecOI`+!&d88c4=)(6G<aUIzl!AIB!7P&5599JN?fm!ulUWR5Vu%SgRh!>t!_+%O^L5O($RFIr^;el*5m)^*T$$?hD<N|VKXODevE~3~G&Y&C4702mK#4L=c^h<;W3T=jX)jOL*u+ClC4N0AzBDV)8K(+GDd3S^i4dchs3?koG=~%iAZgILV%I}P|X7WaebcnnOs{EqEkN)bb8PnqB1tSV97Zt(+cYYqnER9~=;X#6BtcsvPT9KBq9?SHOufE7NDi99#;{tmU@ZS+xC@%|pTswA``~_mhUVc8d0u}s&XihN0%YM=-^`b%_3N59oT?Ha#4z_4uv?MZyMMUd_BLxzWmhvbwGQ92p(`u#wKiAM{KhBf)f9kX%@csUpD7EOk$?i3-2A7?nbU!CWO74hE!ICJuaOWCX9ceM)3SF+8BB=;*hd5d<&PABulon!e8G>0FHK?VI&_&(wB4yFy-dBmcPGs#LPSN3qw{=<28b=sFZoLI8zQF?Nmg+;OhlW9%eB&ITTc>i6^*ehzz84(8TTwzi3Nqx-agPiyT%riiw1bufRlea85*K{<BI`WEpesbf#UQC@d6VB^<|$HG`-HQ{5&@<_E}+kYE4A2KuqWqCb08CHrU^RQj-v}AN?uae#x?&#dJsnx|1XGm#IaZ9`rTu<2N-fe*0c(<u=3-ZL4L9Joh!uO<@mCy`&U)ZWf?RNu}di67vMs1QhQ$*Y1}kI`N4u#p$CtD7ox<6iYj|T1=pCC+MSlbZ2s%}^-+62E^G8~ggUvRK?3}M#kW`JE98rUQI>Omsr221Dp%#xfe~Y6*8TkO<1UB4WdB@68r{T*Win>i(BtKbu&9^pKj%8W3I;HV`aO+YK3-(VJ+|dWWeKh)fN7>}0P!@^g(Nm$k+mHj1XlqSX|!mk_HwqHm#?`(i;Az=5kxW{%4-~m8Qj7~)5WykhWxCVT3C;tyE22_=t3XnGHP*Ev_y@g>%IyOv4FPQA$@l!1EZeIZ%ImkgKNYkZuwmhpqrZXR;nz-mSP~=a@KGUN4OdSIn{*%<##f(`iYF)(ROU&fD?r!9E!?VFD*67fFWtJEEu%F&m}@_`lyU2N1kZQD7E%c0yDmoYz<}%zk9)qKg>qX^Qpdpa4Q_+|8o(Jap(DBB$@%&CKBrZu&hBC-^zp&Zt!CMGwa7JzM1;4JP^jreqS=`0x8DXdqAsoXH5Xb@E7Pku$088NVgl4_)oF;`AJ{O0U~xDF#2%Uc|PL89u|K^&o(@0!|HGTNkbRDp82p0R6NUnn2Tum!t|-g0F4fU6o%*U6gLhJqvwl#nP}LBBitEJrZWR)o6&3lf^b(n246P5?g9*UCZfmA;44E3#*<2&<$DK!8j;Xh=}vDpmBo`e+w4bc7blB%C$h;jD9Y}5s3#r^f5^emL1$_3U!Ymr;e2VS;okIJ_<DK>whQxIkM%_d(kWOhu9fMN#^v|*oaJd;gy4_9&BX6UVQi$Iw=tLqXU?kqp%m<9?rbxKKg4?w!~-@1?_~!1Qs;~CH_c#%*Zn>|6zc;{#8F9ji>{FgQ5WG^!hh+BXU;Z4y}<Ej`EGb65J?xFgro5k49|ypV`rOm)6KxS@D%w7ri;P<MCm#4hZiLGj~|wM;IiUad~|te-0$HZV9&#tB;WSm3?|OElbJsF@J1`}+gp*r2r)T43)5B4^d--?FND4Iey|17t+*W<D8Z0nQ_(o$BL$$_cJdMeAZ@=*0KWjqs}y{RnNe*!<30T#>cTprZP!2?CYA!j1!UV5LAxj!>5lk;Y;VClz_>u7crxY3suiO3??XKUaWh11Z=xp_Hlou4UjjiAS^l>Vl@|Wl*MF9eA=?frnt0J?Z}jwrdsI1I+JiQGD-pkYR_etAW+CUonC${#a`!xs*Fqkl4_5ZuG^#KVp}au}C3`zUN+GR4WN%UzgoYk_JCYoX(*O-R7S6VBXb|`^-VF~2<GnE|{b_|4+ld_WVQv6U9KJYoIds^YK&+T}18)NU{CVK7UGbiHBA$_-N0?VwKRnAOFAMW}qZ>{!iZr|viA71e3`G-hyuW9gfncuJ>1jL@M&5&0QcAn~fm_e3k?sU?VKh7divWSdGkf7$9rYW^#0IiPXx8iTWc<Ti3i$92EmhR=2ZFKwQ~G=|ioziphpQQD0l?aoO{U`M!5B=+V`+Xc7-G?EAjqn+UE-+>!v679X$h-(GYVt@j`^@0>H(FL4*@-f!dR0*Q)NOtM*yHIKIXMmL8rm$`tes#KKVrWQ}9!f)y2Qk{8Q%qqz6=Xd?0eCH=H8D5Ql9=GLBsO6#=6f=#a_68Q^sc4Kho9SOzf@zZSY1=>=;nlu3Y=jmkABHLX_DNm~cS$c9KL4GWLp%|cl+hzj(>Txcjfh=xM-S||*A;-zJIokJiv;Lc_>qO~8k)K7<hbZ;Nub$`LxIa9>>%$;7C3m9`iJ9w~ekQE~R?E)X|3MYg}kSkBBJvqBj(|04R816|Qg|d&P5Fe%qVMyptw}0PtzVOfAovr?nb_)jD=VOJE0SmUrU|b)6gKoa|LYweFVIU|uo+*>yiEhDyKy)(*sF(?LGRPLwY(~`2Z%GI_PmFM%4x71$8ZbT`wSBgr9tVJXlGIFVqdah)EM5bCH^X?kUonj_fOmd75Z69(Io!_k1=6?v-@S;PLPx0Sy-1z#aUYosRC30cU^#U;kcPVeZfWAvP&j`t!Sv7-!){J6wOsIFs4+l@f#o9fcM$I8zr?~lQCLS(TN4PH%*FVc`WnFF9)cAlqcQA=kcR)oIGUXwmXj$ZQF;;}!}1{g!Fh1Z?jX#}Z^dYoBt-RW2%OHI0S;|^4S38yfFqqinHU2Vw1E~w-vBI%BxUsud>3{FtA)QZiDU|PeWw?+j4(0ava0=e1Gf%@6KUaT-i`G1fvoL~OSfDXr)ZI6+X7pO_9|S5BrXk{-Sap2tr(hexS1Y@{8&YrhPhGPiYP)dniwJxh-MS6JgUWBT7yoawbKJyDBd#&pW5sR--R!rp};JWZVSX@7uj_V-@)(ROT<wGX@-S0?kAgLAfCo}gw)0GFW5T#mne4$bjZ$l`uqeOT49~1`CvnRI4Q5{PUHdv$Q!uUa7w&^QLSiN8<_UNKI;GS!aeH$^20nzu@OzAd%f6>%1iWOI{rQif6z_;5;R8&V<y0{fJ4P7B#A6AGC+_d=mD75aP0!#H^4T!JxMtOiIL00G-^>P91B-#pl^ucR$;MgHFNqiu@`Tuc}Zf1{WFKZ6kt)s5e6NaM1Yur&Kvz{N$GR|lH#p@y?On+Ki&H0fB)`m%7vKN_51H{be)ZScQ)t7O1w^gUO$_<97tkU_AfYyC_u~NhzhU($d*i^*O7-_{6iI>4u{el@eO}6>Y)~#B`t?e2Wns>AzpbIjSK=a`~!RK=tow;zzrKv3_BC&+js^cFbtw_%gDF(!4|4f-S9>50fR6KJL5EpKbO@;`_Ko~jDz81ItX#lGo2Xfg%ng%$$*s?M-bRdcr2UPCJFz8x-FUr-;Ed`18+ycNi`2`0TXx={ibZFe<0o)R}v}Bh=3@yg3thOhvUF@_&Lw3L8yOcOTDa#6HahA5ay4gN#3z$Fu${<6x>T0t-&yS#EjVI88{H`#rR|}F5e$y>`1pGTyZ2FfbU;o@pLz6M7S~CB(Th=dz~neQ({!;H@#_)5~*-YV7>E~pc@y})D-_k`=KXnM9aH@jXUtH7d8h{iR?=gKHg2^uAKFIVerHO=0kr5(Gl^Y-^uM~VgrGQcYLaO977ZJoNdJDa(kie6tBd>u{edQ3}ANfUkW1hb$?h!`wFcs{<@A?r*4Jzlibn&!;Od^+yHfQH-jJn^O2|@l<uF>p!uTcHpja&9CY;o(8=u%hEs{K8EQ_R6$r83Y&Rd33tJ8)De245`C_=o1Scn#+D$78!jMxG)e-{g4I^rtIxJwDD79kB;XZV@8&Pn#GjR3j2ik=R3NAAgC*#V50;hOfziSi%%m#wKb&ALec?;|-WK9rnw}3+D`SUk8JNm8JR={rB;2x1)@*}#zvkvq=1|u9McajBW+%|FP-M#=hV?-=3GMiEi>?H@_un8qI7?05(XmTV|kpVV;gTU6hRQ4`&z8#B5Lp~b-tJcN(Hx!GYN#h%PF{uqNT|{&J6*EYhvk8r&B)I6F1;C++$I(<=1mr!TdoTRibs-Y-;ON7j-SJEx(Y6)bSwJY?0pT%Wn~^MGM&c;F8PCjlgv+lo_zNulBIq(LogYd{;>Ob#W0s*Mm^`ZvhVPJ3(Su%k62&F%h_w;j&Xy=;-<@p^MdO2PL68sf7pL$59U~qXh&*;HG8o1)7>cmY&@#C}NMkpnAh&wLbTPw&XPXK7EJkP0xCn+5yO~1MH{K6c0s0A{aQ~k<!*<oEVV$w;KpM>(U46OD3``b@dE=Qd{yG>3t29Ea4&;aF`4q%ztMCt)E!~rCE7TY2D_p5C&%&*)6!J<ogSV4H?tQ3C@AUFtu#-E$QCZl)hdJPAdJ6xuIgq_dgf2noyhhr*kP{fWKqoGW4l-s0;>rF#WyQv+1OoH<7>1AZw*`Ldrm*4$C_U#E9AtQ4#86C}g!KXGkxXnWWSyDYgs0WX9xSt?lSt(3p_@0)O2AP}GnQbHeyn|pB*R47WLzjp_!*PtOwX&vzxptXj09&Lr76K8p<A33B}vIp6s!kY1o&gLz`K!tOe-Xmn}uaBLaOp^*n{eC8<bUNg!0@N{j2J+Kjcmo@x(*d6dn94iXt(Fw<jR_7f-hjnTk{YbcdyO0BeTy11`G<cF`XeE_C)95t;c``WW~RRvsw7KtA&$`6U)+tY+E?9(6MUr0R~7*y8zIHxGC+!S!yGniJJY_)oA>GGGq?2U3ZRoHW~3#HX8mR1X6-6>3BHzaH>ewJ#(cLZ?V&64!u@hw%qke?Qhkc^2C~j3%Kc#E}Xw8pAZS7?krQH`J0ds^)|A7}>FXx{Sf+LW5_~FW3XMG0=XDrRy*|Yc|waQA)-4C!@?0@P#`O(j#Xj<dk?CT|Kya*T7<gbu%MlCDlMyNE_C3ad7$*X{8tWE_iT~#GhFmAE`^aIBvhfg@+`3F&`Atcj)V8MD#E1#y<MD@K84D03Y2R1UclO9o+_5nAQM}Zgj(gzLX!=Nc=!DK9Tmr8Fh;Ie+rD2RA0siW8`GY&~i>u4unl}4aMj?GUi$W7~P=U0_F&kBDl}l2=cWQVA0L~@K88q0xA-u8dR0KR{%}aiR^Nh3nI0+HWgipa<e`f5D)z(2{r|Yqm+o&V#St*J=B%OYK^!Hd8iA6AMqg$sBvtAGBrBTkXE7h<sd^U0PcYo!U+Z`@euwnm%hsiNgRR>EJV|M9;}dbN!3f*_ab8aZFho0eeZ9F9CV$&6m?<)uFnYHSbgPoc#x}%!>%jP52mM9i+H}xxwYg#-}wm)?xo02S_U+)66EKPtd)(6S5w>$-|fSlq)6GKJipT$3-gkD&NgG|UomLU_kBZsSQ85rPGCM<^S$~-(GhSgR&sNqK8e-Ukr38^oG${+IW#4fi?l%7?K}^n#TnxdWnEKe$Eks|h+2utYm$#d&w;Q^i=xg!UnqSwKsqhrZ0;K+HVgvrF32FvZ$-%;;!slxi*(#~>r1h6{GlT?1+1e#Op#PDWO_1TIYq*~f;L0pbY+vM(&2o;e(A+p*Hk8)pt*-KVLH_qSO<|iJZ(l#DbvbhkwK~<LRk;iZ3dM{R0_yDk;|akoGm3mIiF)eo2xABb0KVQh_rn?Fd6Q=6$J&_8m;Cgy&hKT_LCrL6sL!sUkxRDR|rSbDN~bib47x>dZIQj9wT>5FU{lP11Dq|geCL;^_W)zo}O*|*$f-gH3SUU9mfxCI^k*`O3Zb0yugPI^Y49BI0S3Xr(r8uKOD?;Ebou7o8L{9#Re1@6;cDOL~bgs4!Av;;>fNW{zWg`qS1b+mrfC@Mn4a`FE$M@FW2KLX48-M9P(D1ab3RWqd|!SRyxW>3`&V}=m@a^9*WXesA@s9%*16Fi;^6nOjgM8yM0<AxdDMiCT|2wq>Z2}aIMmVNGg#(@c^xyFQ8lH{ZVH5ZabMh?+{NKO#B*%qw=p{k_`;?rJU8uTx%dyis6+s6-J<G9SDVDc+1Jv`ruBkXYen$f^b$*Ht_|>$#-l!BLnI9Cin+8c{tc6|AxL<-i>J@{uG(suZd)GJq-e!E9FG_FxCO5hr&`e_6Z~SteO#lAapY$OcUVS8yU>{vDpC%vIlgzl3~0cPu+Rg&AGtlcata>;pozX@Ph$hL|GQjK^U+_G%fENCtyWxrsC}Q`A0Z_B3#{+O_@eHC?eo>rNZQA8;6;btcHcT(|Eq$B|ON@{_KZ2jJJ3PTp={bO{y>yUqCrUrG!`{ftgzHdEh*SjXCIAE{m!maA;9%!3eTNqI7%Ga!~tWJ#G>Ay4HPG8WIte5U3c`yeMwdE~9!-mEF+C(r!;ECAlgsMfDY;adgHr3GgL|Lg`RH)-6OtaTTqWg0$)1p=1kZH2eP=hSCKmEBl^#_UmJ3bdqGiuo#~Q-fpi9K?$OSOkT7tgyC4C@d0ofW26A@M(*};%`QhbGBRYrzD*<p(g%#kehfguvOvzHLqp--#6X&P04b8mejQYc+hK7)8$wdTBJYyA2Mw_yo!_iy$6|kCdu;qsCLOg}cUJL%I{j;!U(AevQG2!r0<k6>B`EK&N7-KD4Zp6v#7jO^>q3aQO@?NQOg2r<eHB;;EJ&pW?TE^Wb;r2RDN5X$rV8;PSiD=I;3r)t49XbRC%T<LBn$<gcl#k5TqI6r&NdU6{-zBIA>@eoA$=_ImLm$Uv4|ZEW34|3et&>M%tmkvL%prx7KVC#a0~UV;ac@kt+;7FooI!)@P98tTxc%k?3I#zZ`yjgqTwxA)mQcDLpS0=y>wikANK<;Sg%K#tFLOs2lmt>Yp&peTxh<!-`F}a!7cDFR_T!&WubPuYHcn!APef>jIm&iy=&fk=R#SqSEgVG9)tyJ;$^M+#Eq@cnBJ)`k87w3*3qu>xd2p!Ms>?71EC+(O0)IyzP-F#FP*wz73}guYxP+Gq(Wojef{x{`CS*L0?$H^)VM2yQ?PQ|_2qs0!5e$#sWttMmm_yJU0=FyKUlXW59_1Hzf@-J$)~mIY5noLT5-mHddv&6PPQ6_d;c>$+HN=nUSVT;6c&SX!2ehiWhRMzRJNvHI=@-DS^RDCsg>JnKHlP?*7z832oHjNTZM6J?9iHg*<4)X<@+HM>eYw#%ZfEQ-Z*(ze=re%mq5?zr}_Hn%UW@@UM?D85*i0<&BeoJIcKfB2n0y59zC?irs|7T7;1n;Xg*qLuKoc3y*wboe}rJdUn)7ii@#JRt-0yuaL!(M@JnT?1s;Mu`jhp1w0>{XnqIb+PvFJ>D)1YDPzdf%wE#kZN7h{4DwKk-5BTE&&<A+l`EfJifjzZQUtZAh4y=P&>&-Ji*nxF?Xg~PD4|D*W!P3eeUiaf1NGj&6(i402)Btr*e{^W&UIVXLC-*~V3r55P*txY`1d{gmGf6#=2lmRawYJVgXsrKWfIA==nQsg~vsdRmSO>M@6ubkgw4W5bNC(#1Q`mtC-vAce7<&xTOl?d;99UCxjrDN_aL~*j@;?>A0ldLaG=PKV@TfIE36FtwE&w*L-@Ugd-@|&Xsi)TD#N~hu>OVfU<{$DKK*#?KvCNVT`f1n(w?i<OUD&sd_h7pE6wX*X-G<dWgL&p)a06?0tX^J0Rrh2c^sha&*{J>$2x@?0w|pNcq%@}=%%Cwk1HU4xO&r_nRRfFx>o<Gv6^t`t7&LM_pswxdg?gzN2wc!u8Lhuxh40jJ)Aff-Er1JnK;!;2f6ok50Q_Y=SVBgs48ujxn7k!eL4D<gwe`HdQL;|&p*ntah@y(-3dsoqkO~^lOZKxF`(56u<Ve0f0SUoxTo$Cj+OAj=C4Oi>JG9nk>SbVoReN?s+~>-${rKcp22G%Ey#DxwJvk2~1o~MoO2C4ku))A!hHg~1YvsfGdKq*bTwqXxKqy=QkO_2OWBZ6V%ZeROZfwt*-v(6=v((CO>iI3ShlomG6!4mK%KTCpX*&Xe`<$0(Dz-=5+n(e-<2gRiH#{Xjfn=do^A2$9(`)TQ9cXO6wH{8xdU=t&33WmqlJZi~GAWESpKUVnYbU3T)8$5fR=g`j)W~PU3s@_Y$Q-3pYpbfifl6!h@!tkvfYl5f7A<IJl#j=HdSor^E0_WJ8Kk3qZ_h9xUvLA=0Lzeza0Zx`7eNf5z9cmc=hp&Ypi$jt!s)|22m>t3f(Do&20ZT|wLGJk3O<+tpf0ie(kDU<fF>mFQX}w_G=x9o#v2ggIS_AvSJ47;K+&x=<bdFNxDxq8M{ZpbZNSPsYz~irFaU=O{D<b)T)n#GX<`k47XW(zd>p|k@EF{rdS&$jWC8J+#d&a>lm%y%-d>C+U@dPprb=*VV3&e5LT<CLW`ke^n8G|BDEYOp1BCo7J%Ni{D{i9OxL9i3tJary!Kj2Cv36n|uU3oVZ+;d|hIJ3qnRP$R0BXEe9F}I?NINhBa2ea<*2=j3g6t$(SaW!(IYP>l{Nl#`c75a2u}hZ6S#q(*7z_je_MkQYqcwYs3<va(CwcYV|45~SBW8277D=Np85Iiwk&)Vkapq3A<o4XFTCv178t;yMUEvA0ZujR&S@((qlXh&Y7Jpu2V`5ML6^-s(!Png{EizMgzh<o&y8HRo!l}ZMdb|5Wjgw>b*y-)Ze>C&QZ1H?{Z-3)(43;IFN3hGm9D6<kv~51yM=|Pu3xpVRwy&!n+$Z20HPt6I^NU~y+^o$vE<#ryfh(uadFkeT>u8tf^UQ$?h6dyQXf(^^PwCpnxzXN1kGN5|hwf9c#O|Yfh3*f2QWA5-)3>jDc30CrTVC#l{aW!&b7Jmt-TJUHVO7iNVIj=!jja=Kzr{j4t@<K-DI<tH=#v`tnIs~-mKy~>9(+l@u;LvK9&+r9Kj7)rw};Ek9~W5dc$@TDX@GbG)5g@E-xxdg|L*Cf=P~>Vd;4+iWX9B%-xw?CGa0+`d5mW!Z&QBr)ucX=w<TYg&AHe1?kSjT_SA-<6Q2ix0H{|Mtl=LxuF|3h-&$K@X#xL*BLEi1?t73c%;To^d-V$Hl*6}7eq-M~+640t^}wRJ<sL(Duxo9cx!qozDM?|wINw~FH+S1J5j^7pI_)`<A-pab&(NFeIYMC{?eIp;t@UEilR|TXymL^vrMFDNz}|Xz2V4_WW^*s$&I4N*d+M#d0`BMWyz_nU9{B5?J$QTQ`7r9s#aeaF+d<FK6}3lm3q79_3~fF+H8jp!58vVZk6v>`&d@b)<>oL1CBAh8vd_~n&p%lsIh&F(u7-L3O)cNuGY_gBLxFPro`!i|8JJqu*gamHuU}qp;Ld2hv@X`~@0iCB)3YbeNw~V@!E>#Z)|!tOO^x#6+j4!zHhFPbc%&2&#`buzSQ^PH#nc&JFON5-N3G$x=BtOiB~N3#wR~ddCpiIDU!Su!=K~t#nX%ZD4(y2MyD4nsol*XxuSuJosa8$!Y<R*TCY7lLo&(3$)|55&P7fcO8{m~C&bQOh^A5kU#5J|LgOIB~*tX`TVTd}Gz#ezD8LjcL+Q~X7@#fNEKzBP2WI3&LSWs)bm{rm)u$f(qb5qdV$IfXYrVWUX;MR4kT&izAY`%VgDIyu8_4cc?&|yBgpiSMHpR!jU2E}Y;Upj|tITUMdNw=Sm)VGG4_ePo%51VfnFX}|M*XHU|8|>S_bLFXA(1&jCF4`cVVW}j3fKv8qo`c#Kb)VO&4;)QN=~y7OO$o1ne)HzzH574g$L#yL=Hg-f(NT*|^TrzZk2^rV`p9<ur%H?7a%-i4iE{LwW*ftMVA!>xuiQQusXrM*kCueI&_zTv^fE^d?E5e5)i+?$;X-zcK-gMw0bRHK8F-f+vbOb(+r=?^5e-|BQ6ZjYZidyN6S6V|9#tcs#~pA$<aEL==B*!Qt;vnXd=;KI7xt~{4(8=n^Ss`x>J?YSW3n~(<|y_#TQ5HXMzdc$hGpQw#(rdW;!F~+;mTXXS&QixlyZTyR`D&SVk9N`9<xg1m9(J`y#C`18fW*X>(j#d_AnDmi2B-ym78uZKd~mu^^qT~ogHg;gBNwxo!<4*c7694_dom0{%IZLq72^5f{l;NL8pbw<ix?-Q6-}qlRq`8Wot*!t1VsK*6NbAjG=Ztn8T;12c|gwgG3vfv)(+z(g+YvBosxFLtFZ{Q38z}vrtuZvsT_Q(Hez$kQlY%w3T~lO}|6~W~@wZF=-bva(Q*_>dUsaR_iY?J!(zuvdV+c*NXShIa)mAdr*HrVoj8|1OmkaY-wtjbJV!jCzJN`6?q}r)R2w3{q;!gWWm}Vg=Jb>$JXLIaYc!etVuw?aY+jY8o26$S1LHLZB5upOxRO1u)_NMKI<zG_<XGPyZ7iVJlKYHg2btpC%kIn*&C~pvvc#H--LE(YrA#5oU_J?RuLF<x?X+O-1v#DJtXVc5lOyzSUQ#g++X^i;SsQfn+uN{qZ?@Tf_UCN!HrelT2s@!D?wtXts4AWd+UG=W5;Zkrm`|urIqSf^12Q0?yTkrjWs`4UoW`(svFyzjd#ONW3~MQNcCZ-v${DkXN@drt<~_LUfuF{R`c`5`Z(Lzp1x`sV=XsdE%=(MISh;8ZgNPqPHOvU!Q*$B+o>@iRT<_;sQq-JRz9@Wj`dDzE^IP&Qi}i;k><aL-+pNmwY~DbaSFoI9c<h>g{|B9H}D*@cr!nN!om-)PjbpxbxvDjd(CH?uEyzRd7-hj=5$SS%uR2bRz~WVH%-F~svO7FGY#wHh%QH{@n^kNT5aQV+NIgA5nq&_Lc2;vR^hEib)U0H6g+l)@^9BM&GAxpCHV`yn!m%KEEhwGkElulj-m?=rx!&sZ1Sl!k+TXp5q%<;U!)tZs6iTxd5j_&R?8EpHHvzMu`!T5*7%V%w=cBkud^>&PmOW?gSEK;#zDQZ3Vt+bk>=tC?9|?T(>PjXPLgZm*o1R9ubyL}q!zXSf!$o3Lzir46xfo>JXv^IlLfYwtk-*3(?nku!uyMRp7k~OF9H_=aKKmRf2@@FhY*N;UdETUH_HUO^Z8nFu5q|mE58BLp<dd<LeiB<>(!$F61KUq8L9nz22P|g4BpOo^T{dd+j6O~wFM`y&w*UeckcBfm}9U~{1EO1b^+&I5fZGqc)z|n%!|LMrCBJJ$$4w~h05}LY9BM^F@jTmqV}U!d~a<ZH+J%huz{V-9&Lx~x@;#iMxH6x$*hc|6vYcXk^|CL(!z|NI@(nk8$HFUKF(D=n2&YmX+<uVYA}EpyedQIvWS`-Y=LKI?pUs!tm6(TkZEdFW-peb!@mAxD|ZMBXzo4dLO)M$vhX8;mK0|-G$w=Z3yuoy?X|xVS={_`l`HBzJ;?Uq3%l~3V~d9NW8v0PuDZ=_$4p*(VVm_F`8&gC(@u`V*{BjuYi$X6c=?2?m`Hk(Nn?#2*2+&=*}-`?9voRG&)E9sV_|Oh^d5_k%6PcH@0j1UCZD+@*P`v1e{JMv-M^|TRr*;aLcBf4{Ikj=1U4OuvJ+Y=iWiPY2lX3+eDaSrHyLw!$}`m0T#O$3^kKdH$bNpmvHy;p0@+{On47A<JJnl@?Zqu{>YcV?c1YZ9#bB<WD_DB`wY!SBZh^&xy}B)A6$O~MCa_j~j0aTu0sWNROEkkYa<G=SUk}?a-mn;<=je9Zn`^AWLB-jRw^hXr+niQzT4z|no9<>}_z>qg3@yaG2o+j)HxG*+=Z@^<T~psM|IQmSbqw?G_RLhRQZ%&+^Y1Fj<Y^Gr>7#r|Pm{111MX@02`GHNJy+i+tS^OS7}`2(>%urg^Z22Exgb)6i8gk~{4S#??d%C=?t}H!-`_{M_Uxs-_e5AlR0hHt)Uhkq);Vy+R+}>S)vzn<{uK<dyvuSK!&37P!Pclhe$gBrwq~DV&~f{S>q&rT$<r8N2CToEK_>xdO8lm?!&htk)z2J_0U|vZ58j(j62RJe4!;Vzue{@H&b~EfGwAM%`1rjsYy1H3{_4E_bP?XFuWxf@n%KP5W?!Y#m(N4rJG(WFlY6TD#V^og6k!%ScxI=XE5qWLwbRAJCbtfb8D-rM4|$J)jlCjA%S#~%=+kSycUZ3(-!ZrKiZT_`3#P7KDN<*^UjAC$yl@(zF5n_Jp1Sl5#xIGvYDJ6#Hnui6ifJ$JH}>}%rw_46s`MjJy;cTB+iu*e>Sv3u)A8~>^&c-ES9@D}nX>jHkgO}U%91_1hEHgdycta@=XkJ^9jxetxko-VD@R=SU;p~o{{;)RVj2')).decode('utf8'))  # Replaced with compressed JSON by the standalone builder.
_PACK_CODE = re.compile(r"^[a-z]{2,8}(?:-[a-z0-9]{1,8})*$")
_PACK_PLACEHOLDER = re.compile(r"\{[A-Za-z_]\w*\}")
_PACK_HTML_TAG = re.compile(r"<\s*/?\s*[A-Za-z][^>]*>")
_PACK_MAX_BYTES = 2 * 1024 * 1024


def canonical_language_code(value: object) -> str:
    """BCP-47-style matching, accepting the host's underscore and encoding suffix."""
    return str(value or "").strip().lower().replace("_", "-").split(".", 1)[0].split("@", 1)[0]


def validate_language_pack(raw: object, filename: str = "catalog.json") -> dict:
    if not isinstance(raw, dict) or type(raw.get("schema_version")) is not int or raw["schema_version"] != 1:
        raise ValueError("Language pack requires schema_version 1: " + filename)
    if not isinstance(raw.get("code"), str):
        raise ValueError("Language code must be text: " + filename)
    code = canonical_language_code(raw["code"])
    if not _PACK_CODE.fullmatch(code):
        raise ValueError("Invalid language code: " + filename)
    name = raw.get("native_name")
    if (not isinstance(name, str) or not 1 <= len(name.strip()) <= 80
            or _PACK_HTML_TAG.search(name) or any(ord(char) < 32 for char in name)):
        raise ValueError("Invalid native language name: " + filename)
    direction = raw.get("direction", "ltr")
    if direction not in ("ltr", "rtl"):
        raise ValueError("Invalid text direction: " + filename)
    order = raw.get("order", 1000)
    if not isinstance(order, int) or isinstance(order, bool):
        raise ValueError("Invalid language order: " + filename)
    translations = raw.get("translations", {})
    if not isinstance(translations, dict):
        raise ValueError("Translations must be an object: " + filename)
    checked = {}
    for english, translated in translations.items():
        if not isinstance(english, str) or not english.strip() or not isinstance(translated, str) or not translated.strip():
            raise ValueError("Translations must contain nonempty text: " + filename)
        if _PACK_HTML_TAG.search(translated):
            raise ValueError("Translations are plain text, not HTML: " + filename)
        if sorted(_PACK_PLACEHOLDER.findall(english)) != sorted(_PACK_PLACEHOLDER.findall(translated)):
            raise ValueError("Translation placeholders differ: " + filename)
        checked[english] = translated
    return {"schema_version": 1, "code": code, "native_name": name.strip(),
            "direction": direction, "order": order, "translations": checked}


def _language_json_object(pairs: list) -> dict:
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("Duplicate JSON object key: " + str(key))
        result[key] = value
    return result


def read_language_pack_files(folder: Path, strict: bool = False) -> tuple[dict, list[str]]:
    """Read only immediate JSON files; invalid optional packs cannot disable the UI."""
    found, errors = {}, []
    if not folder.is_dir():
        return found, errors
    for path in sorted(folder.glob("*.json")):
        try:
            path.resolve().relative_to(folder.resolve())
            if path.stat().st_size > _PACK_MAX_BYTES:
                raise ValueError("Language pack exceeds size limit: " + path.name)
            raw = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=_language_json_object)
            pack = validate_language_pack(raw, path.name)
            if pack["code"] in found:
                raise ValueError("Duplicate language code: " + path.name)
            found[pack["code"]] = pack
        except (OSError, ValueError, TypeError, UnicodeError) as exc:
            if strict:
                raise ValueError("Invalid language pack " + path.name + ": " + str(exc)) from exc
            errors.append(path.name + ": " + type(exc).__name__)
    return found, errors


def load_language_packs(folder: str | Path | None = None, *, embedded: dict | None = None,
                        strict: bool = False) -> tuple[dict, tuple[str, ...]]:
    """Bundle data first, then optional local JSON overrides, sorted by metadata."""
    packs, errors = {}, []
    for filename, raw in (embedded if embedded is not None else _BUNDLED_LANGUAGE_PACKS).items():
        try:
            pack = validate_language_pack(raw, str(filename))
            if pack["code"] in packs:
                raise ValueError("Duplicate embedded language code: " + str(filename))
            packs[pack["code"]] = pack
        except (ValueError, TypeError) as exc:
            if strict:
                raise
            errors.append(str(filename) + ": " + type(exc).__name__)
    directory = Path(folder) if folder is not None else Path(__file__).resolve().parent / "locales"
    files, issues = read_language_pack_files(directory, strict=strict)
    errors.extend(issues)
    for code, pack in files.items():
        if code in packs:
            pack = {**pack, "translations": {**packs[code]["translations"], **pack["translations"]}}
        packs[code] = pack
    packs.setdefault("en", {"schema_version": 1, "code": "en", "native_name": "English",
                            "direction": "ltr", "order": 1, "translations": {}})
    return dict(sorted(packs.items(), key=lambda item: (item[1]["order"], item[0]))), tuple(errors)


def resolve_language(value: object, available: object, default: str = "pt") -> str:
    code = canonical_language_code(value)
    if not code:
        return default if default in available else "en"
    candidate = code
    while candidate:
        if candidate in available:
            return candidate
        candidate = candidate.rsplit("-", 1)[0] if "-" in candidate else ""
    return "en"


def language_pack_payload(packs: dict) -> list[dict]:
    """Metadata is used by the UI directly; there is no second locale allowlist."""
    return [{"code": code, "native_name": pack["native_name"], "direction": pack["direction"]}
            for code, pack in packs.items()]

# ===========================================================================
# MODULE: vase_studio.locale_catalog
# ===========================================================================

"""Message adapters for discovered offline JSON language packs.

Catalog text lives in locales/*.json; this module contains only stable English
message identifiers and the public formatting adapters used by UI and controller.
"""
pass  # [bundled] hoisted __future__ import
pass  # [bundled] resolved intra-package import

UI_MESSAGES = {'btn_surprise': 'Surprise Me',
 'tab_shape': 'Shape',
 'tab_textures': 'Textures',
 'tab_print': 'Wall & Print',
 'tab_presets': 'Presets',
 'sec_presets': 'Preset Gallery',
 'btn_save_preset': '+ Save',
 'btn_ok': 'Save',
 'cat_all': 'All',
 'cat_organic': 'Organic',
 'cat_geometric': 'Geometric',
 'cat_planter': 'Planters',
 'cat_user': 'Saved',
 'sec_silhouette': 'Silhouette & 2D Curve',
 'mode_sliders': 'Sliders',
 'mode_curve': 'Freeform 2D Curve',
 'btn_to_curve': 'Sliders → Curve',
 'hint_curve_sliders': 'Drag handles directly on the 2D silhouette or fine-tune sliders below.',
 'hint_curve_free': 'Drag knots · Click curve to add knot · Double-click/right-click interior knot '
                    'to remove.',
 'sec_resolution': 'Mesh Resolution',
 'mat_emerald': 'Orca Emerald Silk',
 'mat_terracotta': 'Terracotta Clay',
 'mat_white': 'Matte White Ceramic',
 'mat_copper': 'Copper Bronze',
 'mat_xray': '🔬 X-Ray / Wall (Translucent)',
 'mat_heatmap': 'Overhang Heatmap (°)',
 'vp_xray': '🔬 X-Ray / Wall',
 'vp_calipers': '📏 mm Calipers',
 'vp_heatmap': '🔥 Overhang',
 'vp_wire': '⌗ Wireframe',
 'vp_saucer': '🍽 Saucer',
 'vp_layout_nested': 'Nested',
 'vp_layout_side': 'Side-by-Side',
 'hud_title': 'Printability',
 'hud_wall_floor': 'Wall / Floor',
 'hud_mouth_hole': 'Ø Mouth Bore',
 'hud_dims': 'Dimensions (mm)',
 'hud_overhang': 'Max Overhang',
 'hud_weight': 'Est. Filament',
 'hud_Tris': 'Triangles',
 'leg_outer': 'Outer Wall',
 'leg_inner': 'Cavity & Floor',
 'cam_front': 'Front',
 'cam_top': 'Top',
 'cam_bottom': 'Bottom',
 'cam_fit': 'Fit View',
 'vp_cut': '✂ Cross-Section Cut',
 'vp_cut_y': '✂ Vertical Cut (Profile Y)',
 'vp_cut_z': '💿 Horizontal Z Slice (Plan 5%–100%)',
 'sec_envelope': 'Envelope & Global Twist',
 'sec_textures': 'Combinable Textures',
 'tex_ribbed': 'Ribbed / Fluted',
 'tex_waves': 'Organic Waves',
 'tex_origami': 'Origami Diamond',
 'tex_cellular': 'Cellular / Coral 3D',
 'lbl_ridge_mode': 'Ridged Coral Veins',
 'sec_print_mode': 'Wall & Opening (mm)',
 'mode_hollow': 'True Hollow Vase (mm Wall)',
 'mode_spiral': 'Spiral Mode (1 Line)',
 'lbl_stl_open_hollow': 'Always keep open mouth on .STL export',
 'note_spiral_honest': 'Spiral Mode builds a solid base block whose top is removed by the slicer '
                       '(.3MF). Keep the toggle below checked so .STL exports stay open!',
 'banner_spiral_safe': 'Spiral Mode: solid base block for .3MF (slicer removes top) · .STL '
                       'protected w/ Open Mouth',
 'banner_spiral_closed': 'Warning: Solid Spiral Block — .STL will export CLOSED at top for Spiral '
                         'Slicing!',
 'perim_hint_fmt': '≈ {n} loops of {lw} mm · Bore Ø {id} mm',
 'spiral_floor_fmt': '≈ {mm} mm floor ({n} lay.) · Nozzle {noz}mm (ideal {wmin}–{wmax} mm)',
 'wall_badge_hollow': 'Hollow · {w} mm',
 'wall_badge_spiral': 'Spiral · {w} mm',
 'cal_ext': 'Ø Outer: {v} mm',
 'cal_hole': 'Ø Bore: {v} mm',
 'cal_wall': 'Wall: {v} mm',
 'cal_wall_range': 'Wall: {v} mm ({min}–{max} mm)',
 'cal_floor': 'Bottom: {v} mm',
 'cal_z_slice': '💿 Z Slice = {z} mm ({pct}%)',
 'lbl_2d_wall': 'Wall {v} mm',
 'lbl_2d_floor': 'Bottom {v} mm',
 'lbl_2d_hole': 'Ø Bore {v} mm',
 'lbl_2d_spiral_cap': 'Spiral Cap (.3MF)',
 'lbl_auto_slicer': 'Auto-configure OrcaSlicer on send',
 'lbl_spiral_smooth': 'Smooth Spiral XY Seam',
 'lbl_clamp_overhang': 'Auto-Clamp Overhang Slope',
 'sec_gardening': 'Gardening: Drainage & Saucer',
 'lbl_drainage': 'Bottom Drainage Holes',
 'note_drainage_spiral': 'Smart blind cavities through solid bottom layers: real drainage holes '
                         'without breaking single-contour Spiral Vase!',
 'note_drainage_hollow': 'Watertight cylindrical drainage tunnels straight through the hollow pot '
                         'floor.',
 'lbl_include_saucer': 'Include Matching Saucer',
 'warn_saucer_spiral': 'Vase + Saucer together automatically switch to Open Hollow Mesh on '
                       'send/export.',
 'lbl_saucer_tex': 'Match Vase Texture on Saucer',
 'btn_send_plater': 'Send to OrcaSlicer Plater',
 'btn_exp_3mf': 'Export .3MF',
 'btn_exp_stl': 'Export .STL',
 'poly_circle': 'Smooth Circle',
 'poly_sides_fmt': '{n}-Gon',
 'active_tex_fmt': '{n} active',
 'bed_exceeded': 'Exceeds printer build volume ({bx}×{by}×{bz} mm)!',
 'btn_fit_printer': 'Fit to Printer',
 'printer_sync_tip': 'Click to sync active OrcaSlicer printer',
 'toast_printer_synced': 'Synced active printer: {name} ({dims})',
 'toast_fitted_printer': 'Dimensions fitted to {name} build volume!',
 'status_ok': 'PRINTABLE',
 'status_warn': 'WARNING',
 'status_crit': 'CRITICAL',
 'toast_randomized': 'Generated printable vase design!',
 'toast_preset_saved': 'Preset saved!',
 'toast_converted_curve': 'Converted sliders to PCHIP Freeform Curve!',
 'btn_off': 'Off'}


UI_MESSAGES.update({'tex_geometric': 'Geometric Relief', 'lbl_geometric_pattern': 'Sidewall Pattern', 'pattern_diamond': 'Diamond Facets', 'pattern_leaf_scales': 'Leaf Scales', 'pattern_crater_cells': 'Crater Cells', 'pattern_folded_petals': 'Folded Petals', 'pattern_spiral_bloom': 'Spiral Bloom', 'pattern_ripple': 'Ripple Rings', 'pattern_coral': 'Coral Lattice', 'hint_geometric': 'Relief is part of the wall. Combine layers or disable other textures for a clean pattern.'})

UI_MESSAGES.update({'lbl_ribbon_quality': 'Ribbon Quality', 'quality_draft': 'Draft', 'quality_normal': 'Normal', 'quality_fine': 'Fine', 'quality_adaptive': 'Adaptive', 'hint_ribbons': 'Round hollow cup with closed overlapping ribbons. Check the sliced result. Spiral mode and other textures are unavailable.', 'hint_ribbon_flatten': 'Brings folds closer to the cup without thinning the ribbons. Steep overhangs may remain; check the sliced preview.'})


def discovered_language_packs() -> dict:
    return load_language_packs()[0]


def supported_languages() -> tuple[str, ...]:
    return tuple(discovered_language_packs())


def normalize_language(value: object, default: str = "pt") -> str:
    return resolve_language(value, discovered_language_packs(), default)


def locale_vocabulary() -> dict[str, dict[str, str]]:
    return {code: pack["translations"] for code, pack in discovered_language_packs().items()}


def locale_payload(packs: dict | None = None) -> dict:
    packs = discovered_language_packs() if packs is None else packs
    return {"metadata": language_pack_payload(packs),
            "vocabulary": {code: pack["translations"] for code, pack in packs.items()},
            "messages": UI_MESSAGES}


def translate_text(text: str, language: object) -> str:
    packs = discovered_language_packs()
    code = resolve_language(language, packs)
    return packs[code]["translations"].get(text, text)

# ===========================================================================
# MODULE: vase_studio.geometric_patterns
# ===========================================================================

"""Periodic sidewall reliefs, evaluated identically by NumPy and the offline preview.

Original analytic patterns inspired by the public Vase Maker gallery. No source
from the reference plugin is included. Relief is part of the existing continuous
radial surface, so it does not introduce overlapping decorative solids.
"""
pass  # [bundled] hoisted __future__ import

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import numpy as np

GEOMETRIC_PATTERNS = (
    "diamond", "leaf_scales", "crater_cells", "folded_petals",
    "spiral_bloom", "ripple", "coral",
)

GEOMETRIC_DEFAULTS = {
    "enabled": False, "pattern": "leaf_scales", "depth_mm": 3.0,
    "cells_around": 14, "cells_vertical": 10, "twist_deg": 0.0,
    "phase_deg": 0.0, "strength_bottom": 1.0,
    "strength_middle": 1.0, "strength_top": 1.0,
    "ribbon_width_mm": 34.0, "ribbon_thickness_mm": 1.2,
    "ribbon_curl_deg": 382.0, "ribbon_overlap_mm": 1.4,
    "ribbon_flatten_pct": 0.0,
    "ribbon_stretch_pct": 8.0, "ribbon_stagger": 0.5,
    "ribbon_quality": "fine",
    "ribbon_nozzle_mm": 0.4,
}


def geometric_displacement(z_norm: np.ndarray, theta: np.ndarray, p: dict) -> np.ndarray:
    """Return bounded radial relief in mm; angular seam is exactly periodic.

    Staggered cells are evaluated in three neighboring rows. Their compact
    support fades to zero before the row leaves the window, avoiding the steps
    caused by directly switching a row's angular phase at integer heights.
    """
    import numpy as np

    if p["pattern"] == "folded_petals":
        return np.zeros(np.broadcast_shapes(z_norm.shape, theta.shape), dtype=np.float64)

    u = (theta + np.deg2rad(p["twist_deg"]) * z_norm + np.deg2rad(p["phase_deg"])) * p["cells_around"] / (2 * np.pi)
    v = z_norm * p["cells_vertical"]
    pattern = p["pattern"]
    if pattern == "ripple":
        relief = np.sin(2 * np.pi * v + 0.35 * np.sin(2 * np.pi * u))
    elif pattern == "spiral_bloom":
        relief = (np.cos(2 * np.pi * (u + v)) + 0.3 * np.cos(2 * np.pi * (u - v))) / 1.3
    elif pattern == "coral":
        a = np.sin(2 * np.pi * u + 0.9 * np.sin(2 * np.pi * v))
        b = np.sin(2 * np.pi * v + 0.9 * np.sin(2 * np.pi * u))
        relief = 1 - 2 * np.abs(a * b)
    else:
        relief = np.zeros(np.broadcast_shapes(u.shape, v.shape), dtype=np.float64)
        center_row = np.floor(v)
        for offset in (-1, 0, 1):
            row = center_row + offset
            x = np.mod(u - np.mod(row, 2) * 0.5 + 0.5, 1) - 0.5
            y = v - row
            if pattern == "diamond":
                cell = np.maximum(0, 1 - 2 * np.abs(x) - np.abs(y) / 0.6)
            else:
                q = (x / 0.48) ** 2 + (y / 0.62) ** 2
                support = np.maximum(0, 1 - q)
                if pattern == "crater_cells":
                    # A recessed basin surrounded by a raised, continuous lip.
                    cell = support ** 2 * (5 * q - 1)
                elif pattern == "folded_petals":
                    cell = support * (0.25 + 1.5 * np.abs(x)) * (0.75 + 0.25 * y / 0.62)
                else:  # leaf_scales: a pointed overlapping lens with central vein
                    cell = support ** 2 * (1 - 0.45 * np.abs(x) / 0.48) * (0.7 + 0.3 * y / 0.62)
            relief += cell
        relief = np.clip(relief, -1, 1)
    # C1 interpolation at the middle zone; endpoints keep their exact strengths.
    t = np.clip(np.where(z_norm < 0.5, z_norm * 2, (z_norm - 0.5) * 2), 0, 1)
    t = t * t * (3 - 2 * t)
    low = np.where(z_norm < 0.5, p["strength_bottom"], p["strength_middle"])
    high = np.where(z_norm < 0.5, p["strength_middle"], p["strength_top"])
    return relief * p["depth_mm"] * (low + (high - low) * t)


# Kept next to the NumPy evaluator so parity tests can exercise the production
# browser function directly, including fractional coordinates and angular seam.
GEOMETRIC_JS = r"""
  function geometricDisplacement(zNorm, theta, p) {
    if (p.pattern === "folded_petals") return 0;
    const u = (theta + p.twist_deg * Math.PI / 180 * zNorm + p.phase_deg * Math.PI / 180) * p.cells_around / (2 * Math.PI);
    const v = zNorm * p.cells_vertical;
    let relief = 0;
    if (p.pattern === "ripple") {
      relief = Math.sin(2 * Math.PI * v + 0.35 * Math.sin(2 * Math.PI * u));
    } else if (p.pattern === "spiral_bloom") {
      relief = (Math.cos(2 * Math.PI * (u + v)) + 0.3 * Math.cos(2 * Math.PI * (u - v))) / 1.3;
    } else if (p.pattern === "coral") {
      const a = Math.sin(2 * Math.PI * u + 0.9 * Math.sin(2 * Math.PI * v));
      const b = Math.sin(2 * Math.PI * v + 0.9 * Math.sin(2 * Math.PI * u));
      relief = 1 - 2 * Math.abs(a * b);
    } else {
      const centerRow = Math.floor(v);
      for (let offset = -1; offset <= 1; offset++) {
        const row = centerRow + offset;
        const rowParity = ((row % 2) + 2) % 2;
        const rawX = u - rowParity * 0.5 + 0.5;
        const x = rawX - Math.floor(rawX) - 0.5;
        const y = v - row;
        let cell;
        if (p.pattern === "diamond") {
          cell = Math.max(0, 1 - 2 * Math.abs(x) - Math.abs(y) / 0.6);
        } else {
          const q = (x / 0.48) ** 2 + (y / 0.62) ** 2;
          const support = Math.max(0, 1 - q);
          if (p.pattern === "crater_cells") cell = support ** 2 * (5 * q - 1);
          else if (p.pattern === "folded_petals") cell = support * (0.25 + 1.5 * Math.abs(x)) * (0.75 + 0.25 * y / 0.62);
          else cell = support ** 2 * (1 - 0.45 * Math.abs(x) / 0.48) * (0.7 + 0.3 * y / 0.62);
        }
        relief += cell;
      }
      relief = Math.max(-1, Math.min(1, relief));
    }
    let t = Math.max(0, Math.min(1, zNorm < 0.5 ? zNorm * 2 : (zNorm - 0.5) * 2));
    t = t * t * (3 - 2 * t);
    const low = zNorm < 0.5 ? p.strength_bottom : p.strength_middle;
    const high = zNorm < 0.5 ? p.strength_middle : p.strength_top;
    return relief * p.depth_mm * (low + (high - low) * t);
  }
"""

# ===========================================================================
# MODULE: vase_studio.schema
# ===========================================================================

"""Unified parameter schema and validation for Orca Vase Studio."""

pass  # [bundled] hoisted __future__ import

import copy
import math
from typing import Any
pass  # [bundled] resolved intra-package import

SCHEMA_VERSION = "1.0"

DEFAULT_PARAMS: dict[str, Any] = {
    "name": "Ondas Organicas",
    "height_mm": 160.0,              # [30.0, 500.0]
    "base_diameter_mm": 76.0,        # [20.0, 450.0]
    "belly_diameter_mm": 110.0,      # [20.0, 450.0]
    "belly_height_ratio": 0.34,      # [0.08, 0.85]
    "waist_diameter_mm": 68.0,       # [16.0, 450.0]
    "waist_height_ratio": 0.68,      # [0.15, 0.92]
    "neck_diameter_mm": 82.0,        # [16.0, 450.0]
    "lip_flare_mm": 4.0,             # [-15.0, 25.0] extra radius added smoothly over top 8% (z_norm 0.92..1.0)
    "lip_bevel_mm": 1.0,             # [0.0, 4.0] subtle top rim rounding/bevel
    "polygon_sides": 0,              # 0 = smooth circle; 3..24 = polygonal cross-section
    "polygon_roundness": 0.35,       # [0.0, 1.0] blends polygon radius toward circle (1.0 = pure circle)
    "use_custom_profile": False,     # bool: when True, base silhouette comes from profile_points instead of base/belly/waist/neck
    "profile_points": [              # list of [z_norm (0..1), radius_mm (8..225)], >= 2 points, endpoints clamped to z=0.0 and z=1.0
        [0.0, 38.0],
        [0.34, 55.0],
        [0.68, 34.0],
        [0.92, 41.0],
        [1.0, 45.0],
    ],
    "resolution_angular": 240,       # [64, 360]
    "resolution_vertical": 220,      # [60, 400]

    # Global texture envelope & helical twist
    "bottom_fade_mm": 8.0,           # [0.0, 60.0] smoothstep 0->1 from z=0 to z=bottom_fade_mm (flat bed adhesion!)
    "top_fade_mm": 6.0,              # [0.0, 60.0] smoothstep 1->0 from z=(H - top_fade_mm) to z=H
    "global_twist_deg": 0.0,         # [-720.0, 720.0]

    # Combinable Surface Texture Layers (summed radial displacement in mm)
    "textures": {
        "geometric": copy.deepcopy(GEOMETRIC_DEFAULTS),
        "ribbed": {
            "enabled": False,
            "depth_mm": 2.6,         # [-15.0, 15.0]
            "count": 32,             # [3, 180] circumferential rib count (density)
            "duty_cycle": 0.50,      # [0.10, 0.90] width of rib vs flat spacing gap
            "sharpness": 0.35,       # [0.0, 1.0] 0=smooth cosine, 0.5=rounded flute, 1.0=sharp triangular/chiseled
            "twist_deg": 60.0,       # [-720.0, 720.0]
            "phase_deg": 0.0,        # [0.0, 360.0]
        },
        "waves": {
            "enabled": True,
            "depth_mm": 3.0,         # [-15.0, 15.0]
            "vertical_wavelength_mm": 26.0,  # [4.0, 120.0] vertical wave spacing in mm
            "angular_lobes": 6,      # [0, 48] circumferential wave count
            "interference_mix": 0.45,  # [0.0, 1.0] mix of counter-helical wave creating organic woven/ripple pockets
            "wave_skew": 0.0,        # [-0.8, 0.8]
            "phase_deg": 0.0,        # [0.0, 360.0]
        },
        "origami": {
            "enabled": False,
            "depth_mm": 3.2,         # [-15.0, 15.0]
            "cells_around": 12,      # [3, 60] horizontal diamond density
            "cells_vertical": 8,     # [2, 50] vertical diamond tiers
            "crease_sharpness": 0.75,  # [0.0, 1.0]
            "stagger": 0.50,         # [0.0, 1.0]
        },
        "cellular": {
            "enabled": False,
            "depth_mm": 2.4,         # [-12.0, 12.0]
            "scale_angular": 8,      # [2, 40] cells around circumference
            "scale_vertical_mm": 22.0,  # [5.0, 100.0] vertical cell spacing in mm
            "ridge_mode": True,      # bool: True = ridged coral/stone veins, False = smooth organic billows
            "octaves": 2,            # [1, 4]
            "seed": 42,              # [1, 99999]
        },
    },

    # Printability & Wall Structure
    "print_mode": "shelled_hollow",  # "shelled_hollow" | "spiral_vase"
    "stl_always_open_hollow": True,  # keep open mouth when exporting .stl even if spiral_vase is selected
    "auto_configure_slicer": True,
    "spiral_line_width_mm": 0.65,    # [0.40, 1.20]
    "spiral_bottom_layers": 5,       # [2, 15]
    "spiral_smooth": True,
    "wall_thickness_mm": 2.4,        # [0.8, 25.0] used when print_mode == "shelled_hollow"
    "bottom_thickness_mm": 3.2,      # [1.0, 25.0] used when print_mode == "shelled_hollow"
    "auto_clamp_overhang": False,
    "max_safe_overhang_deg": 48.0,   # [35.0, 65.0]

    # Gardening: Drainage & Matching Saucer
    "drainage": {
        "enabled": False,
        "hole_count": 4,             # [1, 9]
        "hole_diameter_mm": 8.0,     # [3.0, 20.0]
        "ring_radius_ratio": 0.48,   # [0.0, 0.68]
    },
    "saucer": {
        "clearance_mm": 8.0,         # [3.0, 25.0]
        "rim_height_mm": 22.0,       # [10.0, 60.0]
        "wall_thickness_mm": 2.4,    # [1.2, 5.0]
        "floor_thickness_mm": 2.6,   # [1.2, 6.0]
        "inner_ribs_height_mm": 2.0, # [0.0, 6.0] raised drainage ribs inside saucer floor
        "match_vase_texture": True,
    },
}


def _to_float(val: Any, default: float, lo: float, hi: float) -> float:
    if isinstance(val, bool):
        return default
    try:
        f = float(val)
    except (TypeError, ValueError):
        return default
    if not math.isfinite(f):
        return default
    return max(lo, min(hi, f))


def _to_int(val: Any, default: int, lo: int, hi: int) -> int:
    if isinstance(val, bool):
        return default
    try:
        f = float(val)
    except (TypeError, ValueError):
        return default
    if not math.isfinite(f):
        return default
    i = int(round(f))
    return max(lo, min(hi, i))


def _to_bool(val: Any, default: bool) -> bool:
    if isinstance(val, bool):
        return val
    if isinstance(val, (int, float)):
        if math.isfinite(val):
            return bool(val)
        return default
    if isinstance(val, str):
        s = val.strip().lower()
        if s in ("true", "1", "yes", "on"):
            return True
        if s in ("false", "0", "no", "off", ""):
            return False
    return default


def _normalize_profile_points(raw_pts: Any) -> list[list[float]]:
    default_pts = copy.deepcopy(DEFAULT_PARAMS["profile_points"])
    if not isinstance(raw_pts, (list, tuple)) or len(raw_pts) < 2:
        return default_pts

    parsed: list[list[float]] = []
    for item in raw_pts:
        z_raw: Any = None
        r_raw: Any = None
        if isinstance(item, (list, tuple)) and len(item) >= 2:
            z_raw, r_raw = item[0], item[1]
        elif isinstance(item, dict):
            z_raw = item.get("z", item.get("z_norm"))
            r_raw = item.get("r", item.get("radius_mm", item.get("radius")))
        else:
            continue

        z_val = _to_float(z_raw, -1.0, 0.0, 1.0)
        r_val = _to_float(r_raw, -1.0, 8.0, 225.0)
        if z_raw is None or r_raw is None:
            continue
        try:
            zf = float(z_raw)
            rf = float(r_raw)
            if not (math.isfinite(zf) and math.isfinite(rf)):
                continue
        except (TypeError, ValueError):
            continue
        parsed.append([max(0.0, min(1.0, zf)), max(8.0, min(225.0, rf))])

    if len(parsed) < 2:
        return default_pts

    parsed.sort(key=lambda p: p[0])
    parsed[0][0] = 0.0
    parsed[-1][0] = 1.0

    # Deduplicate near-identical z_norm knots so PCHIP never divides by zero
    cleaned: list[list[float]] = [parsed[0]]
    for pt in parsed[1:]:
        if pt[0] - cleaned[-1][0] < 1e-4:
            if pt[0] >= 1.0:
                cleaned[-1] = [1.0, pt[1]]
            else:
                cleaned[-1][1] = 0.5 * (cleaned[-1][1] + pt[1])
        else:
            cleaned.append(pt)

    if len(cleaned) < 2:
        return default_pts
    cleaned[0][0] = 0.0
    cleaned[-1][0] = 1.0
    return cleaned


def _deep_merge_dict(base: dict[str, Any], override: dict[str, Any]) -> dict[str, Any]:
    for k, v in override.items():
        if k in base and isinstance(base[k], dict) and isinstance(v, dict):
            _deep_merge_dict(base[k], v)
        elif k in base:
            base[k] = v
    return base


def normalize_params(raw: dict[str, Any] | None) -> dict[str, Any]:
    """Deep-copy DEFAULT_PARAMS, merge raw recursively, coerce types, and clamp bounds."""
    out = copy.deepcopy(DEFAULT_PARAMS)
    if isinstance(raw, dict):
        _deep_merge_dict(out, raw)

    # Top-level string & mode fields
    raw_name = out.get("name")
    if isinstance(raw_name, str) and raw_name.strip():
        out["name"] = raw_name.strip()[:120]
    else:
        out["name"] = DEFAULT_PARAMS["name"]

    d = DEFAULT_PARAMS
    out["height_mm"] = _to_float(out["height_mm"], d["height_mm"], 30.0, 500.0)
    out["base_diameter_mm"] = _to_float(out["base_diameter_mm"], d["base_diameter_mm"], 20.0, 450.0)
    out["belly_diameter_mm"] = _to_float(out["belly_diameter_mm"], d["belly_diameter_mm"], 20.0, 450.0)
    out["belly_height_ratio"] = _to_float(out["belly_height_ratio"], d["belly_height_ratio"], 0.08, 0.85)
    out["waist_diameter_mm"] = _to_float(out["waist_diameter_mm"], d["waist_diameter_mm"], 16.0, 450.0)
    out["waist_height_ratio"] = _to_float(out["waist_height_ratio"], d["waist_height_ratio"], 0.15, 0.92)
    out["neck_diameter_mm"] = _to_float(out["neck_diameter_mm"], d["neck_diameter_mm"], 16.0, 450.0)
    out["lip_flare_mm"] = _to_float(out["lip_flare_mm"], d["lip_flare_mm"], -15.0, 25.0)
    out["lip_bevel_mm"] = _to_float(out["lip_bevel_mm"], d["lip_bevel_mm"], 0.0, 4.0)

    poly_sides = _to_int(out["polygon_sides"], d["polygon_sides"], 0, 24)
    out["polygon_sides"] = 0 if poly_sides < 3 else poly_sides
    out["polygon_roundness"] = _to_float(out["polygon_roundness"], d["polygon_roundness"], 0.0, 1.0)

    out["use_custom_profile"] = _to_bool(out["use_custom_profile"], d["use_custom_profile"])
    out["profile_points"] = _normalize_profile_points(out.get("profile_points"))

    out["resolution_angular"] = _to_int(out["resolution_angular"], d["resolution_angular"], 64, 360)
    out["resolution_vertical"] = _to_int(out["resolution_vertical"], d["resolution_vertical"], 60, 400)

    out["bottom_fade_mm"] = _to_float(out["bottom_fade_mm"], d["bottom_fade_mm"], 0.0, 60.0)
    out["top_fade_mm"] = _to_float(out["top_fade_mm"], d["top_fade_mm"], 0.0, 60.0)
    out["global_twist_deg"] = _to_float(out["global_twist_deg"], d["global_twist_deg"], -720.0, 720.0)

    # Textures
    tex = out["textures"]
    dt = d["textures"]

    rib = tex["ribbed"]
    d_rib = dt["ribbed"]
    rib["enabled"] = _to_bool(rib["enabled"], d_rib["enabled"])
    rib["depth_mm"] = _to_float(rib["depth_mm"], d_rib["depth_mm"], -15.0, 15.0)
    rib["count"] = _to_int(rib["count"], d_rib["count"], 3, 180)
    rib["duty_cycle"] = _to_float(rib["duty_cycle"], d_rib["duty_cycle"], 0.10, 0.90)
    rib["sharpness"] = _to_float(rib["sharpness"], d_rib["sharpness"], 0.0, 1.0)
    rib["twist_deg"] = _to_float(rib["twist_deg"], d_rib["twist_deg"], -720.0, 720.0)
    rib["phase_deg"] = _to_float(rib["phase_deg"], d_rib["phase_deg"], 0.0, 360.0)

    wav = tex["waves"]
    d_wav = dt["waves"]
    wav["enabled"] = _to_bool(wav["enabled"], d_wav["enabled"])
    wav["depth_mm"] = _to_float(wav["depth_mm"], d_wav["depth_mm"], -15.0, 15.0)
    wav["vertical_wavelength_mm"] = _to_float(wav["vertical_wavelength_mm"], d_wav["vertical_wavelength_mm"], 4.0, 120.0)
    wav["angular_lobes"] = _to_int(wav["angular_lobes"], d_wav["angular_lobes"], 0, 48)
    wav["interference_mix"] = _to_float(wav["interference_mix"], d_wav["interference_mix"], 0.0, 1.0)
    wav["wave_skew"] = _to_float(wav["wave_skew"], d_wav["wave_skew"], -0.8, 0.8)
    wav["phase_deg"] = _to_float(wav["phase_deg"], d_wav["phase_deg"], 0.0, 360.0)

    ori = tex["origami"]
    d_ori = dt["origami"]
    ori["enabled"] = _to_bool(ori["enabled"], d_ori["enabled"])
    ori["depth_mm"] = _to_float(ori["depth_mm"], d_ori["depth_mm"], -15.0, 15.0)
    ori["cells_around"] = _to_int(ori["cells_around"], d_ori["cells_around"], 3, 60)
    ori["cells_vertical"] = _to_int(ori["cells_vertical"], d_ori["cells_vertical"], 2, 50)
    ori["crease_sharpness"] = _to_float(ori["crease_sharpness"], d_ori["crease_sharpness"], 0.0, 1.0)
    ori["stagger"] = _to_float(ori["stagger"], d_ori["stagger"], 0.0, 1.0)

    cel = tex["cellular"]
    d_cel = dt["cellular"]
    cel["enabled"] = _to_bool(cel["enabled"], d_cel["enabled"])
    cel["depth_mm"] = _to_float(cel["depth_mm"], d_cel["depth_mm"], -12.0, 12.0)
    cel["scale_angular"] = _to_int(cel["scale_angular"], d_cel["scale_angular"], 2, 40)
    cel["scale_vertical_mm"] = _to_float(cel["scale_vertical_mm"], d_cel["scale_vertical_mm"], 5.0, 100.0)
    cel["ridge_mode"] = _to_bool(cel["ridge_mode"], d_cel["ridge_mode"])
    cel["octaves"] = _to_int(cel["octaves"], d_cel["octaves"], 1, 4)
    cel["seed"] = _to_int(cel["seed"], d_cel["seed"], 1, 99999)

    # Printability & Wall Structure
    pm = str(out.get("print_mode", d["print_mode"])).strip().lower()
    out["print_mode"] = pm if pm in ("spiral_vase", "shelled_hollow") else d["print_mode"]
    out["stl_always_open_hollow"] = _to_bool(out["stl_always_open_hollow"], d["stl_always_open_hollow"])
    out["auto_configure_slicer"] = _to_bool(out["auto_configure_slicer"], d["auto_configure_slicer"])
    out["spiral_line_width_mm"] = _to_float(out["spiral_line_width_mm"], d["spiral_line_width_mm"], 0.40, 1.20)
    out["spiral_bottom_layers"] = _to_int(out["spiral_bottom_layers"], d["spiral_bottom_layers"], 2, 15)
    out["spiral_smooth"] = _to_bool(out["spiral_smooth"], d["spiral_smooth"])
    out["wall_thickness_mm"] = _to_float(out["wall_thickness_mm"], d["wall_thickness_mm"], 0.8, 25.0)
    out["bottom_thickness_mm"] = _to_float(out["bottom_thickness_mm"], d["bottom_thickness_mm"], 1.0, 25.0)
    out["auto_clamp_overhang"] = _to_bool(out["auto_clamp_overhang"], d["auto_clamp_overhang"])
    out["max_safe_overhang_deg"] = _to_float(out["max_safe_overhang_deg"], d["max_safe_overhang_deg"], 35.0, 65.0)

    geo = tex["geometric"]
    geo["enabled"] = _to_bool(geo["enabled"], False)
    if geo["pattern"] not in GEOMETRIC_PATTERNS:
        geo["pattern"] = GEOMETRIC_DEFAULTS["pattern"]
    geo["depth_mm"] = _to_float(geo["depth_mm"], 3.0, -8.0, 8.0)
    geo["cells_around"] = _to_int(geo["cells_around"], 14, 3, 36)
    geo["cells_vertical"] = _to_int(geo["cells_vertical"], 10, 2, 24)
    geo["twist_deg"] = _to_float(geo["twist_deg"], 0.0, -720.0, 720.0)
    geo["phase_deg"] = _to_float(geo["phase_deg"], 0.0, 0.0, 360.0)
    for zone in ("bottom", "middle", "top"):
        key = "strength_" + zone
        geo[key] = _to_float(geo[key], 1.0, 0.0, 2.0)
    for key, low, high in (("ribbon_width_mm", 8, 80), ("ribbon_thickness_mm", 0.4, 4),
                          ("ribbon_curl_deg", 180, 430), ("ribbon_overlap_mm", 0, 4),
                          ("ribbon_stretch_pct", 0, 25), ("ribbon_stagger", 0, 1),
                          ("ribbon_nozzle_mm", 0.2, 1.2), ("ribbon_flatten_pct", 0, 60)):
        geo[key] = _to_float(geo[key], GEOMETRIC_DEFAULTS[key], low, high)
    if geo["ribbon_quality"] not in ("draft", "normal", "fine", "adaptive"):
        geo["ribbon_quality"] = "fine"
    if geo["enabled"] and geo["pattern"] == "folded_petals":
        out["print_mode"] = "shelled_hollow"
        out["polygon_sides"] = 0
        for layer in ("ribbed", "waves", "origami", "cellular"):
            tex[layer]["enabled"] = False

    # Drainage
    dr = out["drainage"]
    d_dr = d["drainage"]
    dr["enabled"] = _to_bool(dr["enabled"], d_dr["enabled"])
    dr["hole_count"] = _to_int(dr["hole_count"], d_dr["hole_count"], 1, 9)
    dr["hole_diameter_mm"] = _to_float(dr["hole_diameter_mm"], d_dr["hole_diameter_mm"], 3.0, 20.0)
    dr["ring_radius_ratio"] = _to_float(dr["ring_radius_ratio"], d_dr["ring_radius_ratio"], 0.0, 0.68)

    # Saucer
    sc = out["saucer"]
    d_sc = d["saucer"]
    sc["clearance_mm"] = _to_float(sc["clearance_mm"], d_sc["clearance_mm"], 3.0, 25.0)
    sc["rim_height_mm"] = _to_float(sc["rim_height_mm"], d_sc["rim_height_mm"], 10.0, 60.0)
    sc["wall_thickness_mm"] = _to_float(sc["wall_thickness_mm"], d_sc["wall_thickness_mm"], 1.2, 5.0)
    sc["floor_thickness_mm"] = _to_float(sc["floor_thickness_mm"], d_sc["floor_thickness_mm"], 1.2, 6.0)
    sc["inner_ribs_height_mm"] = _to_float(sc["inner_ribs_height_mm"], d_sc["inner_ribs_height_mm"], 0.0, 6.0)
    sc["match_vase_texture"] = _to_bool(sc["match_vase_texture"], d_sc["match_vase_texture"])

    return out

# ===========================================================================
# MODULE: vase_studio.ribbon_geometry
# ===========================================================================

"""Curled ribbon surfaces adapted from Vase Maker 0.8.19 (MIT).

Copyright (c) 2026 Dante x, original ribbon construction.
Copyright (c) 2026 Orca Vase Studio, vectorized and browser implementations.
SPDX-License-Identifier: MIT

Source: https://cloud.orcaslicer.com/p/3e9de58df37d
The cup and ribbons are separately closed solids, as in the reference. This
module does not claim to Boolean-union intersecting surfaces.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
pass  # [bundled] hoisted __future__ import

import math


def ribbon_plan(params: dict, interactive: bool = False) -> dict:
    g = params["textures"]["geometric"]
    quality = "draft" if interactive else g["ribbon_quality"]
    dz, row_factor, width_steps = {
        "draft": (1.5, 8, 16), "normal": (0.55, 16, 24),
        "fine": (0.28, 28, 36), "adaptive": (0.6, 14, 22),
    }[quality]
    if quality == "adaptive":
        nozzle = g["ribbon_nozzle_mm"]
        dz = max(0.55, nozzle * 1.5)
        width_steps = min(28, max(12, math.ceil(g["ribbon_width_mm"] / max(1.6, nozzle * 4))))
    nz = min(1200, max(g["cells_vertical"] * row_factor, math.ceil(params["height_mm"] / dz)))
    vertices_per_ribbon = 2 * (width_steps + 1) * (nz + 1)
    triangles_per_ribbon = 4 * width_steps * nz + 4 * nz + 4 * width_steps
    count = g["cells_around"]
    return {"nz": nz, "nu": width_steps, "count": count,
            "vertices": count * vertices_per_ribbon,
            "triangles": count * triangles_per_ribbon}


def ribbon_triangles(nz: int, nu: int):
    """Oriented, closed boundary of one thick rectangular parametric strip."""
    import numpy as np

    grid = np.arange((nz + 1) * (nu + 1), dtype=np.int32).reshape(nz + 1, nu + 1)
    back = grid.size
    a, b, c, d = grid[:-1, :-1], grid[:-1, 1:], grid[1:, 1:], grid[1:, :-1]
    chunks = [np.stack((a, b, c), -1).reshape(-1, 3), np.stack((a, c, d), -1).reshape(-1, 3),
              np.stack((a + back, d + back, c + back), -1).reshape(-1, 3),
              np.stack((a + back, c + back, b + back), -1).reshape(-1, 3)]
    # Traverse the perimeter in the front surface's CCW parameter order.
    loop = np.concatenate((grid[0, :], grid[1:, -1], grid[-1, -2::-1], grid[-2:0:-1, 0]))
    nxt = np.roll(loop, -1)
    chunks += [np.column_stack((loop, loop + back, nxt + back)),
               np.column_stack((loop, nxt + back, nxt))]
    return np.concatenate(chunks)


def build_ribbon_mesh(params: dict, profile_radii, interactive: bool = False):
    """Vectorize the reference's midpoint/normal/offset construction per ribbon."""
    import numpy as np

    g = params["textures"]["geometric"]
    plan = ribbon_plan(params, interactive)
    nz, nu, count = plan["nz"], plan["nu"], plan["count"]
    radii = np.asarray(profile_radii, dtype=np.float64)
    if radii.shape != (nz + 1,):
        raise ValueError("Ribbon profile sampling does not match the mesh plan")
    t = np.linspace(0, 1, nz + 1)[:, None]
    q = np.linspace(0, 1, nu + 1)[None, :]
    strength = np.where(t <= 0.5,
        g["strength_bottom"] + (g["strength_middle"] - g["strength_bottom"]) * 2 * t,
        g["strength_middle"] + (g["strength_top"] - g["strength_middle"]) * 2 * (t - 0.5))
    twist = math.radians(g["twist_deg"] + params["global_twist_deg"])
    phase = math.radians(g["phase_deg"])
    vertices = []
    triangles = []
    strip_tris = ribbon_triangles(nz, nu)
    vertex_offset = 0
    for strip in range(count):
        row_phase = 2 * math.pi * g["ribbon_stagger"] * (strip % 2)
        blend = 0.5 + 0.5 * np.cos(2 * math.pi * g["cells_vertical"] * t + row_phase)
        blend = blend * blend * (3 - 2 * blend) * np.clip(strength, 0, 1.5)
        sweep = math.radians(32) + (math.radians(g["ribbon_curl_deg"]) - math.radians(32)) * blend
        arc_length = g["ribbon_width_mm"] * (1 + g["ribbon_stretch_pct"] / 100 * blend)
        base_radius = arc_length / sweep
        theta = (q - 0.5) * sweep
        local_radius = base_radius + g["ribbon_overlap_mm"] * blend * (0.5 - q)
        tangent = local_radius * np.sin(theta)
        radial = base_radius - local_radius * np.cos(theta)
        radial += 0.35 * g["ribbon_overlap_mm"] * blend * np.tanh((0.5 - q) * 7) * np.abs(2 * q - 1) ** 1.8
        center = 2 * math.pi * strip / count + twist * t + phase
        radius = radii[:, None] + radial
        if g.get("ribbon_flatten_pct", 0) > 0:
            # Compress distance from the actual cylindrical profile, including
            # tangential reach. Offset the skins afterwards to retain thickness.
            rho = np.hypot(radius, tangent)
            target = radii[:, None] + (rho - radii[:, None]) * (1 - g["ribbon_flatten_pct"] / 100)
            scale = target / rho
            radius = radius * scale
            tangent = tangent * scale
        mid = np.stack((radius * np.cos(center) - tangent * np.sin(center),
                        radius * np.sin(center) + tangent * np.cos(center),
                        np.broadcast_to(t * params["height_mm"], radius.shape)), axis=-1)
        # Centered differences match the reference's endpoint-aware tangents.
        tu = np.concatenate((mid[:, 1:2] - mid[:, :1], mid[:, 2:] - mid[:, :-2], mid[:, -1:] - mid[:, -2:-1]), axis=1)
        tz = np.concatenate((mid[1:2] - mid[:1], mid[2:] - mid[:-2], mid[-1:] - mid[-2:-1]), axis=0)
        normals = np.cross(tu, tz)
        lengths = np.linalg.norm(normals, axis=-1, keepdims=True)
        if np.any(lengths < 1e-10):
            raise ValueError("Ribbon surface has a collapsed tangent; adjust width, curl or overlap")
        normals /= lengths
        edge = np.clip(np.minimum(q, 1 - q) / 0.12, 0, 1)
        edge = edge * edge * (3 - 2 * edge)
        thickness = g["ribbon_thickness_mm"] / (1 + g["ribbon_stretch_pct"] / 100 * blend)
        thickness = thickness * (0.35 + 0.65 * edge)
        front = mid + normals * thickness[..., None] * 0.5
        back = mid - normals * thickness[..., None] * 0.5
        for face in (front, back):
            np.clip(face[:, :, 2], 0, params["height_mm"], out=face[:, :, 2])
            face[0, :, 2] = 0
            face[-1, :, 2] = params["height_mm"]
        if g.get("ribbon_flatten_pct", 0) > 0:
            tangent_edges = np.diff(mid, axis=1)
            for face in (front, back):
                if np.any(np.sum(np.diff(face, axis=1) * tangent_edges, axis=-1) < -1e-10):
                    raise ValueError("Flattening pinches a ribbon fold. Reduce flattening or thickness, or increase ribbon width.")
        verts = np.concatenate((front.reshape(-1, 3), back.reshape(-1, 3)))
        vertices.append(verts)
        triangles.append(strip_tris + vertex_offset)
        vertex_offset += len(verts)
    return np.concatenate(vertices), np.concatenate(triangles)


RIBBON_JS = r"""
  function ribbonPlan(p, interactive) {
    const g=p.textures.geometric;
    const nozzle=g.ribbon_nozzle_mm;
    const spec={draft:[1.5,8,16],normal:[0.55,16,24],fine:[0.28,28,36],adaptive:[Math.max(0.55,nozzle*1.5),14,Math.min(28,Math.max(12,Math.ceil(g.ribbon_width_mm/Math.max(1.6,nozzle*4))))]}[interactive?'draft':g.ribbon_quality];
    const nz=Math.min(1200,Math.max(g.cells_vertical*spec[1],Math.ceil(p.height_mm/spec[0]))),nu=spec[2],count=g.cells_around;
    return {nz,nu,count,vertices:count*2*(nu+1)*(nz+1),triangles:count*(4*nu*nz+4*nz+4*nu)};
  }
  function buildRibbonMesh(p, profileRadii, interactive) {
    const g=p.textures.geometric,plan=ribbonPlan(p,interactive),{nz,nu,count}=plan;
    const positions=new Float32Array(plan.vertices*3),indices=new Uint32Array(plan.triangles*3);
    const normals=new Float32Array(positions.length),overhangs=new Float32Array(plan.vertices);
    const parts=new Float32Array(plan.vertices),roles=new Float32Array(plan.vertices);
    const perSide=(nz+1)*(nu+1),perStrip=2*perSide;
    let ti=0;
    const tri=(a,b,c)=>{indices[ti++]=a;indices[ti++]=b;indices[ti++]=c;};
    for(let strip=0;strip<count;strip++) {
      const mid=new Float64Array(perSide*3),thickness=new Float64Array(perSide);
      for(let iz=0;iz<=nz;iz++) {
        const t=iz/nz,strength=t<=0.5?g.strength_bottom+(g.strength_middle-g.strength_bottom)*2*t:g.strength_middle+(g.strength_top-g.strength_middle)*2*(t-0.5);
        let blend=0.5+0.5*Math.cos(2*Math.PI*g.cells_vertical*t+2*Math.PI*g.ribbon_stagger*(strip%2));
        blend=blend*blend*(3-2*blend)*Math.max(0,Math.min(1.5,strength));
        const sweep=32*Math.PI/180+(g.ribbon_curl_deg-32)*Math.PI/180*blend;
        const baseRadius=g.ribbon_width_mm*(1+g.ribbon_stretch_pct/100*blend)/sweep;
        const center=2*Math.PI*strip/count+(g.twist_deg+p.global_twist_deg)*Math.PI/180*t+g.phase_deg*Math.PI/180;
        const cc=Math.cos(center),ss=Math.sin(center);
        for(let iu=0;iu<=nu;iu++) {
          const q=iu/nu,theta=(q-0.5)*sweep,localRadius=baseRadius+g.ribbon_overlap_mm*blend*(0.5-q);
          let tangent=localRadius*Math.sin(theta);
          let radial=baseRadius-localRadius*Math.cos(theta);
          radial+=0.35*g.ribbon_overlap_mm*blend*Math.tanh((0.5-q)*7)*Math.abs(2*q-1)**1.8;
          let radius=profileRadii[iz]+radial;
          if((g.ribbon_flatten_pct||0)>0) {
            const rho=Math.hypot(radius,tangent),target=profileRadii[iz]+(rho-profileRadii[iz])*(1-g.ribbon_flatten_pct/100),scale=target/rho;
            radius*=scale;tangent*=scale;
          }
          const k=iz*(nu+1)+iu;
          mid[k*3]=radius*cc-tangent*ss;mid[k*3+1]=radius*ss+tangent*cc;mid[k*3+2]=t*p.height_mm;
          let edge=Math.max(0,Math.min(1,Math.min(q,1-q)/0.12));edge=edge*edge*(3-2*edge);
          thickness[k]=g.ribbon_thickness_mm/(1+g.ribbon_stretch_pct/100*blend)*(0.35+0.65*edge);
        }
      }
      const offset=strip*perStrip;
      for(let iz=0;iz<=nz;iz++) for(let iu=0;iu<=nu;iu++) {
        const k=iz*(nu+1)+iu,ua=(iz*(nu+1)+Math.max(0,iu-1))*3,ub=(iz*(nu+1)+Math.min(nu,iu+1))*3;
        const za=(Math.max(0,iz-1)*(nu+1)+iu)*3,zb=(Math.min(nz,iz+1)*(nu+1)+iu)*3;
        const ux=mid[ub]-mid[ua],uy=mid[ub+1]-mid[ua+1],uz=mid[ub+2]-mid[ua+2];
        const zx=mid[zb]-mid[za],zy=mid[zb+1]-mid[za+1],zz=mid[zb+2]-mid[za+2];
        const nx=uy*zz-uz*zy,ny=uz*zx-ux*zz,nzv=ux*zy-uy*zx;
        const length=Math.hypot(nx,ny,nzv);
        if(length<1e-10) throw Error('Ribbon surface has a collapsed tangent; adjust width, curl or overlap');
        const h=thickness[k]*0.5/length;
        for(let side=0;side<2;side++) {
          const sign=side===0?1:-1,out=(offset+side*perSide+k)*3;
          positions[out]=mid[k*3]+sign*nx*h;positions[out+1]=mid[k*3+1]+sign*ny*h;
          positions[out+2]=iz===0?0:(iz===nz?p.height_mm:Math.max(0,Math.min(p.height_mm,mid[k*3+2]+sign*nzv*h)));
        }
      }
      if((g.ribbon_flatten_pct||0)>0) {
        for(let iz=0;iz<=nz;iz++) for(let iu=0;iu<nu;iu++) {
          const a=(iz*(nu+1)+iu)*3,b=a+3;
          for(let side=0;side<2;side++) {
            const out=(offset+side*perSide)*3;
            const dot=(positions[out+b]-positions[out+a])*(mid[b]-mid[a])+(positions[out+b+1]-positions[out+a+1])*(mid[b+1]-mid[a+1])+(positions[out+b+2]-positions[out+a+2])*(mid[b+2]-mid[a+2]);
            if(dot < -1e-10) throw Error('Flattening pinches a ribbon fold. Reduce flattening or thickness, or increase ribbon width.');
          }
        }
      }
      const at=(iz,iu)=>offset+iz*(nu+1)+iu;
      for(let iz=0;iz<nz;iz++) for(let iu=0;iu<nu;iu++) {
        const a=at(iz,iu),b=at(iz,iu+1),c=at(iz+1,iu+1),d=at(iz+1,iu);
        tri(a,b,c);tri(a,c,d);tri(a+perSide,d+perSide,c+perSide);tri(a+perSide,c+perSide,b+perSide);
      }
      const loop=[];
      for(let iu=0;iu<=nu;iu++) loop.push(at(0,iu));
      for(let iz=1;iz<=nz;iz++) loop.push(at(iz,nu));
      for(let iu=nu-1;iu>=0;iu--) loop.push(at(nz,iu));
      for(let iz=nz-1;iz>0;iz--) loop.push(at(iz,0));
      for(let k=0;k<loop.length;k++) {const a=loop[k],b=loop[(k+1)%loop.length];tri(a,a+perSide,b+perSide);tri(a,b+perSide,b);}
    }
    // Area-weighted normals from the exported indexed boundary, including caps.
    let signedVolume=0;
    for(let i=0;i<indices.length;i+=3) {
      const a=indices[i]*3,b=indices[i+1]*3,c=indices[i+2]*3;
      const ux=positions[b]-positions[a],uy=positions[b+1]-positions[a+1],uz=positions[b+2]-positions[a+2];
      const vx=positions[c]-positions[a],vy=positions[c+1]-positions[a+1],vz=positions[c+2]-positions[a+2];
      const nx=uy*vz-uz*vy,ny=uz*vx-ux*vz,nzv=ux*vy-uy*vx;
      signedVolume+=positions[a]*nx+positions[a+1]*ny+positions[a+2]*nzv;
      for(const k of [a,b,c]) {normals[k]+=nx;normals[k+1]+=ny;normals[k+2]+=nzv;}
    }
    for(let i=0;i<normals.length;i+=3) {
      const l=Math.hypot(normals[i],normals[i+1],normals[i+2])||1;
      normals[i]/=l;normals[i+1]/=l;normals[i+2]/=l;
      overhangs[i/3]=Math.asin(Math.max(0,-normals[i+2]))*180/Math.PI;
    }
    return {positions,indices,normals,overhangs,parts,roles,volumeCm3:signedVolume/6000};
  }
"""

# ===========================================================================
# MODULE: vase_studio.mesh_generator
# ===========================================================================

"""Parametric 3D vase and saucer manifold mesh generator for Orca Vase Studio."""

pass  # [bundled] hoisted __future__ import

from dataclasses import dataclass
import math
from typing import Any

try:
    import numpy as np
except ModuleNotFoundError:
    import os as _os
    from pathlib import Path as _Path
    import sys as _sys

    if _sys.platform == "win32":
        _appdata = _os.environ.get("APPDATA", "").strip()
        _orca_base = _Path(_appdata) / "OrcaSlicer" if _appdata else _Path.home() / "AppData" / "Roaming" / "OrcaSlicer"
    elif _sys.platform == "darwin":
        _orca_base = _Path.home() / "Library" / "Application Support" / "OrcaSlicer"
    else:
        _xdg = _os.environ.get("XDG_CONFIG_HOME", "").strip()
        _orca_base = (_Path(_xdg) if _xdg else (_Path.home() / ".config")) / "OrcaSlicer"

    _orca_pkg_dir = str(_orca_base / "python" / "packages" / f"cp{_sys.version_info.major}{_sys.version_info.minor}")
    if _orca_pkg_dir not in _sys.path:
        _sys.path.insert(0, _orca_pkg_dir)
    import numpy as np

pass  # [bundled] resolved intra-package import
pass  # [bundled] resolved intra-package import
pass  # [bundled] resolved intra-package import


@dataclass
class MeshData:
    vertices: np.ndarray      # float32, shape (V, 3), min Z == 0.0, centered at X=0, Y=0
    triangles: np.ndarray     # int32, shape (F, 3), outward CCW winding (right-hand rule)
    face_normals: np.ndarray  # float32, shape (F, 3), unit normals
    bounds_mm: dict[str, list[float]]  # {"min": [x,y,z], "max": [x,y,z], "size": [dx,dy,dz]}
    volume_cm3: float


# ---------------------------------------------------------------------------
# Section 2: Shared Mathematical Surface Evaluation (Python <-> WebGL2 Parity)
# ---------------------------------------------------------------------------

def _smoothstep(edge0: float, edge1: float, x: np.ndarray) -> np.ndarray:
    span = edge1 - edge0
    if span <= 1e-9:
        return np.where(x > edge0, 1.0, 0.0)
    u = np.clip((x - edge0) / span, 0.0, 1.0)
    return u * u * (3.0 - 2.0 * u)


def _prepare_knots(params: dict[str, Any]) -> tuple[np.ndarray, np.ndarray]:
    if params["use_custom_profile"]:
        raw = [[float(p[0]), float(p[1])] for p in params["profile_points"]]
    else:
        r_base = 0.5 * float(params["base_diameter_mm"])
        r_belly = 0.5 * float(params["belly_diameter_mm"])
        r_waist = 0.5 * float(params["waist_diameter_mm"])
        r_neck = 0.5 * float(params["neck_diameter_mm"])
        r_lip = max(4.0, r_neck + float(params["lip_flare_mm"]))
        raw = [
            [0.0, r_base],
            [float(params["belly_height_ratio"]), r_belly],
            [float(params["waist_height_ratio"]), r_waist],
            [0.92, r_neck],
            [1.0, r_lip],
        ]

    raw.sort(key=lambda pair: pair[0])
    raw[0][0] = 0.0
    raw[-1][0] = 1.0

    # Ensure strictly increasing z_norm knots so PCHIP never divides by zero
    dedup: list[list[float]] = [raw[0]]
    for z_k, r_k in raw[1:]:
        if z_k - dedup[-1][0] < 1e-4:
            if z_k >= 1.0:
                dedup[-1] = [1.0, r_k]
            else:
                dedup[-1][1] = 0.5 * (dedup[-1][1] + r_k)
        else:
            dedup.append([z_k, r_k])

    if len(dedup) < 2:
        dedup = [[0.0, raw[0][1]], [1.0, raw[-1][1]]]

    xs = np.array([p[0] for p in dedup], dtype=np.float64)
    ys = np.array([p[1] for p in dedup], dtype=np.float64)
    return xs, ys


def _pchip_interpolate(xs: np.ndarray, ys: np.ndarray, x_eval: np.ndarray) -> np.ndarray:
    """Monotone Piecewise Cubic Hermite Interpolating Polynomial (Fritsch-Carlson / PCHIP)."""
    m = len(xs)
    if m == 2:
        t = np.clip((x_eval - xs[0]) / max(xs[1] - xs[0], 1e-9), 0.0, 1.0)
        return ys[0] + t * (ys[1] - ys[0])

    h = np.diff(xs)
    delta = np.diff(ys) / h
    d = np.zeros(m, dtype=np.float64)

    # Interior slopes: weighted harmonic mean when adjacent secants share sign
    for k in range(1, m - 1):
        if delta[k - 1] * delta[k] > 0.0:
            w1 = 2.0 * h[k] + h[k - 1]
            w2 = h[k] + 2.0 * h[k - 1]
            d[k] = (w1 + w2) / (w1 / delta[k - 1] + w2 / delta[k])
        else:
            d[k] = 0.0

    # Shape-preserving endpoint slopes
    d0 = ((2.0 * h[0] + h[1]) * delta[0] - h[0] * delta[1]) / (h[0] + h[1])
    if d0 * delta[0] <= 0.0:
        d0 = 0.0
    elif (delta[0] * delta[1] <= 0.0) and (abs(d0) > abs(3.0 * delta[0])):
        d0 = 3.0 * delta[0]
    d[0] = d0

    dn = ((2.0 * h[-1] + h[-2]) * delta[-1] - h[-1] * delta[-2]) / (h[-1] + h[-2])
    if dn * delta[-1] <= 0.0:
        dn = 0.0
    elif (delta[-1] * delta[-2] <= 0.0) and (abs(dn) > abs(3.0 * delta[-1])):
        dn = 3.0 * delta[-1]
    d[-1] = dn

    x_clamped = np.clip(x_eval, xs[0], xs[-1])
    idx = np.searchsorted(xs, x_clamped, side="right") - 1
    idx = np.clip(idx, 0, m - 2)

    hk = h[idx]
    t = (x_clamped - xs[idx]) / hk
    t2 = t * t
    t3 = t2 * t

    h00 = 2.0 * t3 - 3.0 * t2 + 1.0
    h10 = t3 - 2.0 * t2 + t
    h01 = -2.0 * t3 + 3.0 * t2
    h11 = t3 - t2

    return h00 * ys[idx] + h10 * hk * d[idx] + h01 * ys[idx + 1] + h11 * hk * d[idx + 1]


def _hash3_u32(ix: np.ndarray, iy: np.ndarray, iz: np.ndarray, seed: int) -> np.ndarray:
    """Deterministic 32-bit integer hash matching JS Math.imul bit-for-bit."""
    ux = ix.astype(np.int64).astype(np.uint32)
    uy = iy.astype(np.int64).astype(np.uint32)
    uz = iz.astype(np.int64).astype(np.uint32)
    us = np.uint32(int(seed) & 0xFFFFFFFF)

    with np.errstate(over="ignore"):
        h = (
            ux * np.uint32(374761393)
            + uy * np.uint32(668265263)
            + uz * np.uint32(1274126177)
            + us * np.uint32(1597334677)
        )
        h = h ^ (h >> np.uint32(13))
        h = h * np.uint32(1274126177)
        h = h ^ (h >> np.uint32(16))

    return h.astype(np.float64) / 4294967295.0


def _value_noise_3d(cx: np.ndarray, cy: np.ndarray, cz: np.ndarray, octaves: int, seed: int) -> np.ndarray:
    total = np.zeros_like(cx, dtype=np.float64)
    amp_sum = 0.0
    freq = 1.0
    amp = 1.0

    for oct_idx in range(max(1, int(octaves))):
        x = cx * freq
        y = cy * freq
        z = cz * freq

        ix0 = np.floor(x).astype(np.int64)
        iy0 = np.floor(y).astype(np.int64)
        iz0 = np.floor(z).astype(np.int64)

        fx = x - ix0
        fy = y - iy0
        fz = z - iz0

        ux = fx * fx * (3.0 - 2.0 * fx)
        uy = fy * fy * (3.0 - 2.0 * fy)
        uz = fz * fz * (3.0 - 2.0 * fz)

        s_oct = int(seed)
        c000 = _hash3_u32(ix0, iy0, iz0, s_oct)
        c100 = _hash3_u32(ix0 + 1, iy0, iz0, s_oct)
        c010 = _hash3_u32(ix0, iy0 + 1, iz0, s_oct)
        c110 = _hash3_u32(ix0 + 1, iy0 + 1, iz0, s_oct)
        c001 = _hash3_u32(ix0, iy0, iz0 + 1, s_oct)
        c101 = _hash3_u32(ix0 + 1, iy0, iz0 + 1, s_oct)
        c011 = _hash3_u32(ix0, iy0 + 1, iz0 + 1, s_oct)
        c111 = _hash3_u32(ix0 + 1, iy0 + 1, iz0 + 1, s_oct)

        nx00 = c000 + ux * (c100 - c000)
        nx10 = c010 + ux * (c110 - c010)
        nx01 = c001 + ux * (c101 - c001)
        nx11 = c011 + ux * (c111 - c011)

        nxy0 = nx00 + uy * (nx10 - nx00)
        nxy1 = nx01 + uy * (nx11 - nx01)

        n_val = nxy0 + uz * (nxy1 - nxy0)
        total += amp * n_val
        amp_sum += amp
        freq *= 2.0
        amp *= 0.5

    return total / max(amp_sum, 1e-9)


def _compute_texture_displacement(
    z_grid: np.ndarray,
    z_norm_grid: np.ndarray,
    theta_grid: np.ndarray,
    theta_g: np.ndarray,
    textures: dict[str, Any],
    global_twist_rad: float,
) -> np.ndarray:
    dr = np.zeros_like(theta_g, dtype=np.float64)

    rib = textures["ribbed"]
    if rib["enabled"] and abs(rib["depth_mm"]) > 1e-9:
        count = float(rib["count"])
        duty = float(rib["duty_cycle"])
        sharp = float(rib["sharpness"])
        twist_rad = math.radians(float(rib["twist_deg"]))
        phase_rad = math.radians(float(rib["phase_deg"]))

        phi = np.mod((theta_grid + twist_rad * z_norm_grid + phase_rad) * count / (2.0 * math.pi), 1.0)
        u = np.abs(phi - 0.5) * 2.0
        t = np.clip(u / max(duty, 1e-6), 0.0, 1.0)
        w_smooth = 0.5 * (1.0 + np.cos(math.pi * t))
        w_sharp = 1.0 - t
        shape = (1.0 - sharp) * w_smooth + sharp * w_sharp
        dr += float(rib["depth_mm"]) * shape

    wav = textures["waves"]
    if wav["enabled"] and abs(wav["depth_mm"]) > 1e-9:
        wl = max(float(wav["vertical_wavelength_mm"]), 1.0)
        lobes = float(wav["angular_lobes"])
        mix = float(wav["interference_mix"])
        skew = float(wav["wave_skew"])
        phase_rad = math.radians(float(wav["phase_deg"]))

        kz = (2.0 * math.pi * z_grid / wl) + phase_rad
        ka = lobes * theta_grid + global_twist_rad * z_norm_grid
        w1 = np.sin(kz + ka + skew * np.sin(kz))
        w2 = np.sin(kz - ka)
        dr += float(wav["depth_mm"]) * ((1.0 - 0.5 * mix) * w1 + 0.5 * mix * w2)

    ori = textures["origami"]
    if ori["enabled"] and abs(ori["depth_mm"]) > 1e-9:
        c_around = float(ori["cells_around"])
        c_vert = float(ori["cells_vertical"])
        crease = float(ori["crease_sharpness"])
        stagger = float(ori["stagger"])

        v = z_norm_grid * c_vert
        tier = np.floor(v)
        fv = v - tier
        u = (theta_grid / (2.0 * math.pi)) * c_around + tier * stagger
        fu = u - np.floor(u)

        diamond = 1.0 - (np.abs(2.0 * fu - 1.0) + np.abs(2.0 * fv - 1.0))
        soft = np.sin(math.pi * (fu - 0.5)) * np.sin(math.pi * (fv - 0.5))
        val = crease * diamond + (1.0 - crease) * soft
        dr += float(ori["depth_mm"]) * val

    cel = textures["cellular"]
    if cel["enabled"] and abs(cel["depth_mm"]) > 1e-9:
        s_ang = float(cel["scale_angular"])
        s_vert = max(float(cel["scale_vertical_mm"]), 1.0)
        octaves = int(cel["octaves"])
        seed = int(cel["seed"])
        ridge = bool(cel["ridge_mode"])

        cyl_scale = s_ang / (2.0 * math.pi) * 4.0
        cx = np.cos(theta_g) * cyl_scale
        cy = np.sin(theta_g) * cyl_scale
        cz = z_grid / s_vert

        n = _value_noise_3d(cx, cy, cz, octaves, seed)
        val = (1.0 - 2.0 * np.abs(n - 0.5)) if ridge else (2.0 * (n - 0.5))
        dr += float(cel["depth_mm"]) * val

    geo = textures.get("geometric")
    if geo and geo["enabled"] and abs(geo["depth_mm"]) > 1e-9:
        dr += geometric_displacement(z_norm_grid, theta_g, geo)

    return dr


def evaluate_radius_grid(
    params: dict[str, Any],
    n_z: int | None = None,
    n_theta: int | None = None,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Evaluate outer vase surface radius grid (z_vals, theta_vals, radii_grid)."""
    p = normalize_params(params)
    nz = max(2, int(n_z)) if n_z is not None else int(p["resolution_vertical"])
    nt = max(3, int(n_theta)) if n_theta is not None else int(p["resolution_angular"])

    height_mm = float(p["height_mm"])
    z_vals = np.linspace(0.0, height_mm, nz, dtype=np.float64)
    z_norm = z_vals / height_mm
    theta_vals = np.linspace(0.0, 2.0 * math.pi, nt, endpoint=False, dtype=np.float64)

    # 1. Base silhouette R_base(z_norm) via monotone PCHIP
    knot_x, knot_r = _prepare_knots(p)
    r_base_1d = _pchip_interpolate(knot_x, knot_r, z_norm)

    z_grid = z_vals[:, None]
    z_norm_grid = z_norm[:, None]
    theta_grid = theta_vals[None, :]

    global_twist_rad = math.radians(float(p["global_twist_deg"]))
    theta_g = theta_grid + global_twist_rad * z_norm_grid

    # 2. Polygonal cross-section factor
    n_sides = int(p["polygon_sides"])
    if n_sides >= 3:
        alpha = math.pi / float(n_sides)
        two_alpha = 2.0 * alpha
        sector = np.mod(np.mod(theta_g, two_alpha) + two_alpha, two_alpha) - alpha
        poly_scale = math.cos(alpha) / np.cos(sector)
        roundness = float(p["polygon_roundness"])
        r_prof = r_base_1d[:, None] * ((1.0 - roundness) * poly_scale + roundness * 1.0)
    else:
        r_prof = np.broadcast_to(r_base_1d[:, None], (nz, nt)).copy()

    # 3. Vertical texture fade envelope E(z) (forced 0.0 at z == 0 for flat bed contact)
    bfade = float(p["bottom_fade_mm"])
    tfade = float(p["top_fade_mm"])
    if bfade <= 0.01:
        e_bot = np.where(z_vals > 1e-9, 1.0, 0.0)
    else:
        e_bot = _smoothstep(0.0, bfade, z_vals)
        e_bot[0] = 0.0

    if tfade <= 0.01:
        e_top = np.ones_like(z_vals)
    else:
        e_top = _smoothstep(0.0, tfade, height_mm - z_vals)

    env = (e_bot * e_top)[:, None]

    # 4. Combinable surface textures
    dr = _compute_texture_displacement(
        z_grid=z_grid,
        z_norm_grid=z_norm_grid,
        theta_grid=theta_grid,
        theta_g=theta_g,
        textures=p["textures"],
        global_twist_rad=global_twist_rad,
    )

    radii = np.maximum(6.0, r_prof + env * dr)

    # 5. Optional overhang slope clamping (2-pass 1D Lipschitz projection)
    if p["auto_clamp_overhang"] and nz >= 2:
        dz = height_mm / float(nz - 1)
        max_dr = dz * math.tan(math.radians(float(p["max_safe_overhang_deg"])))
        for i in range(nz - 1):
            radii[i + 1] = np.clip(radii[i + 1], radii[i] - max_dr, radii[i] + max_dr)
        for i in range(nz - 2, -1, -1):
            radii[i] = np.clip(radii[i], radii[i + 1] - max_dr, radii[i + 1] + max_dr)
        radii = np.maximum(6.0, radii)

    return z_vals, theta_vals, radii


# ---------------------------------------------------------------------------
# Watertight 2-Manifold Mesh Construction Primitives
# ---------------------------------------------------------------------------

class _MeshBuilder:
    """Collects indexed vertices and CCW outward-facing triangles."""

    def __init__(self) -> None:
        self._verts_chunks: list[np.ndarray] = []
        self._tris_chunks: list[np.ndarray] = []
        self._v_count: int = 0

    @property
    def vertex_count(self) -> int:
        return self._v_count

    def add_vertices(self, pts: np.ndarray) -> np.ndarray:
        arr = np.asarray(pts, dtype=np.float64)
        if arr.ndim == 1:
            arr = arr[None, :]
        n = arr.shape[0]
        start = self._v_count
        self._verts_chunks.append(arr)
        self._v_count += n
        return np.arange(start, start + n, dtype=np.int32)

    def add_vertex(self, x: float, y: float, z: float) -> int:
        idx = self._v_count
        self._verts_chunks.append(np.array([[x, y, z]], dtype=np.float64))
        self._v_count += 1
        return idx

    def add_polar_ring(self, radii: np.ndarray | float, thetas: np.ndarray, z: float | np.ndarray) -> np.ndarray:
        r_arr = np.broadcast_to(np.asarray(radii, dtype=np.float64), thetas.shape)
        z_arr = np.broadcast_to(np.asarray(z, dtype=np.float64), thetas.shape)
        pts = np.column_stack((r_arr * np.cos(thetas), r_arr * np.sin(thetas), z_arr))
        return self.add_vertices(pts)

    def add_circle_ring(self, cx: float, cy: float, radius: float, z: float, count: int) -> np.ndarray:
        phis = np.linspace(0.0, 2.0 * math.pi, count, endpoint=False, dtype=np.float64)
        pts = np.column_stack((cx + radius * np.cos(phis), cy + radius * np.sin(phis), np.full(count, z, dtype=np.float64)))
        return self.add_vertices(pts)

    def add_triangles(self, tris: np.ndarray) -> None:
        arr = np.asarray(tris, dtype=np.int32)
        if arr.size > 0:
            self._tris_chunks.append(arr.reshape(-1, 3))

    def add_quad_strip(self, ring_a: np.ndarray, ring_b: np.ndarray, reverse: bool = False) -> None:
        """Connect two equal-length closed CCW rings.

        With reverse=False, normal is (+dz * r_hat - dr * z_hat):
        - upward outer wall (dz > 0) -> outward (+r_hat)
        - inward top rim (dr < 0) -> upward (+z_hat)
        - downward inner cavity wall (dz < 0) -> inward (-r_hat)
        """
        a0 = ring_a
        a1 = np.roll(ring_a, -1)
        b0 = ring_b
        b1 = np.roll(ring_b, -1)
        if not reverse:
            t1 = np.column_stack((a0, a1, b1))
            t2 = np.column_stack((a0, b1, b0))
        else:
            t1 = np.column_stack((a0, b1, a1))
            t2 = np.column_stack((a0, b0, b1))
        self.add_triangles(np.vstack((t1, t2)))

    def add_tube_grid(self, rings: list[np.ndarray], reverse: bool = False) -> None:
        """Vectorized quad-strip across an ordered sequence of equal-length rings."""
        arr = np.asarray(rings, dtype=np.int32)  # (S, M)
        a0 = arr[:-1, :]
        a1 = np.roll(a0, -1, axis=1)
        b0 = arr[1:, :]
        b1 = np.roll(b0, -1, axis=1)
        if not reverse:
            t1 = np.stack((a0, a1, b1), axis=-1).reshape(-1, 3)
            t2 = np.stack((a0, b1, b0), axis=-1).reshape(-1, 3)
        else:
            t1 = np.stack((a0, b1, a1), axis=-1).reshape(-1, 3)
            t2 = np.stack((a0, b0, b1), axis=-1).reshape(-1, 3)
        self.add_triangles(np.vstack((t1, t2)))

    def add_disk_fan(self, center_idx: int, ring: np.ndarray, normal_up: bool = True) -> None:
        m = len(ring)
        c = np.full(m, center_idx, dtype=np.int32)
        r0 = ring
        r1 = np.roll(ring, -1)
        if normal_up:
            tris = np.column_stack((c, r0, r1))
        else:
            tris = np.column_stack((c, r1, r0))
        self.add_triangles(tris)

    def get_vertices_array(self) -> np.ndarray:
        if not self._verts_chunks:
            return np.zeros((0, 3), dtype=np.float64)
        return np.vstack(self._verts_chunks)

    def build(self) -> MeshData:
        verts64 = self.get_vertices_array()
        tris = np.vstack(self._tris_chunks).astype(np.int32) if self._tris_chunks else np.zeros((0, 3), dtype=np.int32)

        # Anchor min Z cleanly at exact 0.0 in float32
        z_min = float(verts64[:, 2].min()) if len(verts64) else 0.0
        verts64[:, 2] -= z_min
        verts64[np.abs(verts64[:, 2]) < 1e-7, 2] = 0.0

        verts32 = verts64.astype(np.float32)
        if len(verts32):
            z_min32 = float(verts32[:, 2].min())
            if z_min32 != 0.0:
                verts32[:, 2] -= np.float32(z_min32)
            verts32[np.abs(verts32[:, 2]) < 1e-7, 2] = np.float32(0.0)

        # Compute exact face normals & signed volume from float32 vertex positions
        v0 = verts32[tris[:, 0]].astype(np.float64)
        v1 = verts32[tris[:, 1]].astype(np.float64)
        v2 = verts32[tris[:, 2]].astype(np.float64)

        cross = np.cross(v1 - v0, v2 - v0)
        norms = np.linalg.norm(cross, axis=1, keepdims=True)
        face_normals = (cross / np.maximum(norms, 1e-30)).astype(np.float32)

        signed_vol_mm3 = float(np.sum(np.einsum("ij,ij->i", v0, cross)) / 6.0)
        volume_cm3 = signed_vol_mm3 / 1000.0

        vmin = verts32.min(axis=0)
        vmax = verts32.max(axis=0)
        vsize = vmax - vmin
        bounds_mm = {
            "min": [float(vmin[0]), float(vmin[1]), float(vmin[2])],
            "max": [float(vmax[0]), float(vmax[1]), float(vmax[2])],
            "size": [float(vsize[0]), float(vsize[1]), float(vsize[2])],
        }

        return MeshData(
            vertices=verts32,
            triangles=tris,
            face_normals=face_normals,
            bounds_mm=bounds_mm,
            volume_cm3=float(volume_cm3),
        )


def _bridge_closed_loops_up(
    verts_xy: np.ndarray,
    loop_in: list[int] | np.ndarray,
    loop_out: list[int] | np.ndarray,
    center_xy: tuple[float, float],
) -> np.ndarray:
    """Triangulate the annular region between two star-shaped closed CCW loops (normal +Z).

    Guarantees:
    - Outer loop edges emitted once as (O_q, O_{q+1})
    - Inner loop edges emitted once as (I_{p+1}, I_p)
    - Every internal spoke emitted once forward and once backward (strict 2-manifold)
    """
    lin = [int(i) for i in loop_in]
    lout = [int(i) for i in loop_out]
    m1 = len(lin)
    m2 = len(lout)
    cx, cy = center_xy

    ang_in: list[float] = []
    for p, idx in enumerate(lin):
        a = math.atan2(float(verts_xy[idx, 1]) - cy, float(verts_xy[idx, 0]) - cx)
        if p > 0:
            while a <= ang_in[-1]:
                a += 2.0 * math.pi
        ang_in.append(a)
    ang_in.append(ang_in[0] + 2.0 * math.pi)

    raw_out = [
        math.atan2(float(verts_xy[idx, 1]) - cy, float(verts_xy[idx, 0]) - cx)
        for idx in lout
    ]
    best_s = min(
        range(m2),
        key=lambda s: abs(((raw_out[s] - ang_in[0] + math.pi) % (2.0 * math.pi)) - math.pi),
    )
    lout = lout[best_s:] + lout[:best_s]

    a0 = math.atan2(float(verts_xy[lout[0], 1]) - cy, float(verts_xy[lout[0], 0]) - cx)
    while a0 - ang_in[0] > math.pi:
        a0 -= 2.0 * math.pi
    while ang_in[0] - a0 > math.pi:
        a0 += 2.0 * math.pi

    ang_out: list[float] = [a0]
    for q in range(1, m2):
        idx = lout[q]
        a = math.atan2(float(verts_xy[idx, 1]) - cy, float(verts_xy[idx, 0]) - cx)
        while a <= ang_out[-1]:
            a += 2.0 * math.pi
        ang_out.append(a)
    ang_out.append(ang_out[0] + 2.0 * math.pi)

    tris: list[tuple[int, int, int]] = []
    p = 0
    q = 0

    while p < m1 or q < m2:
        if p == m1:
            advance_out = True
        elif q == m2:
            advance_out = False
        else:
            skew_if_in = abs(ang_in[p + 1] - ang_out[q])
            skew_if_out = abs(ang_out[q + 1] - ang_in[p])
            advance_out = skew_if_out < skew_if_in

        if advance_out:
            tris.append((lin[p % m1], lout[q % m2], lout[(q + 1) % m2]))
            q += 1
        else:
            tris.append((lin[p % m1], lout[q % m2], lin[(p + 1) % m1]))
            p += 1

    return np.array(tris, dtype=np.int32)


def _drainage_zone_radii(r_avail: float) -> tuple[float, float]:
    """Return (r_collar, r_guard) strictly inside r_avail with guaranteed manifold margins."""
    r_av = max(2.2, float(r_avail))
    safe_margin = max(0.35, 0.10 * r_av)
    r_usable = max(1.2, r_av - safe_margin)
    r_guard = min(r_av - 0.15, max(r_usable + 0.10, r_av - 0.50 * safe_margin))
    r_collar = 0.92 * r_usable
    return r_collar, r_guard


def _compute_drainage_layout(
    drainage_cfg: dict[str, Any],
    r_avail: float,
) -> list[tuple[float, float, float]]:
    """Compute safe non-overlapping (cx, cy, r_hole) list for 1..9 holes inside r_avail."""
    k = int(drainage_cfg["hole_count"])
    req_r = 0.5 * float(drainage_cfg["hole_diameter_mm"])
    req_ratio = float(drainage_cfg["ring_radius_ratio"])
    r_collar, _ = _drainage_zone_radii(r_avail)

    if k <= 1:
        max_safe_r = 0.68 * r_collar
        r_h = max(0.20, min(req_r, max_safe_r))
        return [(0.0, 0.0, min(r_h, max_safe_r))]

    if k == 2:
        eff_ratio = req_ratio if req_ratio >= 0.15 else 0.45
        r_ring = min(max(0.36 * r_collar, eff_ratio * r_avail), 0.68 * r_collar)
        max_safe_r = 0.60 * min(r_ring, r_collar - r_ring)
        r_h = max(0.18, min(req_r, max_safe_r))
        r_h = min(r_h, max_safe_r)
        return [(r_ring, 0.0, r_h), (-r_ring, 0.0, r_h)]

    eff_ratio = req_ratio if req_ratio >= 0.15 else 0.48
    r_ring = min(max(0.42 * r_collar, eff_ratio * r_avail), 0.72 * r_collar)
    dpsi = math.pi / float(k)
    r_hub = 0.32 * r_ring
    max_safe_r = 0.60 * min(r_ring * math.sin(dpsi), r_ring - r_hub, r_collar - r_ring)
    r_h = max(0.18, min(req_r, max_safe_r))
    r_h = min(r_h, max_safe_r)

    holes: list[tuple[float, float, float]] = []
    for c in range(k):
        psi = 2.0 * math.pi * float(c) / float(k)
        holes.append((r_ring * math.cos(psi), r_ring * math.sin(psi), r_h))
    return holes


def _add_planar_disk_with_holes(
    mb: _MeshBuilder,
    outer_ring: np.ndarray,
    z_plane: float,
    holes: list[tuple[float, float, float]],
    r_avail: float,
    normal_up: bool,
    m_hole: int = 32,
) -> list[np.ndarray]:
    """Triangulate a planar disk bounded by outer_ring with 0..9 circular holes.

    Uses a radial polar guard ring + strictly convex sector decomposition + loop bridging
    so zero triangles can flip or degenerate even on sharp polygonal/textured profiles
    or 25 mm walls with 9 holes, and every shared edge is traversed once in each direction.
    """
    k = len(holes)
    if k == 0:
        c_idx = mb.add_vertex(0.0, 0.0, z_plane)
        mb.add_disk_fan(c_idx, outer_ring, normal_up=normal_up)
        return []

    r_collar, r_guard = _drainage_zone_radii(r_avail)

    # Project outer_ring radially onto a pure circular guard_ring at r_guard < r_avail
    verts_init = mb.get_vertices_array()
    outer_xy = verts_init[outer_ring, :2]
    outer_norms = np.maximum(np.hypot(outer_xy[:, 0], outer_xy[:, 1]), 1e-9)
    guard_pts = np.column_stack((
        (r_guard / outer_norms) * outer_xy[:, 0],
        (r_guard / outer_norms) * outer_xy[:, 1],
        np.full(len(outer_ring), z_plane, dtype=np.float64),
    ))
    guard_ring = mb.add_vertices(guard_pts)

    o0 = np.asarray(outer_ring, dtype=np.int32)
    o1 = np.roll(o0, -1)
    g0 = guard_ring
    g1 = np.roll(g0, -1)

    hole_rings: list[np.ndarray] = [
        mb.add_circle_ring(cx, cy, rh, z_plane, m_hole)
        for (cx, cy, rh) in holes
    ]

    tris_list: list[np.ndarray] = [
        np.vstack((
            np.column_stack((o0, o1, g1)),
            np.column_stack((o0, g1, g0)),
        ))
    ]

    if k == 1:
        verts_xy = mb.get_vertices_array()[:, :2]
        cx, cy, _ = holes[0]
        tris_list.append(_bridge_closed_loops_up(verts_xy, hole_rings[0], guard_ring, (cx, cy)))

    elif k == 2:
        m_semi = 24
        n_diam = 16
        bot_pole = mb.add_vertex(0.0, -r_collar, z_plane)
        top_pole = mb.add_vertex(0.0, r_collar, z_plane)

        right_angs = np.linspace(-0.5 * math.pi, 0.5 * math.pi, m_semi + 1, dtype=np.float64)[1:-1]
        right_semi = mb.add_vertices(
            np.column_stack((r_collar * np.cos(right_angs), r_collar * np.sin(right_angs), np.full(len(right_angs), z_plane)))
        )

        left_angs = np.linspace(0.5 * math.pi, 1.5 * math.pi, m_semi + 1, dtype=np.float64)[1:-1]
        left_semi = mb.add_vertices(
            np.column_stack((r_collar * np.cos(left_angs), r_collar * np.sin(left_angs), np.full(len(left_angs), z_plane)))
        )

        diam_ys = np.linspace(-r_collar, r_collar, n_diam + 1, dtype=np.float64)[1:-1]
        diam_mid = mb.add_vertices(
            np.column_stack((np.zeros(len(diam_ys)), diam_ys, np.full(len(diam_ys), z_plane)))
        )

        # Right half-disk CCW around (+r_ring, 0)
        cell_0 = [bot_pole, *right_semi.tolist(), top_pole, *diam_mid[::-1].tolist()]
        # Left half-disk CCW around (-r_ring, 0)
        cell_1 = [top_pole, *left_semi.tolist(), bot_pole, *diam_mid.tolist()]
        # Full collar loop CCW around (0, 0)
        collar_ring = [bot_pole, *right_semi.tolist(), top_pole, *left_semi.tolist()]

        verts_xy = mb.get_vertices_array()[:, :2]
        tris_list.append(_bridge_closed_loops_up(verts_xy, hole_rings[0], cell_0, (holes[0][0], holes[0][1])))
        tris_list.append(_bridge_closed_loops_up(verts_xy, hole_rings[1], cell_1, (holes[1][0], holes[1][1])))
        tris_list.append(_bridge_closed_loops_up(verts_xy, collar_ring, guard_ring, (0.0, 0.0)))

    else:
        r_ring = math.hypot(holes[0][0], holes[0][1])
        dpsi = math.pi / float(k)
        r_hub = 0.32 * r_ring

        n_spoke = 14
        n_chord = 6
        m_arc = max(12, int(round(64.0 / float(k))))

        spoke_angs = [2.0 * math.pi * float(c) / float(k) - dpsi for c in range(k)]
        spoke_radii = np.linspace(r_hub, r_collar, n_spoke + 1, dtype=np.float64)

        spokes: list[np.ndarray] = []
        for ang in spoke_angs:
            pts = np.column_stack((
                spoke_radii * math.cos(ang),
                spoke_radii * math.sin(ang),
                np.full(len(spoke_radii), z_plane),
            ))
            spokes.append(mb.add_vertices(pts))

        verts_so_far = mb.get_vertices_array()
        chord_interiors: list[np.ndarray] = []
        arc_interiors: list[np.ndarray] = []
        t_chord = np.linspace(0.0, 1.0, n_chord + 1, dtype=np.float64)[1:-1][:, None]
        for c in range(k):
            c_next = (c + 1) % k
            u0 = verts_so_far[spokes[c][0]]
            u1 = verts_so_far[spokes[c_next][0]]
            c_pts = u0[None, :] + t_chord * (u1 - u0)[None, :]
            c_pts[:, 2] = z_plane
            chord_interiors.append(mb.add_vertices(c_pts))

            ang0 = spoke_angs[c]
            ang1 = ang0 + 2.0 * dpsi
            a_pts = np.linspace(ang0, ang1, m_arc + 1, dtype=np.float64)[1:-1]
            arc_interiors.append(
                mb.add_vertices(
                    np.column_stack((r_collar * np.cos(a_pts), r_collar * np.sin(a_pts), np.full(len(a_pts), z_plane)))
                )
            )

        # Center hub k-gon fan (+Z first; flipped at end if not normal_up)
        hub_center = mb.add_vertex(0.0, 0.0, z_plane)
        hub_loop: list[int] = []
        for c in range(k):
            hub_loop.append(int(spokes[c][0]))
            hub_loop.extend(chord_interiors[c].tolist())
        hc = np.full(len(hub_loop), hub_center, dtype=np.int32)
        hr0 = np.array(hub_loop, dtype=np.int32)
        hr1 = np.roll(hr0, -1)
        tris_list.append(np.column_stack((hc, hr0, hr1)))

        collar_ring = []
        for c in range(k):
            collar_ring.append(int(spokes[c][-1]))
            collar_ring.extend(arc_interiors[c].tolist())

        verts_xy = mb.get_vertices_array()[:, :2]
        for c in range(k):
            c_next = (c + 1) % k
            cell_loop: list[int] = [
                *spokes[c][:-1].tolist(),              # U_c .. before W_c (outward)
                int(spokes[c][-1]),                    # W_c
                *arc_interiors[c].tolist(),            # collar arc CCW
                *spokes[c_next][::-1][:-1].tolist(),   # W_{c+1} .. before U_{c+1} (inward)
                int(spokes[c_next][0]),                # U_{c+1}
                *chord_interiors[c][::-1].tolist(),    # inner chord back toward U_c
            ]
            tris_list.append(
                _bridge_closed_loops_up(verts_xy, hole_rings[c], cell_loop, (holes[c][0], holes[c][1]))
            )

        tris_list.append(_bridge_closed_loops_up(verts_xy, collar_ring, guard_ring, (0.0, 0.0)))

    all_tris = np.vstack(tris_list)
    if not normal_up:
        all_tris = all_tris[:, [0, 2, 1]]
    mb.add_triangles(all_tris)
    return hole_rings


# ---------------------------------------------------------------------------
# Public Mesh Generators (Section 3)
# ---------------------------------------------------------------------------

def _generate_vase_body_mesh(params: dict[str, Any], layer_height_mm: float = 0.2) -> MeshData:
    """Generate a 100% closed, watertight 2-manifold vase mesh for spiral_vase or shelled_hollow."""
    p = normalize_params(params)
    lh = max(0.05, min(1.0, float(layer_height_mm)))
    z_vals, theta_vals, radii_grid = evaluate_radius_grid(p)
    nz, _ = radii_grid.shape
    height_mm = float(p["height_mm"])

    mb = _MeshBuilder()
    drain_cfg = p["drainage"]
    drain_enabled = bool(drain_cfg["enabled"])

    if p["print_mode"] == "spiral_vase":
        # Outer wall rings from Z = 0 to Z = height_mm
        outer_rings: list[np.ndarray] = [
            mb.add_polar_ring(radii_grid[i], theta_vals, float(z_vals[i]))
            for i in range(nz)
        ]
        mb.add_tube_grid(outer_rings, reverse=False)

        # Top solid cap at Z = height_mm (+Z normal)
        top_center = mb.add_vertex(0.0, 0.0, height_mm)
        mb.add_disk_fan(top_center, outer_rings[-1], normal_up=True)

        # Bottom cap at Z = 0.0 (-Z normal), with optional blind drainage cavities
        if not drain_enabled:
            bot_center = mb.add_vertex(0.0, 0.0, 0.0)
            mb.add_disk_fan(bot_center, outer_rings[0], normal_up=False)
        else:
            z_cap = min(
                float(p["spiral_bottom_layers"]) * lh + 0.30,
                0.34 * height_mm,
            )
            z_cap = max(0.45, z_cap)
            sub_cap_mask = z_vals <= (z_cap + 1e-3)
            r_avail = float(radii_grid[sub_cap_mask].min()) if np.any(sub_cap_mask) else float(radii_grid[0].min())
            holes = _compute_drainage_layout(drain_cfg, r_avail)
            bot_hole_rings = _add_planar_disk_with_holes(
                mb=mb,
                outer_ring=outer_rings[0],
                z_plane=0.0,
                holes=holes,
                r_avail=r_avail,
                normal_up=False,
            )
            m_hole = len(bot_hole_rings[0])
            for idx_h, (cx, cy, rh) in enumerate(holes):
                top_hole_ring = mb.add_circle_ring(cx, cy, rh, z_cap, m_hole)
                # Tunnel wall facing inward into blind cavity (reverse=True)
                mb.add_quad_strip(bot_hole_rings[idx_h], top_hole_ring, reverse=True)
                # Blind cavity ceiling facing -Z into cavity
                roof_center = mb.add_vertex(cx, cy, z_cap)
                mb.add_disk_fan(roof_center, top_hole_ring, normal_up=False)

        return mb.build()

    # Mode 2: shelled_hollow (true thick-walled hollow shell with optional lip bevel & through-drainage)
    wall_t = float(p["wall_thickness_mm"])
    effective_bottom = min(float(p["bottom_thickness_mm"]), height_mm * 0.65)
    z_floor = max(1.0, effective_bottom)

    if nz >= 5:
        r_for_slope = (
            0.25 * np.vstack((radii_grid[0:1], radii_grid[:-1]))
            + 0.50 * radii_grid
            + 0.25 * np.vstack((radii_grid[1:], radii_grid[-1:]))
        )
    else:
        r_for_slope = radii_grid
    slope_z = np.gradient(r_for_slope, z_vals, axis=0)
    slope_z = np.clip(slope_z, -1.75, 1.75)
    extra_radial = np.minimum(wall_t * (np.sqrt(1.0 + slope_z * slope_z) - 1.0), 8.0)
    radial_wall = wall_t + extra_radial

    # Smooth C1 clamp above min_inner_r = 3.0 mm so narrow waists with 25 mm walls never invert or crease
    min_inner_r = 3.0
    min_wall_gap = min(0.65, 0.80 * wall_t)
    delta_in = (radii_grid - radial_wall) - min_inner_r
    inner_grid = min_inner_r + 0.5 * (delta_in + np.sqrt(delta_in * delta_in + 0.16))
    inner_grid = np.minimum(inner_grid, radii_grid - min_wall_gap)
    inner_grid = np.maximum(min_inner_r, inner_grid)

    if p["auto_clamp_overhang"] and nz >= 2:
        dz = height_mm / float(nz - 1)
        max_dr = dz * math.tan(math.radians(float(p["max_safe_overhang_deg"])))
        for i in range(nz - 1):
            inner_grid[i + 1] = np.clip(inner_grid[i + 1], inner_grid[i] - max_dr, inner_grid[i] + max_dr)
        for i in range(nz - 2, -1, -1):
            inner_grid[i] = np.clip(inner_grid[i], inner_grid[i + 1] - max_dr, inner_grid[i + 1] + max_dr)
        inner_grid = np.minimum(inner_grid, radii_grid - min_wall_gap)
        inner_grid = np.maximum(min_inner_r, inner_grid)

    # Determine safe lip bevel radius
    top_wall_span = float(np.min(radii_grid[-1] - inner_grid[-1]))
    bevel = min(
        float(p["lip_bevel_mm"]),
        0.42 * max(0.0, top_wall_span),
        0.15 * (height_mm - z_floor),
    )

    profile_rings: list[np.ndarray] = []

    if bevel > 0.08:
        z_lip_base = height_mm - bevel
        # Outer wall up to z_lip_base (keep >= 0.05 mm Z margin so adjacent rings never quantize-collapse)
        outer_mask = z_vals < (z_lip_base - 0.05)
        for i in np.nonzero(outer_mask)[0]:
            profile_rings.append(mb.add_polar_ring(radii_grid[i], theta_vals, float(z_vals[i])))

        # Interpolate outer & inner radii cleanly at z_lip_base
        r_out_lip = np.array([np.interp(z_lip_base, z_vals, radii_grid[:, j]) for j in range(len(theta_vals))])
        r_in_lip = np.array([np.interp(z_lip_base, z_vals, inner_grid[:, j]) for j in range(len(theta_vals))])
        r_in_lip = np.minimum(r_in_lip, r_out_lip - min_wall_gap)
        r_in_lip = np.maximum(min_inner_r, r_in_lip)

        r_mid = 0.5 * (r_out_lip + r_in_lip)
        half_w = 0.5 * (r_out_lip - r_in_lip)

        # Semicircular lip arch peaking at exact Z = height_mm (gamma = pi/2)
        for gamma in (0.0, 0.25 * math.pi, 0.5 * math.pi, 0.75 * math.pi, math.pi):
            z_a = height_mm if abs(gamma - 0.5 * math.pi) < 1e-9 else (z_lip_base + bevel * math.sin(gamma))
            r_a = r_mid + half_w * math.cos(gamma)
            profile_rings.append(mb.add_polar_ring(r_a, theta_vals, z_a))

        z_inner_top = z_lip_base
    else:
        for i in range(nz):
            profile_rings.append(mb.add_polar_ring(radii_grid[i], theta_vals, float(z_vals[i])))
        profile_rings.append(mb.add_polar_ring(inner_grid[-1], theta_vals, height_mm))
        z_inner_top = height_mm

    # Inner cavity wall descending from below z_inner_top down to z_floor
    inner_mask = (z_vals < z_inner_top - 0.05) & (z_vals > z_floor + 0.05)
    for i in np.nonzero(inner_mask)[0][::-1]:
        profile_rings.append(mb.add_polar_ring(inner_grid[i], theta_vals, float(z_vals[i])))

    r_in_floor = np.array([np.interp(z_floor, z_vals, inner_grid[:, j]) for j in range(len(theta_vals))])
    r_in_floor = np.maximum(min_inner_r, r_in_floor)
    profile_rings.append(mb.add_polar_ring(r_in_floor, theta_vals, z_floor))

    # Connect continuous meridian revolution (outer wall -> lip -> inner cavity wall)
    mb.add_tube_grid(profile_rings, reverse=False)

    outer_bot_ring = profile_rings[0]
    inner_floor_ring = profile_rings[-1]

    if not drain_enabled:
        bot_center = mb.add_vertex(0.0, 0.0, 0.0)
        mb.add_disk_fan(bot_center, outer_bot_ring, normal_up=False)

        floor_center = mb.add_vertex(0.0, 0.0, z_floor)
        mb.add_disk_fan(floor_center, inner_floor_ring, normal_up=True)
    else:
        sub_floor_mask = z_vals <= (z_floor + 1e-3)
        min_outer_below_floor = (
            float(radii_grid[sub_floor_mask].min())
            if np.any(sub_floor_mask)
            else float(radii_grid[0].min())
        )
        r_avail = max(min_inner_r, float(min(min_outer_below_floor - min_wall_gap, r_in_floor.min())))
        holes = _compute_drainage_layout(drain_cfg, r_avail)

        bot_hole_rings = _add_planar_disk_with_holes(
            mb=mb,
            outer_ring=outer_bot_ring,
            z_plane=0.0,
            holes=holes,
            r_avail=r_avail,
            normal_up=False,
        )
        top_hole_rings = _add_planar_disk_with_holes(
            mb=mb,
            outer_ring=inner_floor_ring,
            z_plane=z_floor,
            holes=holes,
            r_avail=r_avail,
            normal_up=True,
        )
        for idx_h in range(len(holes)):
            mb.add_quad_strip(bot_hole_rings[idx_h], top_hole_rings[idx_h], reverse=True)

    return mb.build()


def generate_vase_mesh(params: dict[str, Any], layer_height_mm: float = 0.2) -> MeshData:
    """Generate the vase, or the reference-style cup plus closed curled ribbons.

    Ribbons and cup deliberately retain separate indexed boundaries; overlaps
    are not reported as a Boolean union or unique material volume.
    """
    p = normalize_params(params)
    g = p["textures"]["geometric"]
    if not (g["enabled"] and g["pattern"] == "folded_petals"):
        return _generate_vase_body_mesh(p, layer_height_mm)
    plan = ribbon_plan(p)
    if plan["triangles"] > 3_000_000:
        raise ValueError("Ribbon mesh is too large. Reduce ribbon count or choose a lower ribbon quality.")
    _, _, radii = evaluate_radius_grid(p, n_z=plan["nz"] + 1, n_theta=3)
    if float(radii.min()) - p["wall_thickness_mm"] <= 2:
        raise ValueError("The cup is too narrow for its wall. Increase the profile diameter or reduce wall thickness.")
    cup = _generate_vase_body_mesh(p, layer_height_mm)
    verts, tris = build_ribbon_mesh(p, radii[:, 0])
    builder = _MeshBuilder()
    builder.add_vertices(cup.vertices)
    builder.add_triangles(cup.triangles)
    start = builder.vertex_count
    builder.add_vertices(verts)
    builder.add_triangles(tris + start)
    return builder.build()


def generate_saucer_mesh(params: dict[str, Any]) -> MeshData:
    """Generate a watertight 2-manifold matching plant saucer tray centered at (0, 0), min(Z) == 0.0."""
    p = normalize_params(params)
    sc = p["saucer"]

    nt = max(96, min(240, int(p["resolution_angular"])))
    theta_vals = np.linspace(0.0, 2.0 * math.pi, nt, endpoint=False, dtype=np.float64)

    # Account for custom profile or polygonal vase base radius so the vase always fits comfortably
    _, _, vase_base_radii = evaluate_radius_grid(p, n_z=12, n_theta=nt)
    vase_foot_radius = max(0.5 * float(p["base_diameter_mm"]), float(vase_base_radii[0].max()))

    r_saucer_inner = vase_foot_radius + float(sc["clearance_mm"])
    rim_h = float(sc["rim_height_mm"])
    wall_t = float(sc["wall_thickness_mm"])
    floor_t = min(float(sc["floor_thickness_mm"]), rim_h - 3.0)
    floor_t = max(1.2, floor_t)
    ribs_h = min(float(sc["inner_ribs_height_mm"]), 0.45 * (rim_h - floor_t))
    ribs_h = max(0.0, ribs_h)

    flare_tan = math.tan(math.radians(12.0))
    n_wall = 28
    z_out = np.linspace(0.0, rim_h, n_wall, dtype=np.float64)
    z_out_norm = z_out / max(rim_h, 1.0)

    r_out_base = (r_saucer_inner + wall_t) + z_out * flare_tan
    r_out_grid = np.broadcast_to(r_out_base[:, None], (n_wall, nt)).copy()

    # Optional matching outer vase texture with clean bed/rim fade
    if sc["match_vase_texture"]:
        e_bot = _smoothstep(0.0, min(3.5, 0.25 * rim_h), z_out)
        e_bot[0] = 0.0
        e_top = _smoothstep(0.0, min(3.0, 0.22 * rim_h), rim_h - z_out)
        env = (e_bot * e_top)[:, None]

        twist_rad = math.radians(float(p["global_twist_deg"])) * 0.25
        theta_g = theta_vals[None, :] + twist_rad * z_out_norm[:, None]
        dr_tex = _compute_texture_displacement(
            z_grid=z_out[:, None],
            z_norm_grid=z_out_norm[:, None],
            theta_grid=theta_vals[None, :],
            theta_g=theta_g,
            textures=p["textures"],
            global_twist_rad=twist_rad,
        )
        max_tex = 0.45 * wall_t
        r_out_grid += env * np.clip(0.40 * dr_tex, -max_tex, max_tex)

    mb = _MeshBuilder()
    rings: list[np.ndarray] = []

    # 1. Outer flared wall from Z = 0 up to Z = rim_h - bevel
    lip_r = 0.5 * wall_t
    z_arch_base = max(floor_t + 1.0, rim_h - lip_r)
    for i in range(n_wall):
        if z_out[i] < z_arch_base - 1e-4:
            rings.append(mb.add_polar_ring(r_out_grid[i], theta_vals, float(z_out[i])))

    # 2. Smooth rounded top rim peaking at exact Z = rim_h
    r_outer_top = np.array([np.interp(z_arch_base, z_out, r_out_grid[:, j]) for j in range(nt)])
    r_inner_top = np.full(nt, r_saucer_inner + (z_arch_base - floor_t) * flare_tan, dtype=np.float64)
    r_inner_top = np.minimum(r_inner_top, r_outer_top - 0.6)

    r_mid = 0.5 * (r_outer_top + r_inner_top)
    half_w = 0.5 * (r_outer_top - r_inner_top)
    arch_h = rim_h - z_arch_base
    for gamma in (0.0, 0.25 * math.pi, 0.5 * math.pi, 0.75 * math.pi, math.pi):
        z_a = rim_h if abs(gamma - 0.5 * math.pi) < 1e-9 else (z_arch_base + arch_h * math.sin(gamma))
        r_a = r_mid + half_w * math.cos(gamma)
        rings.append(mb.add_polar_ring(r_a, theta_vals, z_a))

    # 3. Inner flared wall descending to inner floor edge (r_saucer_inner, floor_t)
    n_in_wall = 16
    z_in = np.linspace(z_arch_base, floor_t, n_in_wall, dtype=np.float64)[1:]
    for zv in z_in:
        r_v = r_saucer_inner + (zv - floor_t) * flare_tan
        rings.append(mb.add_polar_ring(r_v, theta_vals, float(zv)))

    # 4. Inner floor radial rings with raised drainage ribs so the pot sits above water
    n_floor_rings = 22
    r_floor_vals = np.linspace(r_saucer_inner, 0.06 * r_saucer_inner, n_floor_rings, dtype=np.float64)[1:]
    n_ribs = 8
    rib_ang_profile = np.maximum(0.0, np.cos(float(n_ribs) * theta_vals)) ** 2

    for rv in r_floor_vals:
        if ribs_h > 1e-4:
            u_rad = np.clip((rv - 0.16 * r_saucer_inner) / max(0.70 * r_saucer_inner, 1e-6), 0.0, 1.0)
            rib_env = math.sin(math.pi * float(u_rad)) ** 2
            z_ring = floor_t + ribs_h * rib_env * rib_ang_profile
        else:
            z_ring = floor_t
        rings.append(mb.add_polar_ring(rv, theta_vals, z_ring))

    mb.add_tube_grid(rings, reverse=False)

    # Bottom flat cap at Z = 0 (-Z normal) & inner floor center fan (+Z normal)
    bot_center = mb.add_vertex(0.0, 0.0, 0.0)
    mb.add_disk_fan(bot_center, rings[0], normal_up=False)

    top_center = mb.add_vertex(0.0, 0.0, floor_t)
    mb.add_disk_fan(top_center, rings[-1], normal_up=True)

    return mb.build()

# ===========================================================================
# MODULE: vase_studio.printability
# ===========================================================================

"""Printability, overhang, bed-fit, and filament weight analysis for Orca Vase Studio."""

pass  # [bundled] hoisted __future__ import

import math
from typing import Any

try:
    import numpy as np
except ModuleNotFoundError:
    import os as _os
    from pathlib import Path as _Path
    import sys as _sys

    if _sys.platform == "win32":
        _appdata = _os.environ.get("APPDATA", "").strip()
        _orca_base = _Path(_appdata) / "OrcaSlicer" if _appdata else _Path.home() / "AppData" / "Roaming" / "OrcaSlicer"
    elif _sys.platform == "darwin":
        _orca_base = _Path.home() / "Library" / "Application Support" / "OrcaSlicer"
    else:
        _xdg = _os.environ.get("XDG_CONFIG_HOME", "").strip()
        _orca_base = (_Path(_xdg) if _xdg else (_Path.home() / ".config")) / "OrcaSlicer"

    _orca_pkg_dir = str(_orca_base / "python" / "packages" / f"cp{_sys.version_info.major}{_sys.version_info.minor}")
    if _orca_pkg_dir not in _sys.path:
        _sys.path.insert(0, _orca_pkg_dir)
    import numpy as np

pass  # [bundled] resolved intra-package import
pass  # [bundled] resolved intra-package import

PLA_DENSITY_G_CM3 = 1.24


def _ctx_float(ctx: dict[str, Any], key: str, default: float, lo: float, hi: float) -> float:
    val = ctx.get(key, default)
    if isinstance(val, (list, tuple)) and len(val) > 0:
        val = val[0]
    if isinstance(val, str):
        val = val.strip().rstrip("%mM ").strip()
    try:
        f = float(val)
    except (TypeError, ValueError):
        return default
    if not math.isfinite(f) or f <= 0.0:
        return default
    return max(lo, min(hi, f))


def analyze_printability(
    mesh: MeshData,
    params: dict[str, Any],
    host_context: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Analyze a generated mesh for overhangs, bed bounds, spiral vase gap risk, and PLA usage."""
    p = normalize_params(params)
    ctx = host_context if isinstance(host_context, dict) else {}

    bed_x = _ctx_float(ctx, "bed_x", 220.0, 50.0, 2000.0)
    bed_y = _ctx_float(ctx, "bed_y", 220.0, 50.0, 2000.0)
    max_z = _ctx_float(ctx, "max_z", 250.0, 50.0, 2000.0)
    nozzle_mm = _ctx_float(ctx, "nozzle_mm", 0.4, 0.15, 2.0)
    layer_h = _ctx_float(ctx, "layer_height_mm", 0.2, 0.04, 1.2)
    line_w = _ctx_float(ctx, "line_width_mm", 0.42, 0.15, 2.5)

    verts = np.asarray(mesh.vertices, dtype=np.float64)
    tris = np.asarray(mesh.triangles, dtype=np.int32)
    normals = np.asarray(mesh.face_normals, dtype=np.float64)
    tri_count = int(len(tris))

    size = mesh.bounds_mm.get("size", [0.0, 0.0, 0.0])
    dx = round(float(size[0]), 2)
    dy = round(float(size[1]), 2)
    dz = round(float(size[2]), 2)

    bed_shape = str(ctx.get("bed_shape") or "rectangular").strip().lower()
    if bed_shape == "circular":
        bed_diam = min(bed_x, bed_y)
        verts_xy_r = float(np.max(np.hypot(verts[:, 0], verts[:, 1]))) if len(verts) > 0 else 0.5 * max(dx, dy)
        fits_bed = bool(2.0 * verts_xy_r <= bed_diam + 1e-3 and max(dx, dy) <= bed_diam + 1e-3)
    else:
        fits_bed = bool(dx <= bed_x + 1e-3 and dy <= bed_y + 1e-3)
    fits_height = bool(dz <= max_z + 1e-3)

    if tri_count == 0 or len(verts) == 0:
        return {
            "max_overhang_deg": 0.0,
            "warning_faces_pct": 0.0,
            "critical_faces_pct": 0.0,
            "fits_bed": fits_bed,
            "fits_height": fits_height,
            "spiral_gap_risk": False,
            "estimated_weight_g": 0.0,
            "estimated_volume_cm3": 0.0,
            "dimensions_mm": [dx, dy, dz],
            "triangle_count": 0,
            "warnings": [],
        }

    v0 = verts[tris[:, 0]]
    v1 = verts[tris[:, 1]]
    v2 = verts[tris[:, 2]]
    face_areas = 0.5 * np.linalg.norm(np.cross(v1 - v0, v2 - v0), axis=1)

    face_z_max = np.maximum(np.maximum(v0[:, 2], v1[:, 2]), v2[:, 2])
    face_z_min = np.minimum(np.minimum(v0[:, 2], v1[:, 2]), v2[:, 2])
    nz = normals[:, 2]

    # Exclude flat bottom faces resting on bed Z == 0
    non_bed_mask = face_z_max > 1e-3

    # In spiral_vase mode, top cap and blind-drainage internal roof are unprinted slicing caps
    is_spiral = p["print_mode"] == "spiral_vase"
    if is_spiral:
        top_cap_mask = (face_z_min >= dz - 1e-2) & (nz > 0.999)
        eval_mask = non_bed_mask & (~top_cap_mask)
        if p["drainage"]["enabled"]:
            z_blind_cap = min(float(p["spiral_bottom_layers"]) * layer_h + 0.30, 0.34 * float(p["height_mm"]))
            blind_roof_mask = (face_z_max <= z_blind_cap + 0.08) & (nz < -0.999)
            eval_mask = eval_mask & (~blind_roof_mask)
    else:
        eval_mask = non_bed_mask

    downward_mask = eval_mask & (nz < -1e-4)
    overhang_deg = np.zeros(tri_count, dtype=np.float64)
    if np.any(downward_mask):
        overhang_deg[downward_mask] = np.degrees(np.arcsin(np.clip(-nz[downward_mask], 0.0, 1.0)))

    # Robust 99.8th area-weighted percentile avoids single microscopic facet spikes while catching real slopes;
    # still report true max on clean surfaces
    eval_areas = face_areas[eval_mask]
    total_eval_area = float(np.sum(eval_areas)) if eval_areas.size > 0 else 0.0

    max_overhang_deg = round(float(np.max(overhang_deg)), 1) if np.any(downward_mask) else 0.0
    if total_eval_area > 1e-6:
        warn_area = float(np.sum(face_areas[eval_mask & (overhang_deg > 45.0)]))
        crit_area = float(np.sum(face_areas[eval_mask & (overhang_deg > 55.0)]))
        warning_faces_pct = round(100.0 * warn_area / total_eval_area, 2)
        critical_faces_pct = round(100.0 * crit_area / total_eval_area, 2)
    else:
        warning_faces_pct = 0.0
        critical_faces_pct = 0.0

    # Spiral vase gap risk & realistic filament usage estimate
    eff_spiral_lw = float(p["spiral_line_width_mm"]) if p["auto_configure_slicer"] else line_w
    if is_spiral:
        horiz_step_mm = layer_h * math.tan(math.radians(min(max_overhang_deg, 84.0)))
        spiral_gap_risk = bool(
            (horiz_step_mm > 0.68 * eff_spiral_lw and warning_faces_pct > 0.25)
            or critical_faces_pct > 0.5
            or max_overhang_deg > 55.0
        )
        # Estimate actual printed shell volume (1 outer wall + bottom solid layers)
        bed_area_mm2 = float(np.sum(face_areas[~non_bed_mask]))
        wall_area_mm2 = total_eval_area
        bottom_h_mm = float(p["spiral_bottom_layers"]) * layer_h
        printed_vol_mm3 = wall_area_mm2 * eff_spiral_lw + bed_area_mm2 * bottom_h_mm
        est_vol_cm3 = max(0.5, min(float(mesh.volume_cm3), printed_vol_mm3 / 1000.0))
    else:
        spiral_gap_risk = False
        est_vol_cm3 = max(0.5, float(mesh.volume_cm3))

    est_vol_cm3 = round(est_vol_cm3, 2)
    est_weight_g = round(est_vol_cm3 * PLA_DENSITY_G_CM3, 1)

    warnings: list[dict[str, str]] = []

    if not fits_bed:
        warnings.append({
            "code": "BED_OVERFLOW",
            "pt": f"Dimensoes XY ({dx:.1f} x {dy:.1f} mm) excedem a mesa ({bed_x:.0f} x {bed_y:.0f} mm).",
            "en": f"XY dimensions ({dx:.1f} x {dy:.1f} mm) exceed build plate ({bed_x:.0f} x {bed_y:.0f} mm).",
        })

    if not fits_height:
        warnings.append({
            "code": "HEIGHT_OVERFLOW",
            "pt": f"Altura ({dz:.1f} mm) excede o limite Z da impressora ({max_z:.0f} mm).",
            "en": f"Height ({dz:.1f} mm) exceeds printer Z limit ({max_z:.0f} mm).",
        })

    g = p["textures"]["geometric"]
    if g["enabled"] and g["pattern"] == "folded_petals":
        warnings.append({"code": "RIBBON_ASSEMBLY",
            "pt": "As fitas e o vaso são sólidos fechados sobrepostos. Confira a união na prévia fatiada. O volume de material inclui as sobreposições.",
            "en": "Ribbons and cup are overlapping closed solids. Inspect their union in the sliced preview. Material volume includes overlaps."})

    if g["enabled"] and g["pattern"] == "folded_petals" and (critical_faces_pct > 0.5 or max_overhang_deg > 55.0):
        warnings.append({"code": "CRITICAL_RIBBON_OVERHANG",
            "pt": "As fitas enroladas têm overhangs acentuados. Confira a prévia fatiada e ajuste curvatura, resfriamento ou suportes conforme necessário.",
            "en": "Curled ribbons have steep overhangs. Inspect the sliced preview and adjust curl, cooling or supports as needed."})
    elif critical_faces_pct > 0.5 or max_overhang_deg > 55.0:
        warnings.append({
            "code": "CRITICAL_OVERHANG",
            "pt": (
                f"Overhang critico de {max_overhang_deg:.1f}° ({critical_faces_pct:.1f}% da parede > 55°). "
                "Ative 'Limitar Overhang Automaticamente' ou reduza a profundidade das texturas."
            ),
            "en": (
                f"Critical overhang of {max_overhang_deg:.1f}° ({critical_faces_pct:.1f}% of wall > 55°). "
                "Enable 'Auto-Clamp Overhang' or reduce texture depth."
            ),
        })
    elif warning_faces_pct > 1.0 or max_overhang_deg > 45.0:
        warnings.append({
            "code": "MODERATE_OVERHANG",
            "pt": f"Overhang moderado de {max_overhang_deg:.1f}° ({warning_faces_pct:.1f}% > 45°). Use boa ventilacao de camada.",
            "en": f"Moderate overhang of {max_overhang_deg:.1f}° ({warning_faces_pct:.1f}% > 45°). Ensure strong part cooling.",
        })

    if spiral_gap_risk:
        warnings.append({
            "code": "SPIRAL_GAP_RISK",
            "pt": (
                f"Risco de frestas no Modo Vaso Espiral (passo lateral > largura de linha {eff_spiral_lw:.2f} mm). "
                "Aumente a largura da parede espiral, reduza altura de camada ou mude para Parede Dupla."
            ),
            "en": (
                f"Gap risk in Spiral Vase mode (stepover exceeds {eff_spiral_lw:.2f} mm line width). "
                "Increase spiral line width, lower layer height, or switch to Shelled Hollow mode."
            ),
        })

    if is_spiral and eff_spiral_lw > 2.0 * nozzle_mm + 1e-4:
        warnings.append({
            "code": "LINE_WIDTH_HIGH",
            "pt": f"Largura espiral ({eff_spiral_lw:.2f} mm) acima de 2x o bico ({nozzle_mm:.2f} mm).",
            "en": f"Spiral line width ({eff_spiral_lw:.2f} mm) exceeds 2x nozzle diameter ({nozzle_mm:.2f} mm).",
        })

    if (not is_spiral) and float(p["wall_thickness_mm"]) < 2.0 * line_w - 1e-4:
        warnings.append({
            "code": "THIN_SHELL_WALL",
            "pt": f"Espessura da parede ({p['wall_thickness_mm']:.2f} mm) muito fina para perimetros duplos ({2.0 * line_w:.2f} mm).",
            "en": f"Wall thickness ({p['wall_thickness_mm']:.2f} mm) is thin for dual perimeters ({2.0 * line_w:.2f} mm).",
        })

    min_foot = max(1.0, min(dx, dy))
    if dz / min_foot > 3.2:
        warnings.append({
            "code": "TALL_SLENDER_RATIO",
            "pt": "Proporcao alta e estreita — considere adicionar Brim no OrcaSlicer para aderencia extra.",
            "en": "Tall slender aspect ratio — consider enabling a Brim in OrcaSlicer for extra bed adhesion.",
        })

    return {
        "max_overhang_deg": max_overhang_deg,
        "warning_faces_pct": warning_faces_pct,
        "critical_faces_pct": critical_faces_pct,
        "fits_bed": fits_bed,
        "fits_height": fits_height,
        "spiral_gap_risk": spiral_gap_risk,
        "estimated_weight_g": est_weight_g,
        "estimated_volume_cm3": est_vol_cm3,
        "dimensions_mm": [dx, dy, dz],
        "triangle_count": tri_count,
        "warnings": warnings,
    }

# ===========================================================================
# MODULE: vase_studio.exporters
# ===========================================================================

"""Binary STL and OrcaSlicer 2.5.1 3MF project exporters for Orca Vase Studio."""

pass  # [bundled] hoisted __future__ import

import datetime as _dt
import json
import math
import struct
import uuid
import zipfile
from pathlib import Path
from typing import Any
from xml.sax.saxutils import escape as _xml_escape

import numpy as np

_STL_RECORD_DTYPE = np.dtype(
    [
        ("normal", "<f4", (3,)),
        ("v0", "<f4", (3,)),
        ("v1", "<f4", (3,)),
        ("v2", "<f4", (3,)),
        ("attr", "<u2"),
    ]
)

_CONTENT_TYPES_XML = """<?xml version="1.0" encoding="UTF-8"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
 <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
 <Default Extension="model" ContentType="application/vnd.ms-package.3dmanufacturing-3dmodel+xml"/>
 <Default Extension="config" ContentType="text/xml"/>
 <Default Extension="png" ContentType="image/png"/>
 <Default Extension="json" ContentType="application/json"/>
</Types>
"""

_RELS_XML = """<?xml version="1.0" encoding="UTF-8"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
 <Relationship Target="/3D/3dmodel.model" Id="rel-1" Type="http://schemas.microsoft.com/3dmanufacturing/2013/01/3dmodel"/>
</Relationships>
"""


def _extract_mesh_arrays(mesh: Any) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Extract validated (vertices, triangles, face_normals) arrays from duck-typed MeshData."""
    vertices = np.asarray(mesh.vertices, dtype=np.float32)
    if vertices.ndim != 2 or vertices.shape[1] != 3:
        raise ValueError(f"Expected vertices shape (V, 3), got {vertices.shape!r}")
    vertices = np.nan_to_num(vertices, nan=0.0, posinf=0.0, neginf=0.0).astype(np.float32, copy=False)

    triangles = np.asarray(mesh.triangles, dtype=np.int32)
    if triangles.size == 0:
        triangles = np.zeros((0, 3), dtype=np.int32)
    elif triangles.ndim != 2 or triangles.shape[1] != 3:
        raise ValueError(f"Expected triangles shape (F, 3), got {triangles.shape!r}")

    num_tris = triangles.shape[0]
    raw_normals = getattr(mesh, "face_normals", None)
    if (
        raw_normals is not None
        and np.asarray(raw_normals).shape == (num_tris, 3)
        and np.all(np.isfinite(raw_normals))
    ):
        normals = np.asarray(raw_normals, dtype=np.float32)
    elif num_tris > 0:
        tris_xyz = vertices[triangles]
        e1 = tris_xyz[:, 1, :] - tris_xyz[:, 0, :]
        e2 = tris_xyz[:, 2, :] - tris_xyz[:, 0, :]
        cross = np.cross(e1, e2)
        lengths = np.linalg.norm(cross, axis=1, keepdims=True)
        safe_lengths = np.where(lengths > 1e-12, lengths, 1.0)
        normals = (cross / safe_lengths).astype(np.float32)
        normals = np.where(lengths > 1e-12, normals, np.array([[0.0, 0.0, 1.0]], dtype=np.float32))
    else:
        normals = np.zeros((0, 3), dtype=np.float32)

    return vertices, triangles, normals


def _mesh_xy_extents(mesh: Any, vertices: np.ndarray | None = None) -> tuple[float, float]:
    """Return (width_x_mm, depth_y_mm) of a mesh from bounds_mm or vertices."""
    bounds = getattr(mesh, "bounds_mm", None)
    if isinstance(bounds, dict):
        size = bounds.get("size")
        if isinstance(size, (list, tuple)) and len(size) >= 2:
            return max(float(size[0]), 1.0), max(float(size[1]), 1.0)
        bmin = bounds.get("min")
        bmax = bounds.get("max")
        if isinstance(bmin, (list, tuple)) and isinstance(bmax, (list, tuple)) and len(bmin) >= 2 and len(bmax) >= 2:
            return max(float(bmax[0]) - float(bmin[0]), 1.0), max(float(bmax[1]) - float(bmin[1]), 1.0)
    verts = vertices if vertices is not None else np.asarray(mesh.vertices, dtype=np.float32)
    if verts.shape[0] == 0:
        return 10.0, 10.0
    dx = float(np.max(verts[:, 0]) - np.min(verts[:, 0]))
    dy = float(np.max(verts[:, 1]) - np.min(verts[:, 1]))
    return max(dx, 1.0), max(dy, 1.0)


def _resolve_bed_dimensions(host_config: dict | None) -> tuple[float, float]:
    """Extract (bed_x, bed_y) in mm from host_config with 220x220 fallback."""
    bed_x = 220.0
    bed_y = 220.0
    if isinstance(host_config, dict):
        if "bed_x" in host_config:
            try:
                bed_x = max(float(host_config["bed_x"]), 60.0)
            except (TypeError, ValueError):
                pass
        if "bed_y" in host_config:
            try:
                bed_y = max(float(host_config["bed_y"]), 60.0)
            except (TypeError, ValueError):
                pass
        printer = host_config.get("printer")
        if isinstance(printer, dict):
            if "bed_x" in printer and "bed_x" not in host_config:
                try:
                    bed_x = max(float(printer["bed_x"]), 60.0)
                except (TypeError, ValueError):
                    pass
            if "bed_y" in printer and "bed_y" not in host_config:
                try:
                    bed_y = max(float(printer["bed_y"]), 60.0)
                except (TypeError, ValueError):
                    pass
    return bed_x, bed_y


def _positions_overlap(
    positions: list[tuple[float, float, float]],
    extents: list[tuple[float, float]],
    min_clearance_mm: float = 3.0,
) -> bool:
    """Return True if any two items overlap on the XY build plate."""
    n = len(positions)
    for i in range(n):
        xi, yi, _ = positions[i]
        wxi, wyi = extents[i]
        for j in range(i + 1, n):
            xj, yj, _ = positions[j]
            wxj, wyj = extents[j]
            overlap_x = abs(xi - xj) < (0.5 * (wxi + wxj) + min_clearance_mm)
            overlap_y = abs(yi - yj) < (0.5 * (wyi + wyj) + min_clearance_mm)
            if overlap_x and overlap_y:
                return True
    return False


def _arrange_items_on_bed(
    extents: list[tuple[float, float]],
    z_offsets: list[float],
    bed_x: float,
    bed_y: float,
    gap_mm: float = 10.0,
) -> list[tuple[float, float, float]]:
    """Arrange 1 or more items cleanly around the bed center without XY overlap."""
    cx = bed_x * 0.5
    cy = bed_y * 0.5
    count = len(extents)
    if count == 0:
        return []
    if count == 1:
        return [(cx, cy, z_offsets[0])]

    if count == 2:
        (w0, d0), (w1, d1) = extents
        total_w = w0 + gap_mm + w1
        if total_w <= bed_x - 8.0:
            left_edge = cx - 0.5 * total_w
            x0 = left_edge + 0.5 * w0
            x1 = left_edge + w0 + gap_mm + 0.5 * w1
            return [(x0, cy, z_offsets[0]), (x1, cy, z_offsets[1])]

        # Place along the bed diagonal when side-by-side exceeds X width
        r0 = 0.5 * max(w0, d0)
        r1 = 0.5 * max(w1, d1)
        diag_sep = r0 + r1 + gap_mm
        step = diag_sep / math.sqrt(2.0)
        half_step = 0.5 * step
        x0 = max(r0 + 2.0, cx - half_step)
        y0 = max(r0 + 2.0, cy - half_step)
        x1 = min(bed_x - r1 - 2.0, cx + half_step)
        y1 = min(bed_y - r1 - 2.0, cy + half_step)
        if math.hypot(x1 - x0, y1 - y0) >= (r0 + r1 + 2.0):
            return [(x0, y0, z_offsets[0]), (x1, y1, z_offsets[1])]
        # If combined radii exceed diagonal bed size, still place cleanly separated
        return [(cx - half_step, cy - half_step, z_offsets[0]), (cx + half_step, cy + half_step, z_offsets[1])]

    # General grid/row layout for 3+ items
    total_w = sum(w for w, _ in extents) + gap_mm * (count - 1)
    cursor_x = cx - 0.5 * total_w
    placed: list[tuple[float, float, float]] = []
    for idx, (w, _) in enumerate(extents):
        px = cursor_x + 0.5 * w
        placed.append((px, cy, z_offsets[idx]))
        cursor_x += w + gap_mm
    return placed


def _build_project_settings_dict(params: dict | None, host_config: dict | None) -> dict[str, Any]:
    """Merge host project settings with print-mode overrides for OrcaSlicer 2.5.1."""
    merged: dict[str, Any] = {}
    if isinstance(host_config, dict):
        raw_ps = host_config.get("project_settings")
        if isinstance(raw_ps, dict):
            merged.update(raw_ps)

    p = params if isinstance(params, dict) else {}
    print_mode = str(p.get("print_mode", "spiral_vase")).strip().lower()

    if print_mode == "shelled_hollow":
        wall_thickness = max(0.8, float(p.get("wall_thickness_mm", 2.2)))
        bottom_thickness = max(1.0, float(p.get("bottom_thickness_mm", 3.2)))
        merged["spiral_mode"] = "0"
        merged["spiral_mode_smooth"] = "0"
        if str(merged.get("wall_loops", "")).strip() in ("", "0", "1"):
            merged["wall_loops"] = str(max(2, min(6, int(round(wall_thickness / 0.84)))))
        if str(merged.get("top_shell_layers", "")).strip() in ("", "0"):
            merged["top_shell_layers"] = "4"
        if str(merged.get("bottom_shell_layers", "")).strip() in ("", "0"):
            merged["bottom_shell_layers"] = str(max(3, int(round(bottom_thickness / 0.20))))
        if str(merged.get("sparse_infill_density", "")).strip() in ("", "0", "0%"):
            merged["sparse_infill_density"] = "15%"
    else:
        spiral_smooth = bool(p.get("spiral_smooth", True))
        spiral_bottom_layers = max(2, min(20, int(round(float(p.get("spiral_bottom_layers", 5))))))
        spiral_line_width = max(0.30, min(1.50, float(p.get("spiral_line_width_mm", 0.65))))
        merged["spiral_mode"] = "1"
        merged["spiral_mode_smooth"] = "1" if spiral_smooth else "0"
        merged["wall_loops"] = "1"
        merged["top_shell_layers"] = "0"
        merged["sparse_infill_density"] = "0%"
        merged["bottom_shell_layers"] = str(spiral_bottom_layers)
        merged["outer_wall_line_width"] = f"{spiral_line_width:.2f}"

    return merged


def write_binary_stl(path: str | Path, mesh: Any, header_name: str = "OrcaVaseStudio") -> Path:
    """Write a duck-typed MeshData object to a standard little-endian binary STL file.

    Binary layout: 80-byte ASCII header + uint32 triangle count + F * 50-byte facet records.
    """
    out_path = Path(path)
    if not out_path.parent.exists():
        out_path.parent.mkdir(parents=True, exist_ok=True)

    vertices, triangles, normals = _extract_mesh_arrays(mesh)
    num_triangles = int(triangles.shape[0])

    clean_header = str(header_name or "OrcaVaseStudio").strip() or "OrcaVaseStudio"
    if clean_header.lower().startswith("solid"):
        clean_header = f"Orca_{clean_header}"
    header_text = f"{clean_header} - Orca Vase Studio Binary STL"
    header_bytes = header_text.encode("ascii", errors="replace")[:80].ljust(80, b"\x00")

    records = np.zeros(num_triangles, dtype=_STL_RECORD_DTYPE)
    if num_triangles > 0:
        tris_xyz = vertices[triangles]
        records["normal"] = normals.astype("<f4", copy=False)
        records["v0"] = tris_xyz[:, 0, :].astype("<f4", copy=False)
        records["v1"] = tris_xyz[:, 1, :].astype("<f4", copy=False)
        records["v2"] = tris_xyz[:, 2, :].astype("<f4", copy=False)
        records["attr"] = 0

    with open(out_path, "wb") as fh:
        fh.write(header_bytes)
        fh.write(struct.pack("<I", num_triangles))
        if num_triangles > 0:
            fh.write(records.tobytes())

    return out_path


def write_orca_3mf(
    path: str | Path,
    items: list[tuple[str, Any, tuple[float, float, float]]],
    params: dict,
    host_config: dict | None = None,
) -> Path:
    """Write an OrcaSlicer 2.5.1 compatible .3mf project archive with meshes and slicer settings."""
    if not items:
        raise ValueError("write_orca_3mf requires at least one item in 'items'.")

    out_path = Path(path)
    if not out_path.parent.exists():
        out_path.parent.mkdir(parents=True, exist_ok=True)

    bed_x, bed_y = _resolve_bed_dimensions(host_config)
    cx, cy = bed_x * 0.5, bed_y * 0.5

    parsed_items: list[tuple[str, np.ndarray, np.ndarray, tuple[float, float]]] = []
    raw_positions: list[tuple[float, float, float] | None] = []
    z_offsets: list[float] = []

    for idx, entry in enumerate(items):
        if len(entry) == 2:
            raw_name, mesh = entry  # type: ignore[misc]
            raw_pos = None
        elif len(entry) >= 3:
            raw_name, mesh, raw_pos = entry[0], entry[1], entry[2]
        else:
            raise ValueError(f"Invalid item tuple at index {idx}: {entry!r}")

        item_name = str(raw_name or f"Object_{idx + 1}").strip() or f"Object_{idx + 1}"
        vertices, triangles, _ = _extract_mesh_arrays(mesh)
        ext = _mesh_xy_extents(mesh, vertices)
        parsed_items.append((item_name, vertices, triangles, ext))

        if raw_pos is None:
            raw_positions.append(None)
            z_offsets.append(0.0)
        else:
            px, py, pz = float(raw_pos[0]), float(raw_pos[1]), float(raw_pos[2])
            raw_positions.append((px, py, pz))
            z_offsets.append(pz)

    extents_list = [it[3] for it in parsed_items]
    if any(pos is None for pos in raw_positions):
        if len(parsed_items) == 1:
            final_positions = [(cx, cy, z_offsets[0])]
        else:
            final_positions = _arrange_items_on_bed(extents_list, z_offsets, bed_x, bed_y, gap_mm=10.0)
    else:
        concrete_positions = [pos for pos in raw_positions if pos is not None]
        if len(concrete_positions) >= 2 and _positions_overlap(concrete_positions, extents_list, min_clearance_mm=3.0):
            final_positions = _arrange_items_on_bed(extents_list, z_offsets, bed_x, bed_y, gap_mm=10.0)
        else:
            final_positions = concrete_positions

    title = str((params or {}).get("name") or parsed_items[0][0] or "Orca Vase Studio").strip()
    escaped_title = _xml_escape(title, {'"': "&quot;"})
    today_iso = _dt.date.today().isoformat()
    ns_seed = uuid.UUID("6ba7b810-9dad-11d1-80b4-00c04fd430c8")
    build_uuid = str(uuid.uuid5(ns_seed, f"orca-vase-build-{title}"))

    object_blocks: list[str] = []
    build_items_xml: list[str] = []
    model_settings_objects: list[str] = []
    model_settings_instances: list[str] = []
    model_settings_assemble: list[str] = []

    for idx, (item_name, vertices, triangles, _) in enumerate(parsed_items):
        obj_id = idx + 1
        tx, ty, tz = final_positions[idx]
        esc_name = _xml_escape(item_name, {'"': "&quot;"})
        obj_uuid = str(uuid.uuid5(ns_seed, f"orca-vase-obj-{obj_id}-{item_name}"))
        item_uuid = str(uuid.uuid5(ns_seed, f"orca-vase-item-{obj_id}-{item_name}"))

        verts_py = vertices.tolist()
        tris_py = triangles.tolist()

        vertex_lines = "\n".join(
            f'     <vertex x="{vx:.5f}" y="{vy:.5f}" z="{vz:.5f}"/>'
            for vx, vy, vz in verts_py
        )
        triangle_lines = "\n".join(
            f'     <triangle v1="{v1}" v2="{v2}" v3="{v3}"/>'
            for v1, v2, v3 in tris_py
        )

        object_blocks.append(
            f'  <object id="{obj_id}" p:UUID="{obj_uuid}" name="{esc_name}" type="model">\n'
            f"   <mesh>\n"
            f"    <vertices>\n"
            f"{vertex_lines}\n"
            f"    </vertices>\n"
            f"    <triangles>\n"
            f"{triangle_lines}\n"
            f"    </triangles>\n"
            f"   </mesh>\n"
            f"  </object>"
        )

        transform_3x4 = f"1 0 0 0 1 0 0 0 1 {tx:.4f} {ty:.4f} {tz:.4f}"
        build_items_xml.append(
            f'  <item objectid="{obj_id}" p:UUID="{item_uuid}" transform="{transform_3x4}" printable="1"/>'
        )

        model_settings_objects.append(
            f'  <object id="{obj_id}">\n'
            f'    <metadata key="name" value="{esc_name}"/>\n'
            f'    <metadata key="extruder" value="1"/>\n'
            f'    <part id="1" subtype="normal_part">\n'
            f'      <metadata key="name" value="{esc_name}"/>\n'
            f'      <metadata key="matrix" value="1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1"/>\n'
            f'      <mesh_stat edges_fixed="0" degenerate_facets="0" facets_removed="0" facets_reversed="0" backwards_edges="0"/>\n'
            f"    </part>\n"
            f"  </object>"
        )
        model_settings_instances.append(
            f"    <model_instance>\n"
            f'      <metadata key="object_id" value="{obj_id}"/>\n'
            f'      <metadata key="instance_id" value="0"/>\n'
            f'      <metadata key="identify_id" value="{100 + obj_id}"/>\n'
            f"    </model_instance>"
        )
        model_settings_assemble.append(
            f'    <assemble_item object_id="{obj_id}" instance_id="0" transform="{transform_3x4}" offset="0 0 0"/>'
        )

    model_xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<model unit="millimeter" xml:lang="en-US" '
        'xmlns="http://schemas.microsoft.com/3dmanufacturing/core/2015/02" '
        'xmlns:BambuStudio="http://schemas.bambulab.com/package/2021" '
        'xmlns:p="http://schemas.microsoft.com/3dmanufacturing/production/2015/06" '
        'requiredextensions="p">\n'
        ' <metadata name="Application">OrcaSlicer-2.5.1</metadata>\n'
        ' <metadata name="OrcaSlicer">2.5.1</metadata>\n'
        ' <metadata name="BambuStudio:3mfVersion">1</metadata>\n'
        f' <metadata name="Title">{escaped_title}</metadata>\n'
        f' <metadata name="CreationDate">{today_iso}</metadata>\n'
        " <resources>\n"
        + "\n".join(object_blocks)
        + "\n </resources>\n"
        + f' <build p:UUID="{build_uuid}">\n'
        + "\n".join(build_items_xml)
        + "\n </build>\n"
        "</model>\n"
    )

    model_settings_xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        "<config>\n"
        + "\n".join(model_settings_objects)
        + "\n  <plate>\n"
        '    <metadata key="plater_id" value="1"/>\n'
        '    <metadata key="plater_name" value=""/>\n'
        '    <metadata key="locked" value="false"/>\n'
        + "\n".join(model_settings_instances)
        + "\n  </plate>\n"
        "  <assemble>\n"
        + "\n".join(model_settings_assemble)
        + "\n  </assemble>\n"
        "</config>\n"
    )

    project_settings = _build_project_settings_dict(params, host_config)
    project_settings_json = json.dumps(project_settings, indent=2, ensure_ascii=False)

    with zipfile.ZipFile(out_path, mode="w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as zf:
        zf.writestr("[Content_Types].xml", _CONTENT_TYPES_XML)
        zf.writestr("_rels/.rels", _RELS_XML)
        zf.writestr("3D/3dmodel.model", model_xml)
        zf.writestr("Metadata/model_settings.config", model_settings_xml)
        zf.writestr("Metadata/project_settings.config", project_settings_json)

    return out_path

# ===========================================================================
# MODULE: vase_studio.presets_catalog
# ===========================================================================

"""Curated built-in presets catalog, user preset storage, and smart printable randomizer."""

pass  # [bundled] hoisted __future__ import

import copy
import datetime as _dt
import json
import math
import random
import re
import uuid
from pathlib import Path
from typing import Any

_PRESETS_FALLBACK_DEFAULT_PARAMS: dict[str, Any] = {
    "name": "Ondas Organicas",
    "height_mm": 160.0,
    "base_diameter_mm": 76.0,
    "belly_diameter_mm": 110.0,
    "belly_height_ratio": 0.34,
    "waist_diameter_mm": 68.0,
    "waist_height_ratio": 0.68,
    "neck_diameter_mm": 82.0,
    "lip_flare_mm": 4.0,
    "lip_bevel_mm": 1.0,
    "polygon_sides": 0,
    "polygon_roundness": 0.35,
    "use_custom_profile": False,
    "profile_points": [
        [0.0, 38.0],
        [0.34, 55.0],
        [0.68, 34.0],
        [0.92, 41.0],
        [1.0, 45.0],
    ],
    "resolution_angular": 240,
    "resolution_vertical": 220,
    "bottom_fade_mm": 8.0,
    "top_fade_mm": 6.0,
    "global_twist_deg": 0.0,
    "textures": {
        "ribbed": {
            "enabled": False,
            "depth_mm": 2.6,
            "count": 32,
            "duty_cycle": 0.50,
            "sharpness": 0.35,
            "twist_deg": 60.0,
            "phase_deg": 0.0,
        },
        "waves": {
            "enabled": True,
            "depth_mm": 3.0,
            "vertical_wavelength_mm": 26.0,
            "angular_lobes": 6,
            "interference_mix": 0.45,
            "wave_skew": 0.0,
            "phase_deg": 0.0,
        },
        "origami": {
            "enabled": False,
            "depth_mm": 3.2,
            "cells_around": 12,
            "cells_vertical": 8,
            "crease_sharpness": 0.75,
            "stagger": 0.50,
        },
        "cellular": {
            "enabled": False,
            "depth_mm": 2.4,
            "scale_angular": 8,
            "scale_vertical_mm": 22.0,
            "ridge_mode": True,
            "octaves": 2,
            "seed": 42,
        },
    },
    "print_mode": "shelled_hollow",
    "stl_always_open_hollow": True,
    "auto_configure_slicer": True,
    "spiral_line_width_mm": 0.65,
    "spiral_bottom_layers": 5,
    "spiral_smooth": True,
    "wall_thickness_mm": 2.4,
    "bottom_thickness_mm": 3.2,
    "auto_clamp_overhang": False,
    "max_safe_overhang_deg": 48.0,
    "drainage": {
        "enabled": False,
        "hole_count": 4,
        "hole_diameter_mm": 8.0,
        "ring_radius_ratio": 0.48,
    },
    "saucer": {
        "clearance_mm": 8.0,
        "rim_height_mm": 22.0,
        "wall_thickness_mm": 2.4,
        "floor_thickness_mm": 2.6,
        "inner_ribs_height_mm": 2.0,
        "match_vase_texture": True,
    },
}


def _presets_clamp_float(val: Any, lo: float, hi: float, default: float) -> float:
    try:
        num = float(val)
        if not math.isfinite(num):
            return default
        return max(lo, min(hi, num))
    except (TypeError, ValueError):
        return default


def _presets_clamp_int(val: Any, lo: int, hi: int, default: int) -> int:
    try:
        num = int(round(float(val)))
        return max(lo, min(hi, num))
    except (TypeError, ValueError):
        return default


def _presets_to_bool(val: Any, default: bool) -> bool:
    if isinstance(val, bool):
        return val
    if isinstance(val, (int, float)):
        return bool(val) if math.isfinite(val) else default
    if isinstance(val, str):
        s = val.strip().lower()
        if s in ("true", "1", "yes", "on"):
            return True
        if s in ("false", "0", "no", "off", ""):
            return False
    return default


def _presets_deep_merge(dst: dict[str, Any], src: dict[str, Any]) -> None:
    for k, v in src.items():
        if isinstance(v, dict) and isinstance(dst.get(k), dict):
            _presets_deep_merge(dst[k], v)
        else:
            dst[k] = copy.deepcopy(v)


def _presets_fallback_normalize(raw: dict | None = None) -> dict[str, Any]:
    out = copy.deepcopy(_PRESETS_FALLBACK_DEFAULT_PARAMS)
    if isinstance(raw, dict):
        _presets_deep_merge(out, raw)

    out["name"] = str(out.get("name") or "Ondas Organicas").strip()[:100] or "Ondas Organicas"
    out["height_mm"] = _presets_clamp_float(out.get("height_mm"), 30.0, 500.0, 160.0)
    out["base_diameter_mm"] = _presets_clamp_float(out.get("base_diameter_mm"), 20.0, 450.0, 76.0)
    out["belly_diameter_mm"] = _presets_clamp_float(out.get("belly_diameter_mm"), 20.0, 450.0, 110.0)
    out["belly_height_ratio"] = _presets_clamp_float(out.get("belly_height_ratio"), 0.08, 0.85, 0.34)
    out["waist_diameter_mm"] = _presets_clamp_float(out.get("waist_diameter_mm"), 16.0, 450.0, 68.0)
    out["waist_height_ratio"] = _presets_clamp_float(out.get("waist_height_ratio"), 0.15, 0.92, 0.68)
    out["neck_diameter_mm"] = _presets_clamp_float(out.get("neck_diameter_mm"), 16.0, 450.0, 82.0)
    out["lip_flare_mm"] = _presets_clamp_float(out.get("lip_flare_mm"), -15.0, 25.0, 4.0)
    out["lip_bevel_mm"] = _presets_clamp_float(out.get("lip_bevel_mm"), 0.0, 4.0, 1.0)

    poly = _presets_clamp_int(out.get("polygon_sides"), 0, 24, 0)
    out["polygon_sides"] = 0 if poly < 3 else poly
    out["polygon_roundness"] = _presets_clamp_float(out.get("polygon_roundness"), 0.0, 1.0, 0.35)
    out["use_custom_profile"] = bool(out.get("use_custom_profile", False))

    pts_raw = out.get("profile_points")
    pts: list[list[float]] = []
    if isinstance(pts_raw, list):
        for item in pts_raw:
            if isinstance(item, (list, tuple)) and len(item) >= 2:
                zn = _presets_clamp_float(item[0], 0.0, 1.0, 0.0)
                rm = _presets_clamp_float(item[1], 8.0, 225.0, 38.0)
                pts.append([zn, rm])
    if len(pts) < 2:
        pts = copy.deepcopy(_PRESETS_FALLBACK_DEFAULT_PARAMS["profile_points"])
    pts.sort(key=lambda pair: pair[0])
    pts[0][0] = 0.0
    pts[-1][0] = 1.0
    out["profile_points"] = pts

    out["resolution_angular"] = _presets_clamp_int(out.get("resolution_angular"), 64, 360, 240)
    out["resolution_vertical"] = _presets_clamp_int(out.get("resolution_vertical"), 60, 400, 220)
    out["bottom_fade_mm"] = _presets_clamp_float(out.get("bottom_fade_mm"), 0.0, 60.0, 8.0)
    out["top_fade_mm"] = _presets_clamp_float(out.get("top_fade_mm"), 0.0, 60.0, 6.0)
    out["global_twist_deg"] = _presets_clamp_float(out.get("global_twist_deg"), -720.0, 720.0, 0.0)

    tex = out["textures"]
    rib = tex["ribbed"]
    rib["enabled"] = bool(rib.get("enabled", False))
    rib["depth_mm"] = _presets_clamp_float(rib.get("depth_mm"), -15.0, 15.0, 2.6)
    rib["count"] = _presets_clamp_int(rib.get("count"), 3, 180, 32)
    rib["duty_cycle"] = _presets_clamp_float(rib.get("duty_cycle"), 0.10, 0.90, 0.50)
    rib["sharpness"] = _presets_clamp_float(rib.get("sharpness"), 0.0, 1.0, 0.35)
    rib["twist_deg"] = _presets_clamp_float(rib.get("twist_deg"), -720.0, 720.0, 60.0)
    rib["phase_deg"] = _presets_clamp_float(rib.get("phase_deg"), 0.0, 360.0, 0.0)

    wav = tex["waves"]
    wav["enabled"] = bool(wav.get("enabled", True))
    wav["depth_mm"] = _presets_clamp_float(wav.get("depth_mm"), -15.0, 15.0, 3.0)
    wav["vertical_wavelength_mm"] = _presets_clamp_float(wav.get("vertical_wavelength_mm"), 4.0, 120.0, 26.0)
    wav["angular_lobes"] = _presets_clamp_int(wav.get("angular_lobes"), 0, 48, 6)
    wav["interference_mix"] = _presets_clamp_float(wav.get("interference_mix"), 0.0, 1.0, 0.45)
    wav["wave_skew"] = _presets_clamp_float(wav.get("wave_skew"), -0.8, 0.8, 0.0)
    wav["phase_deg"] = _presets_clamp_float(wav.get("phase_deg"), 0.0, 360.0, 0.0)

    ori = tex["origami"]
    ori["enabled"] = bool(ori.get("enabled", False))
    ori["depth_mm"] = _presets_clamp_float(ori.get("depth_mm"), -15.0, 15.0, 3.2)
    ori["cells_around"] = _presets_clamp_int(ori.get("cells_around"), 3, 60, 12)
    ori["cells_vertical"] = _presets_clamp_int(ori.get("cells_vertical"), 2, 50, 8)
    ori["crease_sharpness"] = _presets_clamp_float(ori.get("crease_sharpness"), 0.0, 1.0, 0.75)
    ori["stagger"] = _presets_clamp_float(ori.get("stagger"), 0.0, 1.0, 0.50)

    cel = tex["cellular"]
    cel["enabled"] = bool(cel.get("enabled", False))
    cel["depth_mm"] = _presets_clamp_float(cel.get("depth_mm"), -12.0, 12.0, 2.4)
    cel["scale_angular"] = _presets_clamp_int(cel.get("scale_angular"), 2, 40, 8)
    cel["scale_vertical_mm"] = _presets_clamp_float(cel.get("scale_vertical_mm"), 5.0, 100.0, 22.0)
    cel["ridge_mode"] = bool(cel.get("ridge_mode", True))
    cel["octaves"] = _presets_clamp_int(cel.get("octaves"), 1, 4, 2)
    cel["seed"] = _presets_clamp_int(cel.get("seed"), 1, 99999, 42)

    pm = str(out.get("print_mode", "shelled_hollow")).strip().lower()
    out["print_mode"] = pm if pm in ("spiral_vase", "shelled_hollow") else "shelled_hollow"
    out["stl_always_open_hollow"] = _presets_to_bool(out.get("stl_always_open_hollow"), True)
    out["auto_configure_slicer"] = _presets_to_bool(out.get("auto_configure_slicer"), True)
    out["spiral_line_width_mm"] = _presets_clamp_float(out.get("spiral_line_width_mm"), 0.40, 1.20, 0.65)
    out["spiral_bottom_layers"] = _presets_clamp_int(out.get("spiral_bottom_layers"), 2, 15, 5)
    out["spiral_smooth"] = _presets_to_bool(out.get("spiral_smooth"), True)
    out["wall_thickness_mm"] = _presets_clamp_float(out.get("wall_thickness_mm"), 0.8, 25.0, 2.4)
    out["bottom_thickness_mm"] = _presets_clamp_float(out.get("bottom_thickness_mm"), 1.0, 25.0, 3.2)
    out["auto_clamp_overhang"] = _presets_to_bool(out.get("auto_clamp_overhang"), False)
    out["max_safe_overhang_deg"] = _presets_clamp_float(out.get("max_safe_overhang_deg"), 35.0, 65.0, 48.0)

    drn = out["drainage"]
    drn["enabled"] = bool(drn.get("enabled", False))
    drn["hole_count"] = _presets_clamp_int(drn.get("hole_count"), 1, 9, 4)
    drn["hole_diameter_mm"] = _presets_clamp_float(drn.get("hole_diameter_mm"), 3.0, 20.0, 8.0)
    drn["ring_radius_ratio"] = _presets_clamp_float(drn.get("ring_radius_ratio"), 0.0, 0.68, 0.48)

    scr = out["saucer"]
    scr["clearance_mm"] = _presets_clamp_float(scr.get("clearance_mm"), 3.0, 25.0, 8.0)
    scr["rim_height_mm"] = _presets_clamp_float(scr.get("rim_height_mm"), 10.0, 60.0, 22.0)
    scr["wall_thickness_mm"] = _presets_clamp_float(scr.get("wall_thickness_mm"), 1.2, 5.0, 2.4)
    scr["floor_thickness_mm"] = _presets_clamp_float(scr.get("floor_thickness_mm"), 1.2, 6.0, 2.6)
    scr["inner_ribs_height_mm"] = _presets_clamp_float(scr.get("inner_ribs_height_mm"), 0.0, 6.0, 2.0)
    scr["match_vase_texture"] = bool(scr.get("match_vase_texture", True))

    return out


try:
    pass  # [bundled] resolved intra-package import

    pass
except (ImportError, KeyError, ValueError):
    pass

if "DEFAULT_PARAMS" not in globals() or "normalize_params" not in globals():
    DEFAULT_PARAMS = _PRESETS_FALLBACK_DEFAULT_PARAMS
    normalize_params = _presets_fallback_normalize


_USER_PRESETS_FILENAME = "user_presets.json"


def _make_preset_params(overrides: dict[str, Any]) -> dict[str, Any]:
    """Build a clean preset parameter dictionary starting with all textures disabled unless specified."""
    base = copy.deepcopy(DEFAULT_PARAMS)
    for t_cfg in base["textures"].values():
        t_cfg["enabled"] = False
    _presets_deep_merge(base, overrides)
    return normalize_params(base)


BUILTIN_PRESETS: list[dict[str, Any]] = [
    {
        "id": "ondas_organicas",
        "title_pt": "Ondas Orgânicas",
        "title_en": "Organic Waves",
        "category": "organic",
        "description_pt": "Ondulações contra-helicoidais fluidas inspiradas em dunas e correntes marinhas.",
        "description_en": "Flowing counter-helical ripples inspired by coastal dunes and ocean currents.",
        "params": _make_preset_params(
            {
                "name": "Ondas Orgânicas",
                "height_mm": 165.0,
                "base_diameter_mm": 76.0,
                "belly_diameter_mm": 112.0,
                "belly_height_ratio": 0.34,
                "waist_diameter_mm": 68.0,
                "waist_height_ratio": 0.68,
                "neck_diameter_mm": 82.0,
                "lip_flare_mm": 4.0,
                "bottom_fade_mm": 10.0,
                "top_fade_mm": 7.0,
                "global_twist_deg": 40.0,
                "textures": {
                    "waves": {
                        "enabled": True,
                        "depth_mm": 3.0,
                        "vertical_wavelength_mm": 26.0,
                        "angular_lobes": 6,
                        "interference_mix": 0.45,
                        "wave_skew": 0.15,
                        "phase_deg": 0.0,
                    }
                },
                "print_mode": "shelled_hollow",
                "stl_always_open_hollow": True,
                "wall_thickness_mm": 2.4,
                "bottom_thickness_mm": 3.2,
                "spiral_line_width_mm": 0.65,
                "spiral_bottom_layers": 5,
            }
        ),
    },
    {
        "id": "colunas_caneladas",
        "title_pt": "Colunas Caneladas",
        "title_en": "Architectural Fluted",
        "category": "architectural",
        "description_pt": "Caneluras verticais clássicas com espaçamento arquitetônico limpo e sombra marcada.",
        "description_en": "Crisp vertical architectural flutes with balanced flat fillets and clean shadow lines.",
        "params": _make_preset_params(
            {
                "name": "Colunas Caneladas",
                "height_mm": 190.0,
                "base_diameter_mm": 84.0,
                "belly_diameter_mm": 102.0,
                "belly_height_ratio": 0.40,
                "waist_diameter_mm": 88.0,
                "waist_height_ratio": 0.76,
                "neck_diameter_mm": 90.0,
                "lip_flare_mm": 3.0,
                "bottom_fade_mm": 9.0,
                "top_fade_mm": 8.0,
                "global_twist_deg": 0.0,
                "textures": {
                    "ribbed": {
                        "enabled": True,
                        "depth_mm": 2.5,
                        "count": 36,
                        "duty_cycle": 0.58,
                        "sharpness": 0.35,
                        "twist_deg": 0.0,
                        "phase_deg": 0.0,
                    }
                },
                "print_mode": "shelled_hollow",
                "stl_always_open_hollow": True,
                "wall_thickness_mm": 2.8,
                "bottom_thickness_mm": 3.6,
                "spiral_line_width_mm": 0.65,
                "spiral_bottom_layers": 5,
            }
        ),
    },
    {
        "id": "helice_escultural",
        "title_pt": "Hélice Escultural",
        "title_en": "Twisted Helix",
        "category": "sculptural",
        "description_pt": "Lâminas helicoidais contínuas combinadas com seção octogonal suavizada.",
        "description_en": "Sweeping helical fins paired with a softened octagonal cross-section.",
        "params": _make_preset_params(
            {
                "name": "Hélice Escultural",
                "height_mm": 185.0,
                "base_diameter_mm": 78.0,
                "belly_diameter_mm": 108.0,
                "belly_height_ratio": 0.36,
                "waist_diameter_mm": 72.0,
                "waist_height_ratio": 0.72,
                "neck_diameter_mm": 80.0,
                "lip_flare_mm": 3.5,
                "polygon_sides": 8,
                "polygon_roundness": 0.55,
                "bottom_fade_mm": 12.0,
                "top_fade_mm": 8.0,
                "global_twist_deg": 180.0,
                "textures": {
                    "ribbed": {
                        "enabled": True,
                        "depth_mm": 2.4,
                        "count": 16,
                        "duty_cycle": 0.65,
                        "sharpness": 0.55,
                        "twist_deg": 180.0,
                        "phase_deg": 0.0,
                    }
                },
                "print_mode": "shelled_hollow",
                "stl_always_open_hollow": True,
                "wall_thickness_mm": 2.4,
                "bottom_thickness_mm": 3.2,
                "spiral_line_width_mm": 0.68,
                "spiral_bottom_layers": 5,
            }
        ),
    },
    {
        "id": "origami_yoshimura",
        "title_pt": "Origami Yoshimura",
        "title_en": "Yoshimura Origami Diamond",
        "category": "geometric",
        "description_pt": "Dobragem geométrica em diamantes alternados estilo Yoshimura com vincos precisos.",
        "description_en": "Authentic staggered diamond origami facets with crisp Yoshimura paper creases.",
        "params": _make_preset_params(
            {
                "name": "Origami Yoshimura",
                "height_mm": 160.0,
                "base_diameter_mm": 82.0,
                "belly_diameter_mm": 104.0,
                "belly_height_ratio": 0.42,
                "waist_diameter_mm": 86.0,
                "waist_height_ratio": 0.76,
                "neck_diameter_mm": 84.0,
                "lip_flare_mm": 1.5,
                "bottom_fade_mm": 10.0,
                "top_fade_mm": 8.0,
                "global_twist_deg": 15.0,
                "textures": {
                    "origami": {
                        "enabled": True,
                        "depth_mm": 3.2,
                        "cells_around": 12,
                        "cells_vertical": 9,
                        "crease_sharpness": 0.82,
                        "stagger": 0.50,
                    }
                },
                "print_mode": "shelled_hollow",
                "stl_always_open_hollow": True,
                "wall_thickness_mm": 2.0,
                "bottom_thickness_mm": 3.0,
                "auto_clamp_overhang": True,
                "max_safe_overhang_deg": 48.0,
            }
        ),
    },
    {
        "id": "recife_celular",
        "title_pt": "Recife Celular",
        "title_en": "Cellular Coral",
        "category": "organic",
        "description_pt": "Veios orgânicos tridimensionais inspirados em corais marinhos e rocha vulcânica.",
        "description_en": "Three-dimensional ridged veins inspired by reef coral and carved volcanic stone.",
        "params": _make_preset_params(
            {
                "name": "Recife Celular",
                "height_mm": 150.0,
                "base_diameter_mm": 80.0,
                "belly_diameter_mm": 118.0,
                "belly_height_ratio": 0.38,
                "waist_diameter_mm": 76.0,
                "waist_height_ratio": 0.74,
                "neck_diameter_mm": 70.0,
                "lip_flare_mm": 2.5,
                "bottom_fade_mm": 10.0,
                "top_fade_mm": 8.0,
                "global_twist_deg": 24.0,
                "textures": {
                    "cellular": {
                        "enabled": True,
                        "depth_mm": 2.8,
                        "scale_angular": 9,
                        "scale_vertical_mm": 20.0,
                        "ridge_mode": True,
                        "octaves": 3,
                        "seed": 108,
                    }
                },
                "print_mode": "shelled_hollow",
                "stl_always_open_hollow": True,
                "wall_thickness_mm": 2.6,
                "bottom_thickness_mm": 3.4,
                "auto_clamp_overhang": True,
                "max_safe_overhang_deg": 48.0,
            }
        ),
    },
    {
        "id": "tulipa_minimalista",
        "title_pt": "Tulipa Minimalista",
        "title_en": "Minimalist Tulip",
        "category": "minimal",
        "description_pt": "Silhueta escandinava pura e serena com lábio suavemente aberto e parede espessa.",
        "description_en": "Pure Scandinavian silhouette with a serene waist and gently flared tulip rim.",
        "params": _make_preset_params(
            {
                "name": "Tulipa Minimalista",
                "height_mm": 175.0,
                "base_diameter_mm": 70.0,
                "belly_diameter_mm": 106.0,
                "belly_height_ratio": 0.28,
                "waist_diameter_mm": 58.0,
                "waist_height_ratio": 0.72,
                "neck_diameter_mm": 66.0,
                "lip_flare_mm": 6.0,
                "lip_bevel_mm": 1.4,
                "bottom_fade_mm": 8.0,
                "top_fade_mm": 6.0,
                "print_mode": "shelled_hollow",
                "stl_always_open_hollow": True,
                "wall_thickness_mm": 2.6,
                "bottom_thickness_mm": 3.4,
                "spiral_line_width_mm": 0.75,
                "spiral_bottom_layers": 6,
            }
        ),
    },
    {
        "id": "cachepo_botanico",
        "title_pt": "Cachepô Botânico + Pratinho",
        "title_en": "Botanical Planter + Saucer",
        "category": "garden",
        "description_pt": "Vaso estrutural oco com parede dupla, furos de drenagem reais e pratinho coletor.",
        "description_en": "Sturdy shelled hollow planter with real drainage tunnels and matching drip saucer.",
        "params": _make_preset_params(
            {
                "name": "Cachepô Botânico",
                "height_mm": 125.0,
                "base_diameter_mm": 112.0,
                "belly_diameter_mm": 132.0,
                "belly_height_ratio": 0.45,
                "waist_diameter_mm": 136.0,
                "waist_height_ratio": 0.78,
                "neck_diameter_mm": 138.0,
                "lip_flare_mm": 2.0,
                "lip_bevel_mm": 1.4,
                "bottom_fade_mm": 8.0,
                "top_fade_mm": 6.0,
                "textures": {
                    "ribbed": {
                        "enabled": True,
                        "depth_mm": 1.8,
                        "count": 42,
                        "duty_cycle": 0.62,
                        "sharpness": 0.25,
                        "twist_deg": 0.0,
                        "phase_deg": 0.0,
                    }
                },
                "print_mode": "shelled_hollow",
                "stl_always_open_hollow": True,
                "wall_thickness_mm": 3.2,
                "bottom_thickness_mm": 3.8,
                "drainage": {
                    "enabled": True,
                    "hole_count": 4,
                    "hole_diameter_mm": 8.0,
                    "ring_radius_ratio": 0.46,
                },
                "saucer": {
                    "clearance_mm": 8.0,
                    "rim_height_mm": 22.0,
                    "wall_thickness_mm": 2.4,
                    "floor_thickness_mm": 2.6,
                    "inner_ribs_height_mm": 2.0,
                    "match_vase_texture": True,
                },
            }
        ),
    },
    {
        "id": "ampulheta_hibrida",
        "title_pt": "Ampulheta Ondas & Frisos",
        "title_en": "Hourglass Wave-Ribbed Hybrid",
        "category": "sculptural",
        "description_pt": "Curva ampulheta de duplo bojo combinando micro-frisos torcidos sobre ondas suaves.",
        "description_en": "Dual-belly hourglass profile layering fine twisted ribs over gentle harmonic waves.",
        "params": _make_preset_params(
            {
                "name": "Ampulheta Ondas & Frisos",
                "height_mm": 175.0,
                "base_diameter_mm": 88.0,
                "belly_diameter_mm": 116.0,
                "belly_height_ratio": 0.24,
                "waist_diameter_mm": 68.0,
                "waist_height_ratio": 0.52,
                "neck_diameter_mm": 84.0,
                "lip_flare_mm": 4.0,
                "use_custom_profile": True,
                "profile_points": [
                    [0.0, 44.0],
                    [0.24, 58.0],
                    [0.52, 34.0],
                    [0.80, 51.0],
                    [0.93, 42.0],
                    [1.0, 46.0],
                ],
                "bottom_fade_mm": 10.0,
                "top_fade_mm": 7.0,
                "global_twist_deg": 35.0,
                "textures": {
                    "ribbed": {
                        "enabled": True,
                        "depth_mm": 1.6,
                        "count": 44,
                        "duty_cycle": 0.55,
                        "sharpness": 0.40,
                        "twist_deg": 45.0,
                        "phase_deg": 0.0,
                    },
                    "waves": {
                        "enabled": True,
                        "depth_mm": 2.1,
                        "vertical_wavelength_mm": 32.0,
                        "angular_lobes": 5,
                        "interference_mix": 0.50,
                        "wave_skew": 0.0,
                        "phase_deg": 0.0,
                    },
                },
                "print_mode": "shelled_hollow",
                "stl_always_open_hollow": True,
                "wall_thickness_mm": 2.4,
                "bottom_thickness_mm": 3.2,
            }
        ),
    },
    {
        "id": "cristal_lowpoly",
        "title_pt": "Cristal Facetado Low-Poly",
        "title_en": "Low-Poly Geometric Crystal",
        "category": "geometric",
        "description_pt": "Prisma heptagonal lapidado com facetas angulares que capturam reflexos de seda.",
        "description_en": "Gem-cut heptagonal crystal facets designed to showcase silk and dual-color filaments.",
        "params": _make_preset_params(
            {
                "name": "Cristal Facetado Low-Poly",
                "height_mm": 168.0,
                "base_diameter_mm": 74.0,
                "belly_diameter_mm": 114.0,
                "belly_height_ratio": 0.38,
                "waist_diameter_mm": 78.0,
                "waist_height_ratio": 0.74,
                "neck_diameter_mm": 68.0,
                "lip_flare_mm": 1.0,
                "polygon_sides": 7,
                "polygon_roundness": 0.08,
                "bottom_fade_mm": 8.0,
                "top_fade_mm": 6.0,
                "global_twist_deg": 90.0,
                "textures": {
                    "origami": {
                        "enabled": True,
                        "depth_mm": 2.5,
                        "cells_around": 7,
                        "cells_vertical": 5,
                        "crease_sharpness": 0.92,
                        "stagger": 0.50,
                    }
                },
                "print_mode": "shelled_hollow",
                "stl_always_open_hollow": True,
                "wall_thickness_mm": 2.2,
                "bottom_thickness_mm": 3.0,
                "auto_clamp_overhang": True,
                "max_safe_overhang_deg": 48.0,
            }
        ),
    },
    {
        "id": "zen_martelado",
        "title_pt": "Cerâmica Zen Martelada",
        "title_en": "Hammered Zen Ceramic",
        "category": "organic",
        "description_pt": "Vaso wabi-sabi de parede espessa com relevo martelado suave ideal para PLA fosco.",
        "description_en": "Thick-walled wabi-sabi vessel with soft hammered dimples tailored for matte filaments.",
        "params": _make_preset_params(
            {
                "name": "Cerâmica Zen Martelada",
                "height_mm": 138.0,
                "base_diameter_mm": 82.0,
                "belly_diameter_mm": 122.0,
                "belly_height_ratio": 0.36,
                "waist_diameter_mm": 92.0,
                "waist_height_ratio": 0.75,
                "neck_diameter_mm": 76.0,
                "lip_flare_mm": 1.5,
                "lip_bevel_mm": 1.5,
                "bottom_fade_mm": 10.0,
                "top_fade_mm": 8.0,
                "textures": {
                    "cellular": {
                        "enabled": True,
                        "depth_mm": 2.0,
                        "scale_angular": 12,
                        "scale_vertical_mm": 16.0,
                        "ridge_mode": False,
                        "octaves": 2,
                        "seed": 77,
                    },
                    "waves": {
                        "enabled": True,
                        "depth_mm": 0.9,
                        "vertical_wavelength_mm": 38.0,
                        "angular_lobes": 3,
                        "interference_mix": 0.70,
                        "wave_skew": 0.0,
                        "phase_deg": 30.0,
                    },
                },
                "print_mode": "shelled_hollow",
                "stl_always_open_hollow": True,
                "wall_thickness_mm": 4.0,
                "bottom_thickness_mm": 4.4,
            }
        ),
    },
    {
        "id": "lanterna_plissada",
        "title_pt": "Lanterna Plissada",
        "title_en": "Pleated Paper Lantern",
        "category": "architectural",
        "description_pt": "Pregas sanfonadas agudas com anéis horizontais sutis inspiradas em lanternas chochin.",
        "description_en": "Sharp accordion pleats crossed by subtle horizontal rings inspired by chochin lanterns.",
        "params": _make_preset_params(
            {
                "name": "Lanterna Plissada",
                "height_mm": 155.0,
                "base_diameter_mm": 78.0,
                "belly_diameter_mm": 124.0,
                "belly_height_ratio": 0.48,
                "waist_diameter_mm": 102.0,
                "waist_height_ratio": 0.80,
                "neck_diameter_mm": 78.0,
                "lip_flare_mm": 2.0,
                "bottom_fade_mm": 9.0,
                "top_fade_mm": 7.0,
                "textures": {
                    "ribbed": {
                        "enabled": True,
                        "depth_mm": 3.2,
                        "count": 48,
                        "duty_cycle": 0.86,
                        "sharpness": 0.88,
                        "twist_deg": 18.0,
                        "phase_deg": 0.0,
                    },
                    "waves": {
                        "enabled": True,
                        "depth_mm": 1.1,
                        "vertical_wavelength_mm": 18.0,
                        "angular_lobes": 0,
                        "interference_mix": 0.0,
                        "wave_skew": 0.0,
                        "phase_deg": 0.0,
                    },
                },
                "print_mode": "shelled_hollow",
                "stl_always_open_hollow": True,
                "wall_thickness_mm": 1.8,
                "bottom_thickness_mm": 2.8,
                "auto_clamp_overhang": True,
                "max_safe_overhang_deg": 48.0,
            }
        ),
    },
    {
        "id": "anfora_mediterranea",
        "title_pt": "Ânfora Mediterrânea",
        "title_en": "Mediterranean Amphora",
        "category": "classic",
        "description_pt": "Proporções greco-romanas esbeltas com pedestal suave, ombros largos e estrias finas.",
        "description_en": "Classical Greco-Roman proportions with a tapered foot, broad shoulder, and fine lathe ribs.",
        "params": _make_preset_params(
            {
                "name": "Ânfora Mediterrânea",
                "height_mm": 195.0,
                "base_diameter_mm": 72.0,
                "belly_diameter_mm": 120.0,
                "belly_height_ratio": 0.46,
                "waist_diameter_mm": 62.0,
                "waist_height_ratio": 0.74,
                "neck_diameter_mm": 60.0,
                "lip_flare_mm": 7.0,
                "use_custom_profile": True,
                "profile_points": [
                    [0.0, 36.0],
                    [0.12, 33.0],
                    [0.46, 60.0],
                    [0.74, 31.0],
                    [0.90, 30.0],
                    [0.96, 36.5],
                    [1.0, 40.0],
                ],
                "bottom_fade_mm": 28.0,
                "top_fade_mm": 24.0,
                "textures": {
                    "ribbed": {
                        "enabled": True,
                        "depth_mm": 1.2,
                        "count": 60,
                        "duty_cycle": 0.50,
                        "sharpness": 0.20,
                        "twist_deg": 0.0,
                        "phase_deg": 0.0,
                    }
                },
                "print_mode": "shelled_hollow",
                "stl_always_open_hollow": True,
                "wall_thickness_mm": 3.0,
                "bottom_thickness_mm": 3.8,
                "spiral_line_width_mm": 0.65,
                "spiral_bottom_layers": 5,
            }
        ),
    },
]


def _slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "_", value.strip().lower()).strip("_")
    return slug[:32] or "preset"


def _user_presets_path(storage_dir: str | Path) -> Path:
    return Path(storage_dir) / _USER_PRESETS_FILENAME


def _sanitize_user_preset_entry(entry: dict[str, Any]) -> dict[str, Any] | None:
    if not isinstance(entry, dict):
        return None
    raw_params = entry.get("params")
    if not isinstance(raw_params, dict):
        return None
    name = str(entry.get("name") or entry.get("title_pt") or raw_params.get("name") or "Meu Vaso").strip()[:80]
    if not name:
        name = "Meu Vaso"
    preset_id = str(entry.get("id") or "").strip() or f"user_{_slugify(name)}_{uuid.uuid4().hex[:6]}"
    norm_params = normalize_params(raw_params)
    norm_params["name"] = name
    now_iso = _dt.datetime.now(_dt.timezone.utc).isoformat()
    return {
        "id": preset_id,
        "name": name,
        "title_pt": str(entry.get("title_pt") or name),
        "title_en": str(entry.get("title_en") or name),
        "category": "user",
        "description_pt": str(entry.get("description_pt") or "Preset salvo pelo usuário"),
        "description_en": str(entry.get("description_en") or "User-saved custom preset"),
        "created_at": str(entry.get("created_at") or now_iso),
        "updated_at": str(entry.get("updated_at") or now_iso),
        "params": norm_params,
    }


def _write_user_presets_file(storage_dir: str | Path, presets: list[dict[str, Any]]) -> None:
    folder = Path(storage_dir)
    if not folder.exists():
        folder.mkdir(parents=True, exist_ok=True)
    target = folder / _USER_PRESETS_FILENAME
    payload = {"version": "1.0", "presets": presets}
    with open(target, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=2, ensure_ascii=False)


def load_user_presets(storage_dir: str | Path) -> list[dict[str, Any]]:
    """Load and validate user-saved presets from storage_dir/user_presets.json."""
    target = _user_presets_path(storage_dir)
    if not target.is_file():
        return []
    try:
        with open(target, "r", encoding="utf-8") as fh:
            raw = json.load(fh)
    except (OSError, json.JSONDecodeError, TypeError, ValueError):
        return []

    raw_list = raw.get("presets") if isinstance(raw, dict) else raw
    if not isinstance(raw_list, list):
        return []

    cleaned: list[dict[str, Any]] = []
    seen_ids: set[str] = set()
    for item in raw_list:
        sanitized = _sanitize_user_preset_entry(item)
        if sanitized is not None and sanitized["id"] not in seen_ids:
            seen_ids.add(sanitized["id"])
            cleaned.append(sanitized)
    return cleaned


def save_user_preset(
    storage_dir: str | Path,
    name: str,
    params: dict[str, Any],
    preset_id: str | None = None,
) -> list[dict[str, Any]]:
    """Save or update a user preset in storage_dir and return the updated list."""
    existing = load_user_presets(storage_dir)
    clean_name = str(name or "").strip()[:80]
    if not clean_name:
        clean_name = str((params or {}).get("name") or "Meu Vaso").strip()[:80] or "Meu Vaso"

    norm_params = normalize_params(params if isinstance(params, dict) else {})
    norm_params["name"] = clean_name
    now_iso = _dt.datetime.now(_dt.timezone.utc).isoformat()

    target_id = str(preset_id).strip() if preset_id else ""
    updated = False
    if target_id:
        for idx, item in enumerate(existing):
            if item.get("id") == target_id:
                existing[idx] = {
                    **item,
                    "id": target_id,
                    "name": clean_name,
                    "title_pt": clean_name,
                    "title_en": clean_name,
                    "updated_at": now_iso,
                    "params": norm_params,
                }
                updated = True
                break

    if not updated:
        if not target_id:
            target_id = f"user_{_slugify(clean_name)}_{uuid.uuid4().hex[:8]}"
        existing.append(
            {
                "id": target_id,
                "name": clean_name,
                "title_pt": clean_name,
                "title_en": clean_name,
                "category": "user",
                "description_pt": "Preset salvo pelo usuário",
                "description_en": "User-saved custom preset",
                "created_at": now_iso,
                "updated_at": now_iso,
                "params": norm_params,
            }
        )

    _write_user_presets_file(storage_dir, existing)
    return existing


def delete_user_preset(storage_dir: str | Path, preset_id: str) -> list[dict[str, Any]]:
    """Delete a user preset by preset_id and return the remaining presets list."""
    target_id = str(preset_id or "").strip()
    existing = load_user_presets(storage_dir)
    remaining = [item for item in existing if item.get("id") != target_id]
    if len(remaining) != len(existing) or _user_presets_path(storage_dir).is_file():
        _write_user_presets_file(storage_dir, remaining)
    return remaining


def generate_random_printable_params(
    seed: int | None = None,
    current_params: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Generate a cohesive, aesthetically balanced, FDM-printable random vase parameter dict."""
    actual_seed = int(seed) if seed is not None else random.SystemRandom().randint(1, 99999)
    rng = random.Random(actual_seed)

    base_state = normalize_params(current_params) if isinstance(current_params, dict) else copy.deepcopy(DEFAULT_PARAMS)
    params = copy.deepcopy(DEFAULT_PARAMS)
    params["print_mode"] = "shelled_hollow"
    params["stl_always_open_hollow"] = True

    rand_wall_mm = round(rng.uniform(1.8, 4.0), 1)
    rand_bottom_mm = round(max(2.6, rand_wall_mm + rng.uniform(0.6, 1.2)), 1)
    params["wall_thickness_mm"] = rand_wall_mm
    params["bottom_thickness_mm"] = rand_bottom_mm

    # Preserve print mode, slicer settings, and drainage/saucer preferences if current_params was supplied
    if isinstance(current_params, dict):
        for keep_key in (
            "print_mode",
            "stl_always_open_hollow",
            "auto_configure_slicer",
            "spiral_line_width_mm",
            "spiral_bottom_layers",
            "spiral_smooth",
            "wall_thickness_mm",
            "bottom_thickness_mm",
            "drainage",
            "saucer",
            "resolution_angular",
            "resolution_vertical",
        ):
            params[keep_key] = copy.deepcopy(base_state[keep_key])

    params["use_custom_profile"] = False
    height_mm = round(rng.uniform(115.0, 215.0), 1)
    min_stable_base = max(64.0, round(0.40 * height_mm, 1))
    base_diam = round(rng.uniform(min_stable_base, min(126.0, min_stable_base + 38.0)), 1)
    base_r = 0.5 * base_diam

    belly_ratio = round(rng.uniform(0.26, 0.48), 2)
    waist_ratio = round(rng.uniform(belly_ratio + 0.22, 0.82), 2)

    # Bound radial slope dR/dz <= tan(30 deg) (~0.577) so base curve + texture stays well below 45 deg overhang
    max_slope = 0.52
    dz_belly = belly_ratio * height_mm
    max_delta_belly = min(28.0, dz_belly * max_slope)
    belly_r = max(28.0, min(88.0, base_r + rng.uniform(-0.35 * max_delta_belly, max_delta_belly)))

    dz_waist = (waist_ratio - belly_ratio) * height_mm
    max_delta_waist = min(26.0, dz_waist * max_slope)
    waist_r = max(24.0, min(82.0, belly_r + rng.uniform(-max_delta_waist, 0.40 * max_delta_waist)))

    dz_neck = (0.92 - waist_ratio) * height_mm
    max_delta_neck = min(18.0, dz_neck * max_slope)
    neck_r = max(24.0, min(84.0, waist_r + rng.uniform(-0.45 * max_delta_neck, max_delta_neck)))

    dz_lip = 0.08 * height_mm
    max_lip_flare = min(7.0, dz_lip * 0.46)
    lip_flare = round(rng.uniform(-1.5, max_lip_flare), 1)

    params["height_mm"] = height_mm
    params["base_diameter_mm"] = round(base_r * 2.0, 1)
    params["belly_diameter_mm"] = round(belly_r * 2.0, 1)
    params["belly_height_ratio"] = belly_ratio
    params["waist_diameter_mm"] = round(waist_r * 2.0, 1)
    params["waist_height_ratio"] = waist_ratio
    params["neck_diameter_mm"] = round(neck_r * 2.0, 1)
    params["lip_flare_mm"] = lip_flare
    params["lip_bevel_mm"] = round(rng.uniform(0.6, 1.8), 1)

    # Sync profile_points with the generated 5-knot silhouette for seamless switching to custom curve editor
    params["profile_points"] = [
        [0.0, round(base_r, 2)],
        [belly_ratio, round(belly_r, 2)],
        [waist_ratio, round(waist_r, 2)],
        [0.92, round(neck_r, 2)],
        [1.0, round(max(12.0, neck_r + lip_flare), 2)],
    ]

    poly_choices = [0, 0, 0, 0, 5, 6, 7, 8, 9, 10, 12]
    poly_sides = rng.choice(poly_choices)
    params["polygon_sides"] = poly_sides
    params["polygon_roundness"] = round(rng.uniform(0.18, 0.72), 2)
    params["bottom_fade_mm"] = round(rng.uniform(8.0, 16.0), 1)
    params["top_fade_mm"] = round(rng.uniform(6.0, 13.0), 1)
    params["global_twist_deg"] = round(rng.choice([-1, 1]) * rng.choice([0.0, 30.0, 60.0, 90.0, 135.0, 180.0, 240.0]), 1)
    params["auto_clamp_overhang"] = True
    params["max_safe_overhang_deg"] = 46.0

    for t_cfg in params["textures"].values():
        t_cfg["enabled"] = False

    archetypes = [
        ("Ondas Harmônicas", ["waves"]),
        ("Coluna Canelada", ["ribbed"]),
        ("Cristal Origami", ["origami"]),
        ("Coral Orgânico", ["cellular"]),
        ("Trama Ondas & Frisos", ["waves", "ribbed"]),
        ("Cerâmica Texturizada", ["cellular", "waves"]),
    ]
    archetype_label, active_layers = rng.choice(archetypes)
    depth_scale = 0.72 if len(active_layers) > 1 else 1.0

    if "ribbed" in active_layers:
        rib = params["textures"]["ribbed"]
        rib["enabled"] = True
        rib["depth_mm"] = round(rng.uniform(1.5, 3.2) * depth_scale, 2)
        rib["count"] = rng.choice([14, 18, 24, 30, 36, 42, 48, 56])
        rib["duty_cycle"] = round(rng.uniform(0.38, 0.78), 2)
        rib["sharpness"] = round(rng.uniform(0.15, 0.75), 2)
        rib["twist_deg"] = round(rng.choice([-180.0, -90.0, -45.0, 0.0, 0.0, 45.0, 90.0, 180.0]), 1)
        rib["phase_deg"] = round(rng.uniform(0.0, 180.0), 1)

    if "waves" in active_layers:
        wav = params["textures"]["waves"]
        wav["enabled"] = True
        wav["depth_mm"] = round(rng.uniform(1.6, 3.3) * depth_scale, 2)
        wav["vertical_wavelength_mm"] = round(rng.uniform(18.0, 44.0), 1)
        wav["angular_lobes"] = rng.choice([0, 3, 4, 5, 6, 7, 8, 10])
        wav["interference_mix"] = round(rng.uniform(0.0, 0.75), 2)
        wav["wave_skew"] = round(rng.uniform(-0.35, 0.35), 2)
        wav["phase_deg"] = round(rng.uniform(0.0, 360.0), 1)

    if "origami" in active_layers:
        ori = params["textures"]["origami"]
        ori["enabled"] = True
        ori["depth_mm"] = round(rng.uniform(2.0, 3.4) * depth_scale, 2)
        ori["cells_around"] = poly_sides if poly_sides >= 5 else rng.choice([8, 10, 12, 14, 16])
        ori["cells_vertical"] = rng.randint(5, 11)
        ori["crease_sharpness"] = round(rng.uniform(0.55, 0.90), 2)
        ori["stagger"] = rng.choice([0.0, 0.5, 0.5, 0.5])

    if "cellular" in active_layers:
        cel = params["textures"]["cellular"]
        cel["enabled"] = True
        cel["depth_mm"] = round(rng.uniform(1.6, 2.9) * depth_scale, 2)
        cel["scale_angular"] = rng.randint(6, 15)
        cel["scale_vertical_mm"] = round(rng.uniform(15.0, 30.0), 1)
        cel["ridge_mode"] = rng.choice([True, False])
        cel["octaves"] = rng.choice([2, 3])
        cel["seed"] = rng.randint(1, 99999)

    params["name"] = f"{archetype_label} #{actual_seed % 10000:04d}"
    return normalize_params(params)

# ===========================================================================
# MODULE: vase_studio.studio_ui
# ===========================================================================

"""Self-contained offline HTML5 + CSS3 + WebGL2 + 2D Curve Studio UI for Orca Vase Studio.

Generates the interactive 3D & 2D parametric vase design studio for both:
- `mode="page"`: Wide 3-column studio tab inside OrcaSlicer (`PagesPluginCapabilityBase`)
- `mode="dock"`: Compact tabbed side-docked panel beside OrcaSlicer's 3D Plater (`UiDockPanel`)

Zero external CDN scripts, stylesheets, or web fonts are referenced so WebView2 runs 100% offline
without network permission prompts.
"""

pass  # [bundled] hoisted __future__ import

import copy
import json
from typing import Any
from html import escape as _escape_language_label
pass  # [bundled] resolved intra-package import
pass  # [bundled] resolved intra-package import
pass  # [bundled] resolved intra-package import
pass  # [bundled] resolved intra-package import

if "DEFAULT_PARAMS" not in globals():
    try:
        pass  # [bundled] resolved intra-package import
    except Exception:
        DEFAULT_PARAMS = None  # type: ignore[assignment]

if "BUILTIN_PRESETS" not in globals():
    try:
        pass  # [bundled] resolved intra-package import
    except Exception:
        BUILTIN_PRESETS = None  # type: ignore[assignment]

__all__ = ["get_studio_html"]


def _studio_ui_safe_json(payload: dict[str, Any]) -> str:
    """Serialize payload into script-safe JSON (escaping `</` and line separators)."""
    raw = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
    return (
        raw.replace("</", "<\\/")
        .replace("\u2028", "\\u2028")
        .replace("\u2029", "\\u2029")
    )


_STUDIO_UI_HTML_TEMPLATE = __import__('zlib').decompress(__import__('base64').b85decode('c-rK>YjYz>k|6fIe?>HArw6D4K)lFev5M?tk*w;PsVdfy?C$C2aJfk!L1Yui#AGH&f;}Z$yANlQ+38_-GVR)#%=T_2ne5E;;Y=spnypMHv#ozJzhHlY+&vx{5gC~PSXJF~QqL3t#KS$p!^6Wp!o%a~=lh3yC*Qq2V54+0-udh)ez36@UT#;;&tJZIdGd1i)%mO4H!sf5D{K(Ndh-6uql3MZmxpgC&r7{VI`SvJUgYGfgVzU;jgWnB03Q=S^;m!8#fhJ8S7zz3u~}hjG9&b`{&nErOrtohuznP#eh39`f<Zdk9{ATm-*3>5It#)e4ZLw9>3d^;yWMPYKxvSU{hh<O@3C*Z#AnCpY!F0G*LeD8Pm^?xpIdPhrS;EF^@b0;_^NWoe*BEFM&shL;Z3Jo>=*5g_GY{PL?%wX&>v&6-)VI=RC3>o2awuX?`(EkMrvaeUHdWS^}DUEr}BbuI!h7IqxR#ruaaf&8)<~tJKfGB4WP=sh^TI--D_{E+|dl$5MN$+)lRR@I*;nC+pV)!b9196%0%(Nj~mJC0*C?iyY22quVv<?aTH!cUa#HTTo)Zo{oAxL@q!T2eSg>)8tJpt$G$)IyzWIu%NPU`NZ#-tJ=%Q4lOq_GhS%@Iph8Zo<!wIR$mJ-4wOSWLZ#|!%M8j0{vsGt6J@~V+jvZ~U*Yd@A$J`Zqo1#LJdg&}_L|25jzq#Hu(r>&N`#v0AbXzSWrymC?<*dWli=2@+h;BqPTWoWB%Q`*yBO4(8-|WiP#@-+RPzjK0V|r_(O@OkGt+X)=PrD-%hY^y*3zIE&?Zs8mcTBCb%CUbL`RwbLl{!Oq9{Y`Co}~Vy&Yq2f@anbKKc?T$srXR@Y!%hn*B7%eoz)paZ6tmi3~L&$Nfbs~tg`39%o_wA+lvN1z~76)BpQ1OVtxJ^$~2Dr%h}kAArGr0Q?Czf{_Zn#(v5@5QJSB1I+tm)Zb<*xvu?OPd^Ggjv(EQ?7@ORzvjADMZZPnBe!pne^&bt|gT8CltpihKe_GAQt%8X+SReHLo_pe5Z1%hTVSeJZ`<+hb!ZGpI*Ed>^TDgh$=wfrjF};YvHy=N`D4TeX9&cPMoOoRjFzpUWn09BGiKkWQtve=O`{J?RyKqgs!Q;)2d*TfqcUztHB_>{*hNaGWH22y#GQf)ui199>+eQ-H1xSA}9FT-SCtiGs)F<3iZ!n-TEvk#FWgW^7<^+V+C77A5)-SQ}$Vbl3ej{y%<LG9KjRN4W5YsNa{?%n1&BB44ynF%>ZTitTie<WD1j?d$IP@mLcrFVlF_0C29{DIKn(JIvz>N1Bs##59zgdE;=a2n9q=iw)7or>g;wnf5%n7WNBkHyn;))x<vN|9FY;DPsNk5Lp;|nj=DIsK;#7IBixhgf%7zn{fLZb+zh9EU!;HAQfquJylS5c5spI1Z`k;26&$koRsEkeLsG$9JWYn;wm>0*|qQHY8Oh!_x_L{zG53|A12K%%DBC~2u;+*JyIZYHF~0E7GEF@YQe$#m=ixZ&6*D&r?i{1|Ws5il%3nN5hvO8F9iuRUO2fp!KReFo$AU`=5g@l+=|V1vuB5x~*`ghU$nF(&^oOVVICZwSq8i;>iCT=?mY&sqM`n<8$`8frp4f>|n;H0PwC1wbD}5XET(Vy+D}VciJ^)~J)DttrYRqZrmZF^}(H85sDtTdcz;a`OT>ZO}lZ)0MhQoe|6PBnTUV)Gdh?ng{>$W@)738Aq3qK2JK<M3KKOc72p556);{)=Mk`jjFc0>jVF?E>$Pi`ej{8a~f}=$Gyig%MvWAt)h7%lT0OnjItQUmgKQZ3F``3EXYHeda^2)o8-@+p-s_<qnp*oRmdx&S=n^H5rg%JFH5?>?J9xmrz!Fx%mKb^GzE*_i~uF2`zUp9VsFY(U4v}pO(rQ)B-w->qs@n9CW6IJyqMBGYsQ4^^6|>8C0dfCzy_y4$#Nwn(1xH33HE@GplB4;CJjD8O4x+h8b<vY=ZR>RBHL%Hl@6g$I5(%jnm8EKz?PsvNDJfAETK^em5X-UIa?n;E|F%ap{_W14)UV<ms{=IB^-w8%&nXyFkz~oI8JZtY<=VUrdBM&T1tjNGiGsu?U+V^q)ho})-?*q6nn7svC-Gu@_`jZs+Cfi>$K(il-&Xkgv&Lb>eRPk6i<XUGWJscyDHGw!BqtF-mJCmUPba+V-79O5<+X&)dst>Ay!<M7D}|pGC;)$rb&>Lu+d8MKiA-7>i79v&aWB;2p4j{Lm5V+GdDe2O(oXNHqFC+L6cS-&5~u)n5S;7JlENreOAlNlE&CaOQ)Tes)}!MdEHEy58@Pi?KHg$C{Zd<jXF)N0|K!Kk~WLt2&^~1+TCb@qGB<}AWC($=#i-vJ#vcKb*|Kws^=Qr?9oN^T+MBGq*5fS>j`2UU7#=0@IC^egoSjBY8hI`WvJz(k86=%L1QRgycQX#mVj__|DyH8SUY;Snpi6grs>??+Du9`EF2NO!fb_6THS(y@h-+7NQyNrYZY-VO17mb@bGoSg{XX4p~|uX*LhHbOy{UU_BuM*0CvM0gV+`pIaX~1z&BLQV30>jorNNNV&pnqWKZN}fHW;|BPla2OyU^!d){bxr#EG}L0P(eV!)`Cj>a$3U`Z<6O<KGKK*efLR?}J*3i={}ZM3UgPRpXJaJ>n{HFCIV@ERsN`!<TNXqK@TF$fZE_uxk5{Fqt8QpJ%%-CSTV0R#y-_ymD6nc}=?a2pR~S+|Q;Bvc2*rrPb1>e?Q{D0eq{McNIHA^_m~2lufljg~IhnsA{f?6^+rDs3!Q`vn46)TYvUb+zm-sLiYMO|6BaARFHR(nxJz2@tuutUx?%qlfd$e$>BWucLv_-gwu+rH2*RiFc8(Dkm4Lj=1*wfcDa76DV0Dh8jS{Mv4WE@l*ESN8T?otUF=xQD=I^3%zV&L$3H5r4>AYC1KoamA2$*;a2I&#-dZ5cPz{Zh*TC`Bhi;@Sc>?XOuVZTMKkM4)P^#B!vfgUth7HN$z0UL^4$rT9edErgnhw|eW8bHq7*4muAqFxouJ8}_EDz(rqnmM0tHI;r`So}FtAvAbhfhT+PEVI)bz30bn3(KB))qCZ(ZuG#Y}v^O-5?}g*Uj&x4%_9OS4hRWYy9eQO-$nZ_c+mu#n;3#(v_bNv1bUDWNe8#z^zREn8wc)aSRD+#SfIGg49j=#PS_sRehX7Hn?`tQQlwh?pN{LS?(RWs*84g5MdPTUr9vmfIzD>Um;Rk_PHz=722F)?$C^dug>(ml|7(Yil)oHx;+3)X_(4-PGh9+KAMiI@v}JF^-aw(@3sIu@7wm8m&AnA6XXmM#egy-oVaumlbzgd%4}#UScoYs5^=c97VO#bIyC4z#0OBRTr$n8lGh&mc{_tVX)Xi>bA@+r0#}WgZl_)Vp=oEmF>sk6G5Y}+Pqy>Eh{-?ac`ZjwBxI_47k*8*yHAA;p(TP)<<r}z#l86I-A&F41k<TX=0PhPM0@Khz9XXo;z7PiEZ~x?wO+9WnN@nKARo>59ZiLUXW`pDn&ZCW7{`B**^kXT68R(>UOhT>p|jO`wan8`g`O|GJTh_pvh90)99I25hbDQ9C*pdFENg-wlt%uAG(wVt7vw#YT3j3WWDF9Yti}C3P-O!x0)ifSgt%B`<D|W<$xR1$2URRA90hxzbtcP_*o8<JDL%#R&8u(nYFxbYqYr&Uwh*I<o0l(<tzHOnug}yW$Wy-y;%%E_Pp@gOW3pMmd3e{i4A`cq)|-jaEa>k=~b4DgPdD%zu>Ly^DY>Sc`*iyxx`JW(`lI}1^qZml93niA&6%EkvO`M{6W?f;ls87lDwSyVB6D}tedO&Eh*u)z-h^4pcJ!l*5`f%uo^L#+tJM7eYW^~)P-v$JFuV`3;Z*9wNVhJdHYwo&E)$(2qwy)JO+Bg(zXXR<7mt`Q2J>+USLWV?_hM5ZH`c2;6CjJ1|k`I7h;>*6#d=BdY2)z)>|zN>a{n{M8ryVkV%4YHqq7V^)kl)2y05uGQx28UwRN}77giqD?0+T7wqG_%liD`&PN1k76xh2-cAu`8+u7wZmAJ%Pt*An<{hj-mwx4}Nk|hu1%A|gc)cl@;ZUfrHQJR{Ab!_Zb#BTz-R4N<*w$FkA<aRTeruNAeY@GUOoHym@Gg*?-cg*cc}SZ6kZpbzkh>GoGwlA$*t;lm?Pw?Wrk-X9XuF?unX2067iqXyJ&7(a$EJ!&UsrajTv8yaedCl6H#oLsHg<$_g{@I^d)8QQ7M<f*C^I`DJAc>UwsfFI{mh-+ZLtO+m?6b>#&Uk^EBa1sCb<@FZC&^<>~g<Wj7p{Qq_E*~_Sh8dNq^U2s<eGlbUMpUD{Z0_GP~IYeUP^LBfozI*3d(iAA`lN`>TL7i01O+_-(blA^ih!`hYN>LGj&wABccQp0B()sws5dgVPDb{elx7TZ#Ng_L*}_X0dCoY;V&KGY^%e&(>&W`?sIsK*+dFu$23)Yll78J+rw>Z%Se<I*+=i>h-AD7R`BNOMJky*RgQ^SxU>u)W^bEmmBq4V8?-^i;gkx=J#0h^25^Vu2gQvNR8blA3NKhZCSIaT%#90P(_`|H&5;#(FrY$59{u;Z^V5-n!f6CAmCc%_+i<r3=7;)a7u%EuUw+~LEMMs+DlQ&vTjE?Kv}mOb>ArKilgQq<+kQ8$GR!M;NDx_(svo{w$AfT!=gK6>!mJ$VR(bCr%-epOi==54O_hUuH1AXC>s7X&^pN)uWl5rOK$lVcZ5zxLH{cBlZ5@#8GKV`o?o!HejH4E<fpID<V8lhff{m)@_whE$}d>X7C!R`usRNP?|Jq%En};j8C&-1{SzL6uDEy6`K10VijGS<vn+8;w#<Q>j`<UKy%b!KSY^w{*}T$|=H<+0J|l3Z6m1OkmfWmbf|EYQzK+}ZpkO|&GMq~uJd_TYMc9Q78_&lPtY+b5w)`FP{Z+2Uf(%Zhh%V16cgK<gJGs6KU&c}=BU9cjbBiXs`2y=gzls8#HCSi8Lz=lJuiIju3|fCV_L8Jn2_MY{YQhfUXeu04aB-N$)lC8TqxxX!TL$8UF1z7gQw`T{8ke?wp{)AY=RWK1ON8w*hZ~1VPMyrV^JvgN{Q*Y_4L`z3(tR$B34bR^n~%39WiWpV4<m`IaT|N{Rj>V(?cVBei#oE@{psOwbJ%LJcK1G)99;LHQP{aJLW^CuW-<+8Q0mbIx^dx!p<i&$ULs$mLTAd?LczEp<d^eKk>diLo3*V76J1l(cAnTS?A?+@Y>A7TMf&(V7X`skOM(mG9(wP~zi!YNrNnm7Z@4@{uwc#URnh|v==OjWdMa>C(du2=0H?P~2cdU59CR;RIr`p29gezrNxIFiZ!EQ3>$Zq%jqT6UB@w#y19@?x2>+@+eG*VnTam^|DaZV2I8?ZAC1{<<e5eW)(x1S;qP5b>U+7C#Y@%5`US?6u*ZN?$4GFN|G`E-pE8l*WuGBy=?;;on>70G_^}f`{L21!04=tgLThmKk9`D-5%wsL?!K$a~8wE2C8_V}gKmNheVjjHbZGdI`GO%Mp{Hx#-hTs09(lgdYHvt~;qkbDrGrDpw2%vLxTJUF+2kzP|^j?gvYEHll)|&RC$Kour(<+25)<Fk!bUrMBp7~vNI*a@+CGl5wU2hL#{HI%$*|8)-ocL)R^jC8#d8b!xT&>_+E1g{Q`q!(w_OzS#iQXc+j3Wjdo7~@%#`N@m+$nPO*D=y$FLnqr7PE~~uigc`+V0kJ+G)pHvuz!&Y)LUXusl<X0G5l?NS(obFP(T(D0}IL1Gky5L`WNllv&0@_r5V}-q{UzYv;;+mltXzH=gtb5Np$8^CbGQlLtE1N@Y3<&_!>5(D24So`2lW+*<GG>Z&;4b{`Kn)`cNyYN8#^!s;-636~qrLG5nlKJvI#D~QjvAZC@?lQGRz3UIU`%~b=Hh~Sv5<LfSiOy1oojK^RR{)4SFA*TuOFi7)yZ$~>EUiNaAJG$q_daYQr=mpJ1)*h8*^pX|BWY`oa@cMVRw%bvP<q;{5yCl@v^C-geD%36c*&VDkl=7qNy68vshFx{Nc~lyb1=gTAavfb7olq0e2<=upM9b{wt{%G2jIZI^U9wHL-1O}g?KX94pX%C)J{L_+<(uX*5Lhm7%e!oViUU@tjdwCv@OZV_ZnhrP%<3N!eT73P3c<3zuG8(tlR-NDTYiEL^>Zf7avG-+m!@m*$RFd;Hgv^tIe4)Vvg9U3f!1T&yZN9pIo{`thyPl+4t$KgGFx|RY0ipXlCn1uuw~Ha5hlpR3X}DvJzL3#!L2_qHl8+CTgi1E!n+FGZ^CdGEb<yKoL<@+i_bD9gWCOL3Knc!6ozkF9P)9|`II^J1x?U&v!;G0F*J$Cj~`om)sI`(H^Nab8%RS{Py}zUFkG!#9;hG3QE~Xeoc;|wxBU_S1GH@K@b%l>y%To)a{r*Qf4KJ>_WE%DfK~s3HiL1KYP*7ACMtiyprxS~qp*?wI|+Nb%^qX4zZ$~&m~F$EgdS3-b~~&Ha`nPeb|6(t!NwTM1vOo9QRU*T+~SKWI|CA}V7C{y%69z{Gq2G$ZZP%Mi>@877@MZ7DfVuky8GI31dDs5?H`LP9z}q4+rM~Zmpia}SJr&}EMld4`jLVobdMx%E|SkesP27p?G{RY`=(@s3ZfWE_7kkrDup3qN!3eB*zuyW1*bUv(*mR%q(kq|PhsBC%W-r83{h6Hlu#x0l~1M{08f$B-mbusH1+eOS+Y4r(0)NKS|T{cO2W*BC}4cF7H05x8<Su>ie|WVUB4#;_=%exK@@(RcI9J==o^D8k}u`{^@%<`KBSo%JUPZe$YnwOz925)kB<`c0~rMx^0B%pf$;|V;k7@GrYmrWUR(CJpm+ad;^Q+hRb8JW1%=Az19Lkz-riwB=Q3VsQFS(3S+Ky)h88TaC3Yy@LF1mTiT9wMu89|_$Ol{_K=zsyYGLZFD_bH!%|UR@`shOjY1(rQkj2>3&l?SPa`={gb+EgCaKsu7N)<0Gn6-E!Rf8fLRPB`lk?YFG*99t!l&tNF{SKC@2Q`!HORgnsSK1pDp|0@nsMtJ<ZnrBfbXn=a|0`&9kGCs0A{B<dLRSDDY+yVB-a{2xrZxo3PP3zuaI>TDO}8s#v>3@hfNdnxv&KR5rd~Q?gYC-eP1YT4jvMXfI_ovp`yKeie_i;uF1|l*t~Z*G@N1*f?6O`1iYAR-vx~JF>y2K&(QfoutHH}a@mB!#uCnIFxB(zBihm#e0fbHV2ovD5-DWMl60pzpr5cJg7>nX@;m;cA1CT2s-zqQ(0n8pcKvf)%oMBO;F4vX==oEZwC@s1o;aPe$@D1G}#2H;dsXX?>OB~G27BGc3o*_$x1218R@ue4niJerK7Y80c>fWyG`$=#avNwdoAe2rU;|G5>h1#f#0@)Ovtr~0<;at8q4t_twu#vIHk|6BIQ5f8TN*GLVrAZ=4#(NkZ8$=9=c03OHYKG-#tc9bl?ASErCGEyGIKdok<T?5A%t0`QC7-kN!Uv@~=;QU1w>;M|+-}emZ`}=>XYKsM-(j4E_kYFzthd-?!XT~H>`f*)3M@wv4E|k!lX8e__@xryw|E9!{Nq3Wzf9my*ZAlQQOMaQCl<~4-4z#O;g%c-m`F7UwR#yUS+UXAP=ZzW(s=yv`x?G?$hZHXUH{Q+NgjCYF9Lq#E8yRm!2fO`aG3Ma1k8*a2Ha<{*?8w4|K`8>-`#^mD_79o3<<({GK*ng5}^Dse)D~p*^P-`HU_SqgDSVE>sSPO`u90t!gU#e;j@#%m01Uei^UwFWa>kkw#uYI2DY3jgI)oknRn?c{3>DRoF23MdiTY_`Qcl9yYl$_9J)(Li#kZ&cjX=2_u?zI#$J(w-p(KY`ad}t7r$^`B_<}7Alu$K*?o2_)q>Dd%&n|OvyWWht6-s0SrARP>XHr1x5MR2otfgIGX*4{3w7ps6i+;>8^zFduuA*2A*+lXekayT?ggLgo;Glvy7Q7t{P+J;bWhmaM#)3x={w>Amk#{t8Vpx9qOW&fzG2<Q-r=jSU%z4B9v=PX`0eiAfgD=gVzu-=rO?VzL@=)oo}VxdWQ)B$IygQ!Ic5*p@yl0V9e#aqa&iDaFf`EDN8cQ<gZ-B$hf=AeS;bH61fDGZwX__Z>SGowS{EtU7!|718;|{XPIs3THU$PJjBXWItbSsixf1HgWsq2-gtanfF<y-kg6?J`^a4+l!Q2@56dG$BCHZyIG0DXR@GMH0Th>ZpB!!Q7*6K;N6C@5~Dmh^bphYVyJ1~&m_}YtYd6?6V4B}eh&NBL1=~h=w9Z)Z9=p4BSX@$z*23P}NZT0<8GzMw5U3n8teAKOY?PjxS=zcDGgY+B*@uZaC{HP*Fav5<cN8#uS7P5Pg)rdQ*>q%BP+KRhNqPQM)){wP*4~!}gwN<UXka&)1J15Z~N?h$NL!d*BxFVi|F4MtExP1S&@a@CUT>26BJj)@<azICoChz|pe*Z9Jz+9*<=1|G>ojtEV@~7|rj}O9vPhaLxP~y&Of0o>biTIY5#X=%+$EvKWvr5uFBWq6W*s(9zOYE_5NLI1n4k+wfi3rX%{eDs@tfAe(Ud%8Q>KD{#4_fb(#F_aJjpsaobj3i$lXmukxR1{XJIo%7l4hS&K*UP9NSemcP(;YlmM#&b(3sJ@zqmbgF3a!m;A0E;(LhB3&um0_47}J5C*iB$I`)Z>g}hlbvUa#Yn;PQYJaLc~tgj-sh`Oy-wnqeZBJwjYVgbq_)uQlONcGWogpI41aLl}&@6l%jt<?8_%^qzu(Pnk=SDyM}%wWy8#z40=^aXyyTHsxaPa4UQ5}d&P_|N|(XZ!-5$cd6d*^-6EvnVpMHDOHP?Z`NDHwH}`L`jseDRcrpLfj=0lQWtz58Zeuzt2PG`3dtbyx=x!7Vs1)BZ7+Alozv1Qc!N<(s7M-xGK(8@hlFHA}bCSqF!+%XyPN^olhn?DQXH~FZP6g^dRskyh4HxIe&yUxmtAr!unhyDr%gwqCXzbKcJ={M~n_GOIN+|f+W2cQeN|3NJGDWbuXObV0u0TY3~;fdI2Bgpj`OZ{<xHNj4HSaT}Gg<!_Q>JI<$+8{%DSR%dGyd{ba<BveUK&c2;&S_meL28rmJ+*!TY{7~D{dz4pc<uW*4bBVh*g9CvHRxK^xI4OW>n=zHTLMJx9MH-2d9%RNOLg1v(`CkIE$@_vcGcK1$Rf|cFfXWt$?d-1BnzIl1@?c2knlR}GIcMQpFZEcBFv2F6ps9r1=*G4b?nZ`LM(X{ajj|5+PDVo1y(7G^8LlzA+V<Vjxte_3XUShU22VWZ#0l1=7mAiHN&XjC`$$rt4$Rmyr{0XSE;{mFRSEj}T8o0=Wh13U*I!O3Wk2da~u5mymumL-$%TbzoImlYp&YmB?|Jw=h3p)|1%K!%`DX3)7qKRb*A$;<2uk5^y;=T`-ipQQ|@JWxxWC`H?2rrwRU&K*(=jVX)+{(@~%7$^h08Q{9=||U~4=n*5ufgYlQsT}({>^{?zp*0^<i>B=8hZ;uci^+?3Hiyr|NDM0h-yn95cfH9IAr?HYi~;1G8i>v1e2Uq|KZ;|0NeYqc?Is8U+UL6k<4!W#=p^w>uE_(^Xi!cpO}S-jnhV>$^oi>_20rMr7)9GF<k<OB49ZRMNjC=|DuSw6owm6b{2uBGCP0#7k?#%`4VswZ-(b-3m}V9(C+{G|7LGdj|fN63h+U~%yp|kp|O-ZavHFa^SbA-IHx|ymIIiV!7a_4W$;gfFppMj{_oDfkT{}vcR;tl`471>4r8S!Y5i4%?O?~`G{+<OtC%`3!(qgp(KAYx$R<gg^RvsA{=5sG3~Ezxoz{u+yeL1<fT8&pe_4FKXV%~co6z_O#1Q3du?eyaL%o<y*I2Xr`Z*eC&Eu0-3~b)izXVyr`fKc21Y&Xb0#<C#K5fbo>u{Dfz+ArY2W*U+Ai^2ZMIHMxQD)iM8TOgkAOH2gDeiYxoA-G?nD}Ax{{I9!$-nJ`2$`^mU8DKnqY{*zI)9#nY4H|b&jIcc$D;*D-r7B$oY@KK=d$+BE*f%P%-;VS)Fizn7!lP5e#hq(lGeCK{srUxq{ry+Qn^NO54B^dp(wvoeTrnxs4gbdPjB^W-;RTF-MXC(&V}nk*3yAD@XJoZt^36l9j|^X8+VTnf0IA#HdRTh;e2DSK+n!@>y|0n`kmm4-CK;)1!hnb!RU&0d5t~ClkD=XH14!J9yfSh2d?YNPN&%eXx(PVxpU%HzCT{qCLoSS=c5Qm^Zj2#r{ajj!s3om%?8zUcMQO7uK!Hk8U&NXkPy|$q_((ERL$L+c6;OfU-3U1t)IR_kx(#Tc1XSL_4|K&ySPiLVgdJUHhcf@?|=IK@GC5po#(;W!zXlb^-7ydOefzEab{=!i{2)?{OS905(jvi9tZFL7H#H&qfVn6DOM?9wAT97!aleJBEm-fT3qF>XpTAB4ez{c-+3CyqQ?DhrO|2koPN<74mSE7w10!0+{yse&p|5SB6x5MAE6W@1uMf!n1{p7es{A3bHG)KJ@1-UBld+inLaVZ^fJo|jgU#PPeaI7e{;RdyYt8Y>VNL7J7?iNsC0ox1O&FX{>Q)kSL+`QaCaa9e{q>UaltL5r*?V8;Chv~W9<%+W@9Qzdme5<2qy^k7L<jO-4t<)rIOeAoW>Cp->w8nRM~l%l-MH0b%$|eodH1dIZxerj?TIMeZZ#CGzS#Zc0gmiS3CJFoE%J%yo2YS_v(J&=scu>f%p5FH;D7T01hqq88w3K&%hWH9#vq5p=%@_vWjPgs^5tHMPP(z7>s@P9eW6tTpZj1tuc8Fl7T!++4r>)1`*el7O2H~{ILqdLz(T0IA1aRz(jNRW+~Z`rfjgCF65mibL&LE>Et-)#9a-roabQN{*V8R?SYL7)~cjM^{pQRG1zxC=aFPl1MZ3%;KF=|cIm(Tf7o*`4LqIV-vfH|2=LhYFG1kYEqMnMS+c=&hoRTRunDR~+RG`@Amfj!;AMjCN{d`!wkvHs4^2{k3SX6Pbjx&lRx9uLV(h>q-xpG1kGnT+;Eg>kHnq4^4+_|DxX7SHT8_N&u=Gq*Mt;jXE$ytgez|x@q)!(4Fz<jfyf<FznscHS?$jT>eDPK0BKPg?t5;yM9=<(z^YYCLRy{d<TZ8#|a`4-eua6GctKIJoj?jVb;LSG&ub>oseX)DA&r3gKxW#|?=6FdLI&ST*=0n$R+9Bb;fEf#x3_G0iyFt~1v48F1n~tEAf}Ca1Pz2!Eqoc{sYo$JS@|KeGEJ!V^`km(D(5j!%O%G3~shQHC<=PT$2F+q`344hQTd~bm<ScU7k8tM+P23VI@B=+Ys10C;j-#8U9Y#d)oo~D(V%W+fpTsDqg+F1`{big;2s__+TkJ(5${E{rtlDO;f^g*3R&XaF?9r|0b|adipXVny@u!`SRL+%!C;$4}38*7v+Me~QLZ!$%#JTmR0^19UYQRA3H^Cffi+u*yh%F1;WEKMlFfiY!`A{4#;JqfO)ji=k^Ra<%BJj;m1iZbD(D82}_{H3!!rxoGlBI)v^k1?K+}g!s9GIW2W{(f|5>5eJwOz!+3#OUaa(7NMI_Fq@n%Tz)7?ee`G_y!EXd@Yt1XG110Xc?87`fSW$P5W{iH6f`Lhq+U{9K?v`ys-RX%Tz>?^x_lqH8=8nEK<04N<`xfXZFPlY?3l59mC`qw0XhOvea`kGt#4!{s8XgDQrRhejUr_yGg=MBv^_{La_st9y-zF5>OPb5hBc_Z|^d#n_MWrLUx1a*3g!joKx+u}v(Gyg0=D1(v-34}dx<!XVcL^<rOv2cE8xl4)TKJgBd7+>=QZr6asC<XzJpyS*r(bz2VkZ@(+>!sEek1tR0YwOpGFExkXwlG8vS7XpJGXd~|~`BdAQ1CZW5{T;W;PC+}@sG-X_>)F%R)Uq(R*@BQBdW=P!uuCqX8wGRwBMx^uKF8<OmBR9xT(8*$p4`#wgOA9ZoS$OgQxtxFsMM^Vf9O9tsWIjkx@*$mIGrYY;vg@(t4g#EuLGC+^9K_d8_*C9`2Qk-p~PgW9b~);CIOLG9%vxZCm!x-O!$V`M<+2gK|2z$sr-{u*I2bC-tBqf4ShwU^MQYPPanok6PAR@ML>@yvg27i#83?<GDJkN1)JR){0V&-^LG+O>)-#|Yd=_Up2F4k2E80uXo<GD8nToPD)tGEf(!I^SYvy*<KW@FVUYb}Z<;{r#T*v@p*I_+u&(eeg@+k=hd~O`8HSOiBTx~d@xa_PFsUb>L6lb@#ZUdVPw~W*uVQMI1()(i6^o(d;biY*R(4Fj&z_hB{pWx9kAjSO-vB6R-$ddux{v&E;1AU~jLZ4BWMZ=@?1Nyu+OAOSzGeao_1id_dY2Sju!>tH)>OwPYqzEHGkx*IzK@)g?^jmJyQhoEVH9)UPSxDT6dfEbwI4;ODse7L>>PvaKou3VbV_kHI`2p7z?E|-bqGV#*AP9*qi|p}Q-C{{c{}_33wsU%2(RqsJs6#^$G$f_r+2UuCwx7B=N0^5$Mj=q1pOFYWY7Elc<jbt6xi9LUu+M5EsX<bzCSph`l(ld#4NG%oPM&m^mA!6(%b>#W#YtQ6xb0CZ_n`8(m3K^I<+LXgf6mnj_4EQW_Y>6FhsO-=Au94?CjwOdj*N085M!ed#e^LvT~_usu|E6_|szJa!DA(CFh<9p!1<{3Z3XzfRx_QMH8n6u{4nBh%VQZ1ChHVF)Wx-c&}ZO4cAp4B{Y?U6c~O#^Uyc0vV_vfYn;m(J4f`J{ZszCKv?F*WdY(cS(%rXu{Si2Nd>rbp0l%$AH@?V2Qb9o5Mw7qk+t)NK39M_3_{-tkur9k!`~I4c>`~n+klr4Rp!pF_*Nn`3g-8cY%I8-bQft=U<-G}R|VLg#p9Bxwi>YE7^P@<KJBOF@bWv3`Kyd3OuYO+Pmti+l>mS!frT-RNZ0MprVMnpQ3R?OP$;A$HO$~Jk|sM&eSgZNiIcF2H^&V~F9@G-E0>Cs9X!BL26&05`4K3>@4rqz)@UVZ?1O5$n7~WJ^DZy__+t$g=n_Zt5CPw@QRBjgYrq6GrZ_xmX!dOKLrcNJX-XG)+^A+?Q?Lli#7qSo^kSdQLhsrO#%ON3N9+EJ5Rw{0UMM$}j{s^C3<jvPd<0PBkW;=o;=t(E$TH)onNi$$VnKqj)lxi=#xX*zUt0M-<D1+Vidw|9vIhwkQRV?=AFLjsVl|h!&{=*+TWGt+WIcb7;pzlYZnZAhzHyte1(htbR<=g%2CT8?ageyZJ&V}=Lu}l|+gsQ_(afKJYiprFTs+BmA3i`Y7XbPo0n>Ze9?U>V>CgN35fcJLGV<bS!A<1lAbfxpFCdhw@XJhhv7abnO|oyjYY-=Ej7OkcysgFjkiXx-=e3`g6*ma+gG7Z3!p|ltL}OHhPKx{E{fWs5-pD_>bB6nf3+l=TNDE$H+T1jJW1%J78=AO1e?E>b{N%ns=t9}h2R)<jgT``uUpV;pJh}33?hD}K$dE3|kl@mr1Ry=Wi;__=!6WN?Y>Y=7%m;}KH;kW6XsG5$65+n7S9}ciGl>n^%>S(Q3(<)W5E&A}hi&_rQ0~9!r{Kgs&eIRjIwYhrYjoM^-fPlsIf_9%M5Arod(8E|fbl_-y#UD1HruoI0Er9=b@%_YCcJ9tf7UZz_TmGkyaGXoP9@=SR)eF|j`B7wcEecS5hD%;m%i}+{>BfY1Rb9Dz?MxtRwXX16*BWm-WPfQ3))JjGx`-2&wKDy0cWkg3#CRY>Ze?-FNWaqzt*2@q~i}i9F(4TXn^RMptg*mQNl>RKPcWebOZ|b2jzjZ-}pD|n1J#i<^_Jk%P$S3t}37wzMyA@*nxQegnhwI(C#g9Q;|=l{G@Iw3h7SPQo1&A62;u*m3QP`p|^yy>d+e$1Y2`(X*6A_Jb%sUym(K+IX*AsvpHLAKlXyqyTk!HreH87Bcxv2`ALT;!@Bcp_)4vvV8ea-1`WrMH_^&>QHtd5vNCrdC|B9R5DVnRuG)kls_5dS!^>#}d27j9g>mu1y`p$^h}H%E^Rg`;-Gg2MF7=_$yU)vd>PC)55qXI`VSWG7!&sg04eT-8(c!+{coTug*x6!38d6Zcg9JU}+3#omMGQJ!M4>#RIE>i)zsK0m7@b@9%)f_Myli<BBX67+?{F@vxhNWBNqs#1JLgZK7RI6cnLV=~eR9w20JQ5FUg;9yv|i%xAXX8zK%K{)gq}M{%m+HM3hXN6*H5jRe^%%OB7%f{q={~X-6z1}4g$XwQ+QowVJtE%CdRHv1~5jq10V7ggZ(g*QF|wTf)Vr*@+ifiQ|4tGuFF(si7$ir9rh{0FM5vqARsV4?jTBP&HL%5ywy!S$-}^g{wmgts2c~9^YUQ6C6$-E6IcR(F4=q#1Pb+mCvwSh-T0W+lVBQ9!|`Bt>ZdU2h1W8Qcj6fk_yualM=_(sRKO<u3E5FgD*uJ?AHEI5V<GGqEaIy<+vRt^pYz8@wNMV?Ia1LN<2BUch#&Gjc`=~87AlS50K<mUyM?hMsLMb8&A<N3qR3|U<01%40y?03BK$Qpk0QaD@1Es@r{pgDYpiQNYVV9Mp<nqoy2$IEcPB#%;qaf_jfYaa$bq^{)P4P2xk49*l~{x~Nyik2^S>*`OGOSGmzb8rt68u{1L)=ydDzC;Q;d+tII4s_=Xuz=f3_fG#nUy;V7X8T_yfI{vbTr!qRAAR!1km5mBG*kCzo+C%Rj#Bep_lernVzM&^z}nGXz9OUwn%=|KoDK^)}REZeN|#ISad=PFtRDIYTaj@(H+5d$LS&pA?)*FG?dX$wk^U6M5Vk9%fMnt_iMvikMEZk`>UT9|zNP=d<c?7INuZ<?qAdGcEXDXwXk9Pmt50pGnG|9Uh*Xzuo=r)#2_w+h*tIhevz6=ilreADkbbe7*nj@SIBg`uOn8`8m~FTVvZF?LQ8$-NY+8QOLsr@y7>X4jsc%IKg*MxD#w}=kX3<fEp}@(KX2>E}??W>Ady{+Q;ei>*MqNgXg<nzd~vq?Y=$+V)1u#@$siEmV3^#PMJ!%*<$UDR<p%Z?FSFG=-~~KXTNCxHQOySSARlai?y2F9?#7^O|Zo_Hf7cP>jPMIW0U9F4-9Ov&5o?8zag;2dU~>a6krQ4RP$sb@IRn1Q&nhxYWF(N1lBz7&l21{oARJgV3K>|#20mW+W9mJ!W1f=iWz*0WMN(C;aNRP0%EZBbu$fm$+|r=?Qy5hdTl)oyTE!_l~P1TKBE2>>-1W=OnDBlg-?Kr(K2=ffuxc~+P)tQkxaFB_mD)gg4i?O5=;k$rFS7D3I7~PH0d1(T&Z8OsWW+Yvc<aCRsHM}2CyenvYxb|l-?WwEgcEym*v<A6|^+&p=qY!E&wK2{@l=@o=Vj13goMf%8?G%P<%5>)jXxCQ8{;E1d@T*{C;6Xv}8IkMVhaxMB(WUge33zcal}OXI3^Cj9EjV(le5Gnj2X%ZTmnsI$BBPtwwEVWjX3NSf4Y*71_{a!i8pxHcHKwNLH;Umk?*;@%>m=+q*h&x1SAka6>O;_|HK5vK-qf2HV)vdZnCQH2z=QDRJ<<+L&~k+5lM7A(xX)i%l)dI<d#LJ<>X(vsJFm@&IU6M(Szs^|MT)Wx3Ny6ihljvr|NS;KflHRM5cr*r;Ad_Te+FCs{Nqm?`vFyFZWt4|oX-gW!#Cym_KWL(uWk?R|RA@Dc=_xW}&-a77cL6>QzeH$sMNF*B0~zR;oO_ChrJIwH?#EW;aYT!}XZ&3PFdD5w?zxgDF0zI*JmePXC>B%14WHnzF_U7BK>`jGJ*hzzy98D+uJcA88UDx)1^`As522D)~Duz-R-!APd(_^`UXUCzhtGs%AMNF7yr?!fn_d*dkdtI@>|HPJB;^|Lr+sJ=GAq)GfLeMLPuybOkODqDMk&<tQSuFuDjmsYR6F|M4$Z}4**)!8VJ(1RhX;`U86#QRdHcCyMv6rqQHh5g|VDlwdm$NFy&Fg`9Q13j@)smbPYY)?MpD+Q{bLr^#0%qACpjP0pCQRqMCsm&mH9)w^DREISu7?JeaOGi!M%qn(-{|LhBD5$exAsJqV|Gyyu{h$Q^K{yDKM$e#YIysghgKEsRY>BIMNS(+E+nvHbvoF~*4wV1gGWzF&%2~Zq%Vs*!G67mbnI_~;s<mbsy^3!9cn@Y<RS=egOE?sISRMyT{BG+%=IDo<{fx8@V?75rl5cvQmi{A*3~(3?Gy9prCLm8f%T}Y@h?`><3M<kVfoI>6IZ=(ho408q=_5D|Bpb#~1|nr*C1(OQO~XWINPH}C4ns$u3I+6ne{FKLi9KZ<y*q?c=XerX18BwR8BfMLK-ICIvH%iWPvGOJ2@;YXKC}lLy;q<-FL)Z9$q_+7cSqh0<Fivwj`PXbF|%I?x5mEsf)L0)?QCPGGKEGUz#^wDg_=nWl-^e9@0bsxO1P-i09<f1?*wtg#SeI6w*X1=j(u*3moH`VmiR)KYn=^g#_qZ?)UEPwd{v!H3JR+1Ej>X^sdvV>+-VXGd!UN(>{!c=^=zliyBiXN<<esmhIot}gxOr=jMbdZl2P?k$wRWIl|UqO7@*ebnZ(>QN_0Bw_!}{t)%2N&4HPIAa=Iv&L~*KZT6uML0Rt?nc)&WW!7h-4*t?ou6Ou4<8;t@Z-E2UEwMDr$meVE~-KgWU>{JI?*ATSN&RjFF&1ay2$vFe3DU=rAviZmJ#$JNCq8X>+Q*XCE?$eZ$0&C&7r>yNadiq?*O6^c*^*mOF1}Q*;4z=57+Ef*jQU^om+nns{>;aHOBs}D`Yg+Bk3ZTd)a4w`KOWf9k$+*gDc8LHL{mgMk2>~?z(AE=CuxvrWElXNS%w;5r`v4EqH93aAOfmK)rGYN~PM7_l^d9s20H&#Kfo6b=WE-N9X@dr>TY%<B#7#2|wwZ1NH*;<1V85HtX}=*4oF^B+=9xBVF!D{%!s^chml*}%Wwwm~EOHZpG|}@IR89d3m2cy?^dl38+RDo#$+8NtWCd(AgE-XqXP_Ma4E|BcF8)!OHfS&&HPGCYv;d1l7g&+Sfqo_x4%{HdP)G@hLSc4babrKZjvIXN|4vWSwz8@_tcC5!5}vYd%>dmsME`Wc*ZyNtk~uoHmyuiHt?c|>N3BGi76`FAohWWg<fNqY?Flq?D}c!SoyU`3zTS8f-|Pn-OE`N#8C&@S4a!hGp#7IBP<pdPYDMmR!)Sw&gadUfA`eDX^VH5oX6<WMHnvRV)Wu;5>(bx#7JSrX{rusH1;#E==cg;I)8hO42C)2Tiw(^#Q5WYiCGgBc7AHWxNSz<y;1acoe>c}_*%nLgM8^V`D^cfXK0v~J^IT^@PIz|nHmG6kb^QCdqu}LFjVx$(fjU1{ayHI9X0ib3nRPmYVvROwpQwWxFtRf#2Mn26rvod-hfo7xon9%?Vdrb-SQeICi8|l4=eXJ$F4wV_*kC|F`RqEkd9%h^2V(^mE|*(|sj7DO9EV$m^vxHj)9Dx60EX>uv|Ny~jq)N;vP7NE%Gd@DLQ9)P*14HIgN*Dt?N)N?Zs`1E9I{y;w7fbUz&YyYkK-&Lb^!sT@rX+X`p8<7JHa#0@HE{zJC5PZz!iq3NVb`PTRh^x?^K2KtJ{ZvX1qN3ZAPxEGcyVu{1##1uqs7zJ8KHB)kHQ);Kh~QOkwufqt@8$BtxU8s4nw>w}6l!bT*BCnnyH>yF_I@w@&AoUF1;*1P6y2Ff#tc6VMLn8#)v>PY4h?KX7g!UN8qNJIl%gP?=KO(dQXIO|gz$^DwL;bv$&%uDIdIquLTUyvPDLbi7*v1oGVwa_7N$AXbq&teBhi&6W#{dFW6GN-tK&bLLjFSMRw1W(UuOz+{m+9!<A5TlHSo**4>}x)7RHs@{VCZ8%}+N8E*=vO;w{25-50Xq<`{!qQ3s@muxIx*L`_^DKcwCF*$A-m14<K-AIu>8~id-mmJv;>#O+L3I{BWc;~b<pq-or1qsVc}oDwBM+myyRlzRS5=1CrUmQ+EL6*OJ@kWC+gl(n<GD#*CgYuAQ&h{uCZ4cK&8V$wMw-`wl6j&wCD+jz0R?8;np3)8f&;V4t#hvhR1@j%V@qabC**l3Dzi{mDwetegeG-2N|xbb;Va<i!dK}9T~Z8OW1I7($PX>w56OlW&qNlFtf-|eh?>ru8`&bCj66Vh$vXGm;EHuSM={HpLotwmX=DTaNx=8ar91ESk#Cz_rp`S>+}xnKiR2-vOsSKBRYj)N5{w`~tjGus|C2l`@cpZmXSt}R^FpU&mb;ZC0mM?0_?+KpEvF<IFft`+lXRqY3rNm0Cf_5wOr3krxCh*|tOz)AJy9Y^RCf)O%jqURQhXzD<&hHAba~vvk>W;g$L^8oyral0pcvVb$~_kd!^<b%oLr$g_v2ukfm-%-H#~z3dSp2cIi}o(?2d>GYCmXyrUJqpi*kMUk?K8O;W7SK%O5CYc5vo@q;}Y3W})j*W@)>NSUoIqP|CnKOIT3cUQCu@=_*v`u1+WsiMcg{!tMEF*xs%pF#LQ()@?}2O-dt?o@4dN;Rlr4RI*Bli9u4?*uZi6T)FLk6CR1gc5Xw+>7|t$Gb7)g>;;ZoR->Gy>fGInb!nn)=nczzf8~V`-@-2zLb_*|8g5Z3%Y#PnS!CBN+PKppn0t5B7rFOY(>2_j!&x3)t`ITvrdnP%Hf#38w!PGBKQ(;}=uE=6RB1GL-D<Gm)s}~26p-Swo!=x{$o(8#(F7pxX0vH7zqvfXd?}&(6T}SzqTAIj57SkyPA++3cg%q5^v@F$i^I#85Q4)z+m#17)$A0Z=?K>=gHV3)1uHKowxG7Rw|`}9as4Vg2-g5)YsdDl%wv{cJ#m!Qw}-b|vcxcotKuXCPgkNLSgqXZ12dIO1o#vhB7Bo7$gj?7uD+ZikTcog?IJ&?tfo4e{seb(I!$&w!duYf_TlsAoyO`xqJ!`fgBMp1Zt=q0vmk8%EgJA?T+n$tPe)Ps>2BxjAH3)s(FG>*O?ms0t)U&u5Au1DlWz~tA$=S9nLUu@Oc&B=lz`@dz9$pQfwWrn*e@~lA^w4Hd2ax|G~!Fv_>PGeSA9^GVAkLVNZ(t_H30A7ZSzdlpwCuzqDi?=x6!rZvGQ-YWjnka`;wk7+|qm+2<A-ozrdHLdMh#2fIf($Rx>;uW<VJHR|S#D8iG<Yha2QH#yjx-aWEc5GashgZ^9@|s#DoV@*wkWv?E%_X+}03$t8kKtwRdv##HkNnx>jR(5Y~XBBzmBon=4UXEn`5$nrT6?hhEOMR~5ss=0GR+Z*c{9^5&q*$0Gny>IbEEnhEpaA((h<C6oTRn0z8vunKyraBvtLC--w%z)^pX*C6b55uXF@ce!iQR^&|`=?gV^`pXCU69FHK7X``<%v9cd44sE+N>uN3uE`rMB15@iJyta-^Ygxs^wjTFcIM`bRC1mWi}<pF$JeCL6*CWW#FCuVt2pc{+g%3ndUSphFHsMyM4*1U8nT7$d3##EOH`)A}$ZI0^rJfEdI^CUB}|zEaNxEQFE`cyWbGPLVq!%nNM}kRKXQLvRk}TD7Oq?{O0&u4PxEN4KTP;aWU3p2^?W^)TR)-()jU8Frwt~`BHV-R43D%Ou>9H3&w-D_}ugH6wSx#ZGs&#*B<l*zEuvxid5XYwunL;&=&lwGcXNLZxbA{2BbqbfJy@-A}EUR6%l*l?v6<%j(>!X#r_Q=<#VIQeTgSXSi@Il;Ez*pQBgIwuDC<=6$~=v!&iM;jZUx5sN1I~2xZH!6sHn0UZy(N3gP!NTrNkdu-=t{vwg0%wTs)v`IPYUne-rQ&JIc?ef|j_ySCC~sAmuH!<gf$WCu!$GOB`Aav(YmP#;1C>@I#^V@9hmD@)U+TyB1Ha7vtJvr;JsgBIee$_BM~4`A(9eJ5E>IWnb9<51O0XUscj={28jn`9$&sy&*IxvG&N5tY%-pjFhnNC0{bMne7UHg#+@3y+zr^UQ#+A_H>~32`hrUu5(N4f=#_IRxT+N28R?Y-k0IypANC3yem>Fb6V6$FP)+1=yVw4GSqMpwuk1jv^*)Lt0Y?p&)LV^cs=88f2o1Y%G^R^{>4#m#18*Pe`nSI<H;*;lp@~?u9(Nd7J2hY_8?Zjhq5WEXwl6q4!-*Gz%BuS3$T?=l=$yHghqJY@iAo0=&*m4NVv1)SD-Kwh^WWBpRhyY?&_qf(U!Kt3YmmIwC}%+6BLf+s_0QYZ==IgIh5dI;)9yq?*G0G!yfNN<+Y}GO>3N``(pHaS+SYRW@v+Q>cArxM$-8RVay!ScH}e;|@=X0yqWYrABHOQ#*F@sMS(}9f~vr*F(XFnP0jn+Qy<(sFM}4prL4KC~yxII1^A?0+JbG^szM$aICRsC^gz7j;`R3pvypI0V-LPubmGGu%kF-=V#i;OGe$VyPYbY`vr6OcUPyw0o|xX)uAdzj2J4I%*IfI{ek>s9`zn=w7ZYHV5jE`&3U1Xjm^%+dS}C3=#Cd^cOLcHosIURN3K%XDp79z@uP0Hw*lp-6bQ8)Sh6`4sj(yW=lBPc+ud3&KLa{4v6jKvFyYA20@mww9`_z^JnB4N=geY~m>%_e69tLi-52t#55(>RvHL)5bxdPZJ&jVlPMAr4Oa#V1o=xo3VeJ22ze6EP>PceNJM5>rlxQpbNLfP>M8h1T8RK*mlov8yi3h0qlBPGv2=V<Xp^!iGCKi_N-vV!9lT9lMt^EGnnRSO*cPh)gW_R0?J)-T|>aAs*2Xm{y+%9lu6}YQeIEL74+{XcAX5AsSdX71BI|mzmhdFmG3)~FB4T%c3_Quc9ZvG5042drDTw%K_GekNhO5NoO=em_}Zjd8wg6g+ODry3vg%Se)++h$BsB0nbw{ta6>MW|&YCG|Ws)e}Pg}4^fY>|9+_ls9`_pM#px8j<ucDuBHB{<vdg?%(?8`Z;G8V(xAhsbll4>Uv#O0$rKw{2d!t(R`|((Qa{A_vh@gWcw^+j-c$bXzao=B3;1e8XwRQu`kw|3h(VUW3wdz~^mVx~-RP^U`_X-;hux91n56Q1Ll0KF@%2>HBb-<mdycCbNVL=6UKc0!8ox(jv5Sn9^#ln|o&Bk~SgGR6`C{=!9w+IX{1KaQOP*<mlzz`LB=9&nfBX<+EppZ}@K`azHeh&QhPp)%5o%jBDSY_+cs*9$0VgFs@e}pF&JM@$sUr9Hr~R0h<EJA9==tG>GN8W8P{*J;r=JEmNxDw|<7COb<+#{u*eL@I7~Pt)O#M?J_P@p(Kj|&>2o&)3oB5pInXTx?xo%7Z?+R@`|yFrh*`5Y32WhhM_nQG3${-Q?8zJb292#6>;NI9FA0JoKVx0&3M2E5^sJA3<!#oY)zcIaCaPQg^;AeQ9v9GWKgWDac-t;msvS8+?N0f*DMq_$8;!@Z8hS#$wOYbA0<_JS_CR_zN#3JHZ5FfZn&m+giz(VG*sAfiSVHq&<6sJ+GdJzvg&-HIPU=mYD`ddp;BjTI#0~_8h$$Y8q*i?_08D9u2|9SC0KI}BRTzLJcYFle?Y7FB)ByT+fIM>#JKWr%nHi4ueON4vGfxBeTAw@RU8lkHv==>jB6S{n|Q8pQ<C@k0h6=AlvQ$0SS;0+)J}kL0qaAA^^kY*fu56N#*S690X1t*rZR^eSYEIwp8!Z-WJ+A1R0<|^Y7WMW;y`CSae$q%9wazf57QTl)Ln8x%mxc9>CTC^3i1uGq^q=KRl7X77Frc7cSD=ixEG;WM<m*dH_k{d_8#!2Spq8{IGQGZZ6O;Xglm*6P&6+Xg_xD{lO(F3*h3Eefo!h@7i-S|u7-PNw_aQlQqrxehE6Ex2!IZL9x^-YT4dS8i-xJrq?u@~5;PR;HJ!`#0@t#D36p}@$dP=YTK!OpU7kat6R<m{gUN~yvIsl|qXQ@Dj4u5%GERpSC#PfjB2G_s!^@1Pu!iB-Y12{gxh<8mdYT`nQy@z-dK<gd)QoBi5x1xbuCl6)b4K*_gc35~5SGmRKW&!k&&R0QVFl{2<XoV6&tA^^x3Yt{2y?}cI9$N6O3!t^T3DJJyK9_~w#v<;9xcBK;^Ie6moFs~YW^h15uxJsEheT+mgZzplZT2}^wN)X7FF&}8INKK;7#~&vMQz*vnp?qf~qU*Rb5X91sw|2Tw#}D_wM=3OK}YiX2}bn9K}MSa2a(Leh>dn5URP8j#`%^wg&%Z><oppa);kr7v0fCjHhAzBD|fbW>W{z(hd`j&(w7(HMjpns(+QY)PX5W&tdDz4!SW42_O*aTe9RM@p_VpjcIl}-e}t$Sc8c;gyg4>;hk9k2d})uaq1Jv?~p5yu@(9?==L3*w$^laBUcov@XqbXa80!1pfOSuj|Inp0xpFL11zE1gpE=2gnD-x;JMD-wMwKO@l;iv^D{OcFs`X|quIuMB5uwTFEvP$js$IlEL#I!ut@L&C&3R$f)qY=5-1#}KVV~jAbk-bI@)uE9#m*%6}eU!0XS$o9XHJE^L_%;#N#ghZEj8&a^`98yH2eYS1dKU0uUdCqC+w@QZD7v(wH?)x9?TwELt%wWlWE$>6V$TWMVRT$=irLw?vH{3ImcA@W!C%^X)Av_$8}mZiKu}E$?lY-bA~iA{X-n#vrzg0HAj+7aqWz`4@OAT`zB5b~m}xF00*YH=&}}b>Nl(tITDbhGIrqyW*i#hk2eBNX~y2rMlk{?;t-BZtKT$Sdf-(HI*$VM~A0@sKbQ{`bD;=O3oFNwhRa}Fl9k7Hvc5TnV#zHQ;l##OgTg)gc=%f0W?JUN6mad7%YV(j&9uY$M#js=9_}Bln64!9d=I>Nl#p5UdTdDqc(h!y&OeOo)~FDHt&hyJtk(86@5&op8Yh6vpprX^(UrO4JfJ2Cd0_bfE+^4R2rnmE3IWI979d7Z!}dijI)Udi5d8ZOrN2dPnyyFY#&nZIS#t5UkM#+d%2C#Ft;l@Z5Hl}<~`;Z@)cimlqy2kJ2?#=5?g{j73Zb`2?{RM0fZs7xf`$Jz6>crcUIg-VQ1dyYjmbfSX)Bg?LLxba3>Y%6wD1J)tonLv^Amj#GVj_DC6D&fooFqXEC`_@;=+sA-qkqTy<!@(%j4T$Z+ImF^)-t_czblw96_AJ<JzE`a_d2_bC9ZG4TWUqV#ggCr9M(P^?~6coaB1EL{X7%5{*6JDi%0#?MVb(TQ>jib4ex6!hg36h8_nDDpW4Rbici7Ert)lNH?11w$dN%ll6!7eqkL$!8j(T)Khso#UiO!o52OjV;;Yt9f15Rz-$dChEFi*y0~5?VP`!Db}VUpHyiCiYp`B7S!#)J0a%oYXz=gEjiqi%;N+JOI<0rQ%+Hus*^W66y!DCq_K~venKU`Of3&h?eK#&@f8$@0;OSDjh^IMrp4Rqjnw3A_1)h2a;qPj8lTfZK1BN{(mY(ofTe@D?S-5z^%1QGO?MRvxpJ%9mdwtzY*UqApejq{TL3fX)W=c1C1?Y3f&MK+WMZb$)&S*V?Mz@<RY}tg89NMpv1&$xEFg`7q?zAO6Vu#GeB!QU2w<(Ek#5zsBye6PTjjq&4<33Z9J{BYLGqY6Z^vG^rF|FAY@m2MqQuvJGTO2e!~<0(+ATYQm&(&(%aLZ5HM+m$P8P3u3ICTZ^^K?Jx0JUWY3j*}PjE}K+hixP7batRA}wLnw<nEfN9+rB@TP`uz0>Qf>@~0{zHIl&?qR+<+}nM1aK68LvP+N2(K~V?@$K&3Z;tT|IaPS~&5N&hUmTpjJ~-JGRWtz2iD+%U20p%)t8Ltx5uxeTy%~zd-j4>py!mCc_Z#?l_VugXqwlOHTt|KH0=H=AS)G^d%{R!`r0I|rC$C<Gmoto(3)5IN)KqEu(3^2|nIXv#pUUcI=<hAV?IJEMXPX^TDBb2TjwT0T8V7z-6-mDMX;Lsrpkh)pX@f=QxobYBluWMLqMfIeS+G?hnZ$G8Yh_DI!CO$!T3OskR6oRWC12BU#m{~vdRV1NqdWTad8k|w*Osy=8f`(S-6rT&D6p$*=WCaBR%t*v)OynD+G+EjoUPT=g$xRzkI>ciS~X@_FtN&%M=i!rjA-bG6<+&h6u|Oa<@I$RbO#VBq_7YVDxHElhaVcw2BD-x6@-_5;WfFJ;lRH=98xJ<Qz{k5NsMf#LF_TGGF=wOwGCL{avUV1<=GS8p2Q}Emj;8%UMUVBuz~^TdvQa)_2Ljm^@e|1_oJg(+(+t&T;Oj6Dt}E=&IV6DtodZTiMDf$XEnP|B3;`pmGRjp^kyo~cQFUA{COhb)lA0tTo%_x`p1gnWri$_K%%|-kv#~)!)tCU^pd};zx(mjYuueZ{N20Snl<6U)<|uma_!Hv3V*f+ic6C6aws(kJ-=azX@U{k7|96cvEs98^Wm4Z$`gIxiRVxyH5X5t4<3H`=YRI&yK3zZr@uS<-S5t5a{lgjfA&Qs+kvVze~7>Ut5kBkLunrs2|f-ys6-WaOppA_gWGAf^5-a!Bw;{8{aK}Eyp%yT^zM@l;wQ5)J-Z-=S<+M6qTp13AwTc{rJ^P#*IB?<7XgKTQC)_ig_ck(2x!o|N}cyYY=YFX>&F_+I0)Bu6j6W^AUB`*%j&Q2jc>5<{Jys8nR6a9VH(w*xaxl$0u#;Pj}`d91X2Al@h`V3$NnX%#7U*z_a<AFR}@aDQlEuel|6L(tJI@@x>Y&kN9mP!wNr#lGmlWnKJWoPKG{8axp%&Ma&q+Y+1Dqux^uo)ZN!&M0&2%`iUBBeU8gErJc#-;Y*zF4Ge4dm`(v`gcE{st<&<9Sg_Z4;#%DzD_2N(dlrGZl43>)gP#XeXoBY6SF@^c45M+#zt3k$}8RW`Ye&39*WT;GoV88U!U4R!{faOs|$Tf36S*(gVI`IkmV@PqYLW;?SwYTVRo#POS=sWv@bbd8X1x*EsRf{qLYyGFy9SM+YRMuCVW=f1xg(kJdcn?bCV-Wl|5lojsgqtIYpEjFKSO``9%3DgMIfYq8K=!@(3QX}=XcijvPom39ShG(?V9hydqn}rtCf^3>s9O0tgl1GxI;;BTJfIR4^p2{q>RuX;AAVm`K-Ko41M-o-2r`y1Ab)2;E~v<p)i85<6MH2(d+~J6AV!sU(%cl2^3}`zgQN4~w+DO2Dk#K{C}zPxtEk;IlxzXmblnz;xZ5p^)sN4;`uv$!ob6DY%K7*n?FqS>e?`?RGR~6%Ye(Ra&^r=(Z@m;c?XT>M`VR1Rq>h#0Qv{Gj2=o9K5(5wIPdG5XzeIu?9SYCLM8k>1jtEQ+RW5pn#MItct}i?)NpWBD!8)?O;5z`KFBqz$tS=l*d0*_1CaZRZqMH==L=Sc%K{r$vI@(~YJ2`gBFs90Lgy04)-xN>;lFiN_cM2dM1rzoRtLGsbJD@h`PA^Z8Py&9-Ycjr1T5WCb1u<ScD8`{S7i~OkZFI9f*ocl)^&E!0x06JH4+s#B?uHuOO@#vV42fk|cu5^8P^D<38<)bPhC>rgErkd)7>Vc`=>TS7vL?B)wQ3V=qg;ScT_&~{*>ixA?~Aq{yBc(4sB+Nue!iLxkCX_cZyZN99sc3pOB^o<0!-*JQHu6A9Yk`3WwYY9OVm;<ZnnzjA>R*V-(qzK%?k19A@VW_*2_=Pb}`Zu31bz+G9bK?W}Au;yN+SZNGy=<LH$+mX(8i_*(RgxFD-P>d3Ag%bOoeYaQPD9S3=oCUVjyoS`7M}R9w%~)$Zppuf7^a^0P0Kjq5qtsL=7c%b=6qxoTFbxv_wjFd6+J+sEolA=0l|C=E_Y<2((Oycb6H9!SSYn5=-y7RsHHb<D<g6x}R`>I1}@#FfdjMaa~>BAYF`8%tq&JEF(EmcV2^<&k50CmX*1D{IXWOmZxMt%jLD{;?|N*Hr7nFvDWFDq7O395@S*@_VBB$)_~L_IkM<2Qz))+!ILpe0Rj0aqUgVaxe>Z@U*MKs{4MJ;Byv>5oOm+HLbmsY3;32y$(^*LJOAkKHh2FBS;Ies*6>tsgZjCBBdy!(*=vH!1DnU9lMrSUP`guccx3dHJj-Lc<4gs2Qc8bP=6r@awP71of4(girSr0JyYq)-zp#r5gS)RbGpK2*#wYud_`3kA+oQNuE>fw(fqhUBz+CF7ok&^QPr?fOmk`Jm#PSa<QVHN!g600Bn%7rPu%PL01kZa_5E}q3raj?>c>W@EZoDIjNgM?8c~t%v0jQwG5JY=o7+nuvo4peECX@#Y8fFY5#CQNjcyE`v;c>^0qNk0juH~(Jh3O=zg@%@3YT#$(jKi|YZ)1VNEta#Ess#UPbrZqzHcoj2szr|ZYiwdhM}?xZG$Pp6p@KTsP_HT3&u<ysVvhu-yhgG=pl_fo?qC?DaPP&u!rki3eBcg9N6r*^^1&h#{`MJLI=kJliu}Yh0PRghry?9=m^#KI2s27CQhjw8=Y2Y{;Wrvjy*#6UMdWK$tHp0!3s4p&6Wd6r+Dw^Io{|lL*{gsS7KIj_QrbI7Q}1smK_5Ovd<BQgBj!l7TQY_Id&_XvitIN>93$Z*KqTlF_Ad-h~>J`S+IRXNQ(D}6`tH96}EWgZ{a$aJI++h@RA89yKKkXVs3ia!g#GB*P{g+)5rW7?U(py1KX2;9P@~yG9I*01GU`7qCkb4)kQ})0!!g!qGu`ivfFHxGrGXGXi^D``G+v_C^wcwxo~a?oUVs5a(ixzaPomuvj7YeMEDuSHUBhDg1si=u9<9iIz<zR&VBK?*JocaJkngF^GQhQUwtwkK|IUfOECgK_1WPezCQlltHa%WyhWt{Zi+L1d{7A&H*|_B%U6%ot5_bXuiQ`h(@;irdcvKKj0aKwie6pkU+`E221GnrJEjMN@}6p<7vxeTB6v@{aORC=3GRP@kNL>>33?SQK>|7s2J%IpsUHqNbVvYObe)`M4ScX@Vt*j>zMc-CdwPiwNFZ~M{NK;OqDEd+ec<WWK>|a*C4IkhEs8}6^wf}Vz2KuCfJ&C7pPX=GE(*R>-%yZx@s%JQy{v+-_XzJOFG+&SP)6_k(QvcDlLa5<L(pg4efE~u)Lsn+JNz7FB0cG7q|TkG6iSKCg+O7F3Z?dR&F%ReN?4<w_UI=b5M=H`s5s~^=iq$Ka?O{#pk~K@#YmD)5QICR@o=G;2Xq>Q+{Gc;;&(xtLBj8Z%Ic!jIroo9YIL36ohKp+3;bUe6%+YetZHI3Cdv@x@C68j46ij2?E(Pr^i1?@miY04ZebA}wkw@LO0L3`=g<#itqR~41MBtiEm)51<p8zkaNs59QGDrzAnW8C)Kj<nxM~j1$1y7Cq{{#G@%jG2^WCpsVX33t*T<sI!olxYyj?}1rFjltK0pzTW^`Z+lazFH5VZ0K`va^pAQLJ=q(CnNe1fq8vkuf@;Ot<WO)&qOblcaZ#cqMxuSo!EO+nX@sUIH-5hO$jwgkU`;KYlbtO}ywX5@zigTdN}H(MyY-z*gbukkmXFxY1l_x%BjLh(?UmNXo4x7i@}hcQiettp5J?19j1-z?p|4Pcxqb3vea1pq3GOT2K;zN@p!9p-!mX7L>?1(*l&3|-#)KKq^ni=!mjo2762Boq-`tJ%Z=l<3l=V1CD-469<q$HU=}2lTxoI8>30L8!W(Rn?GwFECbl=urT`*4T5TC0ChhpUJl`Uii_zmwLMN#^mQnm^}~2PtOXHmnbxl*timDB)XU-^IaMaBY6}h>5)H;;#3FI9|wMzzNX!E?Y-JTfOFxrjfx=uv(Y-!9=<zNZ|1eK*Z$&A5K{VS#zAVP0G33rLKJwRr3`~Kc}6eY0q^LEoLFW$DwVH6wstb9Oj;kNbu(E^#e&c(NvYngl{$eLI69mGVbLZ4OGR4=D37!=p0~N4;TU<zF0uWIdh!e!`k5x~XP`!r0+op@Sh%w!bqgeOZcL8(tOD-iz^j%MCih+zQ-ZI(cew6Wd4}Rqe8;85<IIRE8RO$i5{{Rgf@F_Ng2X~i4s0BVDJrx`H==n`!EqKhUzjqBO38%M)I|kHd(*gj<<CuD@j*brgXyw_<>-xRO+Pf+fW=P%$e9((=SwYTi@`@8`=y^go4*BHpc-BLP$#Rvy0nU}et5Hx!c~!HcBNU-BHZ%}(@?uO`Ub&pKMo`=8#8+ZR40_{G@-$p$OP>)I6HG(6o7okJ7)Plk}v6}?Wp6HzPwqjdLX-v1DnpLel#?DNaI<FNZYI!KDQ<m<^HdQ04b+emSMM<;E9M`L`NPL!n-^Uy=gL{8<f~)!=3rUzYIdOw_d=a4^qUKbf4?B^#EN4%z^Ju_r_7^i>Wl#uSLJh4QfA{OoDVtl$<-V8xp@hK74~GvakRJ!+F&#j5N0j7%j?rz>}4H<lf5$FvBg^DlJI9gU?LoKqaGKm{wJNo~^{Lth=2>xSNpyh4gqfOH=Y9Hy#sl51{o39<(1J$b!`iAGloTld{|HPOHH)s%USq+`spW`d-j;t80D??V4aIlTqC5GFirMfz@S`JM=2kf-9yuYD}YPRaPw=$z&e(_dqv`qjB;)jwZCvQB}(kT{1oHgV9;#&+3X={gFSIjs34ci`osn@%+v&ArNktxCmsE-$kH8p13!GG?M>Z1o{NKR_jf6823HWabotZfALM=-*nhB9)_{{7dHWP?WPHqh6nvlK*yy^kADH`_g~NjV*2$d-X29!e?iSS^1Z?Q*rz~&>bX{W`hrvFB$!Y<SSd&_3w3_6(QynT@j8)n6f?zM&}-UK(n{IzaSYLRG7(tMsv!9|xopK!tfHKReEC$WL<RR3G~(h<qkN9!Tr-uJD=yU{9GpbRIn}8*A4geGcM&j3Z>bhWFP>|Qc>!_-F?X>FHS{ckSf8$wRY5tmZ{>hy+JxjNu2!%eVrZG(LCW639o#ssm0Z<QW0X@L<yZ!np-1cRG&bbNG}g2m_+hFv^5R{^P-x|go#K}4G;Y$(Gk#B2S}ro&L)@gjG|cUET6ll<d2s6ws-1$8^OBMoLbc~cSoK{u2UyyEBe3fW8lbl1XhX8u%Sv}0rLB!RUZ=C5j=p^-uozXS#+kUA_=if(IjZ|}pm@+1gZnA~T`RjbB|>!E8qv5Yh=pi|5bnG(AD)_^deeFdXTAcEc>$2goepHZ7zmA1O$?L`BnZKN|Lu1Q6p-iQwhk>ci+Q)=?uUU=3%ElUhO}7K6FcAzhH(Nr+<4Sh2hdx$0LYd#Sg&S1a4aW0kmt8sFeLTt_jmAnuC@RKj4ky|+Y|X7Qt!0ia?3(})$;fbg7~7P@6F<C|7c5#OKXN9>U7rmv+ES1oma0FzWN#S4S#K&sPe;zJy<la=wNCO3~vyd;p@Z@H(D{2?}7o0JtrK0o}6tsW%t>&$H~RbWr}FHkLBTO)fmdYXartg<`T|m8DBp_Vny8EFf(bt{z-Au5pg5Gs@A~Jlz3gOb}hqUq&;1&;mKBvlJ!|%ZiKBI(2lCQp9%uwU`#<}p3PqlsueNc8d$Dk7(tk#FH`ut*@q@4uYx3PdIPA9Dgb)zTbD)+&7j8Uq#3_Qv((DV>e<>v;-|7o_8hGloy}@d>`$U=-`S{lb=K>&%2rKHJy1*koQ`o2-1*cx6_Pvo1)8&Q&(+XETpFx4DRiC9BAk)MdtzyL3rObZqUxl8q@7bO(?gcMbzWzkmTQmCn@-2`mtjAG33Vx$wJNCjmTOIQ=tmeq1^?x64>x=<!V&G>?}~IwOVKME8jF$P)LwETgU&Gm4BX&Skc>6SG>61_+O~DV_~W~}S)y*W%Z%>r-=?c!7s8B_iAQsz_S42FhbF>IA>W$1!83GSR3;d=%|zB)m`Y#2v<xs<d|q&`_<5;mrpBh48%UInqOr7?JBKwJ3uI!w)7A@h30@}5LbBv^zls%-g$wmQR3dfIdN3)NBow&-y#Y9A#r$8gYUTZ3SL6#6<nx(RU-6#w`@hN;GE~f(g1IFkJFf=JP=i;($nSB3V)+k$$FRyWnr)jZO(u#|$tb!xiC~$kW)cHzloXSsP&`LY1Dma;iDoSt1=<4`g~DMW$g}oZK~)?gtg42pmdPh#KG{{*{xavfyhIxKDa_ZG;Sb~@fz}q?%QwWZX`60awrM7Eggpq8caH~e8yu(eF+Zlrj8P?hqzP^ykxR1+&F5;}mS4o;?EtA;s?rZ-PSFAjT3IawuB!o`b0}G#>35UlRW$YEbp8#+lUUg0EFSnxHig~5s+C3qZS2Mctm0<OC8KEo%87`AtYDZy?@gUu$}boEiw*$*(6iXs_Fq);p)yAPEd`Oikx^*uW{BMb|5ojFZX2N?i6QBzB2IizY_X_#L!7?gp{Efk`qD1kmWA8-!WVYojx5}<3v2IXYpvbcW*g;=&Ei0HY6}}H3U@%;sx54+DBP<<6YRzo#az!`uEsIp;ds{K%M0(z-&KE?JgA=jZqPh?Sc9+i;-71QHGGo-63`O`)k*f)yVYx%-#K%4ROWZjYQ?d5iIKT%2HWR3x`O!Cn7BTdeCbZUsFh5&F};&pZ8baX&ITBCF}=R^sJ)KwKVQ<1)}s#oxWG7~o%QuBjIWHtGs9rBU=Ma2{#NoicCoj0o{R04HR+w>-Q{q=m0`J)2IGnj3VIy2Npi^td|w3QGsLGz=X02!167K)?>HnnF`@xd*m7HR=Q>O1`{$<dz>UG=QWKB(%cXj1Y7!J_VrkxH9K&<cdMf7mBNiKr80TVd-|glnPi3g^w!>jiLb3%r9R(!fygVBCv=BN1Z70bI_q=1&bo_qq-=Z65z?UuVbMs}%+PY=1rZ`|#a5axUjOk~j6PKAYl($@X1FGUqVW%2wBe60TVo~MGr!p3kwn4UOt*34m92Bo?S7<<UvGlPirpp_ac6sqR($&F{-8j=%P!Pqcyj)8R$Gbct&2>*;(JMSDqB}pLvdAvZt;(rhbhwp4$dTB!d1G%qEw;iKw~&c}cSGf5n`OsfwJT!KD^>>V!b7w&E3V{-jXa^aC)i2!4Ovm<YLI)E!IWmwCg9d3KghZ7oRBY&CVZ<4m(_x;uP2MQ#x%=co`HpzhcOX;Pnpw3sg;B<y+lzgd1+0^#B`nomlxj5-E`xq=}$(^3!NW>+Fbhs34S%v|7DiE<&wj+^<bee!8$SpY#22&GaIMWrjorR7!`F5aN+p4*N%KO9s2?~@lF>f_J*4_*SO1UJ)2gm&Tn5_a87b_++=Jy^1`cM1$~z#9Zvs-X(n@Mgv9r!+GNph71S&pEpubBE;i(uUKGf7p3DlCr2uW`k?YRY9S$KB@Fz4?>!dgtIS&TBcj$G-fj5JJ-D2^)zybjx>)Rs4-MY_nty6^DF;CsxcRao<8Yii6x~p;VVLX3ib@iRS{F*e^oE7p<WywjGG1R@f02ELOUzT@gOYhEtj_d7qv#NfU=q{m7L}gbChrz^Dur8UBXTf4)pj=)>Swe8o2}2Sj=RDS|5*jhNi`$-hnIpMajCe8Ag^r|~cM*((bpF+Bu&Sm)YF%DYF<j_a-qX(E^LQUMayjMArJxmhL75x2**<LyRyHgLceqC@?nkUF^ilgXXtlIXzlug*qU<imWVEdySxi6rO8Mcja6@}GOXe0;B`}*Gm*mKWJZT#%B0j!>NR6FVpw4iEp&4D}-%B$nlJ~j|Ll6KC|Eq-?+~(ROB96!NX92z1?K)aSkc-{5lt-N9tVO!D<;<qjCGY2E>QYV|)!g2ae%P!Xg~}t)7~$hhTDq>Jt(&>{#cIDDDN@xuXNx<b9nFe*b+(x)Jg)3+t7W@Xe*zE3jV9Zp>p2aK*ohY)@!1ph422IEW>qu+*~9Fr@Ixl<D?emlSTdZWpTfN{V`CVW6x88ac(oUed01`ByJ;Hf(dxy)YCOrMMc1QT8oJc;M1C==MIQBuPj8!}PDq_K-c_X|6{A9gcX{Zt&)S7nmu_mazIP3xV2%8P*5p-x{@xStaWrM)V7i7^+WOv9!xIc{bB)C-Y$DO+SOj#~!awqi3}~>0f8=lI{}%qyd>GO#`l}vQgU)TyUv+(SaJz+n)QzS9?;YV^nQ~3h6SV79-e7>Y+I*;(iHh4go6}=!A$$wrYlzRCiwj=+{$-uo@e<fR5l`PhBl5~Ry*ZTPTR$A_!-v_NhMse8W`Rqa?mz^dm0{O%fh0UvYmb&q?+K{q2woaap6IqoSz4=eH+%FvirbKP6AjemnRgl)PvStQp;u=Yb=Ef?QyAQG{4&o4=35x8WB<|^jyBK;{@ua9+YWq(e|H`GnFcNc)y2sgjk}<+8-PPlTHa#b{FvtOegM$HimZ-cNJeu!<Bfkyf4_s@-gvkhUIH8Pxy1uoSU!#F?PCCeuU0{QJp7vT@86mJ68LT&mV!T`4E$;6&>>0t^~AX1mGpCu_FdqC3A*`F6Z+caqYJS4PUvY?^q;FXF6422^7}ZgBCwk7Goktl=AnE#u7OX2^>Po)VJQ-I8hsk-`&sTO(kp)5=?Wls;KTI_DYpYS<kPF%BbxE8@z|WP2_;G>uh1k2oh1f7-5J8+d4R<mG(7nI)--+zig%Gzp+=2Ai?-={jx#;-5NS1@6MaXw_+Vaq%YV#kc!~uO@-K8IqMm3970y~ifE;y6Tf&;upmo$$2++<pYsdu3f67PRY%x>pfMs;J?+Uhp-Z`IXBPi&T*>?L_fj;w=u7#j}4s+`Y47HOPEI?y?1W2r#ayG$KeHNwg_avI)gG*ER#27UR%sluY$;!Wy=P1K7H3}vprL;K{u^`A7<jjuoN;%jrfR0Sissc>9Uz;`~Bv>FF%&84J+_Vxq#-dJ*#1kJ0_)CDKIkL934zO%PN%`{bj>plBKlm!vV5m3++Wg*>lmfmWpKKMZz$~O(X0_5Cy>ix@2iYXa9*9)XLP7pctwul|ZJ2(@qu3NcJq<UPGudeA{j{K<&^5`&UsF_&NBneH@0ue|bgzNUYG6dqnybqeZV*$)^6g9QiA?Ia5Qi?oB?_3*OR8ennd-^6hvxw60lTVc0F8a^C^^#QSRC0eox`vk>2i#hFp6A6DUX_ye;5g}=sLF}3lzMfT9BpJvV}Llk^>)4)dYiIP8t3RALB4cksv8lHCrH?LY->orM4;83kpF8=x9E-sN**jSFloo@(9rC8V5*jsc8?o3ulGfm-NIfG3rC)FIdcPZM3+*jio4ep3A-Et&%{fk!~=&pe!)YHRpymhg$W3vr&U%e?Tl_L%f;m<%y{t%JNt{S6(!gH(A5Lf4WhaRTPp8g4PYmv|MRZ3qe!q=vC}uof<Azg%<t4(WVcnm7~_G4Zr00GPqEn&YQaoWJ449Tw9aO^;FKMB|Ah597k(nZJYgJYBnz2qh&$A%en>zBVUtQe?AUyr;G9UkN8rCFf7q@Od=)?MSR}$1}sVT+Xm_wxF7L(&3@_p1}Ai*I=IbPXfPMNk(;yO%{(hDxQ9w(O{4TO%mTRa&s>s1C&CJ_h?vX3dS?pdl*lQboX)Ut;}D;a7b~MK2JazZ6P(r61RqeVv0pj`tJXm<+p2QnohD~>HCs-T(D-#$TLFUj5nAw;pE@}VaxM`D$^X`m&~$BE7DmW_sW!XkgBZgL+6l=<@*xddZrMsxDhH)u7;>2xZ6}a04}}UsaSMvwu?u|YIi)}C+TwyB0|02APx&j4&LI)X3C&)<Sh-h;KFwHJ!nG&>f<0fj4Y}r8A7@q{XO=Fu8tu|4D*zwy!_iaCHe6{2t*)h%DFel7i%U5u)?b+HTCuz@T=nb43;aR?*Ib97_oC-QndIPA#V2*yeLhvyk77qv?a0N+&b(2>egOw^f|M_srg}Vd>C6c?Gkcq5!aONamGk_U7(^SEC;-aD$(T?#d@^RMEv+8BTfH0BkPiEGXf%mm_{jJHYo9qTyjc;LkQt`@NtNC7`|8~{-WcDHkAp#HAD{jmzeM%@?!=2P{nRx3L%hmM6=b|1#UY|RdnyW?wz8*fIc!Kd<<QUa)plexK!IUy?7AY^1VAobQ5I_ie~&QW4=-)Joeb#>EWCrXGC6ocTg+9+1c?*W*v?M2Oi&xCVNmLfdM61(m?zmbF8QAldX@N2e_?p)8IAyLzwx*(Iz0-`pmqHFI65<|Xfk*une;-)$N<y0a4e_=*^*MwCtO0RA_p+3oQ9*gW2>n@^7~i2;ar3u6Tz~kCTCzPr%f3Z+!=#Qkg1x=hc5ikyBKpXI<*g&+V7*($PK-<jypve1pZ8c8-V$|g}c6tY43($KTzO?p(3BVf#gEkyP;%n(73_mpKFqER6*pXwD<uZ&{B%u*eS>aMUK#LyTid0<f*VXoALm^%Gq>^z6SVgxVX-J?ORWNOIe0%hVz)uV0~ixH+STuX+TwbcOZMGO~-3|AapyMHMP%GT&&Y+xp1Z{;1r=J0A;UNj8c{A^jcDb=O}R&;*+)bS}jn7pGJ@;1dvnGKz&P%=8`zTyQEOOd3O#VjB|{1r01t2KlO5DF#32Pi_niJi$%W3q=WfUK`xJs@p?j{L50aMx*jB;Q;g{f|CD<xW=?jMWCT;lADoY<i1GG1h2HqeI-%Jth$~^m>8Qy-9Xi14Ao-TUKH?#+Y}A*~s9c0`7~pBs^)i7Dj*fo6*I?zhoZChK21P5}3dUgh)21Vef6cio-CHjL)a})?#u_ghK(?SEZt!-q{TTUPbmAWlhl!v5mQ>DEdr4k61K^<uCF@aU#lT@eS@hv;K<m0_ltFLo$8b?=*=SPq$X3%hLqO!Of?@joJy46Vwlzg>n1qFq+wmRuW=V|ojM~&fLyjeQz=O}i(~Yl<9`}g~&Dja6VR<p71pdI4z#nk?JB3ek>pM9){ozdC!R2!f5;J!aK&2HzrPMAY^!c?l_BQtW{8}jUZ$Y{lehZ90N5I7r-M2$?aN;MU^Gl4G?V&0<owMp}3I;#J$RT*;7$-_1Hmb6iEm7<rnNzAu#}A$6`v1$`yDhhoB#DCW^%YrYJ1wLLKmd3V1&WeMlvL7b>ary3qLOJjNgzRF2}Gii07<Y~$L0g}am{vYUv@uX-_F}U%=we~g8hW`OWY$e0ZOW#wlmY#B_cB;JR&?IJls9};)HiO{)Dkq?XvCG_IAX%KFre8+aH)}B5nmzZ*1I;^J!XMC=?)aa^r-A6wLv;E-hNqh>)A?IO0q82IImT0cw~H#ljn2;la(Z&k$})hLAvMo{)O*(QR&WM1-?^b!k+rF1gl9R7Zxq1c1Zh18|hT`M1c))iF*0UD|Rn8WJwirmRS#!u5$)u!Ij63{B#%CYG9;7Tu&L*_bJ6lRq%21*o%4gTmi6?&eYVx*?mnD}I>98m}hijLuMXDFCW9TT&c4D|bKxKbRh<ICZ>R;e%nLHdgPsC!QstT={@?GB-Msp<^Pw;Q1TDvNk?BR%R2V=&vS2^g&$G)giuU$~Svv(f4lA_a#Mj<YuyhFyt`|-z+YHO)(8)I0s(OF<(0=6pxdODc}4WpOfiymR~;s#_{z<SGFXHTBjB9<r>+qQ92K)VaE#x(<%&$A*NmpiYgL<ULNRX8VU8mJ=_tur5>~VN;d=S<Yu>ImnudJ=5OyGl>mJawWuZ)zlqV+e}i6<3ZJwYlet$=437$`GVcB4?Ags%5*+|R5lrj4(-Ir{4I>0#)Y&45*NUl{NAyf6mH=xC>3H4{(C^9v+oo8Pr6@0t^QI~<AUNf5dT>wDy(kRbyZSjy)f|tO(|m5&!~KLomVp=UXz%X`dwg%7su}N=fp^rhdTsS8zZ^YFElMC&DH#ft<TgjuACf)ImaXelwOI--OoIeFY8kQ6O&$o@@jQF}L-**(GuM_!KzwA<sn{V}T&A?<);6-LikO*3h)&6EDyit3S@N@wi`XZ5Si`$C_Lh;sq5Jp6_9F7W6QvO_h|zW~l%Tn$B?3I8b0e0ghx>i6x;EkcmslP(D{3#fwfC_+fUcHa34-`OmM7BH(is4gW2Pj&8Xb21Je_K4i`0ZjojIrWQM17a6$ipyb3ZY(h9nIHOc0##6&N1~e9DJ!N%4*p{<BPHe?nyiFEU|d(QdUprLuXlF&n_GS$shF@Crmk7vx*nJ8QsBc$bb>g3$0qyyb5bkHnX1!e?zjBcLAs;GM>-gMZ^SDs*%OUt=yAil3zwEQlmIiu#3Pn2i(v$~r-<$dG{3dr^1SHj0w<{%b|OIn>+i#;YV1T$QRD?yQ;IguT`Oz&R0S$92;WP#^qd^sC_%5@ZW)$Af?-8q%Z!)I`I=xxP`bf-wP0@nK^5ziQM}ZX&GH4Vbcb%b2rn{CC1=U_}Iw++7QJw*-3E0$+}HxzD;SnN^VW4;Jf=cW2R`BTBNKT|`gQ%T#~t+I&68Qk+unt5q%%lA%$t<++kuG$o%kqTd=q3mC_q6h<Fj4X%&p?2BSwRoP$VvO=zj5o~>@J1L=V+(2{X&DaL7*a<^-f;YdW0}V{VbJ7D*O|s{Vl6i!JH-mOnn>a<nN}x=vSyQ#eQhr-Xyd=MRTf`brYzh&I$!?0Z+F%~KsTQSVk)aX$)S8TM!5CYkE<d|XMSxmBW&5b4u<W_Mpq8^6*s{p3!$@e<;s-P4_*<2d`~qD?hXUy7Rl#@R)^Ov!0N-FuNu>Z>F4xYgSI}+6OwzrW8j=9-s}xG6w!{~!%oP=o(3)Z4O|3Ljb@T5gi75{_!b@GLRXyp;p#P7hOU4&ST_zk;V@@l4y<Ni!w3Yis7V~yWWQ#TC2b+_&#m!d}^M#e9F*0_HcZB)-W|k>$n9t<~?nW&$8_}l{-dh(p+;t4j+x-6b<+~*t-M$6i?epm_KY(ZbVK$APOeU0M9nbxe6JMGiVv%w}V%z0cmlc{%=mU~Jp(3+2p0_#Krb_oEEm%l2)Kp5pwgQ<<Sqe6~5&PXLroNfU88S$?`pYjL>1KMIO;4#T-h<Iy;dX-@U!-)aHonshJVUmun=$7mX8@(EaeNB|S~m?ouELbRwA^dD4H8~@1bV~L%p1$8oLbG4*?o{VRyO*~eyICclP(duH4OEvYPDMrw%C>oXP|3H`U<}l9mHXlcaXn^I;hu<-C4t=&Fhb`t15a_LDd~vUV^Zui?QaqDEoZdC09xaLzd9Sa%tGh2MMDwSrha6ZUr2xn)O%##4P23ux4qpHWa6t^TNMZ-fTrr$;u!igKYEq1!OoD@>oK<r^5@FlAd#WjLU>=Ew$X-qR2FL&L7Kkq5aX#6+(@0Pfhu)+cHfh>=uj*y+%o6f=!PtXWnT`I&Me{E_Xp)N-@v%Rxo1iR5^3{$EuN9+8V2VAK-zi#E9?ZQDGzl(Bncw<I_I5h?agfEIWdQkTW`E%L4d=j-{q_@}0w9S-!yrwGckS+a~*>w)Q2;C6_`Vxy&dLhl6l<?VDE1GSj^Hun8pP67?hdVHLF-!wnX_WK(8v=H-*<*ZnpS()m>i?7p)SlgR+H7-L*Rjvq12$IJ74au37R!yb^UIp~CVv`SdA9TShfk!)o)UrykiftJ#Gubd*^-g(nB4jemxf;q&BGe;nE4NX?tRb;K*na_VTr|qD>;S7G_y;;k_$b@FRm;~T^Lk+EXL0VQXdqdM<TmFw{w^`&+{F^Rvv-v-Akq1by&t2J0Ip$C+8LXA+rV=&N?K|~{FM4M>8ZHvt7uB-o3TP94V{HRhG__;WD?(f8fMub+eG8hRmiVo}-+C6+DAwO|-|$TN2cX@N9MXT3ZKYOhL(hO9`D>gVYC$#(ycxeM6grzvThYrLO>?7TvPF(43p;R}`S~oFj<P=Le3}QzG(y%F7S|x_qnW9^gisc_-&+nf2ns44tm#xhzOs_hb(!>jGSw~F(kCZO*xLK9%>UBwNySFRhE~Ybt|R8RQjjBptMw$xM^YFeRt=26mG27vs<y)#!~WJAAl&;Br^w$7pUA4Uyw!@{PSK$QSFtpX-h3uQ<Y6Q|+nN!TW@z?8)-NPv{<7znc+Vx?bBXtcd>Jr+_q2@UKEa0U4ta+ud7WIFLU5J*tX2xQBg2>|C>v4Hq6Bpq@k6;h=o2EDr6<~^aGp%+9kz~>R|Jk-GP(A2cHOtO4dWbrdECvxgVinym97Y8jxW<NX#=w@s#)PMJlm)eG>4C4_MJfREwH~v_Sd_5{IC|4p4z_+5d%;xND*>+eHFT<RSrYr{45!tTxG@lC^4cUPh0%ubdH}+2kCjNaqru18kP$%6VBb8>DZT{nIle?X>zKr_gF(qN>3XlUP)5Z7GXyWa#D10+6<QV1Cp_ww>@h&tcaD9vKKI67eOSjdT^Hg%d{{-F5b+&K4t3{1!DSqa%p;Q$Y4o#qq%8O8X}AU(4&mn`^)lu{*7El-vq*>^=;phfQx-Gu{}$yB1Fm3>t{39<Wo>E&f0W}Tkll3h*AhO9`~cjw*id|cw4CE6=m_bA-@&jj0)@mC62=sX2<;m=DL1Ev0Cu|Bm56$*4Zw1@uT)tZ8+cKaKtv}LPDt&dGXMls9I7R+<OaBzJk*fmkPKLP12?>6fkBA4Xxjxho&Mo<TBPEn$zH(*lcdZi*coTKF~I+=CNsXd}u<`O?+~jZmX7U;nfKGuF0JUym^#afddVS#|1L0z~>dzD`35N`~BkZ65dvExCmoRY(&tA+*cF#oiGnw6=P);Xay$xeid|$YX#kWWkPp~PQDH3(iVfkDD0#0=?cNyS;KAP|3Vb(ghlS+#R{3*ha5VdY%aGGmb<a7*V$n8A+hcnUX$WW!<)08lgpG&<B;Q{yaS%*S0dJ+aFkMq#4fRQa1O*a5AR*I?%;*8c{CeaUgKcpWu|#L1?ZGfNSsfNGDbs;eZ?$&{_czLUqwMGH@P5T{#Mr?-0f(7iNC0s5@2Ots#|%gwF_p8?Esl-uLSl&D;w-p;yh1Qg0ZR^!)kvFzWO?VlZyViWQ<oZA_YV%pMAZp(BY@SDfP=XGJ%@{s!iVXCKFx6xVet>L{ih95AD6lAnCUa5xm)fyH}R^)9RfM@0S(uzP>|_=>HlJIg0*Fp3ae)n22L%6j9Qj<?tw+sCkZ*pkFL5s5&%q<hn@8Z?7iSr?u1|7Tk?;Lm9J;jVc|GX-jk=Ag417GpmDdTaBVqq<#I)?M%vQVHZRt!%K8Lel7gJefLuOnq1RYA3f_@quxrbbR|rzOgs8!xp67^B~g`!dMvRutSj5qP}g{*#}`{ewQ6`NNZpLEx>-FMvwh|Nyk~wCO*tPwe`kg9EjZ?nkh$=nE(r;wopD8i38XmD)X0w_cguH9Y+6q{W`v}*^kSwPm!YpUKcKow`v_}U+P3#_o~_UU7<lBTe0*@RiFDC+1-ol_l5bdT-IWIau)I6%wiDGNE#^N{XMaGp%V^;)Fdp44D|*OcJU&v9W8mN^ECb%h(H2Hfh$*gyA7RFQEo0p{fmaT)S^p^o>Q;HV&7dimguWOh(^Tc+&JXjebap`bA^AK(vjuF?3e5r)53`GG{>yt)ix&*cf^A&KBGY|I@D?nylw~YBGtA}%4?qp(JKKucJuWomkI`$w=&A6WP*#mbH7vPC_hSKr6dU^7sjR$oD|_R6Nh<~e7T=VEf?=NCFsN+>O3XHw?9*<1Ee@)EMIQ#)MbV2s$Z*Yr8)ZvvILG$P2bB~gnN8mH=e>Z(K6?1V40Lb<z*^J+0PgvPDf)|qi9WOI!PL<MR>6c37rnrSQsdw)*)z6hLnlSW_0^L<%=bJmJ>z%7q^cJ^O(Yto2MK;*BGGV3bWi_mxD>jlf2s+x&gP!;Y?V@HanE^{rCbW%^WMnZ9^aYy<cj$ZY0inb)rulVj~@R~b1>qU{I_95wdv8n4I_k2kN#E3Y4G&z@t=kp0;6YmTRCo9J@w1N{;w|b<>}E=zf_7FIemedG??IC$U#9}9QJ%uJ4wWQk!x{x%SrGP0cE(h0nN(wO{x<t3%6LM3Zi^<)#WF%i&&=;VhT`QBflKQX0o9b{XuswGZRsDaV!z*buhpv+FaqsY!WD+4X$G|i_yEakc1^wHFbwrRX1?aXkuD@ep8C_00a~F>hs%*NeI9&XG4#qWLiR_Fy}{oKPs81003*o)c03qQx||>&fz)jdi=L6*ARszd;!$niAy+3t~f2@iui=neK(Dxsu?%V_w}uT4w`6XKUqxoOCuw?4I4%Y^>Z`&Bj$~qL%9hsS$Br{cmS-zG=)>HxZ~wmL@Iogot@<q+0wq5k5o_z=$9|uO~=V(e@1oR!OzMbI>j)FVhaY(NrWD4w&{N{Q1}_}r_X1zd{)21-J-x@K<wb0&Z9AgFl<Ff=>P=oh=E3ASR8?H)*t10kw!^`nM`K#^IsPU3J$G1u@|&(KNvC*$JLtLY;+o%F~>6m4ryA4p6x$^fAnp4HmocDwAJFGaWfF|@8N#e8QaMyMWo7cO_CXYL<tiZ0y?bGrx}e=U_kQ`%0T%LoqMI3G>&)1Xt31@?l=hv1+OZ`D4H0+F!@k)r>v3FS+ozGYpF9qc$wYXbfu(c!2j(BSi}}GhOJ@@yVQ=zImVdUz@zMcXv+G4&wJg5e(d05`(uNPCfEBP?2>jtBQT_$q)*=J?R(sY68~BH-*4|_4+WaMA@5}y`<s>ufHeS6>9>cQdo23PL4icSuNH*yvf)AhkZqs>Qw~vA1cAeNSz1x0^Yp)e+}KxRZv{-yLm<0eB_q_s=kF@1g@9+`{<j<^xSll58YjzX8t*^)U4_lsM~aPa>xsbd#+mpL@4@#LbhV!7pJ$CkeHOF`KJ9(hbI71SrOPNEMj!5|Vclum5gZEqQoINJCawbh61#BcV~qRo1JwVxkNvL8Cy9H0FwZGFO5g}El@9jZlSraja2aY4fwd<<=oJTRO1y*V+;<@14D%ip-GGfMKB)o77YzZXVf4%(%3iKM+bW16mh2NXBoceKd$(R!#4*0hKNlO~)!n*$(TSbQDr{okJMIbo-JRHU#lPBjob0C{mSux<-)z`uXwU00Ej(Ov!M%z-`Ea$dq0y@ML2`E!HrL**>z#4E&wCD$D1a1B0SNtlsPV`z5UMJPBZPwR=V6!rm|wFSTqZXU_XP^zxAl2}pBM7;0)7X>*zeb=-MiflYyhT@F}smjGq;f~OdVq#0E>??p%<{5Y?wwoSms8QxiQN4bEI;z!veLqX}xZ(*9}S;8rXTCZC|bZ4=Ti<_v2&Z0#6VXa<CEj^)a+5L+77348n)Ng+u@OxnaQ()ceAr`1~9!`ngOALnrLMJS&Jnsb4mJgN1+DG>#sDu@C^%Y;5dTGG^tKh1z37ZHG&YWRf0SY~FR1k!RQY722=A{S8%jXUqKxB^Q;kf<-dFw%@+x%;}mY?)g>22&~}Dgg-T%kFl$2+ppGw{_Ssf?l?M7<j$oA^v>h%UDcI`dKH~r18(9TEs^%eCN8S>$A|l8*MI&qzUuI+4!&Ae%(c)!?N@yJ^Pk~I6>Fr<Q2U??Ks3~S8qq5XHoRs4@3EB!KnNkWz*dmX4!DsgbJnBPZzyjI-i4Tg+4(>jd3vlMiBRVQl`=vLKt`1Ea}0l85~%#<U<}<LRdPwp3#hF$M3L&D&8fd#%z?_S5fys&YO<=JxE5qvGxxHPtR3wjt3WNnH)nje>|8};ljD4x4P>k&HT;K&CE>Tg`Doq9FKamL=VW4TM@Is%GR=qxF;DT4WW%oYaYi7FKFXw(m2mCYOCD@7KO*XGzNb}&`fX-hmr`^9vm|4F!z?D)BLav4|1$Fy{tE8`VPaxAJy-VEM>IRJoFh9{ucO}MCD&7<k{XelpYz#xpx>jl<Dlhh9Svmmtfz*7ou0&zp-$}y1j$#JIPrCwOnSzxE@Fx<bXB2O6D|{+L|qZkY1O;pS`ucHQBEm7wSFCN*`t5;o8-Dj|5j>+UgopxCZEic@vp}y*dD-<dutklmn?!30;aA({Kw4SwVRs$a6{1F^(m)K2el$4Wa&m`$1;cuA;tkimx-;m6Wp8<)rV=PsaYz<PW!i^i~W4OR-TR<b}T8zEnbhN_rkbkE&|W%<`v!kLPLhhmsr8t&JIa2wy~DmO#ZE$W^9YyaJV8E9_|@-{epgLXBcM?6?H;Uj7kSv9*Ssf^M<kVf}uoDxw2;BU#2h3T8@zUnhu27f3S&h&92Kk`f76Pei~K&-s@+z+o4=wnX|NvU#^{9X%#f7%c{MyZg&;7{w3ILuD{m3_*(nQYyHbEx*~CozI*r3LgO3#kKx^KML(x!KOA<^+wG?;y_)8;dGvg8o=wuI&bew&uJY!)q`-`H&(Pf;b3fw&yb&EF<7}GFiue!c94^{(JgMXfOTtefdW(6SfN070cpdR>mY+MtQST9WjisM1hC|GlV}DUsRVzNfnherwE7O7h85OG5S4LYoaP_?ey8Yb+k9rvf?7+njNTED{AO;63!24kNEZD8g?#y@E(e)yoX(NJVa@E7|PCL82`ls2vKSCF}%^iL*5Glud(dMQK*2megdeH|R>v9+V#V`|mWv;lvi)6m_Y5-y^NJ<U|cwq`<a*K7Oit_?wcM8@DzqZw{j(*t@Z%wLn;j^RIf!B-iJVQUsq!FFjogj1Fif$-E&FmSFYW(pq+M*x6L`J!G&oIFsoEKZ@@7*z9kn07!>^d*I_;S;Exv6X(p_d9Iz1WWu#LwM`vh^k(w&-_<e(yq&yVwLibh`9qGXRMru_L680cqQS^uU6&Sp})fkh%t>9RpH_J1Zb<RYBThNSg+v`zEB032EDe^x0erc=Hil4DVozPg6Fc9OjqHqXcBwgkCjZAz;$DVKTE<$xtK?zo&g|*;7LRuo(1-E?q}>AX*{7y<4n0#0ahQp==VhB(jr~*H9OveK6F|yhrNLCZ_mEaV&SCQ$_)r_NIz|O7FI)5{rvNvTJm!u0rf#o_~5W|MkadJzb`as822h5|0#!nWPVTjiYNuP!4`*1<G)#3v^_Gj#=PF7wF0Y-H&!MI6Lm^5V-E)68^ifgT4+a;OlU_hpozAH{zGJm0nDLVU<n;e!kZ~f8{yW!k-GDg$-fO$OjJ|XyU+iv4W_pltf0L>H_gI#8mNEritCbpYIKQ6e38xMho8IH5WEYQ2s`Kjdr{O+%KLyYoMqA6cvD?!a-3%C@KIk#Zvvc5x-2?c7Yu)u%#gyxEI*L;nHk!fgR`fn2@5lrm|KE>^Q$)VhMtFZ8gKY#y(M;{Zd@-@e?iQVkw@GBx3vGu|w3VS*PZB5uyjiQap9&=|((tKN^kD&RNJtXy+|tBM+#Ng=%Dz8(CP5EUZQr!A7`uFnD^};iu)EvALUoJ9FC(tu}^M8^d55)Hzs<{B+-XV)~#T0|#x82%xucHYUz)mR!`&#|Lv*S(nA}409;sADgOPQm#xa)nc{B@hBOjGp^YB>G{#g^IuMnUp{&E{7CeizZ6vLIA6^AY5lSgO;|-lR|LSz!qn1m3E*G&D;XT2l?Z|2j|XpGzk7A~{Pg(b$;pq$v3<ycsL)EuGNty@aYVm*HCa=EeKi^8hxs|S9Xkd>S~q20&J8QE@#5&o53irUIa!I1VIgr{j*sDb_!!<AA1_wpW4JCprYs<s7?CT>8d@@+C;gEa8CJseu&Tt+E&&3`CkY%21koc3X#6lJ{(kuC&0kic=Mb6+AV>g~7@`iW!jX85Wdj?Lu=QGrQ^)C?myzt5FU0pOM02&emfU9-)dfHxuP%U+cy$RB!K+Jv=p8Olri#Y<84^sT1no#5{bX{P;I<p&{RNrxz-&AplV#7-<*Pxxc0O)$p_;iQL_Ihw#ZRnvkWbKFQEGt2$wi{FSEydQO3%*6U04ObM+qEdAh0KBv^`q@=ah`6qol`@bR(in)ch&>Z1m!Mtk;<#e`C45kp8f;Ctuo;C@A`yT|6HXQm^Ofq<}f8*WNxqK1~_NrzE7FF0#qIW@kv?jpyJ}o*KBYH`^#^{nMW=ft$yv#%GZ-2o~Ec?Pv6Ql%0>JXosFCrCBzKF4O*Il$^q{_g}(NH(pXrcnj-0@D>+!;5Dvf`Fb(QK!m&?t|eNWUR+KMsfXLVG&^FvHF|<?8TzH!74x;(7xR6wm<^MDdSvwJGN)X#*`#jj8mSv7dYRpcxF7V|=ugD`pw~u!BGC_qVst37J3`-0EaB=rm9{L%L?NQk`77;j)u}_F=xzUGt&8C|S{Ik0b#WP77ni|xaT#70!KskTgBn?!0-ILy1r0e5@^L;Z`OaRo!4lm30ua79AEDK2S%C{Qdmc+8YybNQXzoQaE&F^8A}ofQEBoFbXVX>Re@ez>pQlMtR8=42rQFE~2#d3qw(y6*jNAc;G%+0dQfDX>#L3taSgc5f=@azYga<TK=%N6ApW?7=Z5w)ZRrskc+}XuqyCT@XTNs_SB3T%gH>uKgs7l)_j9yrghWvnvb*V~cC$?Q(VHoJZwuSd~N;Q^YNDUZDgF6WVI^JSa*?Uyfh>}<WZzli`0O2?qT&gJ=#n5f-FcePNXh7lWI6e(zhk-n>fJoDpSvL3l{KGVjXB8I~=Sc8UWa?E(GW#}q1n8v}J;Zl*@EWmDvVxMM8ucFn=C)&sdWICFg;K0q)aWKxS5KIdk;>e}Zulkw{E&mV+cBEpOFx+n$^s@Cl{>gFo!S})sF`YtviG=b7^dJK%F$#G-9g<WM#t|?7bR{Unz-?XW+ZUDcP~1g0@((v(Pc-c7tsxOq)iN>Uz>D)A00e-79C(*fTp|)IY_3?d>b7M&37j}-y@8vg(?JCU}6l{7=)2WgIcm~Ytu#~@7iSg#NFXcJG$*)X@hvQX^TG~db1lUeLyN{+(Ot4MO1{{$X&(Jb+^e3WQVi5ce-|nEI|{wy{$SzYZz2q;0FObKtqy_6Xi;BW@}7Yw`WBkHKUTsNTfOlDaIr%pR$ta!BMb9g`AwF)mc$WMEK*lgRH>C37wHwxU&!BK2OfcP9>ezIcv)hoj>#%XqsyPkh~T96E%Xt>$wV0`_69MP)A1FnDs8a=U!9nuTT$(N2ft`c4<^yN|22GzRPv1W?ghmu=?vxFpcUBYOtmMR-G6mD{MRr_$=vvdI1~{lmu@6^u-LeD?CG|Y$`0v#RRnZX3uHrC#xx9lO*EZWAd<LcMFl)gsJXQ5|bTFTGHCyiM?uFzZ%a@6Zergzr9+Up<3;2o;yx76I&sWc})$69geh6ALR4;n+Ehc_QNI1vR$Wax1#K(Q+898HFu}FIX;;slVZF;je5kF%J(=Sq_{zjSZU(yN1H^1_TyxL5f)J!E;{m499X);Sz1g|+!q-7iq9oxN}#^Mji4<>CqP_ZUR&rt#0#RI0`1_n$uFW61353R1#%kEHgYSp$F{Z&REc)3VTbroub<$S+4IgfQ_fLmjQu)r%+S1WI3f|#20hh8j!Sl=ZcuE0nd1YgN?Jrs3}^ye@cB5uqC}Et7=Evx1BLzG0#6$<E66YmE!a~rL2p{(zG7#0&#FK}r{+cEPOI```%K%~6m$$u3hTo*^QrdPBNvip+2vBw?cGI^w(Ioin#rh9DuNBS#e{Ern+P9nt_?o@_^}&XFzA09b}x5{E^O`K8mP-<$s`xA0%-kEyjo`%yas&S;O$_Sd$Ei67z~k^K+2@FA(MZ}FBS);`7UQQ?U$?@%;84C1|rzCu!S*I1S||-l#6LJUR-38d{IRGWin}==i>n#3n9D;0@h{5gV>Z^#tBZO?lmDfmPkYa2MZCJO7KIW>0EpS2JH=vf-JDtCXA@K$UiNk6fGFWgL^n2SolcDt}+<>3o&sx{Bxa&%~;M<SS;t@`g^RHFJ8TbgYB+b);4v&zZF>4LIolKuHRy}%cqQ7i9K70+}`Hx6bE;NZiaV6n|DOl-Vxo^I|AFL*%!>Gw<GTFR&J-&3!x*Hzp)UkJ=Wc|#Sw?VYF<IWBtmh2$0fv4;6XIEJMN~r*8JEt@jo^>ph@U%#SJAl-6d*Nw*B!`;RjBQhEY?vVrhU|kN>8Fk2_<WeB!l&Erf#Y_%_V=91aeUucEip<gbe~diV6Gd6>=9h`r|NkT)p;YeL6o=>Xje%=HYb)lxOVA`PgfBzYGKmJpkupj%29(x;h0NvkE$FFk8j<2e2N(6IF?;?&xTJ;jaDCB@y^!f@4Sy#_^a)cd^Pc4JSgWXvS99phw~&O|&>>@M%7c1H>`La_i(n;_G4wjUV4L_c81C@3zg{jyWdQwff0lua^<$H!xOutO_$i)<sbqS3DhySx+N#5#%-Q;=hd8FsCXBUGX>i)c6Cv;d?vb3{Dga2&oJm?ZS9G6gae-B_0<gmbkbHtGH5eX$f8)Py&(8R=FuA8U;6CpEauR+qWVZr8;-V&){X`@|GLt{1JJ^;Cm`j>zea>T-Y^M6j(xU{f6e_L;C5AnTDJ%+xWa>z!~Zfh#_wSl_uzX93{F80sp*EJs2*4gBpA=C<G_9l~6)V<b477AB+us6k-mzPF@1k2rI+RaX#~#UZTSZ+taXeuEU&d47wVl&>3xaW#QG?we;rKqp@{7-J$FKw<pj6;OvezD`e*`Fxh00gD;HyZ6nw0n*<B7li&t^FGM`y54o+Winf$fal*)IbV!!$}fT2D)*DwMfcl(uq(t{te=0ZN%_yq#6R#dam_13^SaEu=(2SBe2i^vt#LuN>Tb{mUvew>`G4X|vcR>NcNMng<=5x0yec9UcXDoV4suTJ3yDHV)z!k=`qv-fCV2tunho!++2k6kePNtqs`Itt{tNW>>nfGY)y1}=+0h(_Zq7*fzm2Ze;(8xjvK#Zf-L_pu>x*_u^+kdKxMf#Zy|~5fJ7s0J)r;a9XluJfy%^-d1xn0uDJ95WBvl-&-RPRy4NIpHT8(|WUAoQcQ_`}dL4bh=v;{cm^;HyKe_f>ST2@}+ut2?*JPndnKrB{*BO6uRr3rW7BZq9sek9_N;3pN}N>hu?I2+Gh2?87nVEEHkQ>-I?h1LK=T2FfVM%??FQq#IjV}+b_iw;)_Mqal}EXuM@Hw^bm&-T8dEi)e*Hj_OqBv~bfMhV3R%lIhTU2|14QgH0)*>sxGB^3H%V>sFeGi<~x<M#Ltq1ELBPM(z&EVs?`v14$|WlTrSKoMbSP4O_ErUMn6RMyTW18JB1{4$-)i#l89#=aqQ2#Po%#c52&$f`rJMPp@XDKp~EZdC~Q>tG1@v*p?V!ZGAW*FrOQ7dm5oSn3a!+YrZ^r#SoHI&wY+>X+#rP2Z?_iqSOyS&yR4ZX2P(xcT?vXp=&!7+znxgI;K!r$&e)*wv%!28`27{rOi6XM;uW(jPB41EQ=+K<Ey*PG#>=H|eSc{_a7chXM-gg7MA9z9{5I6DZ6SEyZ7F^ST{|3H#KH(4pwswFBg;kBB5P0y%r!HD;>g94}3lanPg8cu^kzV7botmfrZ5)#LkR<@nG=Y8e{eFM;vV;C^XDOEo^{g&($0#8#S|AE#t<bieCOZNW}f1@LvUAUp-b5w@*FV?|7NyrPO*wqup87Zf%kT*DZm$)53YR7t=R<Uq`qc+EgB$r`q*W+zlrFiPF>=olvIQ6b+X7|m!)G#Le6#zCit(tQN9D7cG8*VTK-S@ol(x#UO7Td()gGQ8U1edSs=QG}#L_rrXu!mI*C^=TxGT>DWK3zP~M(q)?ALd`%a1^GK?O;~GTmkL@d!F?46lIkRO066JxO`!EzZU$F?8X`m!OwXot6>H&{Ee?2idUAC1<o)T>A78w9e$>$1K&*??Gsd;@i$e?O0@gyGu~!GD&yJq_960zFQ|RzO^Ctii{xo#hm4=L}($GOu8XOa)!4XdyGM-5TZHKOYERu5-y>``*sI`_B*H?_m=#_3tIYO<|l-4w?XiAOx3meiG%_|x*u=<5fQ4pH-@W<2kh3!xbo3+{z>tb~~&kvuI(`m3hjD({d&*2H9jhL*F;QE1uazl*brh;>JXM20ouygl%9d16bocFYcpa^*awSRnb{OX4{&!3&XdUI0Z5w})*G73;<hslO$KVH8B$1mR=odmo$f9G)gy~qxH-H7G@qo;s<4$*}HdI&42=7)Db1|<Sd?g>c-eW;(J!lgWPpXK~Wr2#tsa-wz<%WX_*RrnlN8DzyOPAS!mO8`BnVq7ZG4fjb?BKy508}?hh#~moNAMJO%ckFj^Me23+?ERZ3uLW8E&N$CXuz`aW@vcL~#FC;?bFs-n=LE{KCpoT#^E3}F2SdUREd;fmRcOYnQ27of=O6$%LyLOO5oXC!sLgm?IgLht6!Jo|ckWN!d1&6w-AOxlXYAacE;VX%qO71wav<gunemm>cb**Wq6>|=c~~gtNZ`HPKA3z9int06SG+8y)tL2FB%1%Snt$iw+WG#*M!WO%tvdrQbaOJCZ%5|5L_wtJul6Jv{9!ou7o*3VuP7V_Ocb1}qsuuXDng4XCNoHk*E_nknrXe08<AwkefJI_H?Ejh#bIon=&jIMtrB}e8rDLvowoD*IPbs9Ic5cVcymz<iHdOQQZ?C#YNSW4xtUGgkV(Mmy1)^7b>EWR!0Nid<au@9v2no~orZ#5ZDD$_x;7G>T5Qk)fv!i^;dopAn`&_KA`WiJT@WcEs0Fj+rBUWxP6{(osu69H^zq{G?UR#+^zcXZzUPN8=ITp2Zr&SKcl?cAvZUis>UJH+h4LjGH_cG1JO0)#S<-PRMX^EG?l`T|FIp>F*jTw(oT6o`1&ZCS^U_)2)}1#bm{pxWa*CF89*eEn`7aZGKI_Peub-SeKYI1#@bul$^W*0y$1296@K-o3vhk;01YAE}M{@AQuD1T&*~EP2ba6@F*dCQF2D;lHQEFS9Q)ou?6d>~&iqqJRK8v7?DIlkx&*w=GAB|@2KOlP(zP;PEn_-)hP0^Uy3|bDTX4+lZ%mt=PJB8}WMb__`%{=JP{V-n@-nX0Kt3x(MxNkMHvlDElpHHXh?DTAwPi|7H8R2`+{qES!Y_j>TxRSS!W;SzQHG^gcJ*~ks=VnV^dEW0jb7OR2yK6SnF_G5Umd%KZ>t3LlZ8M&L-Hi85HG@V68fn|Kgq_HnctBB<!-H`){gH1T3rk3}W2^6TY;_~3%+L>y?nGJtJ-WyTX^#yqE=6ym&u*fj;r!Q7uy>FrymvaBJ~=Hr363!TfPyroOo2M3SyedqXoI`qL{*ag@2dV&3!h!0CNPDr<p&E)n~N&iHPIktA<S1|UZ7cnI7`Rl<*Ce92ZL$YgT&=h@p+Q=KbfD|R$vFcfI7Q&ItskFf6t~1*df3fThhox0p3U@3hn$Na>yMuWCr{>ba@G^^Nf^1FEDggy-YHtJ7#>47tUd2g^1aNH?H*C`dSn}n@H|7WXK~<rt)((0L~ZM*x9o0CZXcXs)`~vG}PSMwQCNhGxMJB3eJ%Hsx?S2aS3ME>G%lQLkg_eh`LtQE2l-{UVsL27lGS}PezqhUfNa2z=KC|MFYqD30JJTp|`wu==I2uFwH7PCJnn1RI#KWJcMPKEe?i$)rbrwD}|4GofMzy7(q(E=R+P3+-J|<oxD6fd47Ci)XEC^`QXRH!_yZ}4xR_UK0SQ?=9$TG^GcqRuN~1gvgxc@JV}3?CTu2DmrkI&D(Zr^SMl|RR>k%MqSGBZ{yLkxR@Lv!8Z?Zzhi{JrJ8}B-)k*ZXNR3^;jV(<|KQG?NiN}jI4&vORV9nO@KnuJ5=!2RtD#p>8IX0wtC8Ii{DHp=N>%m?oS8*c<r?VOk-t(=5(+$IM0q`IRf_+s#o#nrYc%WuX-_2d3WY3=e&^>zc3|1jfFyOw)H)*TuCHKHJE1<XmY|Y+Ub<jv?-;OMeooNs-XXbz^VqiZK#DfR&o|7_?Xyk#4(v6Mv@Sg@wZZG1l0d?rnzx4Yh{eIa{t@U)fGKKX$G<S`j&5|qO26&I17vHfVMTD2Bn9nDAk<Fmr^{ZJnPYVwE7M-Qg*;IrGKzr2hW3|t$o3lp_)4wQ`t&k$>2G=eOqF~Br+4a`&vd)6FK#r2EWmS-@$wI3ZD>fdU+>|7X`P<=B=*<96iSO$bX}n0$R`Qt%er$%bGa%azH*y?X!*vEgrd+jHd)W$hRrpTnJ6r8)xRREARWCL<z6CoNcO4f*&oTQe8ZvwxcQ`!8R*B^Vh;C>cR-s@r+OQN%x4x%cC25L&tRZZQk}Fjde00H1q&5od;^C_|&yT5)xt;90Y}mnFv4b%w1Uh@yH=<(_7vcz&cKYs3D=RB@q~y82U`HCduBsiW0dB4b3aA@`f<M}|Q!>!=zobjW{3~<u$59P`*Faq0FHkU@W!m*aRmTI=5z#*|)Q`v#x!+o**#5->QkKU!ENG25`7g(hVc0AI@~Z&I&Tt)w%8^IHqZeNcPP+X_X!QKW(1h5G!0O*S6R&8uoN%U$stT-(4y8adjk0gs0ofY%z*~4<4_^Ak)M9;hw@|S9Du^J$S^zJ<Vg{u1NzJitzbzc?P^D4noo5bCMN{D`3G*sb71d{@oF?;#6p@c`NF48~2{a!l<v=hth<JAEkI?6$z+Cc^Xozku{6fUQMImON)4!Uhq84PNEMk15mR^8JjNgxs4o;sOzI*wE&WX2go}a#c_2$RpQ}y1it0gCHbT8bhDIb|7`it=x;}l?-7e{a3oH)?oKoK#I=_on@BKYQqLp+Z3G1AcYoqUd!HSqMw!C$^L{1O?^Hr)(etjoL9ke*9_(AuJhtlY94tiF7|xFPex3)wf(*t6TOKwxOpjga+#$$VHY@@0Z~xqw~576#&sARg8NcAIXvT7Yk}%CPqoRT4u;zQhQMX*j}UGL4SRSSkOx_P%`W0n%UQz<SKBkdVjeMb@Oibkk&pK`hMJkuqK+Mv2rxBdysmbN87#Qt}u$B^poDz&HD+sBgvzF{=gc{CPT!Lf_YKIkno{*`4I_gX8OtjunT;*DbK_dJD`oW4Xop@@JtDu;H**S2ZPBMTI_x5+1@T-E09#Lv+9z{W+VZLsZd3X!|lwmX5;lN_~fwVB2B{lJI?2NL!JG&<NGze?P5B#RB~D#b+rAOgg=;w%|K^4;x%JIlb~-OI4u<yXzEcuTiMmr9zvYY5E_os_?9X{=sw=*7CM0g!h=<QCqF(5Y{~^GMbN~?lTVEEP{@TjTP1ZbUAJI`K3t15sN!0yipRxMd^C{hvwsaTGioyy14i!-RpnyyZujpL?%vk!G^kLASjd#`XoQ@&(d^Kzq*F`S;Bue4b~oOZLyOC1zlsH1m_dHLjM<hq8xo!OYy`x1+Q+zW5>?9)?W$`9Sg*^1>%7NV$%k3BS3U55IYtK&LXHmY}p{L1c*%w#C;n?#|E+e(YPwRqHEn&r!<TBWI%yr`{+E>zjD6dt!jU1d~veuT=$|n0l2Hfli@`zO^hhBBp3eesL25D8f9LpWITiZuRTN<wp5n-2Dj`%GJsv1U%gC|LA{T;xaQgP7y9=-h_c!27y1`|1Ch5E#f1E&@S`<IoM)`(USdLhj-I<EzRa&%XX$x1d6&#bDt$S;yvQ%plf16`VSGa}DZat@u^E7gkT<Y9ckwzAYw)-C`Ww3PU9AJBSplc%!|9K6IES49472gL9+%?#S-t?eM_6Z!Uw0bO68^jH!e97LL=qb$1xOe+&M7(jbr+p4JJtm=VttA4m-c%OuVN(f!wlntrE&QyqM&T)fHHe-+P(p<Wi02V>l-WsUlJVJVLCCdyzjTR8{C__GSrB|SCJrhqw!bFXZfe}c)lb%O2Y$QBDdrdPU_F%Lb}u1**3-~P)X3!IUa1!;8p#@794IL<MkFKPm{lhc-p-FTO%^tl<kGLpIi*h1$w+KmJNl@>S|)`V68wU?8FSDsC<@Itju?~a0y%={{t|X{;3h2<+Fj%D4S<QBbttremZ!XU#IG}D>R|QoUDv%_uFj{b6UI8>*&rwQuLESmP7}@L)~e>A54Rm0Jm}HI6cqP=*L&^_9CC;AmjB@%P)JH43Na$w>;1DYc$U2T81ohBs?^QX;Lg^=?P}Dq6}PYx!?dmvk<7V!42Gvx<-;u%QGGW@T;XwW*AMb-;D56|5`pXaW-6_EdTheEgQ^BuJ)3$o8Sb<X9Y&`Mn8ZsG)~F!5yaau?u0Rilt?g01YMICc{GIyEuu*Z<;Y2G3}SJb^hZ%XABm9dxIKt(Yh?xVh~}imzLzYiM#(Fgeo>lZ{AD{OW64oAcQbw&a6U1RPXNJaQ5c@XdmEmbB@BV0i+}j^anCCwMv6=18laz18jiCTPV5#6SM-RpgU^rfdnpV&ua^X4Nias3d>COY8OBR`Mi@&sevaw|l$Oxk5W~0{>PxhkJHzY{kE>RL*@Z0(X=5#;v)0lm?!+MGiO^Z!yeuwu+$Ja<M`yD%`Q%=_niECtw!b6Cg3iP}^e4XR5ndb7sK;IT9P+e9Q>g6<l8b#nUyFRmWD76TkAQb&^@*fe#>KW(s?M&>+z;$TBbtRxbeJXvYFK7D?wM15Em51DpC$F~HV}X=UXgb>>eGX*7%v|AYiFC?kwuWNc3caw4WZ*~tL%I<h;!%&y6qtT)Y<AJ-7a<cPs7dO{o$F>N2Hw?LLB>s6#XI_492N52t{QZwAGN9HuQ!uIop!M$#j0i^(FT!RYkhkbHSCG6uJVSliP88urj@)C#X4T9wi9Q^eCQ!$sUb{=al9;P`Y004(tXnBWEDRVL!PbD<I2g*02i-SUjpKkJZl>ed?hJpzO<fMvx`2UWQ=(A$F0|FEEUpet~7A9EvuMoC@nm`Nc4hoLUx=c2%sn=Y3O#l2hAKGRPN0wX_aBY*05%DI`s1MEuyO(h%bfW5@5aLhOb@Y82W3*R#3irOdPHkXd`1x~{nfuFnS{b8g>4POTmleoM%a<bgE+BJ~q65Rxr0CsUtAeu$o|V8>+Dhjmr(W(zm3CS);4xjO{B$59<R#k2Oh(wrQRXrri?T)jvxrsEXw@<eQqx@^zf{>AwA69D|-!6*m8G!kqt60<15;lt!lQ@j$PcuDhI7%;Mh;|w)Zz@A}t-~}NVi2N1aZ~r9u%=h#K04217goz)rbE2sylXIR_Vb=*{nl>2)ngL3^SLIo-H0H%LFSqQItcK9~AIJMklZFT6rif;=qmpqBCE$p|K2yFoaqYz8`rdOUPbTL_axdn1g;CcnH6jj{V^I^RaF`B*<@Kn8HGh*0Q6XYo>UGurJy``XHi6^gzeE#Dy#7tJ>Qtt;;ksJ-pyV^hql^G3*NNLt2Y%3WU)qs|UbfV2TF1;+X!pd9zNF5BV%(a&UCci)zCMa<JB>giXucBSHK$Ph5N9Z){*>;!vK7SOM=LfFV--C^U?<}(;M?I4Wcgnjl~pN%k*;bC)u?wveev|JrhmB}!qK`zP>3?eKrh!Agk4#TLRJ2vVOaL*<LB4&70hS5egDDE88e@qLHgiq#}fPj#>;#q2Ri@|?Y7`xhsoJi+XX`T%U1PdcXM~hKz6o<!$IN#p=?eop!9b(hn@SfEBD)5n>8)OtNTJ}IWS5wlNw3wOm{Or5HPO7NE;f=^9#Q0UcwAOJtLe7pHglhfSZ$R769utAmXPtr&O(`ubbgmq2sh(`~Bu~t)Wi7);xa!Y}laQiGziw{W%u5qVB1aP)APl)l1Bv5jT(dldyvgu|mo<Ozt7qX^GTN&xBW#x@@VZGM6|7riA0_3`B5||LUGNyrN$jecDW&sRd9m+H)=z(K+lL^6fhN5Pw)guZhTDb&|ums9)+xlsXEPayY&cT_`{?zn_ouvt(?f(AqY?+9G7v0&J=zHw`stiBxW>LV2Vxkz&a4o~aO3Ul}o`KEi=<Bw-wdU>r#pM;;7Y#p<y}_PX;F?sf-d4`gF{A==gu!g~g4Bxe+2TJ9%!Rf~;Xafy2ZXyX9DzD|>gxr<7-1c$bixI?j-I~A)>jLi-1WQ?jtm^Rs++wY!kOXL!Kif$WdW&=yi+ev>$!v-RkC!?(YiSqe~Zzhx4$|htRMKsafIB-O-I)nKXdNuiyL%5{w>Qi{-0p{J~!$^+S9?6%S#bveEIE>dDjbQ{!(}Khf24yNHOLq;FZ^^$)`g<gvkMLO>&W*^is1Z(y@X6gcBMN{K+BvT#WgDkr>rnr2=TOID`@>RxSR($=abESv=z8_$F)Y&r0*?ZxMTnG_5OdsEb`j@#%P(M(^sdwjR#0u5=2}x0`;dclIWUI0V;FfrX(Vmw5`IM>HGV2kpyV8-e@4$MnX6HRtuIQ4*J<s1&G3Li?l^~v{e2_aDS_jlAOOiN;lm0bO7IaWUtb9rP_?_W7bx@IU>49vd#?gf-P<8bZ;YexS)(u{7eRQf&`=uO+tT5iZ~Ze`G1M1YS7SQbxtO_nolTzMVzZPoKr`?I@Y(%~7OpOMczxm5O|DDoCf7#Y<l3)0$uE9pjnrjU;I=f2plppbiJaK+f=OMJ2#p(R#uqb+LtR&$X{s^B6cGi3=ObAm!jEYy%1gF)?HeW42ZPAsyVDsQ9wx)@@bN@<afCsJ-zf}|ITn{)S*uEN%~g0HVY(hj?^-q<|IlzdAIcoz9UQz9H=^w=v4-(#t)W|OND{ox!QdIMJ<aDJsYNU%dfZb~$9Na*sMX@k&A-Ox6&c>K9P)CTC4(&c(Eg~|8w~AXX$W47XVBOR#zerp4QFLnS<O%hC={Aw9nA*x8`Bd1BlMf+Ktrq^gO(Tt>X8fJ(b($RH3T|ZA7w(Dal)@5m2qe2SQ0;%u?tz0gPzKA_;XnzU6sm`+h5QvJVvdqxt-!t8&0V(L>hpGC<YN6riQrAP&sYK_)wnGM(<t0pG&=0i3!vo=;T!GVK3K|%BwNyv~q2<VxHZ>PJ|YM7-d5a<O@V>i3nK3E}^EEKBZQhZ7s1_PDC@ptk<HS4Wq$^+CyuKzF|`+Ji%wl@Ex+RbhDt$R*Vbfzb>HO5#1|W0cvzb`?A*psLd|~peK{;f{ed8;*Dy@NW2#Ak*%^%7W4dgnoTSL#JGPUKB2v9rh~J_;o5lkp?C!P0(N7=Y|gjMC;3mDOyhSa4ox@=lWn4SQG{8)7JdrG^(noqKOZ}n^x~>U-s1@fbW!2oP~*kM<4`c5d%@zp$g;H@CF7yGD1)8-Kt~vHiy2;H;_@SzClgLWfj>-8u{_7b{m6Dh495xj165w+msUCv14_ebSJVYg<w<mgcSyL#is>i??i52?L})X%l-GlBe4=!mP5R>nmFzDH<Za;G27wjztCN9*H%kFW!-zDnRQ4=g<|qn|QsmMyRCpKJc$6>FIm~zjJNhz>$jFb3!?4`TAD^{Mb_iIYMd8@7!rJ(N(c9=pNB-!3jLnNiD?STe6N>;7@Xv_LeY6Uy7&E4wz<tgM!kxIMnF@h&Y_QYnY{%B_Hn*1_J~f=wN9-P?ML-D8&%J%m_IDF<JMli?HTy3*@T`3Go?m@uL}y9{18VpXMw^0M4)mI>PhcZ0fJAFjgjWd>X3|Nq{IhhJEXMOX=DLbkft<1<$soU)cpx>kmxDBo)AR`IY3pnOT=ax55K(Tj-gNm*fy~@rQhl;ZR7isIi}~Tb@!`D_w+gsO;Q(`xOi@&O+=4!cp}ZOxq;Rdl<GEcnc+#9o48%^tJHy&rjR9{Aa9mEAr8yi?=KYr-!qjZ>4ER}Q;KMOmq3An)BPtV~Go3A0aHi|{UsOsHC+t(O^!q>@E2pp<wW>*0>UU*pcU4cz>U5ks@7Jh<(WuDg-7o41uf`E9+o5xK+XGI)t4xB^>`>T9MaTKkD!swIK#2FZ<G>jnIO0Fs_p$Kp8LU2}BP;f%#dwG%4^%#d6Mvn}vbWY&SxjN0h(5*ZRq5lp8(Y<?>s^gfDjythfXdlCZqlFU%3LkIp2AoM>3E*JmrK8+Ym}cRn7P-S+udzCUHsj|?Zt+nPiRgXK%de2I=f7JJW*><r@`46c76X7qQd6jOxaf0;2xz#c9Xt6E7BR7k)xSg4fut02r|T==A|^tMHU^qT9CUfWkp#I=sr7GK;7qq4Dev^sTw1BD`)s-Ry^JXf0UEoF5a4nYzM%$be~1XikFF~zY%vBef;|P{71U?;Tg|8`O74qzoPS^NlYo(-=o>N{lN+TDp347nNINn-)2L!>sB~C=B8~eH*yPVv(K*Wl`%~QsN34?Vm6xrUZ~-94E#LNKcAxVqifsy<#Q`;C&nrU;>zIY&r$4Fc<ELcamf?@^VBwNO>t&P=tqznqDhmT6ovp79IEfxa)JSlMR>f!>;f3)x}6U(9lQiCQE3REDsKCy>EM_5Zs=FDt73&e*w%i>5)?9<?Hy%;QyC$aEvCBR!cMr@s<LkESf^~K1O4>%d&nREO#T`Yjaxe^<)!8Jc-4!pB(PC08Z{IrI5_Olzs8#*dUIsFIiWWv#+#?~=BavvJ?QZt^W95+r`#sR3h2on@;y#ZkN#CE#*_RPx{d7_rwQJC%c04|v;nU{Xu!HCC=gEeWXNZRgPO@zV4BrnZZHMMN&emhb2BmE(3;<nfqe1PT^_mt<oYB(G67s0^>t29>-eJeoLmzXIch}pI;zP;pD~{x^%L8oj>kr0%ai<9?6le7GSr}L64()GyAdHvv6rzS8cVE_@CN(=V80ra`z1)MAh<dji>afr(B_d-47hO0V(+OCdksB}KypibIVBFIfc{U7lW&T_Wd_&w0Vw<&;5{XCYVcITx}1}AJELDH-hKkHu@}|23pE`;`*Z9kMw-2W4XcRG)Z4$7lZA`~D>~6uU0|`dr=a)&rbVC5C_ajsS^=n|$08_`(ErR(>t#dsLt9JG_{E3aHDF&Qz}S?-=FcJ6^u>q0X&?Y&`~ob(r>ck8^s8;DY8`<$eelo=niDuwTH|bbIvgjn6r*q}sPMKXCh=p~L$mwrbvDVKCWG^|(n}MwDIc<>$ZDU=opw8V(ArwxC9_B-XiGiIhP5wtwY-v!mK}>RI3tbtwwIBZ{VA{flbF&Cvzz3|`uYd>m7M{y&(Kfo3jV`j!7IGV?DCa9Wn#JvAF^%XJ|=z0x~2~q`j4SM%zchUy}l1wXQdBWl@oJGkN<@3V%<L5xTfiFYnXh6!`K;KYLJgtwToD2cUa<r<LI?Yacr{cj)Rxs-E|Ast}pfL`U;mQIBl3O4YT!L9E=iAC;-#C3b{}9N7a=^YebgsmxPw@m&caxmj;*be?y-s8a4kJ#f~r0p=htf(%Zz*`79g2J_>AV%o0MW?mJylL3ehHJ?-uI_Wjs`i|#F9xCn9cK7!p8VVN~p{Dv7<Iy)S`xordGJ??=;+xG|eg%y6geKt(Ct!iY;bzD-nzq7sB*^(CT4^r3oKDo^1%NMZe*BVWGr+hT{%?dJ-jK^yO?(UWY-gMAJE4&<Xw}W8Y_c<m~tGn&aYX=3-?H$>yb!uMEeH3mdJ3IG<)4=Y|1E8;l(*VU^C!_WfS}s;#$r-?}l@or(PWTxHwb_EdrqjJJTc;@Yz}X4`A_Hc7i#d9DNfN}`_tyf>VIvCKB{1P>%I1#TVkLL=H?J>jZ>aLrFCBo+1F!&_CmYX*^;K|64_e#6B}q;wzz8`9n(&H%?g5jx#U9X`o*DK52}@D2ya4`mwxo@|W@HpW6H3C2K#N=JhBiTrOOaR2wjb%lD>l-z^|UeoifcG<53kX#QKupA)y@~$Af<&}p+3=`VLZjGc!8k}POpWcNoBn;zAeQ!<6x4IAM)yEx!PX&XV=nA4@)S4UsjE8<G5i`1In~TbVd<_!1Q%*>5?IO>rJ0EfmWfw<gI1-VXxokm&tem2#?+!ynOY}xY>>V9HrMFY)8}4vY<P0B+&PWm_}zHen<5uhd)1ge;gH~{A%)jyiyLA$MMU2JkF7Unfd`cM<6f4jE|^@MQX>%GM&A2oDG4MezUkZOJ~lCqQa+&c95eqP;VzINFn^lRF@u;yg449&ZW5@5*`#%MI=$2hf`u~94iPy3lTC2Od$WU!Esrdkf}x5*fA0$X)-#r+E-?oJ#*-o%Aph%rg~F-79a^F1?n&vksEwc#@;A?wE{nJ_Bc7bd(LQ#hHXfwBt^dz3%Q#V_`7S%fKc)nL}<Gtnn+Sa#;vx+%YB;U^MVWxQ;Zy|b@!+yFX~gP55-hSEtK>6U4N8KkLgvNz_hMGGUi`Po4aP$Zfs}QZa#(0LQXeF*0tNs#Jfg$i+8h7np=h4lfV+C#v7=;b9|DfMdX<Ih@-LXIoIA`95blkfVk<HlhzR>Hv%OGv#PFj(Aur^Yukl&V@VWg6V_e*22W`yO4=K}JnWjqcxqjlZd!YTo(8Be9o)o@tGuox)|gQb(B6~_su9tX+~v}k^sloyDN#453wQC~IM!F4hHv8W;tXRn&C)*XLpbP&vSdK~m<NuKQ7Av1gDjd@SV2bZ2DgCRfJ)OVULZ1wbrTRAY|dUy#H8}-tb0rB+B*iJj#Eamic%SELLv85nfKics%A2Iq)0I%tLcxQeWYk)kTE>`Z8raINU@nBsl_LxG(04D%AeA(fyyq}6q9`Qj^V?1JW4P-!A7*T-5jLnvouw)$vIj%t=^}2-u_wGq92cwvr-n*TZqsM^Fi#ogO)=10#0zYZf`z{=K1t1R;+=42mQC9fPv-tcVC<eQS9p^5e4W$EQvMucU{K*B4ymzYkJj!MH@j1{~!j&92`g4fPsx+-8VQ52L5zLFFXC!>*QOEp0?<%2Ty@D?8PtUl=r|_OlfHGS9H5%D|{1*V`xvx=?!M3!>BO@Q5N#z+Yswvnva*~z|6o`wjieH$0H;~!Uul?D$FiK@d9X2G>0S6=wUXsFVB}muHId{J6F!URrYB<_e&ay{G8#MIvu+N=>!c;h3G^>DLj5|XcmH!!iu(=s%&gUH?;)8kXi~uMsk+7O;g=PdP3F-Zgw5Ll&9Kn@2$Z~U`VDWiGF+V`yuN*G0L%gwXq-Fx9>k3%?%o!Rg0KrNhx5`6}zcLQg6L=x|Zr-QwDx8Y;RZ}`K|e>|9MU)XEImP6$)Y1@V8S4ot>{i=O07wzTr?SkI^rLXA=dbhY#=WuDQD%B`CWZav+BTmMbKihpu%8;=potN3~wj*6){5oXzdMHFw(|&8Yj^%Q@q}WUtAlzLBu<kIv_;O?v~`csRN?GDXdPGNscVUH-ez3~itpg^;y0p2`E(t1EGt8H&W@vBRh}7OT`c%Gf^*hi9AZcCFkgZ>Ll*yLC&wtSuhW7-24O7_0g8^5VBr(X#J(C{<M^vm=?4MpxlgapBfVP9>&GMq#ujtSn^WZ6~pxbayKzajSF^x4&Q#1yh4@);Y-58aG(zGa4*^tNGh*iTE0nL*xLsZjeTbUi3fyC3>-#<&EfFGD`<=@Vr<|2KjgEZYeQCuQ4dr0V}edBkRGYRrH$U_=HxpQ|!oRc+7IRuBcR#VLpmFySMY34joaq3webBns2iNu%itFTcPR4F_o5CYs&3-IT($J?gT;!s>>2nQ;;*7Y^)xuYlPKh)inW%HRu;(&Y5d~rbnTTWcBT!c%@aXn)gR($3T%RieAIxv+-$nP!bkMBgAwZmeuVAq298zWx4Ich9Z@ix+1}7ytt!~{E-Huz?;ZAoyP6fHqf*pXLU!DzKqy(6cM_N$c)5{89RBM4NT3nKF`~&4vBHw_6EGh-iR=jYjVKQMC`)|>`sdZ@M<k7j0ttu;SI3p-kRLvZJ5`}^coTm4b`zgt_?BJV3|t(WxX}*E?A`aTU*MtUeDEr!nt093ZE33&0p8y$R*-}K`m<I7OR7|T^fF|=JI}_H7s&zPhgcwl`Zd4ThB5JuvI}diwZSTqG$OEGLcQ{@>;sn)=}?7=Qd>9c)@f(L^ev|4T!79uO=EhBCk3*#$o0%MF=o90FeiLA$5e79|V`%FS9`})lkT)Dl0}nY8Vah<Q4@#WFKvQdE^U6P@(1OA4Z-~gr(@gDVbp?BRrB=OtQU?{`R+sUz@H+b{LV8Q#P6P>mv}MM$3k1;xS+xv+8ZNcFA7CilZE|Naae3xu<0B0S3V|kqxm7yVX1={;yVku2%+`uw20ZP<z#oW$G+V21pB5Lxl}9Xo})B$7>Wl2@kM9QRX=+TQdSKU_(zulz{`{KuF8#-po=q5!2rpfwcI7VcE01oM#-Jb}IcKK3lyUW%CojK5sCqpCqL_U0us=_LiHOJ@C#_O25_YxG$e^UarojJRQGa`&VsoMGcIdUa{A8aeK?FdwM(e0_wVPv!dbs$P5rjxwbG}ju@gHoy-{cV9$AvJGd;#s#+gd(3$Qp323m=;g^G&npT7%=bw<r{&Y^#mf9nAH+*bHu9(*PtWP;)lNs!Y^iWV#gj&a+58YJ7mZuS~5Ij1yTu@o^5pWj9>|i#ZA3=INo+Q&^1aoYHFlM+4GBT)e?vfW%r=$*g2g3?W#@S8!j^32D6!vQsK7zhytM;fOYn@|YF;Xv`ae?>Zi*fog$M8GJczKh$0dQ{TJzW~u;XhZ;f3BV{4U2-)XNNiY!sT+igN>4eRje(ecUbn(eq`mMC&msJ!4FV>F|$H{y0ZcG-3iVLb(neqVQv|oWkmpi$U&xx=?hH$t4Z`?mZq3{T6puLZD}K-4UZke8}3mmtRK+3HG(NFqJ&}|un8=h1b**@=_(}!6gv=uxjou9Wg`q4x8`PiXsOStXW|wf?9RnRf1F%QL9|Txc3k@J)@gM#IF>)ifu!Piu<HkQ@j;-!F)cBuzDa(?^pE9J?7^AN3pcEoOGt>07!{!kXRG^ggI0YXoliwRn;TxbNh3Nl{E!ohE)$)>pFJb?L?tb=$P|B}Wm~{#3ny|iWdKic`HYvC?*UVB4`>Zp(PfeK`HOboP+51f$uqQ}eDL5wNs7e|r&wH%`j@6%)P|ZEkhTKYhfg0FVaBDJ;tX%l<^X$)_?2BB-0Z2*ecB6VC3MLL75{??h;<TJ5zRk;yBJV^1RbA25y9Zo2D4OJIx4{y(e-Qha`a}RtJ_=LWG;kk=*uGPi&JMPcT1xG#fC1%lQbBBP(TBeaADB_axWzhOLo!uHLAhTuoD~b>tFvnUXkFNfp~LqQ42<Lw-?w$`(P8t<E!;}FL6L(>F-@dh_$gCE(B|s8>aFA`@HHXyA_#V<B$qO0$W9gy)!2%#89U;&9M;YZ1sJI$smf2!H|K*7zwPbPo0nUQG=^U9x$DD)d?e9xx@Vs{r7t#K8QYb{647y;ht@ER~~((9TObByMBXx6+84W=PCGLSAv<K5p2*QzU^nky?L1hD{hF2O~0a7Sl~#JB<PG`eGe@(m;lA`3NR&@Y_G;-S-dtlib<lNn=zqyAzg2@m=0i(7nm$)fF3YoOni5{MOz(s#~O*Ie2wV-4i2Sju35U%TXV&Bsyg9?3M%bIhc``CH-f;;h#WR_n&XD>Gh#2Sc58Qg-Enm*#^pu(C?D4jQ-qzhhvf$vDH+xd4X7hSH>^3V&5B`p0hmfhwcA}as>)7mg=hu^D}g47wP=c)naci^;?RtJVh@7e!XCzsH#-z1ue)s+g_x&av7Gdec{{$HjF+Jx#$oQwiGc`5+!RM&6$mjvbe;WOrE3WDrcO@uTgO!75nRAAULxjwwI1UZK^sjZ-ZpZhSND&K+xMUq{rHN^A!qrxh@NJ27tx5`%~FsFis*-AJjQ^>e}+$E__9dG(T_~{|9}ojA2wXUN9hnbsoy`_(fN4(sKn3N0C+eZt15I;aD4dc+4G~*<9E*wj;n49F>*B2GK>3nhIwJ#68&`nm^p^Ui2*6=cRm1Ck|uY4zjg;b;Q%OX@HxgMy;J*m$5x~xxR|a*vk8i1wg+I^Cq5D(z#^F<^WEx1k0ZSLtDCPo;zHcD2+Stg{3i;ejh9SIx>__zPD6K3i{99$77(AJc*8lgYyJ6b+?*+&VNrx`h+m$(K8*I&_PO(LkX=Spd7rDnBCb6GL>NTx&ckAwOsrC43|C)^7<<qqei6dpqlfpfwg=K}_c9qbuV#tYIF`*O)5Y8>Jy~4TA`F1EUz?E6a}8y1qkVXy<}p~C`8v7g*EkWzdzu&efG*%Ee-Yl)Vp6p5hVvYA>3f0RddOM;fKoi%14LLagRd+M<Un)8nw3c4oH%~~4&;iIqji=%wfmed?Qw}YyNi1L!R(>2pF}F6#l>3H#VmXEY2B4UsC{r2=*OD1okitXLUBZJMloe(pxx^<jni7%a!b#=)g)JnMde_FKf))b7FbB{b4_ADs4a$~!|ybGJ^HsHXQU^8G#JG_{?m{{?a3bv(Usn+Q8b9Y^_a?iwp8e%DJvKtzq-YxfqTDNuJ>I}OZM4RPL_9v7Fk6{@NB|N1cDeyK(s|Xt)M1-WLzx#$WGDJt{_9>ODW}E!YKeuGD6<8Mz)IXH=@f@u73S1C7lUucJb4i$BjKyT23*qD#nIJ5<zw7rCFb)&}ZokSj_?1Ru%UAmMbisc@;c8P^n^cgi~X2zV=KScbV48aWACSW_4Hatt&X!6})StqhhYHn}~Te&=9Xvw?8799Ij~T6vbp~Z1S{Mfh?H>84G8~0Wk(?Iz1TYfS%HY>TEz`!Tm?weqXfbEIMsbF=U}Ryc5H))K%_fIM3Wy?B?5V11~R~Yk`Imw5=5;`z$vg?kz%H^N`@E#lTJ`Md2kdNiqAMZzVQVXE>eGbU<6;0~B$o4ZLb8wrpR3w(lo~t<V9hUyG`861j7(%DTUpRZAAmGNXuxTnBakDoVb+oy}f2i%F?MxkD;A5d)1wX$?O+!}iFIdRaN-&z4!0IhXaCy11z+l@iBx7q#uuu6nZ;(nC2_TxH}Mbv#Ai8g*PPRj`V<_k|C^d{<1QPI7jt68quHcg=cKy(FUDz84V9DdEr8ch>5Db{)>VRpwhlxw;;genRbjFS0`VVk66M+epW21O^Dxu}H?pC`KCh3pB(AccM|Pg>S6Tk2k6no=*IyVR}L-W84mHYQ3z;0)TcNq~%m5y!L1wInX=`D)i7!oA+#_?0vW1MT8MWQO7uFheE#Nj%lpSC_ue4=+??Rh_CBFApb#S4??#Ep&qb0eT^RY09W)NpxFPa4g@kaxb1t_y_Qb?k*(XVQr?ThsREd6Je2CuJh-0BX2}vn2l`uOUJ{#q3+X{u+qrmF)Rm?@A2M;-C<bfkt=3D5uo}9WBZa4~nM%3z)ORj1*V^3PVc`?P(6!Ne8`lT!lhKvXOE;wlJrLS|CG@fl=K*&MhF}YU@Ad*swTytwxxA`)G0QKG5kOt>Cnb`BmyA;YD;E_o@a9RL6!SW|QO)t!DL|R0gHsU*({iT*UM5A4D#1b85i{{4`v274$(nH^(%ti=59|KU&cXrnfp~m-hDo7YpVB4ZP>Bc?-cnSt>h>cjZs0C-Za^+q@cdZCqNkT6JsS+azV5IMxvrng=V)IgMHpm)L{b7<szG5~s_7rw-+Gc5UB;zC&pJYe=uJa|i#>osoX|pqBSK$lnuTQy5jre$9;fvCU@?~q+?o8W_*JuucGLljZ=O%yS9vnQ_a;<tqWNxfX=j6lZ@;cx_r|W9O{P^<;d7H>r6B;j=J;$}RTDn@H7Qatj5Mb4@`V*DjsWN9=VREDeDw@_@_WFWUFlb<^lMcmyAJf-xb>b)=`LiSCggEc+or%&I%WnHAc3;hY1^-z^~M0)m=8TU$2ewK4)D(Mf~UKNv$1^-j~zBnZq3PPxR3VjI25D~J9BRh#(AG8^nfCD*WM0?HQz!aU_7;csPVEG7q*_x>zG?@BdYzEsBTy_f~Zkj!<?xMvVm?kRD!7qA%kvTy&Bk?+DhG0P`PDO_<X#i4^=w?3pLNMl(`*LRhPC;Jaa@-l^OjlQg(R?goB|8DmVcj^BFgO+RtWv3`GFQQ11xZ>F{E1AC1PjXhhaAy)Uz~vz)T3?pwXYE-Yp#x=7}1eAY@Q=w3YVtp5W=;V^=;b^<ebXPA!%cyOn4ICSsqc}+jfulLJvedjE{ZgR0^KAjhL6vFGOa;)LB3Ur9YWR)=f<-Q);<2%D~dVQyNXOd4+yAPBV`X#Ui<((M8*QOeq*#}iQHUL%hf|~E$IfIq`DS(Rq1*GC^zAW!ak&Y!g{>o)Nj0hO94U%c!${FT5rvkQ>4LzOCN8)JQU(W&~0H2_sg6pHvZxeKEHMAO&G_8v9s*4?mEFUl~AMRj{ba1C}=PJ2O3;3JQvh(C3gI|4+02Uw*-udWmSU!%*C!s(3)P%7$?`&X024_;|nz4X@{iY3Lbli`p!okcBMmZ4HihTe_KOOsA+`yh$KenKix35t}jAn!H(+OoC2r<QJLgxtJ>4@q^2k<z*^RXenUyA(gy2N3gPYWth%xA>viU{pc<S9pZ5G9Yrce^lWV1mN0=|^?pc|L`b7=OVl_A$U*?;EW3oxr-hv*GCXk!gI~QZ@z1LI&&#%oS-LR#Z6dnN|mqRSv||Va5k4t~`6VBrQMh1hS!METAyb*ZJ4gGI!4<i5HXAp0{`lN!kwr#KwkQfVNh}cd_LvO31BPQN%lhtTOh<ozoLfNG@;+A1Y7Ce(;2ZT4;=glHZ3KqXVkcXx#Wi3=n_Hk>GFD<=V$`$xy<s5)RQ@N|y6%;`+&Ku+k<DmkSnTGoVi)YdHKI6SM$hE^rQ`dYb3sG;uT%a^ZaV^ifSu2$5MKqVswF8BVec&hK!E*&7}CNCBu6k_<}eNmwdL$7%>7S%(cFzh0vcz_oDm#I<-3*60I3;N~p|LWJTT#2O*h!jvd(fsnBd)z1||oDV}HBGx#u&ufy=1hPO-!=svHH9Wd&79iCb`Lhxb)ki=C(TSc#tB6P=I)F6EKNhoU6i5U|*%ZS)qoYJL$!~7pl$nAwK$^5@q=G)HtX(U~F&5&r;!$H&UvFpi%Artla7svGR-Y2K5ZqI_mJPaf^||J#a6_qF48^V1-1c1Xa-mm(_wvX1%5!VCWBCKZco}(mG9F8_K0+i<ld|gz(MtuiieO&x<+#uUsVW#o1SSwwOWE0C4x@CNu4yUQs<qD6K&dF~i0UWaX;K$svMFwFhmc3h5`~GCtB*=Haq(KxsI2eehGGiY$yYF(cR1OQxspVxp{=fKw25qADF0$W5#eLv9(Ty~_7w5|zDb0^Tg4c(k`d9}R<)9TBVr$y@~ft1sDy_IHGVa50WOBVo#Iq87o+-I!p_jt#KB@?+TVoxAc-)FW&<oLu(e{(7gLJywrb&uvymd8c}v%T;Vs_L*QLpFP4wXmumPfLR1hGa7REMkK^0RoAf`=`y+l=`kn^yhU9Ypr5xGK`Ik8|JVqfoK<j`&NHqNb_T$`0CV^X)>aPw<PSi9SC2$(SgfmJ95MUz*)4lgd~00FG5T&62g7G9Sy2m}Iu%taY0c?F2Tq5`)iWs++yLn!oO-3G!-|CFUy(|k6MUQLEMX0n-B(F=Jb{CbVeAh-xDU30R1X*jR?7<pwSEC$oe`j|Gl3>M0%>%+ozVDC~5NpDm0ZQ#_r%!&-81D`3?esAOBWQZ(RP|$$Sr^)y#Sr(`HG@S^(#aOqMtzRXxiP1EkBHxP!Z5sp!;juRbo(7wH4ZP|9_kaCw|4h8;zx|*8cdZQQ38iQ@Y#E$yrQmV<@q7r5@D#0UlpfgrM443vzE)hWXtjKQX&xoZ2F7pB;DjM!0S65tD0-PDa}4r8vrw3UU1!Pi>3p(EjJljQv825S@y%g+UR4*1G{@<AIvLn?`+%pln(gyw9NBAhv0m*FkK3)hqSvBUu;WEK2E118w-ktgK)t!s1gc|+^D1uC-ZfYODOK!1gJHyS7Akk?YH&Osv6z=?F;pzDf-My5CK#HRn5U<b+qQe689|9SRv<Xj$1TvP=}+aDzq|>a;#f?zx@~me0g<3Bp)MLFTp`GoT}C^pzYi!3Mj4?D1j=yKAQ=8fSURlQ4+udh^@~~v4hN)K2MWdUv|&(>pXS$<H*P8bLQ^u|Me{7bc4z|vU&VTIBvF^=v=I_J2wEZk@l^QG2raRNq!k;)1tf73D=Y;RBVr{46eEV|HzOw2IPz2w3JjhkBx6w7)8Q=DCyeplSP<ql(QL9}E>W{Jm?haHIZp%HF#zx;pI5FXRhw9*36wUcl6w$~o_P4OwuywKZZ<2_RH9?C>|u!xM<5V;bt=It^^L%y{ZVTfElb_S8hC_Kec;V}EW(GMf!nD(Zn&=C@`yLGvj|U*sl*zmC4&lAKTMV@V*6S^nqw+&kyS!PEKpK1q1mKAUJO#v<%($(n29BdJb3jGKnzwXIaY*D7q}tta@es#K-HEHG!^@>7=@Z)wBN6bkZgj|elvs@4`j$dqp+rvtiV7Z0tQp8_{-@j&)unbFIT(%fF=sHN-L~@aiL|OffugN$EysT@Zz9}Ma^ZzRbv6dIi00?2fmrdupP<6;^yWDqfeGMQ8s9xueGbPNUM6A4J^SUh1%)3)gPt(PwBuo+b@-%B>V`ueRR>|t7vsA6~5qi?(o7e<b75cgni2whM+IP!Z6&Mz%Uf!4lNAEyDkjF(f4nSXidu&i-N&dR#dNI+7+0luzE3<oq`f;fZ@egZbjpduTOR$gY$GXlBgJ6t_AP}qGb~$X?fM<-Y8Vb+a{c3G0&S6-_n~l{B#N!9cJgyu~RM->Ixr3#YLXaM<rJq{4r3O!u2#Ua2@)rhP!}8PGyk*40#~CwOuA5P*o6Hc@S0+c5BFd<iVVI<K?5{0<)CTJ?N>J*w}J}3;1c;H1#6+lyW2)%zSZtd0yv>4mJRHY~KPF;#TRszkj~^IcJdXh_q*T8AK6o-%;bWntqMJ`0cmKvKf;;-B;;e!rAYzp%v*Nsfd?r(==K>YE-4(bdv+V9iq*5ea0?PN0>*i(`~i=oPhPsO-i^2UAY@=qOE2?d#up1p;BO=31#hdM5ldp7}a9R-M39S;<0rT3`L<tYtChPT62M;by5faW8+G$6+jgsM&YHoCSHUq=ADPd<#|LGWc#(vb}ixy2l%~Hi!QVD3QZepZJ3Bn`2UU>4d>27a%~qD8G7<`-=aIwueAu1g6zwTyqyP~MrUWc(Qb9SaZO|q*{}Vn-98&8+ww(Ibg0wXs@=1iya(NVbSFe5FfV(-gyI0`%6UFp*0Xtff#C$k6!S~*pLnRLm&^!K`XGrE9k@ek?B<5aHNb53MGNGWQA2DW=2r+#`-TJ>SrjN@$W|n0L;z2-;>W^bot?VC8MEt$tPWj})VZkh=NjGY*dNZ5*&v;SzVs8o*p$CmeG$$!C@|<pb%vC^cg~i;5HvSaG6*aX>ZxSP0-usue-s?tY+20L9-D2>{0QR(mX0EyohK7>4BrO_ftvYHS1m_qxzOyj%sIYA^t2y<`EewOb9hxPLGYPZG_j<W!G^2aKL7mA497+1kGcNyi!*e+LF=&!Loh!6agmF@ml-%PG>#iC9Fai2%+4qE-#<5eFdwpyjp+ACY>^&eE&3d<N(d_e;ekERCf}e-HYB%K<d0=`tF&LLwF>(WT%8!hQ4}?7=4c+P$eq0P#ZND2?Z%}c;#||a{w#&cVlCBcgX~gYzG%Zb8P|>5AhSF=fM`o$&bxgn7bL=yAIrTW-IOqNq!YasJKdRQb51yAkVL4&fTb54Jy6Nh>D+mdPK2Kvo5DaNwoR*7)B~pK?m4maihfzg@Y^h#;@&l(ny&@yvL4+Af<_t6$I2jjVvgpc#l;z&-T{W%q>RwW@1H4}Tqy3F4;UzVQmcxlC(4m7<B<<DT)J4Cg$m0)Im>3kG1~|sZp1LNdH1IFY-Kg<ho#?`aFnSFFIF0@A?vpE3`^p_PDz|qD_ohy0C>T`2dR5q=xkC>W@7qSah2d+g-^}1`K0C*cA~xikN+c3MC?w-r|B7BZJq|&4}@d#bNgJ{?qum@3*(l)o8{Bw938hObuVnt_XQk~CpkLZ)_*4t&z>CL>3}=ah_XR1lJw|vY&R15XN=Nhn8z2N{6_wYg^|2sfsip2jcCQrV8MsHcaEC{J_kYyiCvvcr%?A`1fpi0k?F_5;(}|S_{)<CIn-MZb=?F)24QhR`OsR5ebuGAlQ_vXs%DtIj99IJLOV()2uoPTj*=o$JgU45sh{O@<kpgLBp7H>{QEfI=~%|m1_Bz`x@j-gpV|B8*Hg@0DZ3=JAT)nPgnAt~%&~{#rL*&)<X_U|SKI7cY{;D1kU87!BY4Gy%){wP=E8O#%YK-D^n-@Y`?oaSpL^E(YE|@09rHfS4a<CJ)3}p>O;E3;gk{rM#7^Z<u@x&r0(@n}XMJ1?Hrw3V<gl<;>FG%x|H)Z~zHBcSt|Tx^r;2c4yv(B%tzj(D^&%V~$iDH+X!i!A5#oekGw{cbBmyrnW>7jQptofI8Iv=;^A;GM{sjdWa#UJxFGp*%sr>iJBU<S`fzF>>e*Cg+uMjm)&GAdK7gwa~_~CZlNQ-%f_6~znu6`QsNT3*XMYL&l116-nT_2zZ3<Y@BKDx98+jojk+t`rV@GzSfPf4tUkMaRps)srPjN$j#6ZnhpvG^&FBsv1kJ)uE!U@Q$?Jm01P)<#)vIOh3e=2<Nbj}`;AkQZ5ut%Zm-!7uZ1x*7x(ZE^zjJ!ki<u8pPadimvObv1P#U{$?3pRX}w!kt|aR>10txJ(=amux&<T@NR9Q8clz)7@k?S!ar76IchXeGc9Ytg=6aLd|5H&gMbu(=+B&*8?DpM8Ap8mvo{Li_~-SIHq_dG7#Yf+0?(jz#Y(SZN)~~a%Gr-q1#=1>!Axqq~%69o2_n0eQb2f;ryvjs4>1rI^&^yROy{`2nl2F=#d#OJ(+?NM(KXq?hDx6`}ghsx|yX+=xj95&&T<Ua%S5$v8%5D4d05|WiqQb<pRcq7}pGM3h|lZoF{$E^VOsbQ*q7G^^l1T5rbF|1qTC$Pl*WWM*{>|3;wttJ5?XM9}TS@5fVKE^yswA=dFX-fBk<HUb&8qQE^5;ing~s6!mA>JVqT(U6tC}E<vP5pm?2sifdjx5+Z3aQ#N<u{5ORH-#JH|r!g;;b7SKXt&5rDc|HJHA)=Y!4O5+-DT;`3+0rJEWFjL}|5(g3Vw_QK&+p~&iKm!x*ukTL$CedZF)M_D)As@lo{R=QTWwQ)Ew}(Y8U>*_Po}5PqffCJ;gCtSUJd+g>jE5N&9_IQ4={%~xiq(;gO4M&JI9I4KN${Y0=8#{$8gBef?7Exh_MCI_{xS`!qi5*GuknBmp%*t6N0R}M3qgoO6EiMTmh=IqeYV?Q>Eji<r5tU_?N(!)AYKZrX-LULXP3BadvI^kNDnZ!f6K~UB_`5jODs8mgO*R)`5Y1^-UayE%Eu7!!zD=6vb!nR>6#bRU%YKK44`$LbGsr077xpQd}@y-cYEUoZRKQ%5d{?WMBkjx@ysL`L&?XkY$(tmc+g_QDs8=5#d-DTA94xvp<}XotpoCB-lSvy2~wHt9jih3EuQGBdUI7RS>gk>8G;G@*s*;QZ2~iKtFzb<;E|XX+DdKS)AxhU`*h9YDCBT0X1M*KiYg2sX%!)y*<cgeXA~RjbfBc!!yQg9Y!i5<%-MnGuy>bzmu#)9oQV_#1`#b6JOVDhmZBC*ke>^yRA4Mxod%TegR0@`d`+rIoe5nWBDUb4R1o>Oz4(>mYrww!pv+dfZT;+Hfow(Fh0PZe?++sC9CT|g(ey6Tt}VNs==7!c-i-ttHl?w(gL!}YI9Aqu656#vqBZOfI#IPsSUR1Eg)DTjJ6vk)f#t3Q%GS-Y7+t8WZET->bOkVzy5bl|0*_uND7Ou)I9Bd=j6oWf#}xxIoP@haE&&~86bI!GEcJcyJSXd^26=gu<l-A?N4WUAAO!Fc9IF2?~gTku?ofxlwmeba0XX{u}dmAUJXTsYlkmQQETdX6ANcz({q+L4sgMTKf85JAA03N?^Tr&lgA#4Ya_F}zvbDaUW@+57G1UI-~Rc3r$)&|oY(Rxs%1~-+0-+)#vD)?ol>Z&&H5*^WKxXjvPe1^sq+R-s`2t<1Y70FWN?^Z^0{+uk*)TV{2?|K=CXEUEX)yzGIFFR(Xln5j7_u7u{Pk8iKDo0uK`Pdtiva7e)#dp56@3uKR<c$?8(U!SOh>S<+$i(#kh=Oqa>+`&`sz|sda~%;U$9Ana9>+3retS7qS!M`OI=$k&T??gQebr*6R>%QHP>XW7zpxj``S&)z-{ds##DmvuC<;Yyfhsn8!*#JQqt!tT5GI*NKgm!5aRUym*ZM$cnK75%gG~kIaS)lG!J8RH*&izx==Kp8GHVT(eAR9j?mi=p-McYeg~1I=hp~@FfIkRjel}R1&NNTd*(HKgGI&Cro_`#uoW^3}Y<A_o~Qhc0Q2Rx!as5YJQ#(nUqccE>Fy+q8E$gYzC?-65*8Ihn3tq2^vzCH+`1Ea>DB;gc>s9c5cv$xl;UJs^CJV&TfB=INxgqf>ey^zL5~OBr-+=PBt`6ZFE}Qb>fBN;(`WkU3c+n0%Ro{?AvawqGQYFvspf~wd;77oiB<XM2Y?1ai8=gO)BQ_;TgPX@W6^*;6AUxqb-bD992*P{VWOFQmt3$ku+$3u^5k!=Zis>%koZSZaEfr?wmmI)*$yM0M&>`s8Qovxv<{8Ja{ApP#4<$JC-d${Y(UKICB*`v-BdrOzU@qLg!B7PKw=fsuSds>;ggbVT?2UoiFC*2S@9Hwx<12ouI`|iU4E2_T7nX;k?=ivnJ86a3ODN-6rhG^(%_yP&GS(zobz>Lq!26{NMhT8q1ShJ)Y1Geo970#nVNxbZ)?PpnKacD75MuR_;902=()KrOip>%VNpj6s3ZlJb0ZJqm%rHcR!++l10OUbgz_xRnonc<c({iVU6gxqtjTd;txO!&TW}*rPJyx)m12yXB;h5xKwS<gvLJer2k2rdF)l8Yr*=R`Lz&sxR&GZ7@9AfDVwJ2xg&a0EFA~@wHT9x093Lj2r7KG;}_&EjFDnLO#ON}l~#fW8PF)IfNYK+a2g>x>jUfobcla$5{WhZDQhOBvuw9h$8J0IZZ+UZeF{Xt#GV)tF=XH3Kpirvk&1AWZC#sKT6ltWA`6D>(yXQh)plF|+=w=J+U>yRBeElQ?l?V4V8vem6{;6$IshS7HiMH#W)|W-&iyl-@=1PGN4?XdM|S3`8Cq?H({~aa(qLs5i*db({#O7?5IWm&BkFdyc6Phn?al*~Za2F-J6pRC9(3+ojVLDoQL`O`?7h`}u=QZ)e)oa8D*9}7X=Zh3oHwFTW{82~96fQM-*t2^s*kd$3Gd=P8_IN5O0;Pp_=cTsbZT9GN3~*<j$vELKmf8(_~z9zmzxG6>gnvZvwEks+laPoCn(iT5n`*fa+fP_1uJ{G-dG!nZDI_yE=;9vs4|@wRN3h^qE5SO)TmCtH4SF;n$_E_2het>wYBSl65W+K$@CzBU)^e;PG;BC$;2AHm3g?P;mlqLc4rsCKJZ{w^kkc=?6!kFsm{kW4JY^_lpu0plp0hxTNV~>ME6_U!TGkGeD>u&!2p)sT@b840OEI`dL!D!xrG0^A3snB$)2LF_SH^oWXYSh&d2##0xS56dQah%?6uMCVDLNm2Y2{3LfCfH)BR7flGD_d>V1hLJQ5<VPu`MfJ7o-O+plgp!CSREYt(k!->v#xzqsq>Zk69G9h<Ofb9W_7&W^DL+*&d)ze7Ht)@ExbxFQ^+lmOU80K4k|Ks6bR_7oOGT6q26#1$1+APEnq|G&FyZ*JQ-;{W?oK<tb|RwOMy$ED(UWXZMFSg}WxqsEVNAQFsFkpK%oR%DO9dw2I9xF-Noq|<38BXfYmJ@)qQ_V)2xgAX$FcK93ow^M%T2nE-6RDKp%anO#V6Zj87@Ht4tNlJpTA-guqqS+{<+80<QE}7o~``obttN5B>di;uLG!d8W76=zYXa12-wJ1(HC_d8<G0&Fv{#ttvv-w$bWT{9;r+LS-H}B|08@l4sXgH5x<=osrma`?(nQ`ucW1nMURU{<~QD^@(die)BC=ZKh-ey)0mD5n5Oq49T!mj%z%u@x}`QFEWeY*P8>j$5=@BQ9oR@*F|x0Mo~a`tLu#9Oi!WSz2~_wM12w5I=9efM|z0flA+r*TG(yeN1V8)!@t`7BN*?+-n>zv%9zL%l>_;D$0y)&Tcng`tS5ceT{VX<~xgVC;gOqCM)k^DZWu=|Achl#`V!@r41Ou>xUqpfmuo2)+7MOt|8dkNwdszu29M_!*uvo0I`u**=7Y*2Yx{a*yV);!(-#S}&ikgYIWQT4O_4+PM8+32<;Mebq*X{wMxSh6`u<LZv*85X;MvYTJmSbyH^z6(G~N=oM*CWK&e<&XY>IQv&UOh_V!M$LDdLlbuk+;qds>fLBX9X>fH8Tn&32-$!sc7b#k9g2n9e_c#gQ>ba$x+3d(Hy3mqp$-(kElgV1jZ)gW+mLPdE)+`SeR}vAsG^rj+(v6-)6<opI0XMTPf+-NG7F$Z#0V`k)i}gs1L+O&Ie7iM;vE|+XwT9zx0(avb^ceP7e>hSLZltK>?onChHl-OS6_7PqTS)`?tT`F{pJ2{28f3)TcUgkmf3V}Fh%&RsQ4R<1+p|2%kb@mFEc>YE+qnw!*YRW$CAe1f>%TOAhG)n4Dv7R)b`(7ij4z9$Tpbiuk6WLl4%365qLTr680>0g&mCn;2iqMzw2-%lBjZ1X7PEZvap!Y?%oJzGWD{0B2C--Ea((iGP#xmV{bkQJk5e@ojr=7Mv*!VJ|D1jqT`*{Ggcp_`HCn;yI<)z#VJ&5?DL#Gj8O?h?WpiCF6`cpgK25r9Wp{>M7bMj=3a|VFQIb^JcFE(2O6o<0ny>E67GQVg)ruW~R14j-@sdUAy89Z?f-BTmZ5t~d(BCctIL!yXi;@wByj&=*46&`!cCIg`(Q)L<QBPV;PiTguP%}Zz=ui`A{Ey-2;N{=<-oH5+z1ut9I~p1vn&G<IS}@R!oo_i7H%1X=F%?pcn?_3Apmp6cUa6@;%MHuSNJ<e2@@4fDR!pELTXp3HPn$f|iN-CW+h$MFLdbcMu2#()b(joqOxiq5F2k9qi5=p!jMd#xcx}*DMnUS^+wAis`lApZAG7xcH^JHlQBIVBPrt>Jfvl>FJsgz7yOF8d+&*RAeS@}*7NQdfN2-=tcNZ1ugVO)0%X=|WJB0g(ujeH<TB}evu2rtW68wNz9J+AAT#qzjYfecOE=n_UJx3=cden$;H;QzAkd7}{f{K&yOvUVnP47jmy%1g8E_zUukS;3hg}gSmhKRpJeb2He3$m|BzOovJFBH6GQfQ03&|A7BW4P1Ry3vVoL&xB6#}WR2!3KZf82p79I3ap|QJFldEJZv}4%Zon@3p^s%<K-)7TAONEd_Z9_q4kl-i>8O(;1)o+QVWZIaVWK;Vi69c2d^YgQ6y?OoJ@uY7IIt4Fx%c4ip$PpJ7-Nyi{fb#mz8I5F%|6X%H}aIWcQgs!Np_cpOweqN1sZ%FU$XwlW4e_b9py6zxj+8Qt`r_uKyP5Ob>{jMZ$u{FL2_=<AquT{VT>VZ`LLd#?N*)X`BWvE0;kX~Yu6U0*;V9ffhSG|IF9Il_-Syb?M6YAba(JV-9gYy_VS=<l-Pv5m$<>UxbeC+LBU^6&_iTBR|+s}xdtpzduP@yqunO6)fR^Krm|9MyL<V{;<?RA7?anA?HAoP~>ozUbY0IyoDb*nXpX2y>Xj`fP`P;j4gskOv$lsfQbI)oH6V;68Dc0;`<5HtrpY@_L<)BN(QYAHj$LT771^hG3nWYLnGxr(TlIPrbj(V%gY7Wod$A^3?DuF2?8DrmN*fX`%tIOVgrxDXntBt93uQ&E=@+9mq)d(tt335?wR_{kxEbGYe|pE#f#$%8F<&Q+A!C=?u@@w#?PF&C+-UAmD{rG{Nw!{k?-=J{Nht5K>s+_=vn-9oaK2`Bbf8iNn93`cAVWsR!JgU29nSFKee!6b8C_uH*$vYanrK8mSeyp0A=|L#JnEc?#xwujWksD-%DJd*+v63Nv=(_)=^<6<)O-(cR)3kxH%6T~ryRk<V(^T61=$s|w1S<gA&4wGLmVbZaEl!s229#zxk$I@Qz`e7L*TehZFScIF&5gM>lxR3#+CFlrxX;z1puZfiCf<?-x-fFtCWrUFT_b0U3X*F}=6IBTd?!IIOAN$Ok1BjXOzAjuH5t6vyFKCDmCBb%&04P3*Oc_A7M*wnUeIUe8k#Pau1<X>vkRXrt8gFHbk$^b;!huE`*T(!(F7ID(7_h_{qF6f@Or9WAouc*}(_)4_cvA1RUs%BMzSitnvT(gsF*!%Mr4I>1gXk~Z+ugVks$6l_k?z@P|U0kWhdD)n^49yGs4w)>*yMOQvs{mT`uR}CM_RtS^S3Fyw^o}FyKYX(5(DN(T1Zg5H8<=J(B?&N_AY0hG!{Dz_?_)<>J1ewRq>H6ny5E2FX!(|y6Zq1N^`Nx}E6^}z6s-8pzJ(oJ!Xd;nVg~z{m~I(kHVb6ZUqM<XfLiVq82koO?&~y*zoK#v9?!xgAPZ6Op`&ZdE(?}F@Vfc!MB1pHk(J84lT;Y8lsZ&n7P%cuv8yy?{fMS4hp?p?!XEFq#VnCLG+bb0SEtbyTcKKRcBV^meqE8AU+c;F)j`gZW(<+cCYov>w8{7rWyv9j;KQV7Lk&UCF4hHNqhY@rJbjEJ)06)d(xV=d`iT>Ol!piO!+CA1Abl0pBz5%59{TwMRUXs7%D!AlipueNu53Endwa7(|Eqmj<Mjji`#hXYZ^7O5jHx_%hU*(R6B%-#EcK0(*S$+oU-X`=nYih6+DvR)#T(#HSe<Ziop7-7z418BCJ3+++znnbBzC4s)KaQ55boDeIB6uXAuKpI(y=cq#W$sLw+N>cxP=%OVGb^%DwpNf?0d`d?lqIEG=N6O)-7ywmZUtJbd(e<dSs`CeeQISME`J@P*>JZXjcIcP3T#T0&O)9rV`H`n*6N91&OFsxh3)xq8q0wc?Ft{nw0iJ%vY|w+akv+@t@_~IWne->;N5qS(!C}{irCZq!o~PxBR8m%meawMR_%&shSXMS5xEK=}2qYaRqI<KU=9+E8H*%tDzE(r^ZPS=g|+-bOyXMT0|h^=RY_MS>8sF&iN=L|NUoAcbEL`3%_qXdt@Gi%L1@$(A=Oh1B0^Y{Ri$)adGYBg!MB52an;6K67)!8q6tXCfp5jxg(u!lYMthHX~H*u+3_{&Y+FrC|%CJJDRhvBUkoXhELu~aZ-@=6-4{qK8`*(4QDf<?CJ)?lQ+RzOksS4@aDlVoJPep2wJZwcOyodXtI_dDP2|>7WC5Q$tvvnH5e)lbN~w&e^qtqay&-_l4+rDNgy5JVEr_5At-E?Ol1-c#)(b!tdvWG`B_v7?0U^^nO!fly4Zfj@M#r@FS}-k6t4^g-D4i~2}$88MjQ22g}_RpZleh{zHxzJ;Ml%fwjv{d!<}J${il={DWvv%s$3zJuue_x_I76YWdc^6iR0@BW%a;JEWb=2w7l~xv~A_3U;pI05e>eFWP$?}>E1RnG&7gntvPy4gXXqa)vViqrA))_hK6GEKQrutsJEHThpO*WQeBc#Mj}byZMe{o0q0?M9dH!1y8#122smz9&=$s_C&3F6&(RuGq~mnfQI2W`f%am3fN5og?$fz^zxv4>k|tBH$#D{gJaSf7(1cuh+d^045$qBR1m(?IMoLB(44now=yX}ul67+TWuu+0R;I?wS1-)h%7`)7z`&W)R+5^T!;!1B9)qzOiLv!I8;3)7_F$I4;Eb_Yl4ACXBw=AyZ4e}qNr=P3n+ayu?DSD6vIu$O3PhDN6%l8T9?qvNbk;GS!$IG2CFq#WIh)wEJP%s*FHTP}YuPC{rrZtQfihxw%M-vspHf@Ri`~sI5$`-&a}5r{aMrLGVB6n`wT$+mOUxslX!ifacO*8FQqA5T>@Wo?&E_c=UuoX?eq;VC!utw-j;_yA)E^Jep_1`s0kgMXWV7uL!9DilH}PY59#4zy4|M<$7t!@3y-KP*R*Mj2BY7NY+G}|C3$gff3nN9m>KEzz#X=@H85l`<sCK00;V<vrpU?u9k4|3x^JMS%<(_r-#SfvSF$@)mg5N|4TpRw3Mg{60jLel;MK>ujZ$F^OK{O37XGPmM3!;9Gbfj99$Z)k7afK3JZW#_&?&@{pt~$GRqi8mXlXNI71|fHH9_M{@CSgd-sI=<xMm-?S1K$g_>T{5&XAwNx<7f#3`%$;7zjQkJK&y5?TnxN#*msL8#c`ab*$kH0aGXULIpccD$^$DNT*J;2k2&hVn|L1M%JIDDN;E6|?F-a>!)LxX>^q7#Jxs>w9M%GVKX5+n-f;sW3>?o`Ss%vC!25=MH;D=$&0+Fy+Wl~cq=49g?*;n`B;E-V?2i~w^T2+@X(f^C2g>hmi7&>(&+bS8wZxBt8zN&PB`K4FBqFvhwjvY^5zMjXaWB;O3buveS+JkyBEZ-)@U{XwtABy5^9W;v&#>N6%&~cO5kbppaTU6a3Gqa*Q#_>#c~SB4nCu`39jDRRt2ZLFp{>}zoQ8K3sB8C5ZFKZ%fNmZj0Dkx)so8Bq!L-(yVE4{V2mk(fFCS;|qWB4ZVe~QndtS_EKi&B+7rk3d')).decode('utf8')


def get_studio_html(mode: str = "page", initial_context: dict[str, Any] | None = None) -> str:
    """Return the complete 100% offline self-contained Studio HTML5/WebGL2 application.

    Args:
        mode: `"page"` for the wide 3-column OrcaSlicer tab, or `"dock"` for the
            compact right-side docked panel beside OrcaSlicer's 3D Plater.
        initial_context: Optional initial state dictionary (`lang`, `theme`,
            `printer`, `builtin_presets`, `user_presets`, `params`, `export_dir`).
    """
    norm_mode = "dock" if str(mode or "").strip().lower() == "dock" else "page"
    ctx: dict[str, Any] = copy.deepcopy(initial_context) if isinstance(initial_context, dict) else {}

    packs = discovered_language_packs()
    norm_lang = resolve_language(ctx.get("lang"), packs)
    ctx["lang"] = norm_lang

    theme_raw = str(ctx.get("theme") or "dark").strip().lower()
    norm_theme = "light" if theme_raw == "light" else "dark"

    fallback_params = copy.deepcopy(DEFAULT_PARAMS) if isinstance(DEFAULT_PARAMS, dict) else None
    fallback_presets = copy.deepcopy(BUILTIN_PRESETS) if isinstance(BUILTIN_PRESETS, list) else []

    boot_payload: dict[str, Any] = {
        "mode": norm_mode,
        "initial_context": ctx,
        "fallback_params": fallback_params,
        "fallback_presets": fallback_presets,
    }

    html = _STUDIO_UI_HTML_TEMPLATE
    html = html.replace("__GEOMETRIC_JS__", GEOMETRIC_JS)
    html = html.replace("__RIBBON_JS__", RIBBON_JS)
    html = html.replace("__VASE_LOCALE_PACKS__", _studio_ui_safe_json(locale_payload(packs)))
    options = "".join('<option value="' + _escape_language_label(code, quote=True) + '">' + _escape_language_label(pack["native_name"]) + '</option>' for code, pack in packs.items())
    html = html.replace("__LANGUAGE_OPTIONS__", options)
    html = html.replace("__INITIAL_DIRECTION__", packs[norm_lang]["direction"])
    html = html.replace("__INITIAL_LANG__", norm_lang)
    html = html.replace("__INITIAL_THEME__", norm_theme)
    html = html.replace("__INITIAL_MODE__", norm_mode)
    html = html.replace("__ORCA_VASE_STUDIO_BOOT_JSON__", _studio_ui_safe_json(boot_payload))
    return html

# ===========================================================================
# MODULE: vase_studio.plugin_main
# ===========================================================================

pass  # [bundled] hoisted __future__ import

from collections.abc import Sequence
import copy
import ctypes
import json
import locale
import math
import os
import re
import sys
import threading
import time
import types
from pathlib import Path
from typing import Any, Callable
pass  # [bundled] resolved intra-package import

# Intra-package imports (stripped cleanly when bundled into single-file PEP 723 script)
if "normalize_params" not in globals():
    pass  # [bundled] resolved intra-package import
    pass  # [bundled] resolved intra-package import
    pass  # [bundled] resolved intra-package import
    pass  # [bundled] resolved intra-package import
    pass  # [bundled] resolved intra-package import
    pass  # [bundled] resolved intra-package import


# ---------------------------------------------------------------------------
# OrcaSlicer `orca` Native Binding Import (with standalone fallback stub)
# ---------------------------------------------------------------------------


def _build_fallback_orca_module() -> types.ModuleType:
    """Create a lightweight stand-in when imported outside OrcaSlicer."""
    mod = types.ModuleType("orca")
    mod._registered_capabilities = []
    mod._requested_permissions = {}
    mod._plugin_cls = None
    mod._saved_configs = {}

    class PluginType:
        PrinterConnection = "PrinterConnection"
        Pages = "Pages"
        Analysis = "Analysis"
        Importer = "Importer"
        Exporter = "Exporter"
        Visualization = "Visualization"
        Script = "Script"
        SlicingPipeline = "SlicingPipeline"
        ResourceTexture = "ResourceTexture"
        Unknown = "Unknown"

    class LifecycleEvent:
        NewProject = "NewProject"
        ProjectOpened = "ProjectOpened"
        ProjectBeforeSave = "ProjectBeforeSave"
        ProjectAfterSave = "ProjectAfterSave"
        ProjectClosed = "ProjectClosed"
        ProjectDirtyChanged = "ProjectDirtyChanged"
        SliceStarted = "SliceStarted"
        SliceGeometryFinished = "SliceGeometryFinished"
        GCodeExportStarted = "GCodeExportStarted"
        GCodeExportFinished = "GCodeExportFinished"
        SlicingJobComplete = "SlicingJobComplete"
        ObjectAdded = "ObjectAdded"
        ObjectDeleted = "ObjectDeleted"
        ObjectTransformed = "ObjectTransformed"
        ObjectChanged = "ObjectChanged"
        ObjectRenamed = "ObjectRenamed"
        PlateCreated = "PlateCreated"
        PlateDeleted = "PlateDeleted"
        PlateSelected = "PlateSelected"
        PlateRenamed = "PlateRenamed"
        PresetSelected = "PresetSelected"
        PresetSaved = "PresetSaved"

    class LifecycleEvtCode:
        Ok = 0
        Warn = 1
        Error = 2

    class PythonPluginBase:
        def __init__(self) -> None:
            pass

        def get_name(self) -> str:
            return ""

        def get_type(self) -> str:
            return PluginType.Unknown

        def on_load(self) -> None:
            pass

        def on_unload(self) -> None:
            pass

        def on_cancelled(self) -> None:
            pass

        def on_lifecycle_event(self, event: Any, ctx: Any = None) -> None:
            pass

        def has_config_ui(self) -> bool:
            return False

        def get_config_ui(self) -> str:
            return ""

        def get_default_config(self) -> dict[str, Any]:
            return {}

        def get_config(self) -> str:
            raw = mod._saved_configs.get(self.__class__.__name__)
            if raw is not None:
                return raw
            default_cfg = self.get_default_config()
            return json.dumps(default_cfg) if isinstance(default_cfg, dict) else "{}"

        def get_config_version(self) -> str:
            return "1.1.1"

        def save_config(self, config: str) -> bool:
            try:
                parsed = json.loads(config)
                if not isinstance(parsed, dict):
                    return False
            except Exception:
                return False
            mod._saved_configs[self.__class__.__name__] = str(config)
            return True

    class BasePlugin:
        def __init__(self) -> None:
            pass

        def register_capabilities(self) -> None:
            pass

    class PagesPluginCapabilityBase(PythonPluginBase):
        def get_type(self) -> str:
            return PluginType.Pages

        def get_ui(self) -> str:
            return ""

        def get_icon(self) -> str:
            return ""

        def on_message(self, data: Any) -> None:
            pass

        def post_message(self, data: Any) -> None:
            pass

    class ScriptPluginCapabilityBase(PythonPluginBase):
        def get_type(self) -> str:
            return PluginType.Script

        def execute(self) -> Any:
            return None

    class PluginResult:
        Success = 0
        Skipped = 1
        RecoverableError = 2
        FatalError = 3

    class ExecutionResult:
        def __init__(self, status: int = 0, message: str = "", data: str = "") -> None:
            self.status = status
            self.message = message
            self.data = data

        @classmethod
        def success(cls, message: str = "", data: str = "") -> "ExecutionResult":
            return cls(PluginResult.Success, message, data)

        @classmethod
        def skipped(cls, message: str = "") -> "ExecutionResult":
            return cls(PluginResult.Skipped, message, "")

        @classmethod
        def failure(cls, status: int, message: str, data: str = "") -> "ExecutionResult":
            return cls(status, message, data)

    class NotificationLevel:
        ProgressBarNotificationLevel = "ProgressBarNotificationLevel"
        HintNotificationLevel = "HintNotificationLevel"
        RegularNotificationLevel = "RegularNotificationLevel"
        PrintInfoNotificationLevel = "PrintInfoNotificationLevel"
        PrintInfoShortNotificationLevel = "PrintInfoShortNotificationLevel"
        ImportantNotificationLevel = "ImportantNotificationLevel"
        WarningNotificationLevel = "WarningNotificationLevel"
        SeriousWarningNotificationLevel = "SeriousWarningNotificationLevel"
        ErrorNotificationLevel = "ErrorNotificationLevel"

    def plugin_decorator(cls: type) -> type:
        mod._plugin_cls = cls
        return cls

    def register_capability(cap_cls: type) -> None:
        mod._registered_capabilities.append(cap_cls)

    def request_permissions(**kwargs: Any) -> None:
        mod._requested_permissions.update(kwargs)

    pages_mod = types.ModuleType("orca.pages")
    pages_mod.PagesPluginCapabilityBase = PagesPluginCapabilityBase

    script_mod = types.ModuleType("orca.script")
    script_mod.ScriptPluginCapabilityBase = ScriptPluginCapabilityBase

    plugin_sub = types.ModuleType("orca.host.plugin")
    plugin_sub.storage = lambda: str(Path(__file__).resolve().parent)

    host_mod = types.ModuleType("orca.host")
    host_mod.app_info = lambda: {"version": "2.5.1", "language": "pt_BR"}
    host_mod.app_language = lambda: "pt_BR"
    host_mod.preset_bundle = lambda: None
    host_mod.plater = lambda: None
    host_mod.model = lambda: None
    host_mod.selected_printer = lambda: None
    host_mod.plugin = plugin_sub
    host_mod.ui = types.SimpleNamespace(
        NotificationLevel=NotificationLevel,
        create_dock_panel=None,
        create_window=None,
        push_notification=None,
        message=None,
    )
    host_mod.preset = types.SimpleNamespace(
        process=None,
        printer=None,
        filament=None,
    )

    mod.base = BasePlugin
    mod.PythonPluginBase = PythonPluginBase
    mod.PluginType = PluginType
    mod.PluginResult = PluginResult
    mod.LifecycleEvent = LifecycleEvent
    mod.LifecycleEvtCode = LifecycleEvtCode
    mod.ExecutionResult = ExecutionResult
    mod.plugin = plugin_decorator
    mod.register_capability = register_capability
    mod.request_permissions = request_permissions
    mod.pages = pages_mod
    mod.script = script_mod
    mod.host = host_mod

    return mod


try:
    import orca  # type: ignore[import-not-found]
except ImportError:
    orca = _build_fallback_orca_module()


PLUGIN_SLUG = "orca_vase_generator"
WM_COPYDATA = 0x004A
SMTO_ABORTIFHUNG = 0x0002
ORCA_OTHER_INSTANCE_DWDATA = 1

ICON_SVG_CONTENT: str = """\
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64" fill="none">
  <defs>
    <linearGradient id="orcaBodyFill" x1="13" y1="10" x2="50" y2="55" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#00E5FF"/>
      <stop offset="46%" stop-color="#00BFA5"/>
      <stop offset="100%" stop-color="#00897B"/>
    </linearGradient>
    <linearGradient id="orcaBodyShade" x1="12" y1="32" x2="52" y2="36" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#00E5FF" stop-opacity="0.32"/>
      <stop offset="45%" stop-color="#00BFA5" stop-opacity="0.0"/>
      <stop offset="100%" stop-color="#004D40" stop-opacity="0.46"/>
    </linearGradient>
    <linearGradient id="orcaRimStroke" x1="14" y1="9" x2="50" y2="56" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#00E5FF"/>
      <stop offset="55%" stop-color="#00BFA5"/>
      <stop offset="100%" stop-color="#00897B"/>
    </linearGradient>
    <linearGradient id="orcaWaveLight" x1="16" y1="14" x2="46" y2="53" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#B2FFFC" stop-opacity="0.92"/>
      <stop offset="50%" stop-color="#00E5FF" stop-opacity="0.78"/>
      <stop offset="100%" stop-color="#00BFA5" stop-opacity="0.35"/>
    </linearGradient>
    <linearGradient id="orcaMouthWall" x1="18" y1="8" x2="46" y2="15" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#FFE082"/>
      <stop offset="52%" stop-color="#FFB74D"/>
      <stop offset="100%" stop-color="#F57C00"/>
    </linearGradient>
    <linearGradient id="orcaMouthCavity" x1="22" y1="9" x2="42" y2="15" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#6D3605"/>
      <stop offset="48%" stop-color="#B45309"/>
      <stop offset="85%" stop-color="#F59E0B"/>
      <stop offset="100%" stop-color="#FFB74D"/>
    </linearGradient>
    <clipPath id="orcaVaseClip">
      <path d="M18.5 11.5 C18.5 15.2 20.4 18.2 19.6 21.6 C18.4 26.5 12.6 31.2 13.0 38.0 C13.4 45.0 17.6 50.6 21.8 53.2 C24.8 55.0 28.2 55.8 32.0 55.8 C35.8 55.8 39.2 55.0 42.2 53.2 C46.4 50.6 50.6 45.0 51.0 38.0 C51.4 31.2 45.6 26.5 44.4 21.6 C43.6 18.2 45.5 15.2 45.5 11.5 Z"/>
    </clipPath>
  </defs>

  <!-- Subtle CAD Plater Base Ring -->
  <ellipse cx="32" cy="54.2" rx="22.5" ry="5.6" stroke="#00BFA5" stroke-width="1.25" stroke-opacity="0.48"/>
  <path d="M13.5 54.2 H50.5 M21.0 50.0 L43.0 58.2 M43.0 50.0 L21.0 58.2" stroke="#00E5FF" stroke-width="0.75" stroke-opacity="0.26" stroke-linecap="round"/>

  <!-- Sculpted Organic-Wave Vase Silhouette -->
  <path d="M18.5 11.5 C18.5 15.2 20.4 18.2 19.6 21.6 C18.4 26.5 12.6 31.2 13.0 38.0 C13.4 45.0 17.6 50.6 21.8 53.2 C24.8 55.0 28.2 55.8 32.0 55.8 C35.8 55.8 39.2 55.0 42.2 53.2 C46.4 50.6 50.6 45.0 51.0 38.0 C51.4 31.2 45.6 26.5 44.4 21.6 C43.6 18.2 45.5 15.2 45.5 11.5 Z"
        fill="url(#orcaBodyFill)"/>
  <path d="M18.5 11.5 C18.5 15.2 20.4 18.2 19.6 21.6 C18.4 26.5 12.6 31.2 13.0 38.0 C13.4 45.0 17.6 50.6 21.8 53.2 C24.8 55.0 28.2 55.8 32.0 55.8 C35.8 55.8 39.2 55.0 42.2 53.2 C46.4 50.6 50.6 45.0 51.0 38.0 C51.4 31.2 45.6 26.5 44.4 21.6 C43.6 18.2 45.5 15.2 45.5 11.5 Z"
        fill="url(#orcaBodyShade)"/>

  <!-- Helical Spiral Wave Ribs (Clipped Inside Vase Body) -->
  <g clip-path="url(#orcaVaseClip)">
    <!-- Deep sculpted wave valleys -->
    <path d="M15.0 14.0 C13.5 24.5 21.5 34.0 26.5 44.5 C29.0 49.8 31.8 54.0 34.5 57.0"
          stroke="#00695C" stroke-width="2.4" stroke-linecap="round" stroke-opacity="0.45"/>
    <path d="M23.5 13.0 C21.0 23.5 30.5 33.5 36.0 44.5 C38.8 50.0 41.0 53.8 43.2 56.5"
          stroke="#00695C" stroke-width="2.4" stroke-linecap="round" stroke-opacity="0.48"/>
    <path d="M33.0 13.0 C31.0 23.5 40.0 33.0 45.5 43.8 C47.8 48.2 49.5 51.5 51.0 54.0"
          stroke="#004D40" stroke-width="2.4" stroke-linecap="round" stroke-opacity="0.50"/>

    <!-- Crisp specular spiral wave crests -->
    <path d="M17.2 14.0 C15.2 24.2 23.5 33.8 28.6 44.5 C31.2 49.8 33.8 53.8 36.2 56.8"
          stroke="url(#orcaWaveLight)" stroke-width="1.75" stroke-linecap="round"/>
    <path d="M25.8 13.2 C23.6 23.4 32.8 33.4 38.2 44.2 C40.8 49.5 42.8 53.2 44.8 55.8"
          stroke="url(#orcaWaveLight)" stroke-width="1.85" stroke-linecap="round"/>
    <path d="M35.2 13.5 C33.2 23.2 42.0 32.6 47.2 43.2 C49.2 47.4 50.6 50.5 52.0 53.0"
          stroke="#00E5FF" stroke-width="1.55" stroke-linecap="round" stroke-opacity="0.68"/>
    <path d="M12.2 28.0 C15.0 35.5 19.8 43.2 24.8 51.8 C26.2 54.2 27.6 55.6 29.0 56.8"
          stroke="#80FFEA" stroke-width="1.45" stroke-linecap="round" stroke-opacity="0.65"/>
  </g>

  <!-- Crisp Outer Silhouette Contour (Native Contrast on Light & Dark Tabs) -->
  <path d="M18.5 11.5 C18.5 15.2 20.4 18.2 19.6 21.6 C18.4 26.5 12.6 31.2 13.0 38.0 C13.4 45.0 17.6 50.6 21.8 53.2 C24.8 55.0 28.2 55.8 32.0 55.8 C35.8 55.8 39.2 55.0 42.2 53.2 C46.4 50.6 50.6 45.0 51.0 38.0 C51.4 31.2 45.6 26.5 44.4 21.6 C43.6 18.2 45.5 15.2 45.5 11.5"
        stroke="url(#orcaRimStroke)" stroke-width="1.85" stroke-linecap="round" stroke-linejoin="round"/>

  <!-- Warm Amber-Gold Open Mouth Wall Rim & Hollow Interior -->
  <ellipse cx="32" cy="11.5" rx="13.5" ry="4.5" fill="url(#orcaMouthWall)" stroke="#FFB74D" stroke-width="1.1"/>
  <ellipse cx="32" cy="11.6" rx="10.1" ry="3.05" fill="url(#orcaMouthCavity)" stroke="#FFF3E0" stroke-width="0.65" stroke-opacity="0.65"/>
  <!-- Inner Cavity Spiral Depth Hint -->
  <path d="M25.5 10.2 C26.8 11.8 28.8 13.1 31.2 14.3 M32.8 9.0 C34.2 10.9 36.2 12.5 38.4 13.8"
        stroke="#FFE082" stroke-width="0.9" stroke-linecap="round" stroke-opacity="0.45"/>
</svg>
"""


# ---------------------------------------------------------------------------
# Environment, Host Inspection & In-Process Win32 `WM_COPYDATA` IPC Helpers
# ---------------------------------------------------------------------------


def _is_native_orca_host() -> bool:
    """Return True only when running inside the real C++ pybind11 OrcaSlicer host."""
    base_cls = getattr(orca, "base", None)
    return base_cls is not None and type(base_cls).__name__ == "pybind11_type"


def _is_mock_callable(obj: Any) -> bool:
    """Detect unittest.mock objects without importing unittest.mock eagerly."""
    cls_mod = getattr(type(obj), "__module__", "")
    return cls_mod.startswith("unittest.mock")


def _orca_os_default_data_dir() -> Path:
    """Resolve OrcaSlicer's default `data_dir()` across Windows, macOS, and Linux."""
    if sys.platform == "win32":
        appdata = os.environ.get("APPDATA", "").strip()
        if appdata:
            return Path(appdata) / "OrcaSlicer"
        return Path.home() / "AppData" / "Roaming" / "OrcaSlicer"
    if sys.platform == "darwin":
        return Path.home() / "Library" / "Application Support" / "OrcaSlicer"
    xdg_cfg = os.environ.get("XDG_CONFIG_HOME", "").strip()
    if xdg_cfg:
        return Path(xdg_cfg) / "OrcaSlicer"
    return Path.home() / ".config" / "OrcaSlicer"


def _orca_data_dir() -> Path:
    """Resolve OrcaSlicer's active `data_dir()`, honoring custom/portable `--datadir` or Flatpak
    installations whenever `__file__` resides inside an `orca_plugins` directory tree on the host OS.
    """
    platform_matches_host = (sys.platform == "win32") == (os.name == "nt")
    if platform_matches_host:
        try:
            here = Path(__file__).resolve()
            for parent in here.parents:
                if parent.name == "orca_plugins" and parent.parent != parent:
                    return parent.parent
        except Exception:
            pass
    return _orca_os_default_data_dir()


def _default_installed_plugin_dir() -> Path:
    return _orca_data_dir() / "orca_plugins" / PLUGIN_SLUG


def _default_plugin_data_dir() -> Path:
    return _orca_data_dir() / "orca_plugins" / "plugin_data" / PLUGIN_SLUG


def _resolve_storage_dir(*, in_callback: bool = True) -> Path:
    """Resolve current plugin storage folder safely (`orca.host.plugin.storage()` inside callbacks)."""
    # 1. Inside capability callbacks, query canonical `orca.host.plugin.storage()` first
    if in_callback:
        host_plugin = getattr(getattr(orca, "host", None), "plugin", None)
        top_plugin = getattr(orca, "plugin", None)
        holders = [host_plugin]
        if isinstance(top_plugin, types.ModuleType):
            holders.append(top_plugin)
        for holder in holders:
            storage_fn = getattr(holder, "storage", None)
            if callable(storage_fn):
                try:
                    raw = storage_fn()
                    if isinstance(raw, (str, os.PathLike)) and str(raw).strip():
                        return Path(raw)
                except Exception:
                    pass

    # 2. In native OrcaSlicer, prefer `plugin_data/orca_vase_generator`
    if _is_native_orca_host():
        data_dir = _default_plugin_data_dir()
        try:
            data_dir.mkdir(parents=True, exist_ok=True)
            return data_dir
        except Exception:
            pass

    # 3. Fallback to __file__ parent if available
    try:
        here = Path(__file__).resolve().parent
        if here.exists():
            return here
    except Exception:
        pass

    return _default_installed_plugin_dir()


def _format_other_instance_payload(file_paths: Sequence[str | Path]) -> str:
    """Format Win32 `WM_COPYDATA` payload matching `OrcaSlicer.dll` `unescape_strings_cstyle`.

    Produces `"orca-slicer.exe";"<resolved_path_1>";...` where every token escapes
    `\\` -> `\\\\`, `"` -> `\\"`, `\\r` -> `\\r`, `\\n` -> `\\n`, wrapped in double quotes and
    joined by `;` with NO trailing `;` (`OtherInstanceMessageHandler::handle_message` skips `args[0]`).
    """
    resolved_files = [str(Path(p).resolve()) for p in file_paths if str(p).strip()]
    if not resolved_files:
        raise ValueError("file_paths must contain at least one model path")

    tokens = ["orca-slicer.exe", *resolved_files]
    escaped: list[str] = []
    for tok in tokens:
        s = (
            tok.replace("\\", "\\\\")
            .replace('"', '\\"')
            .replace("\r", "\\r")
            .replace("\n", "\\n")
        )
        escaped.append(f'"{s}"')
    return ";".join(escaped)


def _find_orca_mainframe_hwnd(target_pid: int | None = None) -> int | None:
    """Locate OrcaSlicer's `MainFrame` `wxWindowNR` `HWND` in `target_pid` (`os.getpid()` by default).

    Prefers `wxWindowNR` windows marked with OrcaSlicer's `Instance_Hash_Minor` or
    `Instance_Hash_Major` properties, falling back to a visible top-level `wxWindowNR` of that PID.
    """
    if sys.platform != "win32":
        return None

    from ctypes import wintypes

    pid = int(target_pid) if target_pid is not None else os.getpid()
    user32 = ctypes.windll.user32

    WNDENUMPROC = ctypes.WINFUNCTYPE(wintypes.BOOL, wintypes.HWND, wintypes.LPARAM)

    enum_windows = user32.EnumWindows
    if not _is_mock_callable(enum_windows):
        enum_windows.argtypes = [WNDENUMPROC, wintypes.LPARAM]
        enum_windows.restype = wintypes.BOOL

    get_pid = user32.GetWindowThreadProcessId
    if not _is_mock_callable(get_pid):
        get_pid.argtypes = [wintypes.HWND, ctypes.POINTER(wintypes.DWORD)]
        get_pid.restype = wintypes.DWORD

    get_class = user32.GetClassNameW
    if not _is_mock_callable(get_class):
        get_class.argtypes = [wintypes.HWND, wintypes.LPWSTR, ctypes.c_int]
        get_class.restype = ctypes.c_int

    get_prop = user32.GetPropW
    if not _is_mock_callable(get_prop):
        get_prop.argtypes = [wintypes.HWND, wintypes.LPCWSTR]
        get_prop.restype = wintypes.HANDLE

    is_visible = user32.IsWindowVisible
    if not _is_mock_callable(is_visible):
        is_visible.argtypes = [wintypes.HWND]
        is_visible.restype = wintypes.BOOL

    get_parent = user32.GetParent
    if not _is_mock_callable(get_parent):
        get_parent.argtypes = [wintypes.HWND]
        get_parent.restype = wintypes.HWND

    hash_visible: list[int] = []
    hash_any: list[int] = []
    fallback_visible: list[int] = []

    def _enum_cb(hwnd: int, _lparam: int) -> bool:
        if not hwnd:
            return True
        win_pid = wintypes.DWORD(0)
        get_pid(hwnd, ctypes.byref(win_pid))
        if int(win_pid.value) != pid:
            return True

        cls_buf = ctypes.create_unicode_buffer(64)
        cls_len = get_class(hwnd, cls_buf, 64)
        if cls_len <= 0 or cls_buf.value != "wxWindowNR":
            return True

        minor = get_prop(hwnd, "Instance_Hash_Minor")
        major = get_prop(hwnd, "Instance_Hash_Major")
        vis = bool(is_visible(hwnd))
        hwnd_int = int(hwnd)

        if bool(minor) or bool(major):
            if vis:
                hash_visible.append(hwnd_int)
            else:
                hash_any.append(hwnd_int)
        elif vis and not get_parent(hwnd):
            fallback_visible.append(hwnd_int)
        return True

    cb_ref = WNDENUMPROC(_enum_cb)
    enum_windows(cb_ref, 0)

    if hash_visible:
        return hash_visible[0]
    if hash_any:
        return hash_any[0]
    if fallback_visible:
        return fallback_visible[0]
    return None


class _COPYDATASTRUCT(ctypes.Structure):
    _fields_ = [
        ("dwData", ctypes.c_size_t),
        ("cbData", ctypes.c_uint32),
        ("lpData", ctypes.c_void_p),
    ]


def _dispatch_copydata_to_hwnd(
    hwnd: int,
    payload_str: str,
    timeout_ms: int = 5000,
) -> tuple[bool, str]:
    """Send UTF-16LE `WM_COPYDATA` (`dwData = 1`) to `hwnd` via `SendMessageTimeoutW` (`0x0002`)."""
    if not hwnd or int(hwnd) <= 0:
        return (False, "OrcaSlicer MainFrame HWND not found")
    if not payload_str:
        return (False, "Empty WM_COPYDATA payload")
    if sys.platform != "win32":
        return (False, "WM_COPYDATA requires win32")

    from ctypes import wintypes

    wchar_buf = ctypes.create_unicode_buffer(payload_str)
    cds = _COPYDATASTRUCT(
        dwData=ORCA_OTHER_INSTANCE_DWDATA,
        cbData=ctypes.sizeof(wchar_buf),
        lpData=ctypes.cast(wchar_buf, ctypes.c_void_p),
    )
    result = ctypes.c_size_t(0)

    user32 = ctypes.windll.user32
    send_msg = user32.SendMessageTimeoutW
    if not _is_mock_callable(send_msg):
        send_msg.argtypes = [
            wintypes.HWND,
            wintypes.UINT,
            wintypes.WPARAM,
            ctypes.c_void_p,
            wintypes.UINT,
            wintypes.UINT,
            ctypes.POINTER(ctypes.c_size_t),
        ]
        send_msg.restype = ctypes.c_size_t

    ret = send_msg(
        int(hwnd),
        WM_COPYDATA,
        0,
        ctypes.byref(cds),
        SMTO_ABORTIFHUNG,
        max(100, int(timeout_ms)),
        ctypes.byref(result),
    )
    if not ret:
        err = ctypes.windll.kernel32.GetLastError()
        return (False, f"SendMessageTimeoutW failed (GetLastError={err})")
    return (True, "ok")


def _dispatch_non_win32_plater_open(file_paths: Sequence[str | Path]) -> tuple[bool, str]:
    """Graceful macOS / Linux Plater open fallback when running outside Win32 (`WM_COPYDATA`)."""
    resolved = [str(Path(p).resolve()) for p in file_paths if str(p).strip()]
    if not resolved:
        return (False, "No model files to open")
    if not _is_native_orca_host():
        return (False, f"WM_COPYDATA requires win32 (platform={sys.platform})")
    try:
        import subprocess

        if sys.platform == "darwin":
            subprocess.Popen(
                ["open", "-a", "OrcaSlicer", *resolved],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            return (True, "darwin_open_ok")
        # Linux / POSIX: try sibling `orca-slicer` binary with `--single-instance`, else `xdg-open`
        exe_dir = Path(sys.executable).resolve().parent
        for cand_bin in (exe_dir / "orca-slicer", exe_dir.parent / "orca-slicer", exe_dir.parent / "bin" / "orca-slicer"):
            if cand_bin.is_file():
                subprocess.Popen(
                    [str(cand_bin), "--single-instance", *resolved],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                )
                return (True, "linux_single_instance_ok")
        subprocess.Popen(
            ["xdg-open", resolved[0]],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        return (True, "xdg_open_ok")
    except Exception as exc:
        return (False, f"Non-win32 Plater open fallback skipped: {exc}")


def _slugify_filename(name: str, fallback: str = "vaso") -> str:
    cleaned = re.sub(r"[^\w\-. ]+", "", str(name or "").strip(), flags=re.ASCII)
    cleaned = re.sub(r"\s+", "_", cleaned).strip("._-")
    if not cleaned:
        return fallback
    return cleaned[:64]


def _extract_first_float(val: Any, default: float) -> float:
    if val is None:
        return default
    if isinstance(val, (int, float)) and not isinstance(val, bool):
        f = float(val)
        return f if f == f else default
    if isinstance(val, (list, tuple)):
        for item in val:
            res = _extract_first_float(item, float("nan"))
            if res == res:
                return res
        return default
    s = str(val).strip()
    if not s:
        return default
    m = re.search(r"[-+]?\d*\.?\d+", s)
    if not m:
        return default
    try:
        return float(m.group(0))
    except ValueError:
        return default


def _parse_bed_geometry(
    raw: Any,
    default_x: float = 220.0,
    default_y: float = 220.0,
) -> dict[str, Any]:
    """Parse OrcaSlicer `printable_area` / `bed_shape` polygon into bed dimensions and shape.

    Supports:
    - `['0x0', '220x0', '220x220', '0x220']`
    - `'0x0,220x0,220x220,0x220'` or semicolon-separated strings
    - `[[0, 0], [220, 0], [220, 220], [0, 220]]` or numpy arrays
    - `orca.host.Point` / `Pointf` objects exposing `.x` / `.y` or dicts `{'x': ..., 'y': ...}`
    - Circular / delta beds with `> 6` polygon vertices around origin or bed center
    """
    fallback = {
        "bed_x": float(default_x),
        "bed_y": float(default_y),
        "bed_shape": "rectangular",
        "bed_center": [round(float(default_x) * 0.5, 2), round(float(default_y) * 0.5, 2)],
    }
    if raw is None:
        return fallback

    xs: list[float] = []
    ys: list[float] = []

    tokens: list[Any]
    if isinstance(raw, str):
        s = raw.strip()
        if not s:
            return fallback
        if s.startswith("["):
            try:
                parsed = json.loads(s)
                tokens = parsed if isinstance(parsed, list) else [s]
            except Exception:
                tokens = re.split(r"[;,]+", s)
        else:
            tokens = re.split(r"[;,]+", s)
    elif isinstance(raw, Sequence) and not isinstance(raw, (bytes, bytearray)):
        tokens = list(raw)
    elif hasattr(raw, "__iter__"):
        try:
            tokens = list(raw)
        except Exception:
            return fallback
    else:
        return fallback

    for tok in tokens:
        if tok is None:
            continue
        if isinstance(tok, str):
            m = re.search(r"([-+]?\d*\.?\d+)\s*[xX:,]\s*([-+]?\d*\.?\d+)", tok.strip())
            if m:
                try:
                    xs.append(float(m.group(1)))
                    ys.append(float(m.group(2)))
                except ValueError:
                    continue
        elif isinstance(tok, dict):
            if "x" in tok and "y" in tok:
                try:
                    xs.append(float(tok["x"]))
                    ys.append(float(tok["y"]))
                except (TypeError, ValueError):
                    continue
        elif hasattr(tok, "x") and hasattr(tok, "y"):
            try:
                xv = tok.x() if callable(tok.x) else tok.x
                yv = tok.y() if callable(tok.y) else tok.y
                xs.append(float(xv))
                ys.append(float(yv))
            except Exception:
                continue
        elif hasattr(tok, "__len__") and hasattr(tok, "__getitem__"):
            try:
                if len(tok) >= 2:
                    xs.append(float(tok[0]))
                    ys.append(float(tok[1]))
            except Exception:
                continue

    if len(xs) >= 2 and len(ys) >= 2:
        min_x, max_x = min(xs), max(xs)
        min_y, max_y = min(ys), max(ys)
        dx = max_x - min_x
        dy = max_y - min_y
        cx = 0.5 * (min_x + max_x)
        cy = 0.5 * (min_y + max_y)

        if dx >= 30.0 and dy >= 30.0:
            if len(xs) > 6:
                mean_x = sum(xs) / len(xs)
                mean_y = sum(ys) / len(ys)
                best_cx, best_cy = cx, cy
                best_radii = [math.hypot(x - cx, y - cy) for x, y in zip(xs, ys)]
                mean_radii = [math.hypot(x - mean_x, y - mean_y) for x, y in zip(xs, ys)]
                if (max(mean_radii) - min(mean_radii)) < (max(best_radii) - min(best_radii)):
                    best_cx, best_cy = mean_x, mean_y
                    best_radii = mean_radii

                r_max = max(best_radii)
                r_min = min(best_radii)
                if r_max >= 15.0 and (r_max - r_min) / r_max <= 0.12:
                    r_avg = sum(best_radii) / len(best_radii)
                    diam = round(2.0 * r_avg, 2)
                    if abs(diam - round(diam)) < 0.08:
                        diam = float(round(diam))
                    return {
                        "bed_x": float(diam),
                        "bed_y": float(diam),
                        "bed_shape": "circular",
                        "bed_center": [round(best_cx, 2), round(best_cy, 2)],
                    }

            bx = round(dx, 2)
            by = round(dy, 2)
            return {
                "bed_x": float(bx),
                "bed_y": float(by),
                "bed_shape": "rectangular",
                "bed_center": [round(cx, 2), round(cy, 2)],
            }

    return fallback


def _parse_printable_area(raw: Any, default_x: float = 220.0, default_y: float = 220.0) -> tuple[float, float]:
    """Parse OrcaSlicer `printable_area` into `(bed_x_mm, bed_y_mm)`."""
    geom = _parse_bed_geometry(raw, default_x=default_x, default_y=default_y)
    return (float(geom["bed_x"]), float(geom["bed_y"]))


def _parse_line_width(raw: Any, nozzle_mm: float, fallback_raw: Any = None) -> float:
    """Parse OrcaSlicer line width (`'0.42'`, `'105%'`, `'0'`, `['110%']`) relative to `nozzle_mm`."""
    default_lw = round(max(0.15, min(3.0, float(nozzle_mm) * 1.05)), 3)

    def _parse_single(candidate: Any) -> float | None:
        if candidate is None or isinstance(candidate, bool):
            return None
        if isinstance(candidate, (list, tuple)):
            return _parse_single(candidate[0] if candidate else None)
        s = str(candidate).strip()
        if not s:
            return None
        if s.endswith("%"):
            pct = _extract_first_float(s[:-1], 0.0)
            if pct > 10.0:
                return round(max(0.15, min(3.0, float(nozzle_mm) * (pct / 100.0))), 3)
            return None
        val = _extract_first_float(s, 0.0)
        if val <= 0.05:
            return None
        return round(max(0.15, min(3.0, val)), 3)

    parsed = _parse_single(raw)
    if parsed is not None:
        return parsed
    if fallback_raw is not None:
        parsed_fb = _parse_single(fallback_raw)
        if parsed_fb is not None:
            return parsed_fb
    return default_lw


def _resolve_attr_or_call(obj: Any, attr_name: str) -> Any:
    """Read an attribute on a pybind11/mock object whether exposed as a property or 0-arg method."""
    if obj is None:
        return None
    try:
        val = getattr(obj, attr_name, None)
    except Exception:
        return None
    if val is None:
        return None
    if callable(val):
        try:
            return val()
        except Exception:
            return None
    return val


def _extract_preset_name(obj: Any, fallback: str = "") -> str:
    if obj is None:
        return fallback
    if isinstance(obj, str):
        return obj.strip() or fallback
    if isinstance(obj, (list, tuple)):
        for item in obj:
            got = _extract_preset_name(item, "")
            if got:
                return got
        return fallback
    if isinstance(obj, dict):
        for k in ("name", "preset_name", "printer_name", "id"):
            v = obj.get(k)
            if isinstance(v, str) and v.strip():
                return v.strip()
        return fallback
    for attr in ("name", "preset_name", "selected_preset_name"):
        val = _resolve_attr_or_call(obj, attr)
        if isinstance(val, str) and val.strip():
            return val.strip()
    return fallback


def _preset_get_value(preset_obj: Any, key: str) -> Any:
    """Read `config_value(key)` directly from an `orca.host.Preset` instance if available."""
    if preset_obj is None or isinstance(preset_obj, (str, bytes, dict, list, tuple)):
        return None
    for method_name in ("config_value", "full_config_value", "get"):
        fn = getattr(preset_obj, method_name, None)
        if callable(fn):
            try:
                val = fn(key)
                if val is not None and val != "" and val != []:
                    return val
            except Exception:
                continue
    return None


def _bundle_get_value(bundle: Any, key: str, preset_obj: Any = None) -> Any:
    from_preset = _preset_get_value(preset_obj, key)
    if from_preset is not None:
        return from_preset
    if bundle is None:
        return None
    for method_name in ("full_config_value", "config_value", "get"):
        fn = getattr(bundle, method_name, None)
        if callable(fn):
            try:
                val = fn(key)
                if val is not None and val != "" and val != []:
                    return val
            except Exception:
                continue
    return None


def _detect_language(app_info: dict[str, Any]) -> str:
    raw = app_info.get("language") or app_info.get("lang")
    if raw:
        return normalize_language(raw)
    try:
        detected = locale.getlocale()[0]
        if detected:
            return normalize_language(detected)
    except Exception:
        pass
    return "pt"


def _detect_theme(app_info: dict[str, Any]) -> str:
    theme_raw = str(app_info.get("theme") or app_info.get("color_mode") or "").strip().lower()
    if theme_raw == "light":
        return "light"
    if theme_raw == "dark":
        return "dark"
    if app_info.get("dark_mode") is False:
        return "light"
    return "dark"


def _make_execution_result_success(message: str) -> Any:
    exec_cls = getattr(orca, "ExecutionResult", None)
    if exec_cls is not None:
        success_fn = getattr(exec_cls, "success", None)
        if callable(success_fn):
            try:
                return success_fn(message)
            except TypeError:
                return success_fn(message, "")
        try:
            ok_code = getattr(getattr(orca, "PluginResult", None), "Success", 0)
            return exec_cls(ok_code, message, "")
        except Exception:
            pass
    return {"status": "Success", "message": message}


# ---------------------------------------------------------------------------
# Shared Studio Session & Message Router
# ---------------------------------------------------------------------------


class VaseStudioController:
    """Coordinates live host reading, mesh generation, exports, and Plater IPC."""

    def __init__(self) -> None:
        self._lock = threading.RLock()
        self._current_params: dict[str, Any] = normalize_params(DEFAULT_PARAMS)
        self._listeners: dict[str, Callable[[dict[str, Any]], None]] = {}
        self._manual_language: str | None = None
        self._language_loaded = False
        self._language_revision = 0
        self._last_language_requests: dict[str, int] = {}
        self._last_plater_worker: threading.Thread | None = None
        self._last_plater_outcome: dict[str, Any] = {}

    def _load_language_preferences(self) -> None:
        # Storage is callback-only in Orca: never consult it while importing or
        # registering capabilities. The first context read is a UI callback.
        with self._lock:
            if self._language_loaded:
                return
            self._language_loaded = True
            try:
                prefs = json.loads((_resolve_storage_dir() / "ui_preferences.json").read_text(encoding="utf8"))
                if isinstance(prefs, dict) and prefs.get("language"):
                    self._manual_language = normalize_language(prefs["language"])
            except (OSError, ValueError, TypeError):
                pass

    @property
    def current_params(self) -> dict[str, Any]:
        with self._lock:
            return copy.deepcopy(self._current_params)

    def set_current_params(self, raw: dict[str, Any] | None) -> dict[str, Any]:
        norm = normalize_params(raw)
        with self._lock:
            self._current_params = norm
            return copy.deepcopy(norm)

    def get_presets_dir(self) -> Path:
        base = _resolve_storage_dir()
        target = base / "presets"
        try:
            target.mkdir(parents=True, exist_ok=True)
            return target
        except Exception:
            return base

    def get_export_dir(self) -> Path:
        base = _resolve_storage_dir()
        target = base / "exports"
        try:
            target.mkdir(parents=True, exist_ok=True)
            return target
        except Exception:
            fallback = Path.home() / "Documents" / "OrcaVaseStudio"
            try:
                fallback.mkdir(parents=True, exist_ok=True)
                return fallback
            except Exception:
                return base

    def read_host_context(self) -> dict[str, Any]:
        """Defensively inspect `orca.host.app_info()`, `orca.host.app_language()`, and `orca.host.preset_bundle()`."""
        self._load_language_preferences()
        app_info: dict[str, Any] = {}
        host = getattr(orca, "host", None)
        if host is not None:
            app_info_fn = getattr(host, "app_info", None)
            if callable(app_info_fn):
                try:
                    info = app_info_fn()
                    if isinstance(info, dict):
                        app_info = dict(info)
                except Exception:
                    app_info = {}

            # Official Wiki API (`orca.host.app_language()` -> e.g. "en_US", "pt_BR")
            if not str(app_info.get("language") or app_info.get("lang") or "").strip():
                app_lang_fn = getattr(host, "app_language", None)
                if callable(app_lang_fn):
                    try:
                        lang_val = app_lang_fn()
                        if isinstance(lang_val, str) and lang_val.strip():
                            app_info["language"] = lang_val.strip()
                    except Exception:
                        pass

        lang = self._manual_language or _detect_language(app_info)
        theme = _detect_theme(app_info)
        theme_explicit = any(k in app_info for k in ("theme", "color_mode", "dark_mode"))
        orca_version = str(app_info.get("version") or "2.5.1")

        bundle = _resolve_attr_or_call(host, "preset_bundle") if host is not None else None

        printer_name = ""
        process_name = "0.20mm Standard"
        filament_name = "Generic PLA"

        active_printer_preset: Any = None
        active_process_preset: Any = None

        if bundle is not None:
            # 1. Inspect `bundle.printers` (`PresetCollection` on OrcaSlicer.dll v2.5.1)
            printers_col = _resolve_attr_or_call(bundle, "printers")
            if printers_col is not None:
                for attr in ("edited_preset", "get_edited_preset", "selected_preset", "get_selected_preset"):
                    cand = _resolve_attr_or_call(printers_col, attr)
                    if cand is not None:
                        if active_printer_preset is None:
                            active_printer_preset = cand
                        got = _extract_preset_name(cand, "")
                        if got:
                            printer_name = got
                            break
                if not printer_name:
                    for attr in ("selected_preset_name", "get_selected_preset_name"):
                        got = _extract_preset_name(_resolve_attr_or_call(printers_col, attr), "")
                        if got:
                            printer_name = got
                            break

            # 2. Inspect `bundle.current_printer_preset` (property or 0-arg method)
            cur_pr = _resolve_attr_or_call(bundle, "current_printer_preset")
            if cur_pr is not None:
                if active_printer_preset is None:
                    active_printer_preset = cur_pr
                if not printer_name:
                    printer_name = _extract_preset_name(cur_pr, "")

            # 3. Inspect `bundle.prints` (`PresetCollection`) & `current_process_preset` / `current_print_preset`
            prints_col = _resolve_attr_or_call(bundle, "prints")
            if prints_col is not None:
                for attr in ("edited_preset", "get_edited_preset", "selected_preset", "get_selected_preset"):
                    cand = _resolve_attr_or_call(prints_col, attr)
                    if cand is not None:
                        if active_process_preset is None:
                            active_process_preset = cand
                        got = _extract_preset_name(cand, "")
                        if got:
                            process_name = got
                            break

            for m in ("current_process_preset", "current_print_preset"):
                cand = _resolve_attr_or_call(bundle, m)
                if cand is not None:
                    if active_process_preset is None:
                        active_process_preset = cand
                    got = _extract_preset_name(cand, "")
                    if got:
                        process_name = got
                        break

            # 4. Inspect filament presets (`current_filament_preset_names`, `current_filament_presets`, `filaments`)
            got_fil = ""
            for m in ("current_filament_preset_names", "current_filament_presets"):
                fils = _resolve_attr_or_call(bundle, m)
                if isinstance(fils, (list, tuple)) and fils:
                    got_fil = _extract_preset_name(fils[0], "")
                    if got_fil:
                        filament_name = got_fil
                        break
            if not got_fil:
                fil_col = _resolve_attr_or_call(bundle, "filaments")
                if fil_col is not None:
                    for attr in ("edited_preset", "get_edited_preset", "selected_preset", "get_selected_preset"):
                        got_fil = _extract_preset_name(_resolve_attr_or_call(fil_col, attr), "")
                        if got_fil:
                            filament_name = got_fil
                            break

            # 5. Fallback preset IDs from resolved config keys
            if not printer_name:
                for key_id in ("printer_settings_id", "printer_model"):
                    p_id = _bundle_get_value(bundle, key_id, active_printer_preset)
                    got = _extract_preset_name(p_id, "")
                    if got:
                        printer_name = got
                        break

            if process_name == "0.20mm Standard":
                pr_id = _bundle_get_value(bundle, "print_settings_id", active_process_preset)
                got_pr = _extract_preset_name(pr_id, "")
                if got_pr:
                    process_name = got_pr

        # Optional fallback to `orca.host.selected_printer` if bundle had no printer name
        if not printer_name and host is not None:
            sel_pr = _resolve_attr_or_call(host, "selected_printer")
            printer_name = _extract_preset_name(sel_pr, "")

        if not printer_name:
            printer_name = "Default Printer"

        raw_area = _bundle_get_value(bundle, "printable_area", active_printer_preset)
        if raw_area is None or raw_area == "" or raw_area == []:
            raw_area = _bundle_get_value(bundle, "bed_shape", active_printer_preset)

        bed_geom = _parse_bed_geometry(raw_area, default_x=220.0, default_y=220.0)
        bed_x = float(bed_geom["bed_x"])
        bed_y = float(bed_geom["bed_y"])
        bed_shape = str(bed_geom["bed_shape"])
        bed_center = list(bed_geom["bed_center"])

        max_z = max(
            50.0,
            min(
                1000.0,
                _extract_first_float(
                    _bundle_get_value(bundle, "printable_height", active_printer_preset),
                    250.0,
                ),
            ),
        )
        nozzle_mm = max(
            0.15,
            min(
                2.0,
                _extract_first_float(
                    _bundle_get_value(bundle, "nozzle_diameter", active_printer_preset),
                    0.4,
                ),
            ),
        )
        layer_height_mm = max(
            0.04,
            min(
                1.2,
                _extract_first_float(
                    _bundle_get_value(bundle, "layer_height", active_process_preset),
                    0.2,
                ),
            ),
        )
        line_width_mm = _parse_line_width(
            _bundle_get_value(bundle, "outer_wall_line_width", active_process_preset),
            nozzle_mm=nozzle_mm,
            fallback_raw=_bundle_get_value(bundle, "line_width", active_process_preset),
        )
        top_shell_layers = int(
            round(
                _extract_first_float(
                    _bundle_get_value(bundle, "top_shell_layers", active_process_preset),
                    4.0,
                )
            )
        )
        raw_infill = _bundle_get_value(bundle, "sparse_infill_density", active_process_preset)
        if isinstance(raw_infill, (list, tuple)):
            raw_infill = raw_infill[0] if raw_infill else "15%"
        sparse_infill_density = str(raw_infill if raw_infill is not None else "15%").strip() or "15%"

        return {
            "lang": lang,
            "theme": theme,
            "theme_explicit": theme_explicit,
            "orca_version": orca_version,
            "printer_name": printer_name,
            "process_name": process_name,
            "filament_name": filament_name,
            "bed_x": float(bed_x),
            "bed_y": float(bed_y),
            "bed_shape": bed_shape,
            "bed_center": bed_center,
            "max_z": float(max_z),
            "nozzle_mm": float(nozzle_mm),
            "layer_height_mm": float(layer_height_mm),
            "line_width_mm": float(line_width_mm),
            "top_shell_layers": top_shell_layers,
            "sparse_infill_density": sparse_infill_density,
        }

    def read_full_host_config_snapshot(self, host_ctx: dict[str, Any] | None = None) -> dict[str, Any]:
        """Collect full resolved `project_settings` snapshot from `preset_bundle()` for `.3mf` export."""
        ctx = dict(host_ctx) if host_ctx is not None else self.read_host_context()
        project_settings: dict[str, Any] = {}

        host = getattr(orca, "host", None)
        bundle = None
        if host is not None:
            bundle_fn = getattr(host, "preset_bundle", None)
            if callable(bundle_fn):
                try:
                    bundle = bundle_fn()
                except Exception:
                    bundle = None

        if bundle is not None:
            keys_fn = getattr(bundle, "full_config_keys", None)
            val_fn = getattr(bundle, "full_config_value", None) or getattr(bundle, "config_value", None)
            if callable(keys_fn) and callable(val_fn):
                try:
                    keys = keys_fn()
                    if isinstance(keys, (list, tuple, set)):
                        for k in keys:
                            ks = str(k)
                            if not ks:
                                continue
                            try:
                                v = val_fn(ks)
                                if v is not None:
                                    project_settings[ks] = v
                            except Exception:
                                continue
                except Exception:
                    pass

        ctx["project_settings"] = project_settings
        return ctx

    def build_printer_payload(self, host_ctx: dict[str, Any] | None = None) -> dict[str, Any]:
        """Construct the UI-facing `printer` metadata dictionary from `host_ctx`."""
        ctx = host_ctx if isinstance(host_ctx, dict) else self.read_host_context()
        return {
            "name": ctx["printer_name"],
            "process_name": ctx["process_name"],
            "filament_name": ctx["filament_name"],
            "orca_version": ctx["orca_version"],
            "bed_x": ctx["bed_x"],
            "bed_y": ctx["bed_y"],
            "bed_shape": ctx.get("bed_shape", "rectangular"),
            "bed_center": ctx.get("bed_center", [round(ctx["bed_x"] * 0.5, 2), round(ctx["bed_y"] * 0.5, 2)]),
            "max_z": ctx["max_z"],
            "nozzle_mm": ctx["nozzle_mm"],
            "layer_height_mm": ctx["layer_height_mm"],
            "line_width_mm": ctx["line_width_mm"],
        }

    def build_initial_context(self, mode: str = "page") -> dict[str, Any]:
        host_ctx = self.read_host_context()
        presets_dir = self.get_presets_dir()
        export_dir = self.get_export_dir()
        params = self.current_params
        return {
            "mode": mode,
            "lang": host_ctx["lang"],
            "language_override": self._manual_language is not None,
            "language_revision": self._language_revision,
            "theme": host_ctx["theme"],
            "theme_explicit": bool(host_ctx.get("theme_explicit", False)),
            "printer": self.build_printer_payload(host_ctx),
            "builtin_presets": BUILTIN_PRESETS,
            "user_presets": load_user_presets(presets_dir),
            "params": params,
            "export_dir": str(export_dir),
        }

    def _prepare_effective_vase_params(
        self,
        params: dict[str, Any],
        *,
        is_stl_export: bool,
        include_saucer: bool,
    ) -> dict[str, Any]:
        """Ensure `.STL` exports (when `stl_always_open_hollow` is True) and Vase+Saucer combos
        never generate a sealed top-capped Spiral Vase solid block.
        """
        effective = copy.deepcopy(params)
        if str(effective.get("print_mode", "shelled_hollow")) == "spiral_vase":
            force_open_hollow = bool(include_saucer) or (
                bool(is_stl_export) and bool(effective.get("stl_always_open_hollow", True))
            )
            if force_open_hollow:
                effective["print_mode"] = "shelled_hollow"
                effective["wall_thickness_mm"] = max(
                    0.8,
                    float(effective.get("wall_thickness_mm", 2.4)),
                )
                effective["bottom_thickness_mm"] = max(
                    1.0,
                    float(effective.get("bottom_thickness_mm", 3.2)),
                )
        return effective

    def _compute_process_preset_updates(
        self,
        params: dict[str, Any],
        host_ctx: dict[str, Any],
        include_saucer: bool,
    ) -> dict[str, str]:
        """Build key/value strings for `orca.host.preset.process.begin_update()`."""
        print_mode = str(params.get("print_mode", "shelled_hollow"))
        use_spiral = (print_mode == "spiral_vase") and (not include_saucer)

        if use_spiral:
            smooth = bool(params.get("spiral_smooth", True))
            bottom_layers = max(2, min(15, int(params.get("spiral_bottom_layers", 5))))
            spiral_lw = max(0.40, min(1.20, float(params.get("spiral_line_width_mm", 0.65))))
            return {
                "spiral_mode": "1",
                "spiral_mode_smooth": "1" if smooth else "0",
                "wall_loops": "1",
                "top_shell_layers": "0",
                "sparse_infill_density": "0%",
                "bottom_shell_layers": str(bottom_layers),
                "outer_wall_line_width": f"{spiral_lw:.2f}",
            }

        # Shelled hollow mode OR multi-object plate (vase + saucer)
        lw = max(0.25, float(host_ctx.get("line_width_mm", 0.42)))
        lh = max(0.08, float(host_ctx.get("layer_height_mm", 0.20)))

        wall_mm = max(0.8, float(params.get("wall_thickness_mm", 2.4)))
        bot_mm = max(1.0, float(params.get("bottom_thickness_mm", 3.2)))
        wall_loops = max(2, min(15, int(round(wall_mm / (2.0 * lw)))))
        bottom_layers = max(3, min(125, int(round(bot_mm / lh))))

        updates: dict[str, str] = {
            "spiral_mode": "0",
            "spiral_mode_smooth": "0",
            "wall_loops": str(wall_loops),
            "bottom_shell_layers": str(bottom_layers),
        }
        if int(host_ctx.get("top_shell_layers", 4)) <= 0:
            updates["top_shell_layers"] = "4"
        if str(host_ctx.get("sparse_infill_density", "15%")).strip() in ("", "0", "0%"):
            updates["sparse_infill_density"] = "15%"
        return updates

    def _apply_process_presets(self, updates: dict[str, str]) -> dict[str, Any]:
        """Apply process preset changes on the calling background worker thread.

        NEVER call `orca.host.preset.process.begin_update()` on the wxWidgets UI thread!
        """
        outcome: dict[str, Any] = {"applied": False, "error": None}
        if not updates:
            return outcome
        try:
            host = getattr(orca, "host", None)
            preset_ns = getattr(host, "preset", None) if host is not None else None
            process_ed = getattr(preset_ns, "process", None) if preset_ns is not None else None
            begin_fn = getattr(process_ed, "begin_update", None) if process_ed is not None else None
            if not callable(begin_fn):
                return outcome

            tx = begin_fn()
            if tx is None:
                return outcome

            staged_any = False
            for key, val in updates.items():
                try:
                    tx.set(str(key), str(val))
                    staged_any = True
                except Exception:
                    continue

            if staged_any:
                commit_fn = getattr(tx, "commit", None)
                if callable(commit_fn):
                    commit_fn()
                outcome["applied"] = True
        except Exception as exc:
            outcome["error"] = str(exc)
        return outcome

    def _apply_process_presets_async(
        self,
        updates: dict[str, str],
        delay_sec: float = 0.0,
    ) -> tuple[threading.Thread, dict[str, Any]]:
        """Apply process preset changes strictly on a background daemon thread."""
        outcome: dict[str, Any] = {"applied": False, "error": None}

        def _worker() -> None:
            if delay_sec > 0.0:
                time.sleep(delay_sec)
            res = self._apply_process_presets(updates)
            outcome.update(res)

        thread = threading.Thread(
            target=_worker,
            name="OrcaVaseStudio-PresetUpdater",
            daemon=True,
        )
        thread.start()
        return thread, outcome

    def _write_stl_resilient(self, directory: Path, stem: str, mesh: Any, header: str) -> Path:
        target = directory / f"{stem}.stl"
        try:
            return Path(write_binary_stl(target, mesh, header_name=header))
        except PermissionError:
            alt = directory / f"{stem}_{int(time.time() * 1000)}.stl"
            return Path(write_binary_stl(alt, mesh, header_name=header))

    def _notify_host_toast(
        self,
        text: str,
        level_name: str = "RegularNotificationLevel",
    ) -> None:
        host = getattr(orca, "host", None)
        ui = getattr(host, "ui", None) if host is not None else None
        push_fn = getattr(ui, "push_notification", None) if ui is not None else None
        if not callable(push_fn):
            return
        lvl_enum = getattr(ui, "NotificationLevel", None)
        level = None
        if lvl_enum is not None:
            level = getattr(
                lvl_enum,
                level_name,
                getattr(lvl_enum, "RegularNotificationLevel", None),
            )
        try:
            if level is not None:
                try:
                    push_fn(level, text)
                    return
                except TypeError:
                    push_fn(text)
                    return
            push_fn(text)
        except Exception:
            pass

    def handle_message(
        self,
        raw_data: Any,
        send_fn: Callable[[dict[str, Any]], None],
        default_mode: str = "page",
    ) -> None:
        """Process incoming WebView2 bridge payload and send responses via `send_fn`."""
        try:
            msg = json.loads(raw_data) if isinstance(raw_data, str) else raw_data
        except Exception as exc:
            send_fn(
                {
                    "type": "action_result",
                    "ok": False,
                    "action": "parse_error",
                    "message": f"Invalid JSON message: {exc}",
                    "paths": [],
                }
            )
            return

        if not isinstance(msg, dict):
            return

        msg_type = str(msg.get("type") or "").strip()

        try:
            if msg_type == "set_language":
                language = normalize_language(msg.get("lang"))
                origin_mode = "dock" if str(msg.get("mode") or default_mode) == "dock" else "page"
                request_id = int(msg.get("request_id") or 0)
                with self._lock:
                    if request_id > 0 and request_id < self._last_language_requests.get(origin_mode, 0):
                        return
                    if request_id > 0:
                        self._last_language_requests[origin_mode] = request_id
                    self._language_revision += 1
                    revision = self._language_revision
                    self._manual_language = language
                    self._language_loaded = True
                    target = _resolve_storage_dir() / "ui_preferences.json"
                    target.parent.mkdir(parents=True, exist_ok=True)
                    temporary = target.with_suffix(".tmp")
                    temporary.write_text(json.dumps({"language": language}), encoding="utf8")
                    temporary.replace(target)
                    callbacks = list(self._listeners.values())
                if send_fn not in callbacks:
                    callbacks.append(send_fn)
                for callback in callbacks:
                    try:
                        callback({"type":"preferences_updated", "lang":language, "language_revision":revision, "request_id":request_id, "source_mode":origin_mode})
                    except Exception:
                        pass
                return

            if msg_type == "ready":
                mode = str(msg.get("mode") or default_mode)
                with self._lock:
                    view_mode = "dock" if mode == "dock" else "page"
                    self._listeners[view_mode] = send_fn
                    self._last_language_requests.pop(view_mode, None)
                init_ctx = self.build_initial_context(mode=mode)
                host_ctx = self.read_host_context()
                params = init_ctx["params"]
                vase_mesh = generate_vase_mesh(params, layer_height_mm=host_ctx["layer_height_mm"])
                report = analyze_printability(vase_mesh, params, host_context=host_ctx)

                send_fn({"type": "init_state", **init_ctx})
                send_fn({"type": "analysis_result", "report": report})
                return

            if msg_type == "sync_printer":
                host_ctx = self.read_host_context()
                printer_info = self.build_printer_payload(host_ctx)
                send_fn(
                    {
                        "type": "printer_updated",
                        "printer": printer_info,
                        "lang": host_ctx["lang"],
                        "theme": host_ctx["theme"],
                        "theme_explicit": bool(host_ctx.get("theme_explicit", False)),
                    }
                )
                raw_params = msg.get("params")
                if isinstance(raw_params, dict):
                    params = self.set_current_params(raw_params)
                    vase_mesh = generate_vase_mesh(params, layer_height_mm=host_ctx["layer_height_mm"])
                    report = analyze_printability(vase_mesh, params, host_context=host_ctx)
                    send_fn({"type": "analysis_result", "report": report})
                return

            if msg_type == "analyze":
                params = self.set_current_params(msg.get("params") or self.current_params)
                host_ctx = self.read_host_context()
                vase_mesh = generate_vase_mesh(params, layer_height_mm=host_ctx["layer_height_mm"])
                report = analyze_printability(vase_mesh, params, host_context=host_ctx)
                send_fn({"type": "analysis_result", "report": report})
                return

            if msg_type == "randomize":
                raw_seed = msg.get("seed")
                seed_val: int | None = None
                if raw_seed is not None and raw_seed != "":
                    try:
                        seed_val = int(raw_seed)
                    except (TypeError, ValueError):
                        seed_val = None
                base_params = normalize_params(msg.get("params") or self.current_params)
                randomized = generate_random_printable_params(seed=seed_val, current_params=base_params)
                params = self.set_current_params(randomized)
                send_fn(
                    {
                        "type": "params_updated",
                        "params": params,
                        "source": "randomize",
                    }
                )
                return

            if msg_type == "preset_save":
                params = self.set_current_params(msg.get("params") or self.current_params)
                preset_name = str(msg.get("name") or params.get("name") or "Meu Vaso").strip() or "Meu Vaso"
                preset_id = msg.get("id") or msg.get("preset_id")
                preset_id_str = str(preset_id).strip() if preset_id else None
                user_presets = save_user_preset(
                    self.get_presets_dir(),
                    name=preset_name,
                    params=params,
                    preset_id=preset_id_str,
                )
                send_fn(
                    {
                        "type": "presets_updated",
                        "user_presets": user_presets,
                    }
                )
                return

            if msg_type == "preset_delete":
                preset_id = str(msg.get("id") or msg.get("preset_id") or "").strip()
                user_presets = delete_user_preset(self.get_presets_dir(), preset_id=preset_id)
                send_fn(
                    {
                        "type": "presets_updated",
                        "user_presets": user_presets,
                    }
                )
                return

            if msg_type == "export_file":
                params = self.set_current_params(msg.get("params") or self.current_params)
                fmt = str(msg.get("format") or "3mf").strip().lower().lstrip(".")
                if fmt not in ("3mf", "stl"):
                    fmt = "3mf"
                include_saucer = bool(msg.get("include_saucer", False))

                host_ctx = self.read_host_context()
                lang = host_ctx["lang"]
                export_dir = self.get_export_dir()

                effective_params = self._prepare_effective_vase_params(
                    params,
                    is_stl_export=(fmt == "stl"),
                    include_saucer=include_saucer,
                )
                vase_mesh = generate_vase_mesh(
                    effective_params,
                    layer_height_mm=host_ctx["layer_height_mm"],
                )
                report = analyze_printability(vase_mesh, effective_params, host_context=host_ctx)

                raw_filename = str(msg.get("filename") or "").strip()
                if raw_filename:
                    base_stem = _slugify_filename(Path(raw_filename).stem, fallback="vaso")
                else:
                    base_stem = _slugify_filename(params.get("name", "vaso"), fallback="vaso")

                paths: list[str] = []
                if fmt == "3mf":
                    target_3mf = export_dir / f"{base_stem}.3mf"
                    host_cfg = self.read_full_host_config_snapshot(host_ctx)
                    cx = host_ctx["bed_x"] / 2.0
                    cy = host_ctx["bed_y"] / 2.0

                    vase_label = str(params.get("name") or translate_text("Vase", lang))

                    if include_saucer:
                        saucer_mesh = generate_saucer_mesh(effective_params)
                        vase_rx = float(vase_mesh.bounds_mm["size"][0]) / 2.0
                        saucer_rx = float(saucer_mesh.bounds_mm["size"][0]) / 2.0
                        gap_mm = 10.0
                        total_w = 2.0 * vase_rx + gap_mm + 2.0 * saucer_rx
                        vase_pos = (round(cx - total_w / 2.0 + vase_rx, 2), round(cy, 2), 0.0)
                        saucer_pos = (round(cx + total_w / 2.0 - saucer_rx, 2), round(cy, 2), 0.0)
                        saucer_label = translate_text("Saucer", lang)
                        items = [
                            (vase_label, vase_mesh, vase_pos),
                            (saucer_label, saucer_mesh, saucer_pos),
                        ]
                    else:
                        items = [(vase_label, vase_mesh, (round(cx, 2), round(cy, 2), 0.0))]

                    written_3mf = Path(
                        write_orca_3mf(target_3mf, items, effective_params, host_config=host_cfg)
                    )
                    paths.append(str(written_3mf))
                else:
                    vase_stl = self._write_stl_resilient(
                        export_dir,
                        base_stem,
                        vase_mesh,
                        header=f"OrcaVaseStudio:{base_stem}",
                    )
                    paths.append(str(vase_stl))
                    if include_saucer:
                        saucer_mesh = generate_saucer_mesh(effective_params)
                        saucer_suffix = "prato" if lang == "pt" else "saucer"
                        saucer_stl = self._write_stl_resilient(
                            export_dir,
                            f"{base_stem}_{saucer_suffix}",
                            saucer_mesh,
                            header=f"OrcaVaseStudio:{base_stem}_{saucer_suffix}",
                        )
                        paths.append(str(saucer_stl))

                open_mouth_note = ""
                if (
                    fmt == "stl"
                    and params.get("print_mode") == "spiral_vase"
                    and effective_params.get("print_mode") == "shelled_hollow"
                ):
                    open_mouth_note = translate_text(" (open-mouthed {mm} mm shell)", lang).replace("{mm}", f"{effective_params['wall_thickness_mm']:.1f}")

                ok_msg = translate_text("Exported successfully: {name}", lang).replace("{name}", Path(paths[0]).name) + open_mouth_note
                send_fn(
                    {
                        "type": "action_result",
                        "ok": True,
                        "action": "export_file",
                        "format": fmt,
                        "path": paths[0],
                        "paths": paths,
                        "message": ok_msg,
                        "report": report,
                    }
                )
                return

            if msg_type == "send_to_plater":
                params = self.set_current_params(msg.get("params") or self.current_params)
                include_saucer = bool(msg.get("include_saucer", False))
                auto_cfg = bool(params.get("auto_configure_slicer", True))

                host_ctx = self.read_host_context()
                lang = host_ctx["lang"]
                export_dir = self.get_export_dir()

                effective_params = self._prepare_effective_vase_params(
                    params,
                    is_stl_export=False,
                    include_saucer=include_saucer,
                )
                vase_mesh = generate_vase_mesh(
                    effective_params,
                    layer_height_mm=host_ctx["layer_height_mm"],
                )
                report = analyze_printability(vase_mesh, effective_params, host_context=host_ctx)

                base_stem = _slugify_filename(params.get("name", "vaso"), fallback="vaso")
                vase_stl = self._write_stl_resilient(
                    export_dir,
                    f"{base_stem}_plater",
                    vase_mesh,
                    header=f"OrcaVaseStudio:{base_stem}",
                )
                stl_paths = [str(vase_stl)]

                if include_saucer:
                    saucer_mesh = generate_saucer_mesh(effective_params)
                    saucer_suffix = "prato" if lang == "pt" else "saucer"
                    saucer_stl = self._write_stl_resilient(
                        export_dir,
                        f"{base_stem}_{saucer_suffix}_plater",
                        saucer_mesh,
                        header=f"OrcaVaseStudio:{base_stem}_{saucer_suffix}",
                    )
                    stl_paths.append(str(saucer_stl))

                copydata_payload = _format_other_instance_payload(stl_paths)
                updates: dict[str, str] = {}
                if auto_cfg:
                    updates = self._compute_process_preset_updates(
                        params=effective_params,
                        host_ctx=host_ctx,
                        include_saucer=include_saucer,
                    )

                native_host = _is_native_orca_host()
                copydata_delay = 0.06 if native_host else 0.01
                preset_delay = 0.45 if native_host else 0.01
                dispatch_outcome: dict[str, Any] = {
                    "ipc_ok": False,
                    "ipc_message": "",
                    "hwnd": None,
                    "thread_id": None,
                    "preset_applied": False,
                    "preset_error": None,
                }
                self._last_plater_outcome = dispatch_outcome

                def _plater_bg_worker() -> None:
                    dispatch_outcome["thread_id"] = threading.get_ident()
                    if copydata_delay > 0.0:
                        time.sleep(copydata_delay)

                    hwnd = _find_orca_mainframe_hwnd()
                    dispatch_outcome["hwnd"] = hwnd
                    ipc_ok, ipc_msg = _dispatch_copydata_to_hwnd(hwnd or 0, copydata_payload)
                    if not ipc_ok and sys.platform != "win32":
                        ipc_ok, ipc_msg = _dispatch_non_win32_plater_open(stl_paths)
                    dispatch_outcome["ipc_ok"] = ipc_ok
                    dispatch_outcome["ipc_message"] = ipc_msg

                    if auto_cfg and updates:
                        if preset_delay > 0.0:
                            time.sleep(preset_delay)
                        preset_res = self._apply_process_presets(updates)
                        dispatch_outcome["preset_applied"] = bool(preset_res.get("applied", False))
                        dispatch_outcome["preset_error"] = preset_res.get("error")

                worker = threading.Thread(
                    target=_plater_bg_worker,
                    name="OrcaVaseStudio-PlaterDispatch",
                    daemon=True,
                )
                self._last_plater_worker = worker
                worker.start()

                if not native_host:
                    # Safe to join in standalone/test harness; NEVER join on native wxWidgets UI thread!
                    worker.join(timeout=4.0)
                    slicer_configured = bool(dispatch_outcome.get("preset_applied", False))
                else:
                    process_ed = getattr(
                        getattr(getattr(orca, "host", None), "preset", None),
                        "process",
                        None,
                    )
                    slicer_configured = bool(auto_cfg and hasattr(process_ed, "begin_update"))

                saucer_spiral_note = ""
                if include_saucer and params.get("print_mode") == "spiral_vase":
                    saucer_spiral_note = translate_text(" (Converted to open hollow shell to slice vase + saucer together.)", lang)

                msg_text = translate_text("Sent to OrcaSlicer Plater ({n} object(s)).", lang).replace("{n}", str(len(stl_paths))) + saucer_spiral_note
                self._notify_host_toast(msg_text)

                send_fn(
                    {
                        "type": "action_result",
                        "ok": True,
                        "action": "send_to_plater",
                        "path": stl_paths[0],
                        "paths": stl_paths,
                        "message": msg_text,
                        "report": report,
                        "slicer_configured": slicer_configured,
                    }
                )
                return

            if msg_type == "open_exports_folder":
                export_dir = self.get_export_dir()
                lang = self.read_host_context()["lang"]
                startfile_fn = getattr(os, "startfile", None)
                if callable(startfile_fn) and (_is_native_orca_host() or _is_mock_callable(startfile_fn)):
                    try:
                        startfile_fn(str(export_dir))
                    except Exception:
                        pass
                elif sys.platform != "win32" and _is_native_orca_host():
                    try:
                        import subprocess

                        opener = "open" if sys.platform == "darwin" else "xdg-open"
                        subprocess.Popen(
                            [opener, str(export_dir)],
                            stdout=subprocess.DEVNULL,
                            stderr=subprocess.DEVNULL,
                        )
                    except Exception:
                        pass

                msg_text = translate_text("Exports folder: {path}", lang).replace("{path}", str(export_dir))
                send_fn(
                    {
                        "type": "action_result",
                        "ok": True,
                        "action": "open_exports_folder",
                        "path": str(export_dir),
                        "paths": [str(export_dir)],
                        "message": msg_text,
                    }
                )
                return

            send_fn(
                {
                    "type": "action_result",
                    "ok": False,
                    "action": msg_type or "unknown",
                    "message": f"Unsupported message type: {msg_type!r}",
                    "paths": [],
                }
            )
        except Exception as exc:
            send_fn(
                {
                    "type": "action_result",
                    "ok": False,
                    "action": msg_type or "error",
                    "message": str(exc),
                    "paths": [],
                }
            )


_SHARED_CONTROLLER = VaseStudioController()

_SYNC_LIFECYCLE_EVENT_NAMES: frozenset[str] = frozenset(
    {"PresetSelected", "PresetSaved", "NewProject", "ProjectOpened"}
)
_VALID_DOCK_SIDES: frozenset[str] = frozenset({"left", "right", "bottom", "float"})


def _is_sync_lifecycle_event(event: Any) -> bool:
    """Match `orca.LifecycleEvent` enum values or names for preset/project changes."""
    ev_cls = getattr(orca, "LifecycleEvent", None)
    if ev_cls is not None:
        for nm in _SYNC_LIFECYCLE_EVENT_NAMES:
            cand = getattr(ev_cls, nm, None)
            if cand is not None and event == cand:
                return True
    ev_name = str(getattr(event, "name", event) or "")
    return any(k in ev_name for k in _SYNC_LIFECYCLE_EVENT_NAMES)


def _read_capability_config(cap: Any) -> dict[str, Any]:
    """Read `PythonPluginBase.get_config()` JSON string merged over `get_default_config()`."""
    defaults: dict[str, Any] = {}
    def_fn = getattr(cap, "get_default_config", None)
    if callable(def_fn):
        try:
            got_def = def_fn()
            if isinstance(got_def, dict):
                defaults = dict(got_def)
        except Exception:
            defaults = {}

    get_fn = getattr(cap, "get_config", None)
    if not callable(get_fn):
        return defaults
    try:
        raw = get_fn()
        if isinstance(raw, str) and raw.strip():
            parsed = json.loads(raw)
            if isinstance(parsed, dict):
                merged = dict(defaults)
                merged.update(parsed)
                return merged
        elif isinstance(raw, dict):
            merged = dict(defaults)
            merged.update(raw)
            return merged
    except Exception:
        pass
    return defaults


def _apply_capability_config_to_controller(
    controller: VaseStudioController,
    cfg: dict[str, Any],
) -> None:
    """Apply user-saved capability configuration overrides onto controller parameters."""
    if not cfg:
        return
    updates: dict[str, Any] = {}
    mode_val = cfg.get("default_print_mode")
    if mode_val in ("shelled_hollow", "spiral_vase"):
        updates["print_mode"] = mode_val
    if isinstance(cfg.get("auto_configure_slicer"), bool):
        updates["auto_configure_slicer"] = cfg["auto_configure_slicer"]
    if isinstance(cfg.get("stl_always_open_hollow"), bool):
        updates["stl_always_open_hollow"] = cfg["stl_always_open_hollow"]
    if updates:
        cur = controller.current_params
        cur.update(updates)
        controller.set_current_params(cur)


# ---------------------------------------------------------------------------
# OrcaSlicer Plugin Capabilities (Top-Bar Page + Docked Side Panel)
# ---------------------------------------------------------------------------


class VaseStudioPageCapability(orca.pages.PagesPluginCapabilityBase):
    """Full-screen top-bar tab (`Vase Studio`) beside Prepare / Preview / Device."""

    def __init__(self, controller: VaseStudioController | None = None) -> None:
        super().__init__()
        self._controller = controller or _SHARED_CONTROLLER

    def get_name(self) -> str:
        return "Vase Studio"

    def get_default_config(self) -> dict[str, Any]:
        return {
            "default_print_mode": "shelled_hollow",
            "auto_configure_slicer": True,
            "stl_always_open_hollow": True,
        }

    def on_load(self) -> None:
        _apply_capability_config_to_controller(
            self._controller,
            _read_capability_config(self),
        )

    def on_unload(self) -> None:
        with self._controller._lock:
            self._controller._listeners.pop("page", None)

    def get_icon(self) -> str:
        storage_dir = _resolve_storage_dir(in_callback=True)
        existing_candidates: list[Path] = []
        try:
            existing_candidates.append(Path(__file__).resolve().parent / "icon.svg")
        except Exception:
            pass
        existing_candidates.extend(
            [
                storage_dir / "icon.svg",
                _default_installed_plugin_dir() / "icon.svg",
            ]
        )
        for cand in existing_candidates:
            try:
                if cand.is_file() and cand.stat().st_size > 0:
                    return str(cand)
            except Exception:
                continue

        # Auto-materialize embedded `icon.svg` when user side-loaded only `orca_vase_generator.py`
        write_targets: list[Path] = [
            storage_dir / "icon.svg",
            _default_plugin_data_dir() / "icon.svg",
        ]
        try:
            write_targets.append(Path(__file__).resolve().parent / "icon.svg")
        except Exception:
            pass
        write_targets.append(Path.home() / "Documents" / "OrcaVaseStudio" / "icon.svg")

        seen_dirs: set[str] = set()
        for target in write_targets:
            key = str(target)
            if key in seen_dirs:
                continue
            seen_dirs.add(key)
            try:
                target.parent.mkdir(parents=True, exist_ok=True)
                with open(target, "w", encoding="utf-8", newline="\n") as fh:
                    fh.write(ICON_SVG_CONTENT)
                if target.is_file() and target.stat().st_size > 0:
                    return str(target)
            except Exception:
                continue
        return ""

    def get_ui(self) -> str:
        initial_ctx = self._controller.build_initial_context(mode="page")
        return get_studio_html(mode="page", initial_context=initial_ctx)

    def post_message(self, data: Any) -> None:
        super_post = getattr(super(), "post_message", None)
        if callable(super_post):
            super_post(data)

    def on_message(self, data: Any) -> None:
        self._controller.handle_message(
            raw_data=data,
            send_fn=self.post_message,
            default_mode="page",
        )

    def on_lifecycle_event(self, event: Any, ctx: Any = None) -> None:
        """Push live `printer_updated` + `analysis_result` whenever OrcaSlicer switches presets or projects."""
        if not _is_sync_lifecycle_event(event):
            return
        try:
            host_ctx = self._controller.read_host_context()
            printer_info = self._controller.build_printer_payload(host_ctx)
            self.post_message(
                {
                    "type": "printer_updated",
                    "printer": printer_info,
                    "lang": host_ctx["lang"],
                    "theme": host_ctx["theme"],
                    "theme_explicit": bool(host_ctx.get("theme_explicit", False)),
                }
            )
            params = self._controller.current_params
            vase_mesh = generate_vase_mesh(params, layer_height_mm=host_ctx["layer_height_mm"])
            report = analyze_printability(vase_mesh, params, host_context=host_ctx)
            self.post_message({"type": "analysis_result", "report": report})
        except Exception:
            pass


class VaseStudioDockCapability(orca.script.ScriptPluginCapabilityBase):
    """Opens/shows a docked right-hand Vase Studio panel directly beside the 3D Plater."""

    _active_panel: Any = None
    _panel_lock = threading.RLock()

    def __init__(self, controller: VaseStudioController | None = None) -> None:
        super().__init__()
        self._controller = controller or _SHARED_CONTROLLER

    def get_name(self) -> str:
        return "Orca Vase Studio - Painel Lateral"

    def get_default_config(self) -> dict[str, Any]:
        return {
            "dock": "right",
            "width": 420,
            "height": 780,
            "auto_configure_slicer": True,
            "stl_always_open_hollow": True,
        }

    def on_load(self) -> None:
        _apply_capability_config_to_controller(
            self._controller,
            _read_capability_config(self),
        )

    def on_unload(self) -> None:
        with self._controller._lock:
            self._controller._listeners.pop("dock", None)
        with self._panel_lock:
            VaseStudioDockCapability._active_panel = None

    def get_ui(self) -> str:
        initial_ctx = self._controller.build_initial_context(mode="dock")
        return get_studio_html(mode="dock", initial_context=initial_ctx)

    def _post_to_panel(self, payload: dict[str, Any]) -> None:
        with self._panel_lock:
            panel = VaseStudioDockCapability._active_panel
        if panel is None:
            return
        try:
            is_open_fn = getattr(panel, "is_open", None)
            if callable(is_open_fn) and not is_open_fn():
                return
            post_fn = getattr(panel, "post", None)
            if callable(post_fn):
                post_fn(payload)
        except Exception:
            pass

    def _on_panel_message(self, data: Any) -> None:
        self._controller.handle_message(
            raw_data=data,
            send_fn=self._post_to_panel,
            default_mode="dock",
        )

    def _on_panel_close(self) -> None:
        with self._controller._lock:
            self._controller._listeners.pop("dock", None)
        with self._panel_lock:
            VaseStudioDockCapability._active_panel = None

    def on_message(self, data: Any) -> None:
        """Direct message entry point for testing or programmatic invocation."""
        self._on_panel_message(data)

    def on_lifecycle_event(self, event: Any, ctx: Any = None) -> None:
        """Keep any open docked side panel synced when OrcaSlicer switches presets or projects."""
        if not _is_sync_lifecycle_event(event):
            return
        with self._panel_lock:
            panel = VaseStudioDockCapability._active_panel
        if panel is None:
            return
        try:
            host_ctx = self._controller.read_host_context()
            printer_info = self._controller.build_printer_payload(host_ctx)
            self._post_to_panel(
                {
                    "type": "printer_updated",
                    "printer": printer_info,
                    "lang": host_ctx["lang"],
                    "theme": host_ctx["theme"],
                    "theme_explicit": bool(host_ctx.get("theme_explicit", False)),
                }
            )
            params = self._controller.current_params
            vase_mesh = generate_vase_mesh(params, layer_height_mm=host_ctx["layer_height_mm"])
            report = analyze_printability(vase_mesh, params, host_context=host_ctx)
            self._post_to_panel({"type": "analysis_result", "report": report})
        except Exception:
            pass

    def execute(self) -> Any:
        """Open or focus the docked Vase Studio panel beside the 3D Plater.

        Safe whether invoked on the main/UI thread (documented Wiki contract) or on
        `ScriptAsyncRuntime`'s background worker (`OrcaSlicer.dll` v2.5.1), as
        `orca.host.ui.create_dock_panel` marshals panel creation onto the UI thread.
        """
        cfg = _read_capability_config(self)
        _apply_capability_config_to_controller(self._controller, cfg)
        dock_side = str(cfg.get("dock") or "right").strip().lower()
        if dock_side not in _VALID_DOCK_SIDES:
            dock_side = "right"
        dock_w = max(280, min(960, int(_extract_first_float(cfg.get("width"), 420.0))))
        dock_h = max(360, min(1600, int(_extract_first_float(cfg.get("height"), 780.0))))

        with self._panel_lock:
            existing = VaseStudioDockCapability._active_panel

        if existing is not None:
            try:
                is_open_fn = getattr(existing, "is_open", None)
                if not callable(is_open_fn) or is_open_fn():
                    show_fn = getattr(existing, "show", None)
                    if callable(show_fn):
                        show_fn()
                    init_ctx = self._controller.build_initial_context(mode="dock")
                    self._post_to_panel({"type": "init_state", **init_ctx})
                    return _make_execution_result_success("Painel lateral Orca Vase Studio exibido.")
            except Exception:
                with self._panel_lock:
                    VaseStudioDockCapability._active_panel = None

        html = self.get_ui()
        host = getattr(orca, "host", None)
        ui = getattr(host, "ui", None) if host is not None else None
        create_dock_fn = getattr(ui, "create_dock_panel", None) if ui is not None else None

        if callable(create_dock_fn):
            panel = create_dock_fn(
                html,
                title="Orca Vase Studio",
                width=dock_w,
                height=dock_h,
                on_message=self._on_panel_message,
                on_close=self._on_panel_close,
                dock=dock_side,
            )
            with self._panel_lock:
                VaseStudioDockCapability._active_panel = panel
            if panel is not None:
                show_fn = getattr(panel, "show", None)
                if callable(show_fn):
                    try:
                        show_fn()
                    except Exception:
                        pass
            return _make_execution_result_success("Painel lateral Orca Vase Studio aberto.")

        # Fallback if `create_dock_panel` is unavailable in an older/mocked environment
        create_win_fn = getattr(ui, "create_window", None) if ui is not None else None
        if callable(create_win_fn):
            panel = create_win_fn(
                html,
                title="Orca Vase Studio",
                width=max(440, dock_w),
                height=max(800, dock_h),
                on_message=self._on_panel_message,
                on_close=self._on_panel_close,
            )
            with self._panel_lock:
                VaseStudioDockCapability._active_panel = panel
            return _make_execution_result_success("Janela Orca Vase Studio aberta.")

        return _make_execution_result_success("Orca Vase Studio pronto.")


# ---------------------------------------------------------------------------
# Single `@orca.plugin` Entry Point Class
# ---------------------------------------------------------------------------


@orca.plugin
class OrcaVaseStudioPlugin(orca.base):
    """OrcaSlicer 2.5.1+ Native Plugin Entry Point for Orca Vase Studio."""

    def __init__(self) -> None:
        super().__init__()

    def register_capabilities(self) -> None:
        plugin_dir = _default_installed_plugin_dir()
        plugin_data_dir = _default_plugin_data_dir()
        docs_dir = Path.home() / "Documents" / "OrcaVaseStudio"

        candidate_dirs: list[Path] = [
            plugin_dir,
            plugin_data_dir,
            docs_dir,
        ]
        for extra_fn in (
            lambda: Path(__file__).resolve().parent,
            lambda: _resolve_storage_dir(in_callback=False),
        ):
            try:
                extra_dir = extra_fn()
                if str(extra_dir).strip():
                    candidate_dirs.append(extra_dir)
            except Exception:
                continue

        fs_targets: list[str] = []
        for d in candidate_dirs:
            d_str = str(d).strip()
            if not d_str:
                continue
            cand = f"{d_str}/*"
            if cand not in fs_targets:
                fs_targets.append(cand)

        req_fn = getattr(orca, "request_permissions", None)
        if callable(req_fn):
            req_fn(
                fs_read=list(fs_targets),
                fs_readwrite=list(fs_targets),
                threading=True,
            )

        orca.register_capability(VaseStudioPageCapability)
        orca.register_capability(VaseStudioDockCapability)
