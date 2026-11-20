# /// script
# requires-python = ">=3.12"
# dependencies = ["numpy>=1.26"]
#
# [tool.orcaslicer.plugin]
# id = "orca-vase-studio"
# name = "Orca Vase Studio"
# description = "Parametric 3D Vase & Planter Studio with X-Ray Wall Calipers & 1-Click Plater | Estudio 3D de Vasos e Cachepos"
# author = "Orca Vase Studio"
# version = "1.3.0"
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

_BUNDLED_LANGUAGE_PACKS = json.loads(zlib.decompress(base64.b85decode('c-qZ<>ys2ky7#|Q5^;_Y%Z$73+4ln{&WRXixE;Ce4C=05-l*=*?k=gW>aEMbj6no5;{{a2^@8FJQC1jO6c-jzQ6skF{YQ4_8RpZTKjD2YnN?X;S=Bu-jYcTbm6g{gGoM@LubvmSbfYahUf2@W+oEIt-&qlaj_+;R@tf^i>V89P*@5r3Z}IHNnHB%nvpbk{*bkz(75A=&@T%biq8?G9Ep8M*iXSvYuw}=uw{M98+Y4PA--g)AOdNCrCluBJtcIS1@EZ0QRJ(o4Oxx~a`ffky*zkNr9FO8aKuP)2#`d1IUDx_|>u}(B(DN<(I#5R#_CELF-C_7CA}pYOsWfX36cfQ5yn<gMaBQmq-GCvwKIZzBHDk|W<M_j!wQ(FWC3&83UF?eApc03ImhCxpNP%Cy&)_E|?-71SL;=0P-@RpgpjU@o+lzp}@Mh8mdUt!bLfK3M(hi829v!#s$0CXZjPl7TYcdYF8;}mkHl$*b4ev0w>omAZ^=tc<-9XeP&`>YUMfN+hfyflJ{`vA-X%o3LoP?>sZdq;HYq%n`c&^<!%lE9PjWt<e+Fd`envN&NqSzBwDC?>Lfsc(t<r4wSALOz_%XWL0;g4riX&MyN<j0o%e2iKA(5m}h6!_StU9+9z{<!MOQO}P;>mT1(lde-gYSpppR^(fDqe1WR)s!FCTrpP198UyJs~z!g%R%}(&`-(<r2^6MXNBIqE;Q_`2L2Qa>}8#Z*L?ySaq6&^?SNW|yRMHFL#`)kegsR92;@M$ke90tu;T|r*tVuc=)1ApDE!d7Ol55AfbF(zT2pn~+SL((?KUi!@S`{>0y69hInlN-3+)Z)Z{3f8bd#=)%X(4-z0W!hRG{8rz5_PS%(HC={)HTNhZZJm;JSd-Xj?mBht{zJ5$?cAzuOf7B>LVwE(rc%P5L!hHoL;QKWjH|pZ)KJcm8VqVQku-v!1YMLvB4nTRpA|FWLqrDaW+!_+x*7EQjqtz;=_Fdf(NZhQAHR3j~6-)w1>qJL=e7YwJI5VCe&Pm-c7!p3)8Nmb64!-#%+~I@YA^I$ho&lr#x+3E>6T_Lrmyu1R~|zU7~<zh^xQ6WR=z?cuYUssFuj<_F*uFy4Sl!qedZ7@gNf`WzInlyFb)0^&NynP@YxA;xNRWB3<d?T1tgwj{qKc4pTc*NNtceW}NWO~WA~KVj{5eIFZ?1cijyqw>A?ftkfo+uG>|SUWuLjsqVaX}L@}9pNEo53Q}84w9HtdVd!(1((Wkof--45A-e`hu6EpXx!TExIhbHyy~ZK;Tv3%z*N1K%ltZUfF-tKX0C@~*mi2Zb{&TY4?8t!&%$VdpQ%w{0*)7x<hXXj3Z&KoXbK5&#P1Rl?&8~>umSuIE>t_jm%E+Fdd3mQi1L4m?M6V1`=1{zT9bhvhGR1<s(`y;rIZe`OjxuqQTW-e%>RrCBG^nWX0^5+4*aI$3hR&CGR2ZiTMvr>GT?h$8*lw&?ezm^9{LV1pR<6m)?xXh0I+`dZ~r{`_HTau>wn{I0$F#%y0NnbC@bu3Ei=r3Hw(<Pi{#nk`ZdUS<d_piG}z?L5kFwI!dYljcWRDj14pzB64m0@y^FKL!MU1tYBkZIr55uVp0qvS6|h(#4TQHY{9sOJskTEP#6wF7LYuQVEnqj+lw)^%uR(G$O|f}4Cxz?AF7VSQkfJc6-%b%LD<opa8ZGD;r#vGZ)F`&VUtrb(wmI|+=(UwzZ%fsLLtWuH$Uu12%YF0j)<g}a4#uw*|B(P#{a)V%VP!o7iwV<d#bPN)@U262A9y&;HCF<ya@m=#gMC6}!rJ;95VD>iCI*TE><xa&>1}%(=@G~5xzIW)MAw2z^Q;c-Tv(RlGe`DY;&>Mp7jZ!pS5^(SFi1h@FZ}W4YoHEh&b3~P9k&4@(*o(@G^`p9q~`h{`Hr>y5andoazZJZ;Qbs)@eo&MU~L`$?Sb9f#;vEYUzi^GE!fU1!7b2N>PMjrP(tfvXaUvdXcUj(3|pB&w?N=nafiC#b8qVL^FDUNw|dLm4-f@b7n-n|xD6V9+7Y0$ogJ<f3RL%)8vb^RmJv`DM%)ejNbt&Mjln{d)qX5Xp&doafTm<&gVt6_2c}Mlz1)U!o*Jg=>#!lLV^7ecVs@LG<{i)@kPlov=m1=AGBB>$VglsqZXq4&PY}cA)oIfz4siMIux6;+awI#c<NrMQ4wpaXz*1*AS(Ez@&Fq?jvC~}R*kl=GK~NLU(ge_qD7AxXO6RL%*PY&FpK6xV9NJFMy9nx7M|RuVy=!vs#MB|Hi?c&RQ&NB`L4yDD^eO8F?}P<xy&GD7(|W-@b^?Vlj2PvU1=8sSr-4bxPG#;{-$l_3%UH`!LQKmpEAMnDLlXsuwUyek=f;Vo2mSeZShX*B{`?8ZvK6E)4DE$u9mhKX%oKju$4^+y4)nU9-6jehuC8u(xVoL7ybn{^_AQcoK$#bg$)O?7NS~9HsAo~M*R#QRNo4M@UYM2HAc+O1pCnQ~Bxg1oQcTN(JWR{LysP9r3|$ROBT}}ADUTAwT011awPr}rDM9#O)(i8pu5LX#k(Y$e88S$Qo*PG6KX)M4et}X2LZvz6)J&ohO8f_9q}}P-DGTRh;NNisdcW^AofZgF(#U6+bpQ(w1<5+fL*@*yE-eQ#aBtRO`?BNv!1ra#fB2&{BkT^@#h?exL%B&mBpIc8@P|LD)<Ng*bW`<s28BQBlupN?2GtA9+_6zd=}7%)j}6v2^AxbBKrd*aI7~Fz|AE((*unRLev!3pN2$V<mfY*JzK67=t(%lV+k%y{nT`#NspdLf1GW{Yd=4_#cHqaYwqnOzE$m@X!FB+jguymc8*MTJk2w+8nNSbBJc<%MbWqvEd5HWtVRI<EAJbGxup~u`Y|Rk&w2f*?*t>~(b%>T1a_Swh@v-|*GYCfzF&0>KHBcRa<x%yp>#W{)XyIG1sC0(^7%j{Q)j+T^t@<2}G9Z;O=|7mmpg^IdgcQuB#*Q+!%}k>U<|r{UG)0d<TcC_tb;s>pr|O_{Hk1ab6xz71eaWhjdBY&OAoy(J(JX$R90S4VG<`54!4R=Q6BekT@AK+zj9w2rs<)AZ$*j{GCrC^fSb6Bg@z^#Yedt#*H);g}dJaoDSzE3<XN539^)}knBpoF)B+FOsiYHh^jVp!fSG=mM=VP+Cfzq&QBcQ&WU9>D|5*>_WqmS#WBSKqNYLh%0XM-2IL0y*GF1DYHbXs&p1S6H|FU}{`3^T0O_zd)w#*yw?(8ePwzKixQ_sGW4Q4MKM)Y4fHBeNiDN2xFPoW4cfO@AwOIpzqHPEdErYXd(}6NXnHl*aau?*PRUT8$y6T6P_MbMgf#JzGOE7mnA30Bx`vIIKsaa)?qk?tq^9Lhbm8-g__9=ICGIw%Z<~F4d8-`YIzVFNa-hK5EP6Vr+RuK6~YeQWKK*^*$vsp{`FZ7|0aPd3D)qoygs!tn|DPm0_FL!3HFLsC9(KS)lz4)C?+`tXozHQV9K)C!q5UrxTvomU<1-n$l((cCkRlfNnYw>Vc83vgw3<ENfb`1VCP6rxX>kAkyvd^uB{fCU)-Mg)-^wBl`{<LXI*qeQ@8wJxIkPyAJkV=`CUE<n+EH`z9xF-AqpR&cN?O<Ztvq%f=3M*=GQ{&n&Kf;C)VuwDN=gtdD6v5zy)Mu7kBm%6Y?oEcK9v=!bkP@twl6JL?ly31Ra9u^uC1l6Pq%aq!`+Pww4!*h<`v<W3|e%$Z5U$GOy<kW}U|GU(Cd-7Ana;)q?^mz0VE2Zw?Nqu`}6<@7#7|0?l4DPVRAWI*Oj=mB}&Pcm^c)-<}L)5g+V&w>PqO52+R0z>{JUrB9x#)Durm3Hm02<tv5-0ao>!gRsvw#k2!*rzy5;KjDgGwpP&odV_$$qORB8Te1A_lJFVu7%9bLAkf}*Z;+QWSew0h18@EG6gdE>issY;It1?#e=C<N(eb)u;iqTJQ}qRbn3uXEcIr}3@A2~bEGt{%8@D-ie>M%8zR+&ICrX1AR#Jq`j&JMNk7S6;ZjeOza(*z&<h{N>9Xs?ni5^I>d@f>#84Dq&xg!231o__ty9PlqB$h*?_;13=jCMlxlLw&)@cAwf5MuIqd9AGjyd~&J80qb&W5N;K)>0F!W{;?FS2IZcF>hmaS&9dhM1>?MQ#pRap|aV#u8VJnz6%eBp#@0xTDfpLJv+d>WNO*bt2Re(9`VEs!FC2bGpK7QO-%9SP5Bv+BB-h_WL!`3-|YK*3b!vllKhTcf>+sWXogJ@&V^K=^v2L6hZH*S9frfG4f&6yP2cp(VGZEhmKZkt#_0mGqm*GZo3X_OpR?CIzP*_Q4Xk3dZ0pUBEY4O<LWJ=?<q{(apV<Ch;YPVU-ASr0TZRhPMKilumk$kJp*C|8}w^|l-Sdt70pC;tHta<gkXV73wo<e-=;gpa^07%F^$xi)0%<43BCIoy;Dyn<#foizbk|kTc5fq0b_MR#fqd)4-;HaQMVofn*ziKaSA+62!O>1at+Q1*3h=%v*rpz7Z|U5ZK=bmA{Us_ozq><&W-(~{gdv_diqSFrwg_7$p}2s21P;=80vx_l2Inke_1d2mCLgGiH{i_-!pbo=-zL#q=bG3!3R*O*~4rAw`cFWjzESk$fOL}6(CBvK4zjF3>x^f-EiVCksx@CfmtTNU?2u9@Dz*)%gXmYFePBhU18(74Ih@eE!(0E<k6@SHI_@Dz{m?%O{U0P1-eT6x>#S4rfh0!Ik}Swv4B-kHeyJ!r)(_ZiBiJ%CW1PiQq{4CuI7CPX@SO@^g@$snHV0ZAjklbee8u*kA4NHFQyUV+WMm(ww(?Rx7-t*<k5E=xsYkc)t#o$cH9BSbHKnt$$unv9Xf}=zhDR?Z){$D=p2Vp$P?ehc+yUOVFn^THI{~uJUZG7#%v3Aa7g@iOuFOu&eZ~^!5lh<O&Kwh3-P2xG5Y=fu`!h7R&oRljC3xHXfP}|fUd|B(V4GuW0Q6V7BIB(92jotAz^x;i0KEwh^GmlgKR+>=V2R93-{9)J=*DV86E~wgq-()Xuzxnuv~@hS<wA9kQbHRMX!nKw|Wn>5X7{>Y{Z>Wmr|lFg<RltyXXgSJmeniyoS|7gKESc>e^to`E_ii9tU__6pr)B1WX^uMO4S>RN3Y_QR;({-2}rI3CZ;m-vJY}L2FJx0jdd#cI*I|S2#|L-U++btm3P7X5}_<<+8uR0^P$Vi=+t#Bp42^D<bYFXaUgCunkjj%yNNUQfFzA)2Ym?k}Ht2cM&9C9UU0J(}boiK+AuMq2;J|ix!d#`n?am4*d?u8|-o&282DHIVMCG$*RcNgz<t>PL!ms;+a7+0%HP+2y)2xAXl9Z%|bpj8z*@VD*{QQlMt!eyY9u@Lp*D0$j*k+BM&wDTw}<38uw}<j@mE|Sg0XOK4`qbo7D2<7H#5!mE^1w-P4WTrS(@Qu}kzLIg8$>R&w*grs-4y-?Cj=p{NCbn&r5@Rvq?umIXFghjrXmbgtP3!)C0Z3_x0obQCp<hftXXi53v98C(?P?F#Ui1?;{$otA}>@6lxgKDP3cdm|R~G;P31S0f*8VU3Pjf|z6lejNnqZ0y$gzzzF(7}a4=1Uz)$%{sWe(z_XIj)BG?nvaqBf?aF@{efjP(d+=57TFmLuQRS+H~}j~Rth9XLJ6*iDF(~422u+rR%!!$I%AOmPX}crba@@Z9%;<Mx(8+p?J4h<WRuj%tn*Jf&#<o@<+o}8GXV1xIcnlfg4qmW-ht>9!=B0J8!^<sUHbU&S-B|L--mtz>Gi6E*p7U<vN09g?pTd%#&*JyyYdv6{FK-cyzXK}QW^yy=PbPP!9*1n=z*}5Vcw6SMm3(?!m$$`E_>%&H84Nb=0Rx+Y&Y=7nk+J*OL$=-gdJKVcNRG@W3CiE0G+XV9Kn|Cru&xozS=zO3Sgf_*!GXrQB8%#ag@l~z@fs>>G}?z=~HJ9L+c$|uhzA@XxT7zscv*^upSC~3w<_qyNi>6#BI9bI8!_nyx&P{7&~Uu+#j=R&R7WlSm@RSeTQZrnGg_83MAMQ#Pm@!^)Uetv^sR9CDT<}0cnMe{L-Ti2dqJNq#%<^*5V@_@=qMzKLIU(QZmlB(SojJ*J1ND@XA0Jg<i-kk#~C-*Jzs4gL_;QIT6+Nam`x1!aYe?a!H3^z5C27?N+Q<rtS5XVO6$M^8?z6oV<XN^<g1yf#eddQey9WfPeX8(>`!LT(#(BB;S=}0}(P#BBvj1w`zfJH*jIZZbJmyX;IM12B8J|Kdx);Hr690X^R>NumS8)2wNqRBj^I*Y4s6(w_7NTU>(33X%X+jo$A==NAp;m&WIMxB(xC<)Uy*y04yVAFv3&p;kAOqJ^`UZW(%%u>mXmzIp}vtX@xOAFG#K2kLwe*J6f4Ak94u{Y1I44_-fko<T#ublrk;Sgiu86u88cIuaQt1D57{3i(jRW=#-$-@*{0QJ(*xZ6IhX;HtE=A8Z^TQ-|lh179c-&?;^-QzB6=8nN<gU^hgSIWJ3=1UGlsg^!)}qSV1F1Pjtw9ME8ReS%8%Z_UEE&KXvn=>v4R1JVPvefoXgLP5NU&(%^9m$~p_L%Ym5p_y`;gRbWCcNHb7f#jGQaZ6jUl!3#sn&89SnLGU+t3{4yKc}nG9d=?=$d}5Q(+GNw?4}Y{8+Eu3)>=V{;>xCM*sewf35SQ-SF1qv~N1bxe;WCYZowq(Laj45sK?4sc=;)zP7&K{i2vV`M#nc7=9I9vzW~e0%N}DWGh8*xNo1o7XUGPbJpop>x>Z=1kJZ!g5{Nn~?`!{?<c5D5&^}FBw<HojeYZqSxdfae|__#$^6dFKMShVb2YoPaGT)z!grzXkT)f>W7C}z1yQxoKbe|*rH<l}hp6Pulv*Elr48*qt8-czEp9lt@o?$Y7@xAh-tm?3r_IE@dvx_AIt_kGZ_TbaRhsKQ2JG)X;A<24Z<G%Zw9UAt~mRz651*=wV^6ynWN{REOKwzh&=&?SXHtplE8()WQCH=;H)vCm@#){=+3>C5dFC`VA5)D4isxVE<AB&BC<Gg6U~$8Fdw4shBDd5W6oOhk8(Jhmi3nH*>X^MFS>+p=+uxT&YcB~Oi9lQ5UDRPE9{wkBh-y6wp%N+*M&6V7iZZpiZ-=~%$av#b&3M_t@KPacQ<)1{7vbg5)Ekn%4HH7r%$u7gpI{eTKU#llsqZyxe_M9Pto7IW})8s-yq4b+W5prNM|Z*FJW&A6T<Es{z)F<t{k5y!)pb&v{*8ef>{$`R~J=nAia=c-U|J+e?K<*PWrJ3~Bcu>@{j)I0IsuG7Iqr?Fh@FKiZQ3_S*Rqb)*dwXx*J#S3#|OA#z!S7xdg+Vy6t-pibU@|h>*BOfibG@hJj;(<_H$77;q3`(;)LZge-V580^_tqMjBc&uC9lJ)xV^_YA<JX=Cs%#CnG41gjRvjxzcAPm3ObbOm7g9Y1#e+mBG~EUL<^(yr3_>({zkQ3f6)(7r(KS67sJbykRt&oTt*!bUJ^U%NY@@>InHda^F8oQmhbkbYoZMHle9j(b&)LVhh5T7s{yaRrjur4(->=B7QOE1!+jMM#H4WywXr^xE)LvFMl}T(!cQ28s5y;Exl3&oFDBJ4fR3aarv<Z-b_@Ljm*fAySCVQwu>3QyO9+-%>&7O0bX!6DDUTm~|=@of~aM~KyVRTEAixN6)W3C2y*QuiPf*f57-i=0$=qT1eURQJ@S?GLaH$G|GJ~@flLC+UV_ru5?a<Co&YlgX*FRLKhA)6q%0wM^tWTe-)yi6-CM6~dMWrZYheY!It<!VTq)s|kME>oE#ld@7k52flw%3RXg)kPLytPRqa!0>{#8EE2?*F%g(Fi#x$hQ`zGmmPF*`<kmC9k3m`Y^z+cv;?VEE!(tzEaY3^!U@VU8BVGUxw6MOdJgH=mqVBVCMJ)g(5ozu-SFt6#-{}boJIpDyE;3Vgu+p0umkhr9mp*wPHf*IylUK(@Cvx8U0%y|!gdvC>Ni7yrsPu!nc}|&$doWZrZSI1f~Il_Il$Dc(BV?_#9%4>HwTrXUqzf0|IUD<lAkF?ivL!Fq>Aao!=#F7!y%=_W+J6FsiF}Brbbw~2{DyVF@vRwX(p&tKBWvMWlAlAq_WRLgQF^Plmny8=@r1JOj<cAN>6$)U{v~S1V_my4H_kX6mU_Q#|mInG*^U0Wgd;7DDAl%6_utGP*Iu3A}A{RT);%h-#J8-_D}+f(h_t?l+SG_L{tV4#XmBTsO0AWL{uStC`450>x~1VhRHf494hms3=3sSH6fw$DFz%==6MhZ3R5aDP{V?t42fm<CsXPG@KeRhQs|R0d3fN{aQS{&(5GKcUq%gh8fEPxLOhM2(g#I34U>CxAg70`%ZPC*BpG2&GsB{svPmTvr%Xx#<CJ+E2H`X)hXLP|OBfd5RGuLZaMGWO@TTmu8Q-KQnDI@;v<-lpD)Ur;n~dqzu%_~N1My6iugmdF=JcNl%k(oeIs#PFCRaER&SZEqA}G_Q);JKsRQb9Zy;T0r3|p!KEtNr*vd=l(68$ovmiXaeFiRUPWq>T@5;llf8Y<@oAWB1Kd=O~TFnP1kr1ZCrPEx;e*d+OLC~VTeEEVu1dVVlS(lD6|(4@>`5t@{JHo%f{2_={$L!tqfluIZ<BpDKmkfiK$5sH+3F2azq&y_Hw(pP2-QZcOrfMiH4!ylPa%iu?*R3rMRkW`91GA3uCN9pe}xREKf0&7(A!UQ$Sr<j38#k3;KDEpkl8EFq?03%as5nq&jHe!nkNm*1;`a1_E(jM|qBK@g|AkrTV$e~<<5jIpv%HxLgCj(e0mrw#0G9;Fug$#)$fFUiRfELO;nz2H~v@(#8Db;`v$|Y1lgGyeQ;X%c;GIWqBwFnT(K9_)l3TYLvppqA6SWq#o92jIyuYd=YyeNYSnNmx^LB`}FJ}CQK4Gk)PXMhOh5{wX`Lec<$P{qrE=%C8i0}w(LFH0dp#^iE*kU6~^BV<nBe2mcM);CIg&}b^&JbcjR)H4EP&?Z+n5>(KpSGoC^pv|psM0lVPR5~g^&?ssh9U^En^^Oo1G@^<}2@V=n&7(#Kjk5L(L@4>G;e-<XUuoS+&rXe#)GEm$hV-WlS}6IM;Dw&%&jln{A^DU5g+#PbkWl6^j}g+JvhX1FvkV$!O4T4i@`nKtluP*e;XwHBARv&?fk26-{P0Mihppkk;6NKM^C)3JkE*53!}@GaJ-=9_&o8oDn}O<i*cu)l-}7+gM-J*4Y4w9)J=O0w2<O>A<_Z{3$%|p|J5}#D8^ZJ8l^78`g(M?>r;ubo@8lBlz#aXm2-(pei&&lPa{;H5c`Sf*GLJ=oPWE}U_?*$zT>$1}9!+qZd`ba}lX)zHaI()u_)Ye?0(?{Qq5^+Y@}dlaV@f3mPB;L96BZ#j`1zc#eYXmO^W;Dbjt@`0W#GII9=C{au$GX>Zl`zC%Rq7H^Qoddeo^l_VbVIL07iRaJ80+;jM9Xv5Jnd_7Q*NNatXoTJ5%r+Zip+dfauUyW#(j9om?0r`T)Q@elA~B$1;Kh*Qo_%2pzqiQ3f;u(TQl@E`P)rfsYi`C<$sLKLJab(x66;*Cgl*`)eLSU?X&4##&^fIw%I%RT<idV6?rjZJ-CYgKP_{egglo5cOMcOOUBR1H`i{BOBFmLDK?-Wm_59NDPi_G!fJtsKtr~#x=rEmR+PzmepK}Yt$)^Yg9)>XAONQ8wqGM2NX==3|U*FG@y|^OhBVq-vt`aBm8?{M59bo10x#YE&0-*M$f2bOTar5V3+Y$GQ~A=`P&+qphnME#WZq_F^%@o7egHx)Tkt;5kC8+A&t~majUUAr6G+J8LUq4;&G?rS4K6$&x3V%Ao<8f7tN84BuhWeTd^X*5%9jIUm4$MChn?A5=hTJ$ushCj_MnTa}+&ToTKE#X>0c(;v8{Z?M$4b;SoK)J4>ISn8WX3k-)TCLxwo2C$G)8o?Y}sB8qS{QMWx?u3vMIBVUTjk|0OPw`Fm=%af%|33McJ^?c|9yFEaKXjW8*Is$6h8;*3;js<=yqsz<L8zRb)NTVEK$O5tPFh?G_8C0wzhl3rtzvy5`yIfSi(!sarDx(#9*bDp?8poON{}Uu8j16Tb1_6@d6GzJc|4{Drq)!ud`Xs$8gBsOYn0AZNkeE>Z_{bqYNq8eUGU|)0P$VOQVMeGXq&0%VlbO;{Ml>QSB|TJ=qR#<U4LKVa(WprN$z9Xa6H^o84-D<;qFSy#@{);Slzh$okwr4{wMa%?JLFJCKp9e`9vJFFjA3&F8Uf`8p?&swg?y%{MjH=mw9%MG{)5CcVyQQDOrwgBM*hH%Mv78{!Wwn8uO)2+_%kVA=VBVU8;EICmobgRMq?VKU(1tWVPHoqb$ZyiMr1ed;4gqakE%r1t&VF1^1X@QL`pv#`ur~;q>)1(kR%H(<P8q}b9vXN!-MLq!0({t11}4aj6_y`jgKspkt=laWy2bwgdiKys-tz+z^^%Bq@&)lHYECmA2k{-iV;mJ)bo5SS|f~KBv(%ozX(hyybxo{@t_u!)n#apsDMSm5Ky0qE?%Nio<picE!ZJ~6p;qOU&az63{lj(jxmbx14Hyl#%!D-*A%BH(aR~t4)N6B!~=tW$W*c=H^9%-;c!#0nz`V3RmdVD9M{124Tr}8&1lhz^h)GV3p267fJJ^VibzFlGHaoVGNk09<2gXkz60=dU|${)gz<_d_x0XB_%QK`W(4cfy_={^Yk`X#$UJU91aTO5t0ldU;|~$1NO{D_wa5j=OM?_e<w1%r%5V?l53H5PDN6DIgN{Ye9TchvtUej~N-tpwTa@;oK2+Eut!Ax+A%0P|%fKd0;fuN|d=ccTp<mq`zo_YgEuG0UIEWEs?&?vD>XHMMp@{IJj@J-=wq$iIBR0A0p<)?v-q}I1jHX05YkQ&&%b5I2PU_AvAd2$2!_*;E9@B^!Uh-*vH+7Jdgf^mY9)d6jttc!-8)@-PR9<UqLw*yj5_mM>)!Xt@pt2;oGx=kb^2DPe+L6HPww2M23ggWV#~As@Hb*|n5yh{HeYD^AS{NlsWz^@sGyqcanRGKs>42E8ySAzkY|d^>Uv4eLK%%dR%F`deGzL=gE(=`BjZ%KX-H2ggL4e;KZ1{l*$8^w{CCyF^UX);&wD|;eMzmsK41?5^{l;sSp$XHZ_q|>n1xW@sk|fu18^KLS><%6YrcTZ@e*xk|zt|Diz_V<EOcjG7k(EvC#)iqFg>FJSY5RlSX4;1;%R(b{^#G>nF;Z!4Bs_+epTi#*7>V+_iEr8je9F7fK{IY~JfnfZk$h!KnFAzgVnyXF144nMQU^?~1xACz#ca=EX;g}ef@bMc!O3wM&5=7eV3HD0rUC=$ZYngy3}lL#!BV>vKUM=0IYYG~s8Yux4V>NGm0^_v!4W9z&4{YRZteQOph~D0bcPSBq)wyJ?&gzh`~a>b-T>4TtSA3@q?;{+ns|~4&*{=+sPIbKcXTCprJYm}VTq3`=g~cG1OIUcgjm{b2foWIt4qs6$dBch##vh6I7=NBXX)a|;w<T5fv^fC!!n^OJQ-VQj$$i0T5zQi$5u-AN-D5a{G@sW%tS_5@+>~$g0}+Qr4C2#gZ^?<rI5a)>)4wLo0@Rxcqc<W4)y}H0v0Qe03KBsCG9iLDsoa1I7tynigL&UW2WddNrfW|nk3J;<;j=z+o{~j;!5T)I+9Hl@Ijr0f?CpQ1VNGtF_Mrz(t?sPX66#<!KIP8>4!I?KtUxOk&p8NzXtX_1vF1Qaa8GC)?YR{tkYpWI&NUQ1%{hg78Dic5l1>w+*_+xF>m=@b#*Hs31@^;>QGfbOJE}mzyrHaZbqgM$9oGkIWl6X(&3Z`K>fJDkx5~PSQF#OMX501aAqFRmM=j);>bmH_H$9>qCiD1B3|amhzQW3?LY>OS7c)>TwhlLj1i0EPd|f4A~juyBgyc<MMRPvnqnB$0;y>R{v1e&!Eub*c0C)%C{57f7}Z>%rDi}%>ZJud6BdvGt29ae?FWlz6blY$<jBil6#<Qa{dYws8iR5bq#=#u1+<cwMv8cRH*ynjOowASZ_4;?@l)_n5(*-d*gA_01Oq97NP*Sf5HP|9DL2{JM(hU8MK?N(I~sNs-w>z>a^!ASkfZ%5+%?~CG1L+Hn`|#RLf9N|)BYqnOj0aN-1lGt%Ya8e54I^WZR@bxjWLdtJ(q?!Vz0i|dF_s$<*TOX?joIeY$mcPHN^)-F`6JF-6mzS7Nf|;>wgYtioCgg(UFWq*rJh<8bk6!Xz`2m@I_z_wEcX{B09`r?+VBZ`+0iCBU6~37#21ifl}R@gIn6=%6=5W5y_Pf<>{i6yo<4!h^759REXB;P>Vr?;#a?;@(967bTyu%56vlAYwt+v<y%uqMdpI2O9;LC;ZaE(WGKL^-F#QzVZ#iS9Hr_(hQexW(xh3eZ3v{qbE{62akGyy%8)G$2WhA965?xYGQv>y0K6i?5Ls(Ogcu@U>5%b-K!K}OM;B`Q&l`gav2UA<v;edfQi#m4g>b*HgQYaKkXIF3h?U@9OmHD!P0Dm`(teZyhJ?HfCmN~^TV5(b#w&FeXu}X+$WtC}_KFM$FvR}a<ld?|!Vvi-v%d3UjG@vjh0`H(w%lono@Iy_LlQeNe3T(tC+PJ={KpWHhGYZT3yK7Ja-wR;lM@vnPy1jcJ2stomO`F>I~3#zby~X3JP`3D%z!7nwS`WqPS?%{9>VZc@Ma#GcS=xC@XN7Tt#_S#2qKrjJxL5Aew1*h7`B@!43Se7hseo7oj?(CP;!E$X!9-oG#(K&M3oN_kw};kPmnVN(|ZW86MsX(gm#j3j0WfgOe(A+Q*a1F<iLt_8RewP6VNFTEg$c^;3%mxA?~D+<C_Y-QvfIKr35&kR?})Zv4`$aZmJ9XDuZ!CJ=@~ja%^Chgd&=D@Bvq<K&7Bv3U2}_EzwPW6}qXFK{r*yn`}lmIfQQVyEav7f;WL(fU+gp5V{E{lt7Nqa731m7aRtHn+V<1a$(MEwma_(fo{q+RRM4Mee6S5oGN(J3^iJUZJHJlIqFK{65$%1WkWjwIL-L80gMUwkpbg0(QFd+Bc}*)njzLkkG)UL2qzdzHN>eq48+MPK{yd5FvfWp4#GDPyeaaHL5h6huLW>ZM1C?n1}F_w)ce#D25^(FgPSH??ar;b*qlW*?eqRbsHOp+rWwJz5Z5WAn#6FhCRH#w3j*z$^7s!1ZBq4N2`(ZwfNt6cW`-NXg0lpJo3JXryCVjmn?wR`a%j$q;HHBD7+{3hrWro$jY_ah*n3KBiz;N3GYqPUQiVzes#YPJKwTk6jKf;6i+7`}z(F<9uY@;|Otrfk#W&UMSqX1ajHMdiWYcz*UJZJQ{(%i+oE+%C<vyPD*8?&=4%P!2gS>ivfgq>-q;TaZkU=`t!A7Lc`TuFTzG^yfIx+O9sKtt;R|!qf8q)AiObe33Oq@VSxD!&&8Gl3pj>HZ%I_wJ9R~(;%m?z+4X}#1-pR11|e{_&1FcyeZNk7%}sM&BN<jI~5VDbzzF}Zi&(=!hTc%tiQ4hE^!;ZEI03U_jJxD!GXB8Mt`x`nq>a}|o=;ZBptCx(h^B!)pdk>vD;0y|~08L&=~*f7{BEizKHlM;l(;+-P#@PH@Juf{t~ww;*bv?m<=fiO>5$dmiH15(?sjC2%-A+a^IJD4o02ScKsG>i&ko>CQih|ot4VV+RaR-hpKi59q~^p+u?cB2IcTPrOG_Ee(T{cHdz6hn1Kfb0VKNz|bIUVuMwkAXwV%YKZ5B7U6!p<;!Da+9So5)c%TvhK*Lz)S`0oD?YnKcRV9#}!H%K@RXly2>!Yj+}H-ExU#aVKhSMleUE9X#B!bB@h&k4ll)!ShUlP^MtPX41<NDL8V7&*g$3>S0SQM!DjfB1ImVv>$(aM#XT#*L#dY~a43Nn)(8#77g+OnC^8!ja45lQkk}M3l%o(lI8yevZ3G9^up^!-TNY;P?Ezp=^E6{gB}&!H(|`D&NJ&j$+C;Q@I4Dp?Y4EguH5!^hP%}p+4ji7?xvv0%I<o8FbNdb*++~W4bZA3?k^BS#6)N9?5dxL<paOZwF=;<A6p8>UDHaMBRRtJI;6xJ|N*Li#Hs9?o$3e*qFtv5Zu7E&MLkUtT$!@?u$r?doQ~{r|^~uad%#*CF?wiq0GcZ9mDZF@w=^LO<qzm}T>q?Ll2!<|5&;;JZ9Hk81Gy$S5!i#e3)lnr&;Z2(Fk{mr8)2RgCq-9P#C8Yo-vPfdN{uGl=5DI3Pld()<pbP*zVVU&CtmZJuqn&^}Y`;ne2%k@spq*mED|qBJ!QL>`35r)jo%Y*7t4*s(l|-!5G<p#OlEkGzCnz!)=ad_2(z^<jlbYHB%t=wB8sijuay*U4GZ-gf0y+6LM>Xk`;F~}m3fGpOKpR6qo&nlK#-v@2YbpgbB{ST#>+mj8#4*HXV%I{;p@X;rs%bx>np`Itu2TtW0`hbn(ISUg7SS}*wB1ndNj%69WsoM-^SW}Hm4TXO6sCzLmhzXzYf5pwnuk-BD1w?I{6)$>k`A<L--v2b*Xn>*`Xz{_bQ_S1OsUnSc%~WF-pOKc5@z9;&`dL3_>1;mSDhG?f|-)6RY<0+s~q%+dL@pD*+MgK6&bNiQd~ghQV5e|3|7FFitUL3(4{?&U-#LT@%*gfYsM|nEReu4<sL*{Q<*`8&Xh3&mJTLtl}94-#4HCa;Wf>Kg9`&(X&3TM*ldx{UmDsRsFLevwq_Yz2`!)vz?H~~s&NiPD(RFPfL4M<0V@`)Q3X^&C%7&Uh5;%eT3)^NHLh6=R<bi#CA6EPDy)+HMe2UtMx%+DB{pPNK$a%5h$VYufF(_)I+jldey}i!XQ2T=#Vx^C$<SUWn35PNN@*rlQB<w4GU!kyl}UVSozAPA6r}_m1PMvkpFKR4-)w+Vlp$9bOKg%n_=;p%?6%ZMqtT#~W^@^kv!ozOA<5iGs7w8@)U<jMnv4XRB+sxAl9a9=KF-2vf!^S?$k~`n0^Put=sMA;FiEO(4wZxk4hZm|=HQoCrF5{lG;*+z44KhklG5Wh9gb8Gs#LR+@iHl&)(GKA^8A-B&S@MrwFIy?4ljLTyRwS5cm&ua=vY#*&>1#qv#JF2jlgIMn<O43IEn8NVjoZ|;9baTjlai(cK}ksAx4Z%;_Z*ntx(RBEul%I->bQlyVXH&mryl`M-5G)TW^d^8Y5&<!ozTxHJdRg$S~L2fwa_5yF-{I-Jr$F9Wyq`(V<DKackJ5-^b{S=KCsno4|xkN{~q{dAzB|OmgsNicFgDyqF<B3Yg?{1+|{wk{rBb7&)G8fF&jGtXZj488Jy_ND}^#evZU5orfj)vv^2AA8{|iBy|JUUFeWNb6GnEKvD@F2_2dl=iDYhl0YBEi^*(XW>85Umqu^XR$R^a-6TFo@_-0B8VNQAd1E638VMIuQ~^cOuT5<N97&`#IOSj@AN|_WgTG05q{nS(DCJQaj?3A9J~)!JPwUhm9a&_tNUprJ4P8v}NbFuuJ1?)}p$`IDakS%;%|s$8Q<|$Q^i{(lk(JFiM`Bp20q`~$zjR*yqG3oO9qZs-1K3+^z^3QPcm|drk#IiT#1E3fkz7n<IFdtXBsC{KA7c6vk>tqlGODA$hsPxCx3vx>oi^Z-9*_CT#0Wr1k=A1Gij=?Xi)+L}yGru&pps~9qeivEnzg}x<272W4EyUoj$h$a=avH@N%{@1z=^}UlO9-Y6p%y*nRsbBVT1)VQVZp>GZ2kblxQ2qB1J-->f-gEkztYKQ50GY>TVUThGr9|D-e7-rrQdj8#*A=O94rIvruz@nDIyl$kCbX>JmIso$M@|@JLPpjs!ni&>HHYKK!taa3q&(MM@SXEE4{3$e@)_gB%cv?sDnA)&dZTR9?m*N!>3CLsEC7wL6$2#v<)=)eTQDj}jnKD$`OVl6J|%r$*#$LHZ;~kP1#*6tO4W(|ET74>m;!AW3=M36PZBG&KT}$nThOeCOau)9Bte=O~=v7;_cCNJ)-CSR@<*9n%j9MdJKJ;*c;iY&;upYa{fi8B{}$nn3}2v>UXx-eubftFTA^F%Wwc6ZS~V14GKAkAx9@WRADwI~M5X{7qKsd=`S#TZaEyE?6?<VV4{sqb~KX@CWZS4AL$y5G@DAh!%P&o2bGs#i0R?^e6r@UIviVTb7_n`BDQVP1-OMV_iSe1284c^_IgSK}o2|#X(J&U`ZklN`o+|LX}aNR3)59MK%+eG}T)Mo1!k}Ev%{QgQePA#&0LZfmK8(#r%z1nY*sKR(Hl4XfMU1kHu8zua`6f6Fd(o&~f{DpMV$HHY7+17IDPcKy5?YPL#!Af)ya2K*6#)HiC>=q719#!^-Y0V`3~J&gEbwL0Bb3vpIASQvz0k{RBTT7y|`kYKy99O!HLTEUep&MPu@k7)h|ZWjH1TEQu<>(xenOv{1S(2%6#IG3kv}2V@ch0y530c1u7@2-9)O0y53`F>Kkc$i!so)coF;5s@zkSeoqJg3;m;GyW)x%Op`t%SO}^(3U|<X3Wx|c$O}Fi)zqPSy(1T3|Jq>@c^v?w!~4HsFy|55_9A{Y6-diaTplzZh0rb3|v}9R@me*Ccq`Tp2C)<(C`a&;L;ScjVyF&(rz%bua3q9^QT8+62pdL!g2-F(u2lh!pc(DDnphmna>&=k_q2*NrXt$(y*YV!6BI@Z9Gk&tay#a@uXBY;g&)PT#_=f6uA@*i(GON=#o<%lL=4l6nfuDqcSzCP)n?Z_-e}x3tOVEA;-tb^1><x!<IxAvDEU!Mi5JMxg2fXw5JFnd0c3>VSiyzCFvznqppK65elS)M+>0LHejKn>3};ADvi<o7U6WeBoAPJCp{qo%%@S9Xa}nsswjZD6G$Ui1k^1iRrtsdN)|(ZWL2{NG$7z+T?|2>jWn&7yGhl9!Yf(+s31y2HrY=#GdvgniQS`$L-arG-Zg!ociOUJ{Lm(7zz+dSLT2CTU5Vu9aJ52*(#8A;BQeQ9Odz(~LWW|B!%TI(<&DH)nj}uJdB~(hJX%AblMGpl2qoZ98$~E-MK*v?vK}BF6H2`TKFKlzl%Q9Y_@sgGBt@=Dgc7S34~I_@nV3w>tG!t^m`e~!`<*c4xO=cR`G|W%_#_QU0<xF%GgnuthYibwi96Dp1bDAKRdLGzN=E`vz4&X_@(q|dQh)my;YrIOUaM%4VgTA5o0`1yRR{I4hL{JzNi2g@)iG%^DxB~Lu}Mc{0aY97P!xa(wNjRq)Me;8IcwoXJuxP&rU*b89|E5g@Id6OT6kOn!w{oFC}q|VA(U`!=GUs7n#EGNl9DmqJV~{K@ku<SKu0JwGNT?GwaK5Ok@Gnz{2dsyNmK@H5<wM839mcg{x4vZ&`f0akqM?Gqc*|cheIl%D+K2SSD3=tJf8aIHU?MfMvCQeprDNdmLNkL;Y7p_wOWd$HX5}_))OWzpjNtRfTa)tOWlaPUa(>mC9A_WP3$xwmX7Q@bkG1;`u)?phC?hJV6P~B0u$dzB4SQZGCgvynxRXn=N0Ul#DV#M*d<y$^f7R9P*w+W+6z1ZrE?{Ai8M(ZRuz6pW{N?QcukiWOc{<zH7apO#ZpE%Q_?`)cdY=O!oB6XQ-*CawxJ4zp=!wlb<!I$fSr1$adwG;LLR(AXb$b<H3PD^k~|flr%7fxn7PZjgn~Y~q6+!s;kCiEP$}w3bB1zM7^e#Mq~#t8_5`atw%OB~o=3qFtZ`TkBkZZHOdBR{AnwU(Q)mvq_tjwJ6RrXZ8ku-h%CS%C<H=g)1pl-=5dXw2rDan9lo|hoj(POEQSXA@)hOv&*{}=a$b+BgZ)S=!@TUp<rgs!K*!hdZ2`i&K#WbYH>9*$p0F(&RX3Jtc!K6VRA!`iz$~m&`0u*YFPkple%;2GTr21<kDoV{h-9cpn8!%BZ9Y^5Dy@6?(U{Sr(5uS@FBE-i_U{U&%0;vs=o`C<@#OX0h0OXM4F9S#60P2Zbt_&R2J6&({LAsg)UMq5J<)NSOLcZot%@s1of099V@DrhqTSQ9jL1mm6D4ydsE09uh!;o)oAXI8n8WCi^q{f5^D%CsPwUNokDh3f*fu(RMJ$q8A5i*r?)LUWi`=A^$m2i_NZ>p7`rj(!!xkNQ~iX<8y%D{F)mSD$K@Tvb1F&@k*YaHE#np$o^P$>aw%sC9j%_WDSey*e$Nu_+^+NeaH#?@dd#Y*J{EQ|hxu6-L8yVxv9mE&eNbQz>dXn-m)2vBtxj9SK1q22r|oqhxGR5N&YjLiq;%6KBK%b4K;Kj|m+lG~DJwG2&_o{pw?Dkky(I2CCLUAv2YMiv`VGo@H6`URxyEvpRBibtx_2oP1Vyu^`JP&7#=E2W>z#XL!Jm?b)+A&}K*LqTbWOPNYVHaJv#T%t-stG6ssR;Z=o@eQ)JkTFG@8wtuGq*Z}{AvuLG_6#3HB%z@2bLp_w9WlB{P!Tg0*AG#92~qOF2&Kt+oED*0M+bvy0hvYywW33}<ftu;0>x`8P7dQD^<`^^ZY#*DV8=Zw%oX0K=*DykWwY4^Gj$w0h87XL1VajsojtBfj0|>#%#j^j47-wUytIzg->3V{l$UPQm@ATZk_&fwS8=RVQ%Kk=+NOyR;@wAl8khag6Bi0KTsi_was$!kgq&Lmy$VN-y%Ji5=uC5XJMu&;ffDkX%k>s29DQu45EV138f2q~q+vDfINsufUPh@fU|FEhR~Q-U|DAc1_$#ibh0YNMVA1NMO@bIKOEiIYz2)sh=a^P}zy}q)PD8ZSN+LsL14FSAufeZaOD+b662`z#<m?Fi=S7qQUg1xX172k!LZP(+TPzb3s<(_V9|tuoV_2xndt{}vu`qzJ&^i!&*xc@2p(~k1C>Hx(QV)C%iiMtcG{stEJeA_H4#l$=BnmAxSfa=<8uCVhj>no&SK~?$Sxm*$>$n*)qR^Ke&=5>;tU7vVt*y91dzWJc$I1kUf?YrkWm4xfI2LHnuz{NF7E0k*A`8b#wB5}>V}*JZML1SNy6*XSNF7#eT7;;!w7imXjpV4n{@FoU$^s@>mOP>>#)tyzFB>C@FOpE_c_;Yfj%~!Sv*t&I%1W$tzd>ugB0dz>GtWVIJPHowI}PO~{$<0m<Qz0PkgUjpvXI%Mq2)?Q79GSZKvwTGCgCXM<bZ;(Jv%FWaEp_LfeblS4w}U5roywZa|Li#vi4=zD7-ha`RFXXJDY}#iqP<`%Uezj)Fv`FY928_OE5z~VT<;)kK2C-)Hv&ez`EzjDnfml_UYqL8u}`*`*i&NAmO8M4a6W_tcM62<<G%>Galt?L8Au5jGD@cIBTN_Etpn5(H5hP7DdNx`T;tv9C`CB;5u}}0z`}G0ROEF8P&}CRLU`0&19FChK!P|L0Yf{lveL_ogBd-bCQ^To1t3dDW~B=n^(+uEs7n*4sZ#>$VZOCt)8+f6Jm=MWrA#R9mU8|0=nsF*H1@`*xE0Y#oe?KgMd+Hwct^{lQc1(x%2|ev!Qew`3m+k8Fi|~E?;?JfB6v5E$J&w?%I~(wnE(tpNDP9vj<a_!nsp1OYR&d%`h0VwQTX{*oOvf5hv*&Of4P^+FDLd5fQY7$Bk8>E&2>!7PK`b;s^><LAHK32(s1tsD{2qY}d;nwv2!+uL#(B7A>|I{+|ls`q2zl>lr^lwcRtpv<^^ss1}2@azUcH0>9Q0cv_$+Es4Qd6a109JUEL9VhR?;Z!}=m;U@f^Z;58_QtyHuENYJkWpmMR*eo3VlT%|)(Hk9`H3P=601As18+j&x7Nj}CP&|Xrnx+~kNoCtKaMt12JBqF*Jhlz6BihL39RVxDLQNOiz{OAfKtHr+p>Gi3$-)~sAWQa9b_XgUDnOr)Vo6Avk2}_0$D5Cvy}K>Wf{~+yOBtS+7WH-%(r?PT%Zr-m!tl(Xtb-z&x8tVUyB)?}s|1UMX=8YU(QY+D;WUI1iA5<#E5k)`>M`NKGPIte<f8`o)l+d7`ds73;lWqE+g^ke!Ay9?85FR38#g?x2(M8Ezar*<FOCupYasF}+foJa>VS<Stqc{#ZTBv*8eoE6!Fp>)ExdpgnBiAX(?*AxqznlHYo7-rw^0!;La+|PX4PNk5Lm?FYIbl`I8hOQMdW?L+6kM*Gvlv%=bBBA7gP~`HBsx}?P3opXvSZ`<G7VfiUEBEjH?bbi{?>}O473stSMwSux0WHtce)r#5=|lSAbsa_1kV>!^S~Yr$(sISHR}I6n=H6COjQ{h11|=p;r?ya@dcsec3-T0EG4X80N9w_F%4uLtoMBqoCz+A(i97&{t_zbcKw~s5*y?8MU`}*L8{KBk5p<>`nwz+6Y9OSArRU^%SLoRZ+uFCuq{Q2*KJT@E|aPq^Ib-%wf4zKwv5P2n>jrwh@9QQ($|?JZ)wG)^lm<Z$Wa=rwBwD{%RMjSKL>Y%;(t+mgHvaRiaR+?J^Yf3RkF*$yCFjfKi;>@f(OGqGV@7z^kNpH360~z8jNfso!jpYUeTqe@WP@DWR^z^T0(gFXC2Ykub2H0ooqz-41|P|0gK}(h?RdEhAC^V1ENwMG2<*16v}F<}LduXs4D-J9;}<_2@EW923z47PwQ39${1{Z8R2W1*+Ekn5KYiAn7jw{WRzmb-6|S^e*tzkwLG34aQU{y&BW|4D3Z!8Z@j!J9izl_UxLO+zZvtz;A8^H~V7`jKJDyw{hNarnLOY%6=r+E0QK$7pluZ5aCgUQ@y+4Q1uzHSI7@G4|>JYaWLx2%Vf&ot&lBk2yLYo7!qqm)Z8%EDiv#kqd^gKEyY^#Yz_chd3qKT&PwhEZEJ1}Yo#R;cSbx%#$c%m2So`UD3_Sng61RU<5e)LL@NXBv4vYlouB~&fiAQ_cF$8KgJMCUrtN9(P!47l*)p8fM6Kz@VF)%0IrE%OqNn{VD61K}epK~^Ob!wr)TK~ub8VbHFd`l()L%!{hy@TYgr}g5I2Z}A>N!~pDMm;`;5y_eqAnANsqNNiRU?}uk>KL7yC*sp+KJVuDmrhZ#iz|8Ekvls5y(|W2d>I39xyS%@)NG7Z;B_R(t=hoNj*7aPY!JWoC;rf>>z~hHZ#rj?!u;kd0-Dv6{c!JKW7*tGYcK^cu9vkS%6iMC{H9{CIcg@G!;l?$b+l)Pz!<e6j(%I9$huIi+oubWEDN2lJme|Dq<5b^8xBl5iPHsc1(s<Nf{H4%41g>E|AoK8XiM6fkO~QibJLp{FD%FSO}G|is)hSQ@T-14yu%3v#<<hDLgDdLXak;!>FdFpPqbb=frddM1{YehF=*7)l>Krl&j$&RLT(`4Gx%76f4|(4mBlxpvX9sQ}MBl0;cwPR+GGhlz|<ER@`X`G}i^Un*&U-q1o=;Zky0j@a%-d;*h*7R`OsepmV)#%9BGdO)KOQ6;Le}piz8<-^*5LghVA3$|9=DJO*kn82H)h@(`$LyaEz8kHKzZTRRVb!VFFJ?pL6m<SR0IJbXnQqYUmO(*j80MvX|PXC3b-j8pe9nn6y=mjS{_&uqpx@uPIl+HqKO75g-Rn`CCcmd{&)Y2swOjoF3`2&FP^3?0#gr(}4&RW!@vH*ubM8?^MTQ=|@5;+8mjjTk4qn}8A0Nm>!EG=r{9*pB213z8n>N5d6nhL8s-@f>yAyg)JlCHA1G5t@NX>CAC%S9vq@s3dO3wXs8HMA9As4DcA$(m_py`>R8dxCzv(xJwxf62DXf$>NXXxoa|(9O~#fDvH|V)19WBU8f3kln!(kx_LY^=4dzhL-bk60FI`G)28_d?P%VFGs2#zP8zXAOvW+H*9v;K`Ao+MCrUe<&0K&Hae{vopS>c2=m6f)4aQ&)L3B)>78xK!Qi&xGlU%~3=%E96iE=itD4W1TXorOn5c6ndj3urp$!CHKkzY9^*@Rk~=3q7hh9-F1W(^JlRA|4S7a&HMkYx7(ovH`)vI-$YDZrvNO*8B|!Y#oEY1yELh7u-a03j{=u?&GraY0&%T9(#kKoIvoNe&#j?MpyFGWjS5mmwSFDFuq~3}B!=0@)d`NKU9m0wwRp4i&$*rI0|lLyji?T>}OvP2&DRdUr4kh|XRkzuSb=tbIEW1_W}o9gs1`e2vVUX+_3L6c95zR7^?l=ZGEU;GaDLm=(Ukn~cI6OV8%Yus?f56WJW(KTOCUGH~c{qzw3@rOVV&Kz>MofB=e{PD{xn%d^SE?O4xX^bgXzJ@mSHlBNd)ZZyRB-|mnKK2osHQxq<5Het=_I;Xh?4F&XFu#B;HGZBu5Itk()nX=~+cil{g51pnRqk+r)#Cw(O+|c%#=nX(M52m|gp(hs<)RCZjp5g5g2`hU%Lxeesbo0{UV=QP#1na@$L#;wsvv`)nOGzE?(7e<{+m6Xe@=WX=B|s9WY~DyPJx5hl#DKKx3rHWDDWIps5M$qnMR_O=Mh4}Xp<`pZqTa?o8pFd*2@>n6zlmwqmCmA$&Jst5>XEEeewq@y)#P)amXso%WUK7Sk(Bf#`xqslXU3s}`1(=gR*FwcXuQXVIWu_U!W$#HJqH$E(++B?j?sow0&C?c>IM#C?4HGnXYijre33|7bDqU=1zml;OD)xNu5!2D*U{m7n5!~N(5D#B)UgI71|}tvXKX)9tVaOp*%LUh4RFtnp@iYho8o+Ae<2mL3)m97<K6|VThRB+@XXPT=qge}jcM9Z>#~UM5t-OZnqHk%YP0yBMDNeydk!P8=V(ON@G|J0nQnj|`%d9K)4jX(qb;=ioK}kQc^1P(1?W}xG?dSCae%pL(|bjb&r|fnn$P9RVSHpqm7}+S@R`t#C2)^Z9Xh^8#7JDtpfTfnI005GYPh}I&88>mB#}M)d$-k{!XmK8rY|1_mUNA60;)%IWrD1%Iplh=Ji258wh74|upX_gU=^^2PTLoI0Nu1>4c{{nhZ$TCw@4qxDFO9l)z^o|_59(FW0|`^*(!(?D;Kgyhbp?id~?t}d(leL;=tU^x~-wj=f?KXnbyyQ?|BMa3h8huu~&2Wo`CPWB~9(*Q#d-DLk~E4xcO!yd&0=MfC?z_#lYK4jL!iS4Nj}HyGb>B5JIsNwL6fJy}NBUrjs@tsdm@$7Yg&4>4KbT!PaTh`D5mW4SG*q8V5NL@vQm3RmXJC2+kCH`SAW9EJJU*x)*?lK}Xe`;TaWIeXMt>t@!>!V|=&<SL;yeHh`Mwih}Ob-c-zw=Hbx`<5`{605eVM6Z4?`sGA&*5c2~QfQVYqZETp8(Bcc-JB*cJH)}*7u%zrJdgEbwkC9R|6y7Ij`Yvo=SOwa>mj{LYl%F<&pg?j(T<TB_#k{Bn|LBr%L%1J4Y_;fqAX_S%5B%AUgl~ar0BRyoDpXgG$kI0+5yQk~JEk2omBE0t8}`t|v_g9rU_dh@w6MAkxlT<$AU184vR}Xe?ZlZv7r644XR$v|(c`?j<dMhxr2d(mV0c0OHNM{w6wyEYSfgx3<PY0GBq<D_A7u$A*ONyH_?fa5(TO=65%i@77JuW?C2t*7_emB1q$|$p%~IZ@_#r^@C%|^534)4JVQB#R@S}3e7x6t@3r0hYG7fZ!?cvt}x&95X9)6uUqsha1IEy;kD8=+}iejd*ypmjs=*ebx7#VQ@C$kjSlP!XWYJ}@~-mb>=JZ~3pJ*)5iW%Z-K-oN@u6|(353_|v-EWEn1@Z-wDYby&MuDx?%_0*dhzNi1gXKSzC&LVtPmR??2{Ay+K+m)q-m8H*%K%f5S3o8p(`e$zRPkobt`K&Cxx3Y9~W%2u!rKOdnQzo>}%F<^mORuafU0YfF5-ML=TE-GfcXi;;zwW+v@28LZ*WXWJKgly=epVLFuPl7KvhYO)__O-a>DA>6YahIr1OD{C{qf!p@Aj{M!LKyr&+4T!s~=riKmC~o`r)Ql@0?m$_^AT*bN}wu^`+}ThbO02Km6O;Hy>p1K199cmBmXdODB1BCdAMESFWzT^YzNY)nXkP&`+*5dY2T~H2BYxQ))~wGiO(pZmukyriprsek|jpF5W=WFTRG$>Eyz_JFj8pZ0}YUF86=@^8VGIR^Pp~vhW_Qz4I$47e|c@T7z!ny1Mi|Qwh^yMdLzS!XMbHFYf>JL;uxJAy5D1m)4iAz(7<DFp6_DaJ>kO;=;<pSN*d$i&gbczq)?@5|6QnAzE3wNSVJ`S^CTU%b)j`&i23iq5?{^vUr7xEMp&FI9L!nV?-6<W<}!Pq$YkUg%+)y|6yg}#g(N`cx$eozuiB7#egkZfAyvNr~gI-xQ<I;@w?#>Mt=ZO|Lg8qU=RPgd#Zot)%BBSSKoi*Uw2PeK#Nuuardt*y-EMls#^rU@^b&q5>)b!8(g{+YLqrvfimiUb!YYFyHH)HlT=p(8X0?10y$b)`ij>3CCdBm%F<uy$ERleQU5F~l0UC~@RN={T7Tut%EEPAhZnD`UHYyFL0Y|X_1>K?Ru*m+;YZAR*B6#oPhKv<kBI)T#@;nxkJit<)<63>toZ(qFIv6#jrgMixpL^E)sIg0FI_GpS00MA`o@+1mmeUJ7Ma^$B+hbb{gtyhK+?TCr|(~W3nbF&yEpQnr2eIIJjVq<(%SNOtG7Nuc|-$NP^8uCpRa%XS%O8ncjr}pOwdS>ol`V8QvanZ_kMUgnUE?d((1YEP&|`$02ZnL$>Q3Fx40Y-_m8XRzU{yHXSE<V21Q!EajXCB&F7NJe)n(x`r#AI!PS+6ka&bF^?_!z0^eU*e7zKYwD$KGK@RrcJhifT78Hp7*{|*|0VlayR1%7KB;u0iU@fkG_pt$ol!$AnZuRD8MikQOtI)ew*KVChIkWILV7JisQZUlmtsD23K7j^*JGHX-cUqFS%CJaD2BO55>mR&)|L@<FLXlYI;oYO{j7lKVy*t-oaYEhqU;TRR?c2x`KVRs-@qsE_0!Jd6{+ZYdOMuU4hn<G<zv=(^3YQ%gn}koRAKqD6IMaUxy7J!Y`NfrmYdj8+b!)e;ufD$U3xg(=5dfs`%Hj`F^rBpRi`7|_!6z3|Ed(bPw2;?%&qFql&HXpNPjnF=Bz6)A2@)H-fzzL*h*EN{L7Sit-oO40yn^-GfAw2RM4`X302|`dm4$avu9D~<Eu1MwmVe#-0Bc)&=Za1g7@HjS!dC@~TxLSxz?Z(~fq%sV=P`~7+q8P~%Ib?}p~JZ$<oXWNAUmao@cR0>)5xC|F2E*TeF-MyvbLB(qP(tamm5Pqt=)PNGQ)<ldhe;6tPHYf91-9N#16L1wZUv*AHKfCQ?j!32IyNr7+Dj%M(O#ND_j+@_@pZ40tU2`WI9XVSHYbMJM8-^)Dy~HA_>f31?(xIoSrQQd}0PzmcfjD%9TNyDQaYhQ9wWesdJ4DiGgCVnq<HhDF?Tc1wnD|%3)C4i3%K)w&1FOP`N4N9g=dgA>mN#V6**nk%d5-0eBl&qW#z2y?^C8=xP;^s9Z1p@W-{=AerA-`|wNTkKe<a)8uHlHUK4MR31_J`|gXRGyPMy*U!H>7%A2N=&k#&-hpXeed8_Ai%=8P^zAZ`6sv#0a=6sm@~xi>9|b)jBRXY-zz~3htJgn6?grY=@+}|=>ctsZr|sW`FZ*ZSzjx=PwBJ)HhH^@gC1Z(iI(mxv&iZL2DUJwc@o(4GPkz9XwEyzUYuDdGCa$Or-O%k~62Yg}-#7;rO}77OpUbgT{jYxP|MZb;N=-g?flU07z^YiM(-#}g(VMSJ1&j6>`5zK-b-w@UE!3k=E=XkqM|VN-Yn>F=)CPEE^~0ZXL>Pd=Qr-G8r=Mfzl8%A~v$zP>Bgo$Ya4d~SV3qGFL-*9m!W|x?5s-z<KpVIblU2-<hh=H}<SHznJTQxGMFTYJ-uJgzReNA`*80g$(M0;{#r}tX!)0{)rIm$Kr1HI(sE~%TtWlbfTA2zLt|jIatk(@8w${%6*#8J!RocX`&lNf7PdGQc3O~BA5y)0q9Vj~~Gme*Xv#8k!aEp_1f0xk!DT-TxX{V#M*w4W>X9l^&8f6x^wf@SP{-w*q!M5~@VRgw}qZ<^tPUWy%IY&2?WUq0t<c8o~l+I3J>9_<sT{^vb_QPVuIhYq1_UqT)Hz2%N(5-!V3$zRqy6gVZt@WiVx%W9B7U#h^yaq#jclE1xOu#NOh+ql5o>XQ;btTzy_2p4r>tCGHJC=uZfd;g8XMv>65?Bf#Ck?Q!BomOJfA$<_ssMQPFMYsl1+DfUzgvCx2CV#F{}*r{Uic=M7ZiZp_wL-`^8zEt3n~ChgFQZ2wdMsjgT0iq$WXux_`+$1DavtuP;c&hc>m%JGwutO$jUM$_%C)Mkw-?lkAMa_<QMyXu(EHyhAA#Ze{nu0bpNZDVTerWQv4Se=zseX`jx(VXYGwwjNq^S*I(nbzji%sJU@)2i@9Os(O;~W-uvOq+J|@Y@UPXIpXp;X<G*r~31!yb{l)<Q%B>Q}$DU9F4s8A8%X&WQ!#BWEnH)MEjNh(*{0S&YYnN{*kFf>{;~dHOvZyerB&z}DKw-Ha6GObloi2dG@>KZp?{aiSgqZaDfmNYTVFo33|KjU3b00|OWgaBPUD3O4go+slzz*;-%vf$5xgrJR*!|_3YqxIDx;}+w4{kLQvgjE-U4)XYUb(n>`F*PR8}@sZfXRwR00<1&7o~_YqoKibP(VMiSz84sW5c!tNY?-IG%yMD>sFo>m{Db^jR3Pp-OJ<2_+26zOkgs|vi{PUwI9AD<LFh$$Wo>hO{S^GU!qOEa7&)^Eq+D>hAw|wf-KXEg1BL!Rsk)`G^Ge#3M<RxRzx==%4ENlQOgXj98uQ){=2oWPO}4k?amkMrOyM&66T1S2dd+sw7xw6Pu73)^y<fdrq#(y{U-KFx$;fmGWOh~D_-;48!%=oOBYs_UZZ2oYjg^+fEE)r!AttRL3p#|#6RaJ7yvdS9(g5^7;B#{f}wZ+%BlV*uML8lfldKT6a}VSPu~(%u9c(BRxiKKyl?G`my(0pGN75xD_0g4!J=3_`{vrhR~1OJ{zo^!>|Fi(H^dG;qw_eh*kO?`j{tE7w7Pc(cElBEaP{w?j9pv%_~a_i@mu{LS)X0d#Mw2>1FLQEwPdyN2@OsGtJI?cp7lR|h3+hTNva|)c-|G*_xIme`wZ;VtLx`)^ndsojaT$fT++7?8#wYPV3VL{s~6r$ZQz%#CCVwgC~--iT+j#xM(WGBEwYqThp#ueZ<~%vONdjo@7YC2M8lgS-(9-*-CGHVPLB3)P;B08K4L9B@w-I#mwvd`KlQyjM!2vBrq<VA_y4wx-8}hmVxL22*RH(=+gDC9ofAqS&9>ntgV@%V&#o-K$WyM_N>_@!j%ODQoMbt^{@&_eFRy=wwwiPX@^TynvaSE+h4l|U)Lp1Z)e=`+fAKu|P%hB5p;P@!$i9;k(v&OnJ)x1H+}6HXP6#V?-aD@%JGym)96L(RF_T|>OWn|*E`RqrE?l7M%U5W3{gkj<T^4ZnM+JsUZUVtDphI*|Cx5L17sQWmkfQ*du>HI5CN8#nca{?VvG(^jSI^(pcH4*`a><1w64u4eURz&SR$dKMgkU20s9k4#i9EdbBgm1P{jV0`UtZ)O8|4Zg8E}rpsab5HZSvy%4_~?e(zh8-w{T_c+gE8_UFEA9%Dr|&im;L5>3BikfAIsPDSAg<ybr=1_?YU`%HkR1EQ@C(AJevH|LmpyOLv&p(G|_BwCX;m<H_s9eLj(-Ph?$+vBQg7r~jrS?7+m(uyy^DuVsLBIfJMGu)FueNBy@K`fr}e!t3r|Imx$TCAzNv(h@2T$j#5E=sMi&I32fCD#Ppgr#@c&=tBSGrEHN5#_s+X=lC+9%>4SfBEpVt-XS^IPhUXTNhkh?pWOfcvn;l5_1q0w^DpWqo*7=J-`!A3+BJF45;)X3*dAwfxE<d_G=c4ME=!>4ro!#$G7(6EzpUN<0NruO8u{Ka>LGL=@cp&d{;JLp-eysjc+44cM|R@78PwhCmGi6Lol7xy?5fpKce)n88JN4|`kP)FI|`%HPCzh&Rv0swP6~K<4+6boGg9_L_24=5*`0rr&L0Lh`{-bJ?0hGlVKDW%O}+pHs|1^dv0#(Xb6x}bnQ!*4jk<1JbW@UN2Q%OKkYt7VR?cQ2_fT26@*18{qt#S3N;$s&(8t$5vjEHy{rN9{(?4^oth2vRJYT`rbZz~E^Xuo{hEcA)bAj}x*9d0-dh_deZRN_<#6h-p`Fohz^;gbfX7W&RuM^U6A~IW)Rd4ZhgWSLku=p0;F_($zur#?41{(Y;z-Q=~^i<WItcL&s<}WQ#Z*$u+xw*qWsm%6V`0~mA$ukwZ^kLC~>VizBM^E<ud<7O<wkLF*?arC|w{NQTm+8oeae|<GtiSsWYIySc>1A#ig$Afrbns7ezCg2m0e<AppU;sR^(k)oOCR08@<!P%8iXRuNL6*LmK=6&6h)|aQl5%u>%~i6#4*6CxU;f&nH)i<64_UZD6A0v*x6wbhR^~1#sM#v<ObU5%>o%hGu4+OwEKwPDz=W3Y`6|la_q^yH2@D2gb#^l=FRV#k%#?-TWI!ZJ_-}|FmXum*<k^Ec>m9*$pCzrROz>i@I#toQWfNp`uFVe%i|E)W&pyGoqxKBK1_T$e37^aKm=2E?bd6Ffnfk4CXSEQPw)1xzd2$QqCN!(nE8Bx&yeojIZ21ea@S+F1VXX+R_>m83NiZrobfgbtBUDmT;1mcY~+Iv*RIj>lJ^TFhs%K$vt3P(ii+^XoKLHN>ODT0$iWzM+3sI_J)12(dd%e0ui@u$jk&DJF<mLbQJw@tC+~j4C&s1dM%ZorOJC-4n^BGOtT@Sc;>3yn51rL8Wd')).decode('utf8'))  # Replaced with compressed JSON by the standalone builder.
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
}


def geometric_displacement(z_norm: np.ndarray, theta: np.ndarray, p: dict) -> np.ndarray:
    """Return bounded radial relief in mm; angular seam is exactly periodic.

    Staggered cells are evaluated in three neighboring rows. Their compact
    support fades to zero before the row leaves the window, avoiding the steps
    caused by directly switching a row's angular phase at integer heights.
    """
    import numpy as np

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

def generate_vase_mesh(params: dict[str, Any], layer_height_mm: float = 0.2) -> MeshData:
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

    if critical_faces_pct > 0.5 or max_overhang_deg > 55.0:
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


_STUDIO_UI_HTML_TEMPLATE = __import__('zlib').decompress(__import__('base64').b85decode('c-rK>Yi}e;k|6fIe}#9>P9w9Jnal^tVzH{&$0AwPHB(hAk?ij2=G1b7nUTzBW=7;hM3PMQl(4uD2MIVma3^RN2LXGxk{}$Q4+ov@7Fa<iVEdoUFW8?TGxJCIEAqjr>Y0;fx|o^%FmpFIH#avoH-GZ^!O{NdcW)2bFdvV0KYM~7Y!t+oPb=r=FW<a8eYyAQ{MFu@7w6{{){jy>`QYX8;r{8%qc@Zn<Uu1JhT~8#a{ATb>qE#!$YIcjk8zj>tTznOEX<!)rum?;U194oBMz|sbrjxAk~FWdUJ~bF3<YnZem;EK53i$M*q|SE7R6B>1*1mR3r6A7cC*C+<xxHgcaPFuz`hBxke%eyev~{}=joq4$?_R~?xabQ*FQVc8{QAntI9j}<7bRD8W)$1U^3ZZzi4l@x7)qPGI0{b;Rut%POGz}l6yhght$qyXS>@nQX9kMI!rOI*KKtJl^4a6X^wy%wjZ@al`MPT$P>ig>2@A!09EcqLUlXsjrO+69ZsPQ>E%UG?QGOp=V6_7yLHxTZg15@nI!FpX(O9n05PC`x82>^XqkC=n#7lox6$6%-V`0o!`r+u4x$*+!*I|U80phI#J)cYg6>5}%jidANZtw`KHPrDlM@)0M$qfQph8Zo6>LA+a&i>GTCIygu<7P!$siZ~Y}FZ15B_XzVn^GXHMcnLn7_itwy2QhK|akI$ra)4ZEtps^qU~Xz7GZ$-B!!U>7`LlIh!!{B4-%%lN-^@7TccOvd#wlkqr?4HM_F4Y0!@VR0ibQn%o*`W1#FKD{TbB)9%Q`L4qU+;%tXq2WeIG9aHP9auQx9A^ZAerOuF@M`0tIWqCNRvuC3yzIq+>PU!b@Dt?>*TP1b&^~E&Kr*(!<8(Ek}gPMkGoW#ivtLz6b^ZHT1_LF`H@b{BAOGZJ4Sf9U!GL7T#aykl9$iphxB<KN~zyHjfbff5Un7gx1=Q3^94d{RNtQ%|&9u5NktP6t>#>Sa-79eZZ_50yQ*ejcLy@&mFzvr8Eo4{1XpH}lxt7PK!H~YPC!$0vZwtL;)z@2#QUZ>N!@JzhT&8^nMmNW4lUTkl9rWY~z_M?Xv^CsTIM_U&QCteo>OuIu8rrlX);%OB&Ha!!seeo#VxbRK9{-f=Vf8zBYbz7ayB_>{*hNaFnXzsOfWPleR5aV4Ww~Z{ii;(_eI3Njuj)U|PsZY2kLBCIBT2vQT%Q}?r&j<*uOE5EAtzTl{VThbv{6^XiM#;?%8%DriF{WJvy{pSKnZ|uNdHDn&+Vql9lFD?&2$V(ha1e~6(M%RlVxTAhJql4$G&i}dfEgb)RI{4Ie$xzDFC2wENQ;x0FGM%t#Z{CGm}6Keht%yL#uYb$WwlQP*x8XKvtF8vMi)V<Q$olxiIIN3_f=}-DG-8>ghmlajX`Rpz)PhShtu(eQ&EsopI1Z`k;26&$kj)4T7-aiXhM{L*EpTC(#15-lNc2f5HTP;iKtZB7_KNDf<(=&QPNVyxT_QZ-ONaf0R|68BLdlvvdJg_aD!1uRK`!3_$lCw5@1+>G943>&E-n~zW#uH1=<;O^cjrbgLQ>%$Wy)OfDJC=Mg&U-5E5w+rkMQ0G|QvGtRXbF9Y#{WaS`S>A!qr^V1l?gYp4nJ5N4@d(!7&`765$^K@{f+h`Bb@gmowCTcb{rwx%eP4O3X}#5}%(WuPD4?ywG@$juAjw0;ATPFCtJbw(`D<0x(jQnw^pXde7OnC6L&XOvtf`aJ1a6Gi^E*!7`H9-Ps@te02>8dYs~H~ZmbU8+v3^~<`H<}}_!k9&`0ktJAETSZ+WlT0OnjItQUmgKQd3F``3EXYHedbTQ;o8&K`;hv(ACO4~(tB_Ylvx@0_BL?dsUzT)%+f@QL%yZ;Lm;-#-XbKj;83Ia54^isgq``!vx(3<Gn@m!qOtJ|*Mw<`IOazOccrm4W){F_+<>Te7C0dfCz!s;#oaIVNpe;cc66_HlLD49xO&WZLl&}f0Ge~+<&J)QrN476kD;+|qaBfb3HE}Q|ku5=^m=?yRSwf={Di`gxceXxyG)J1DhPvY5dB}_EpR?Mx=WrORGq-Y<z=WxS;yAgjv(2sRn_9UHYbhB9&6uVcwque+k}~s0v#wD<rr3k6kBz?O&L3Doq}p66bDeg+K4rHc0O4}Yr#kg*kfdXwjf{dk{H_W#_HY%!yf<rY`d1NGYjn`!EFrXZU2U*CTVloaX`w`mA_G*6Xp%+Q95z~M{yPoMCSi}yWp~vmLAa3nJ<2d{I-Tj!YAUgAwrLjkN}9CdXwF$Sjd|+V%AL+S`?FfHEoqEG-08GksjB!Em)Gr#g&<C`*WRsn2_@zVRHIH4>wrKkgQU%(G=be)SnY1LKvA)nqo3ruTJ+G=iXM8!>?T)g=c?x#-R#jt^jytt1f)`AtLq739DSfK^7uXiVGaxF7}YYgiOW#SOCR4Nzk<dvckx=ZLA3;gm-`p3C&t>bfvbtN!eE-t?XB%>j)sLJ!dIA`ILWI!FfhTz2n0#Fre&=nzD3F2X$m}i9q}QWzpPMYS%K?3s6pm4)F3xHI@thrBN&0$7CUmR+K7N}sG7kb50yF#Mfk*UI$gG(aAknpTA(4R*jkvxG4}87rs2Kbl;s9x>Gp{MqgHwvzf6NAsnD9V*aSeuYL8dbS{4fWGJ$QhYrdS8MOWc^6Nqo*&}i@)COi8!Nv~*@u@@-_63u#WqjG*McEeJ|kwV>EU@rj#2|4%#fij-pylC(}9>}t87k80R9Tb~tcY{>d_5en?yR}iK-QXw!0B%3H&z{m~=>pS)4?SVWby`<xQ?c4F5Wu1~mDa1PWq(0!UY#4Y7LI~!d;>@$wS6T(<m$2l@iapZ=a++|cg0>O{gAy0uA|EUE3nhxB4brfE?6CL?GFL%Wyr=*vPKNmhl-6H3mW66_J1GQUS#a<#Ey?Tvr)d#%O*DDimy>x!2?(l#=TZ)OP-dRN>|=2dewQ)!i<1OWzjVfeYu9Eh_A`SyE;*{ZQUHTVV=HW0c>i!v_B!qT-L<-)(My$`_RjbeZfvbp@(Xs6e%!YLHUT5pmD$UQKtU3)Hk>S1xog(uq1C8SS%Zzt!(-Xcf^32J~o|9LKvPb^c(OtrQTZ3#P>5YQu{B0{-xXgR{1O~MyZfhOB<rRljPo<Z*^cH!@o_#EX=b)Z<tU*V-Ssy=A|ZEVms95cbK#e6w(<fDFF0_(Ztk(yHX3bO#++c1TG`yhi#z>>+L*A?TFy_M(386fVJhUq+UHwj7ru(oy;7N1=?B~PQoCscIr}NYjJI@W?NIyOr?%KTAQXO=g~%__S7j1Im9?hN=_2F9;G3)323zPw0vmou(t}<`Scs?LU&ow+PdLbTQ@R$;YQt27;qHT=ALujdkd@~Fj#fLDy-pIMq+6UP#gve3sSdbnvl9%ehuy;oQY}8AXl~@%TEN2!peBNtXekbl*Mm4UCH9BwG6n_ZrG#dcIoP;q}E4nMn4=WrMj5duo(b3lhec|mz^$em=F!(mppf}EQxLZOx`d>yKj3@c=>F1_&=CqTdpA2TvW<*Zjag5o$MchEiF3Eo$7Y8ed|FMT!#$-Q~G;2TQc2BS<+-F%xUz@T@fXr?Cb~GFr2eFw%XE6CSmMT8mywl(W<o{)+g&dPhHE-r&c(6-SDd^LW||f(@A(aMpE|qhWg|t%6mh;We6|lIWqiF4wF0DCR(l9*wA^q<xN|obxwTkiTktfhf8<9qHn8dXnreO=YZ``Qvk9b#MeQ_o+Y<5&OJ<Qg#9Q_Qc{QKs6L-wWhpqwYl8a)Z*7lv!C=gb5$u@fxG8lyE%T(HmnK;@3?e=R$+R~VM>mo`Xg5Xpuq}YZl~W(Q_cSK!_9}i$O1Ld>TJmjB%GtQ+b1wl{jTE-q$<*V0w)lM1hij#MU`aC;_-F8H!zj+({jYSJar@to#%e=(0`!EXZ69i;$%q?JdU-lpu$3&gV06{q9HGF#eOdzsA{hl2!c1+7{_bME%Me<dt(FG$Iv5oqVx@hMNrHGf*469Hd5r%N)|3rv6Nc7*=|QCJXh`Q<*%6?<z>f32=<|m=9}%Q!9OY%Uoiffg^pdtTsS$0@^4SFD9jrl@VdY(ukY;=e{HXcx1{2tZL!qA5XkS{1_}yI9xyf<5bx7thYb@xH=AcWzwVmF5yV<q21l^C}T_8EVqc~mjkTm@v+x#rRxf8Ns?E5d%;9{O@M?1SW^|XzEX8okgRMj@WNW;bIX>xfvGF43ay0TN{k^)iLjdMcW;MkTi><H%yTchZ1SYy3ic8+7AEcOY-`MU<Ur2{qU7w+u-9cvWBHl%!?v7F!fioO%unbX3Zor@5LUD|8Ks8lMCOB*g{k4@1H>F+wom9|fcPG{L^rA?GlW;eT_57JI=81}AUH?+pwF<9)nzY0i$Xg)uV-&EUM(mxQV4+!%q6yNLhfCzZx`6`&9nnLG2IGsS;FF4_`mB^2@Kl7So7Q5!k_BO+~@K9O$Y>j4ic>5_1gpAt+OS#|rEbLDA%;qj_l*C$e9(7OE>tXp`)bYrc_<(1xQ{nuxl$KGbkEOHD8TDIW$G)VCj?s1Vd!%{!VQF<&%CQ)!vD@ZjXZy1)yKS1U(F-4_vd*~8llCJzp{4O*-2?WGxDQCvS6vPST&o;EEPIt<fg1`=X;AN#OH?mPd$3#wIZ9d9?I;H*>z1SL8)aQ_)cm9TyZOtJzLj5a@6Fxm`!?;i&huWwqB~^kr7nPBc!RDdP;?YcPy!VVTfF$L+;kx*8sRn2Ix8BlZWL`wZuu51LZ`#1cNK?O#{P>bd{bwhU$D1f8jVBbr>}6!i;Q#wHKd91ey5+xFIdhNKJy5$Iu7;QJU6zj%~rSAY}u>#&v*p7qV1ydN&Q(A9hY=wS>l*%nFBW+^C$3nDY+oAipj^@ytyaM%Wa$ajKG;vW*FL7(pa?wCw&ULj^Fv9WInAjoJ$@&%pEX`unQeFo{th(&Em^q`8(qFRj$T@49=5;F3&1=$2kXfa(x%RjB}lgOnJA=Et=xy3#<#hDhhPgV4cklY37=|ZVNjZwEl7wWLdcqKAiT|gzcxvL^!J8;xJ9C+XC=M^}*6j2I7RSxZz$?4cBfO&u#faS@p5ceK!4<2;1`<ZagYEb<%a`(V&0&1CBW~{0JvW_qi}8{GB9iKHi#C!2CHpj3lncZ5qs0z4kZHdaJ`N>&Q~~rw4=WL94~u-TPc}@ZEz(VduXHEv#<MY!aoQ)T0Y@<06RTu;iS5j(n90ohe^S1>=^GU*0=Ko(pt-*0v%{bWKs)d2G9|cjqi(OI+M6)5qWYC<q(1EV>Zxq4&Q0>j#ZdN^A%HhR-7e3)Z||B^$s2-3?%c4HY=1Z1tYo0I#=72cdU59P~!9a`b|+Ivn-$l60Hj+*)e6*7qX5HMTd+mqh5-59Gy(GW@Ih^hrQvZABVqb2;Wu!=b`|D?#f-;X_rbkp2w*6|I$4{!(AE@-3Rx<7E~_x7G){ZAgG6r@7@MSo!v|bfpH01sBmM%4h7WuMea?4oZu5d1wh`+?rnU@_5(Y%skTK9;|w*zEv{gu(8};`tc8z7W3deZv!mjmw_D<;$H=yF#Pr(&OKvYbQ9nqKkB#9G?Od;f&e;4rv-nudEl<?Qt!p&s^$f}V6ACCd?d~?JFQaKVjc8AN9V&i&<nrIPG^zdr6m5!uIueVivRRoWpONt5XWJjM!nUXO5W>L8&@m%)=DQAz5ey;u08GMeWJI>F5`#+$7c8Uq%l4HA9czc{dJ5q*~=Y*jKyqgu2=5@UTt@4j&|Cy)@)mco42GG9ax^JMF7i1YNXEKVUUl536#AI<Gz2JutZ23kCa))L-)QhYu?)p_iN|MeU}$%WH*8I1rTe~Bl9Hsk(UQL)=FhM3eZLGu-^zqA)bHSZ@abG(bZLP!0kUCZfuH;q^XH^I18)8^d($wI0v=6h5N{(R;?sH*MgW;$|hrOS1G{JmfWrys6+(EVjbV~ZOG)^ozi#=7U4g5mnP&i0UkuTtM_)a!{KEwclo1xZf(}eMT=h0Tx9K0Sw=5eF-(R{ffBEOe`~uPrC1)5^0-Grojp$yJg-9ClAqndT0<#6`mT$9RBzZ-*PDlPL$bgclqSBTOQRENA{wFH%7<tfd+zF?`^@+nKI@Xbb#tcgMwzv#Q~OlcPV~8Gaw<2P%RpdG;FkBr0F?)<P=<HfuHf-%wcTtzteMq6B>D=6P!@t^b5p0=O(27GhPV6#9qKz<nB_E1B`!_Z;9)qzqiyJl=W_7kO~{f)iW05I-tW3WWgOn;jEDbPP6s}Qt<2WlTAH(Bkmc-60&E%ec!UXZvBG41X)jjtL3A7T4a3vcYAd<ULwHw#`%M@QgJoU=hSN)XYw=mexL><}Ou-VvMQQk^#UURTollulU(f`%Zr0TAWQHd3=+Ps~R{f}TeIp$8ih(p#1x4`o3d7Z^xj@4-P0GU$I{G*8+|!TvKS0a&k6yps+dpL|FAokI2S@wAX0MM94q5dt$QX=9s;3nUGg0{q1}%+)6orlS-^tjMr|c0%`>P?WkJ&byN$4SUX1BwNAXhIfWd~BV6l{#4TvF2)7ga9a$}PUEvNs^n3j6l*R@ts!V&*m4#to*8&9ZC9E5@do*A&~@r|!OXJi+1~YW8Ds#iI<czV|O5+2szb-p^~keipG(J^e_*6S_wd*NNn_5USs9uH8a$%{OyKs3eM!WIw?=t+_B{EUEh35_Y_(V!<ho|Fi%p2kFuK-6_mFdO1oifFb6UoJ*)V^_5Si9{^90)P7olC2116q*<~#Wzc>>E?Ocu#!AA>hA3csv=$cdcpI~5G)$&wx~|_70{lc{N0h`Lr(JGL5#2DjBKdOeU!UpI<3pOM!INVg#atHD?+fA*{)8w&Kaf$NAs?%o5*Tk_7+;5@WU>N>=(S~kOM3TD#vwivQ`Pl3Qc$S88<^W;czcfpy~}v%j;gcWDuM-ewzOb@En%T}4~=`WF5ZKBvMyezA|G&#0L5!osD-Jwu55__HT%&u>!A-Bq-oDJKo(<9K5sPG>Cs#E)#2X3;W2A8C{?_$VAkS^R1Jz~P_<VIM6NF%Ul*t_QnH>_?02wKJ*b&oUve$sX{EhY5$X#6j*88*<o0Q$g)S=_@LvUY-J_=!9FYn`U!f}i4|`xd0^UazS*A7w%uchTlF-=E3nou1v}rMte}KJ_OfMP-&6@=IkoBKdUT?GRaC_8fH#gZvbF<fhPyE+~f1Bd_qvmF#`4GQ0I?XQIXh6}dvC-^et;S|!qt|FRHdw2{%Rup00QIi2?#H+VATf%65B>p!ZT1io;IrLkExi)3&-JAmigg%^@^RtM8t4Py6p?Qgn1ldkk3FC&o=48Gs8N?|%Mo-6zBQB<U6JrCy&Cw2ZV}>)uAo#Nh4Cd0=5`C1A{b4PrQ&{&v7_`dh+&JJRalTl0YB<~S~&=_=rU$+2!}x^oi@e~{%i`hQ5OZWDLh*>*eb%ge18=EZi-<e(|~1B+)I-<x&xIk8skcnC6J8wFap+37!vJd6!p{$b7-uEqps}QH034j#x^*?JZ<DT?sz&7jA3zec3*^`R7X9$e)5**dWPE%n&PedVe_orfA~9$v+&bj@jsg_HXbubYc)5<V}}CEQ3Qj3m*Auv;u?Ob1o$nTLKpw=&;BnH_>*-$`a%?PwsFLw8Na*YV=Oeufq+R=gHWrNp^_CFeGMg8bw5u>Yv0%Ky+dyPgLeH#vn4L@G+YGyI8?yDGlBozLf|mxlQC>F91Lh@vDtX{AOGgR{XhJJL@QU+-i`^vc{WX9U^1Zm34RMhnAweSIByJmJqJ~8QP;5u^z`o?V8V47f#I{0!j)MEhl|Awp%m&vn@nYLLk4>}QwF^PK-1tdRQOfG?m0bX`Ssq5!}FuJ_;%&V`8jl#kd}3jyzl0B@E}O9*gAVf4tl$P`0M}VWnBEid6k%$RD#01bGrBJM5+aGpqN|j8qGd(fv<vvN@YPb-KtA_SZ)rNFLf4*i_R2~d@j_P=SeyatZtM;*TE|7*M_VzcKMyyAiEcQu6x?RdFt*<F7bc*pObsS=6e(uI#1sf7r1obPu5|$iV=Oi_wo(vHujHRef|0k`}XMg*C%iH_7COIqKVbg_mn~_M-joiI(&Z0IFKFo_W1DR@brYOv6GjtzB>B)@bvT$eqd;zuaCbuWQPYYPmiQhNwbQd*a<vE{A;;$@T!kRtY}@NU}IFM&R{eO(;3}eR@f96oG|*XxMKAa^URe{M=pcJ8YQfixrp&<j1Y9U7@-$<nhe{Gen_FQMoH$blb%T~E`S$N!u+yU3L`0e#Ish93rmnVkf}Jr7C?(uR(4?^gVA-6+VarRjtt^j;m!*BTIp6-O&w4#Z0H<LgtSs+a0_+=u-oc|!(;@~>}lmqG7eF<;<cO2rlI@!=nc|y5T)a}1m{N;4#{Q2C5OVv6)a@;Agd8~R@alPaI_VFmqc+r>Z~DadjV{!0@PNu_Cn%0rtO|4{Ur0XcOC*Aa>5mH2f9p$UBcy0e+%C}49#VjaL+RbQIP{WYBK)m-{SWVLk7%+>Y{^6rtj_ty<s@{>Hqv7Eco=LgMt!wUx(A|K1{?-S{4h5#9gbhuFfh+`;2yT%3{a9U@x)9!Xa73f;*(JZ*xR&Vf6c1rLcx}7ke?qP^e!}qXTHYR}vT7hh#M40i-JiDxS2vAEiBfPS~^Uu_$TwNd-i#%oj<MG#Q8pIoi@Cf)pAvn)esYL+7&mE)PDofFBK16!6SO<YM5(b~y=OMb~Lage>LFvXQmJ1=`dQ_vVR%v|xP|X(H;jT7``W_KC>Pyod$JL8?XJvykee?+F`MG2xhbyWgYF2<}pU`fK)ZtBHG7AAh;j7h?u%zBLB=ZbM(-x2y%;xA^3V94WyG><|C!UvS1R;R#2Sl**POG@eC~p{)sH0&hpbnR_W{+8|1jj7^{u@DZbxL`=?P$^vxbq5K{Xofl>-xCo-#q*=mKq>KnE7E@l#GD$&c#HHgJ>u^<^t>Rf69z|9>EJVHHNN|gfe0M$`J5tmX!a*7c|LA@cP<Vw5A9DT(ZSuA10)+LsL{!!|Z^dvlnteb`L5>t1T$ZkS6GT~lFQmNYy^zLX@9JJSN73Yb0Mb4z9rO}DaG+d-*WqX`>ljsV6}n77Ux%OBign0}js9q!ddsZ-ufuG}j*HW_1^cYxT<&LG<TbRrys<z1Z?NHpV(fJ=8V02c^gI$4K+n-yGs3lEwQ8`+<WVmel_^@z4>bJH)R#6z9D@DBH>ZckYUlkDf9>s`zJy(N_kewS`0T~24*TZi;kR#(j!#Q>+`3~(vDem?SQXpGT}Jg{PFx$k_-7jDoF<dTD?Ac>9pt$E9f8(`VH%2Ps0AD8ykG@wFl>p1X%4<N#sY9ft17K^x@Af>z+}H<LgW!g2;mr1+EE|X#Vb?e0S#Pa!a^DXM;&JTXF!JgC+i&09N2&z)a4}40|&B}wYwjtKmF|(_=TN{)MbDJlpIttXwlf(2_by)aj)#YP10TnJC%Sv!{CzvjmZ+gdkJ1PJHJSi_%3vS^W4hrGs=c>y#P({FzY4Ppbsqp9k0PVKq+zeAOGfm_}|%a0CM9uY@NLYq1z8x^_2YNe){`f)K6+lAQ1OC92_!z_jNEKvkXQJ8NwuI)qnVR9>BIe)>YuH`K5lH6KUJ6-}pD0aXp#SQ&&Cn;1jbjvvJyJR5?KPFaJ9jr5t85DyB=|Pz0QhLeUdC^S>%$E`{L+l$}N3sm$&l{`p@?VZH?1ESTbX+5*U;6tw%l`M=p))Fa|yvI2aNFf)BupwL*#9XSoy$a&p!Se)|^WXmDU%jlM7&NBEXQS71>#{a!3Y$T2;-W|~GZ~nb=#$l}VB(1+nupR7#oaT50e-%^bWjsjOGkQkJ64@k)9Y4Eb>33c5WKf%m@3c;o=SBH>1`N$V|I708J+lTs*o4L>AciPshmDbC80y7rvd)^_*Uxc-);u|V#bD2yhnFBrSZ|#@OF%5{UBHSR*r!bnv5uyB1GdW-VV{lA2qK&jeblip6BRo<JHtLR`@_Hb*X8{#YV$rHMB^~de)<ovPYQ2)AVS70Vb{2Q2vG?tPMtq@U|PI|*K>e-#PMj!k+*h_$Jus5`njyVyN4UOAZ0)OYt$rzB^VLa27brq6_VDtNB#xl{iMg}@KU)(@Bp=Asi7#pQ+<jQ&Zs^n)K72qYu}!Oa(#C@?Vk(RhoYtZpdZdV3AgSSS9HAkt!%U&AN|@r>^4<NtKr<RSE6SZw{_<!+WMW~irrg`(*@h0B!STt>+(8#jwjjkO=;X|cQk77x*lBDmEBHr1E6)A9k1oYuY7;Ju8lz)56_1Qj^<B)4V_985(|qvMl~B$)88=wx4rpC>Q+A*XNH8Rj>omdeWGgq-n83WKm8T|v(@_fJCq0o17?TR+g|_lZ*CWNNmVT2zU}75Km5C&zd!s6OJ(<YGz#zu9bCQg<`UB>G(?=)ng4QQn_d3=eK}1dJWWrdpZ*s2%q2&iMmKV-Qo?Ah&8vld@CihOjrz5?%3aYMbF>@Yu590Z63L>*{cfevY4@Cd(Hiu(dL7*VM!U|+0M*YyD&Qh`cncq~6eA@o!%CP3gY8~-dk*G^s}%deHLXVMi(ou?Y>4S)mK7QylVYESkgeYKW|w#85C8T5va#u%h4-M+1s)L)*p1CU{N=yg{Ahr?eF^xB%lxqqZYe#r%PR)gtHfQ)Iz*a{sU+<OXo3(<5bP}|3v;X~;ucHA)%m=eBPjl~5@ktc_hmL`FH&B2kS5j{03@ID)ZORkoEzQ;Y@SRUpqRD`8soj%$#3B}Fh%k%o_pS_`;n*fkOmvP-%W#l>iPnBwBTpd2zD@q&6x10f^8VOM&co>cvh(Tjj%5QBP4@p6teHw8tmlK=niO&$s>>q<XOtTugzf)ab0PFTCB$(t1vv2d0G+YD~2DKXzu<rr+uU;8*HZwd8f%Vo#;26Jm;Kf)qtJz3^up_(?4bVut$a6s-#8rZI}Wv*mpJWkz`o|?#deA!+eMP(tq*)u;)P@1v<sQ2lVI>5U|Z(g216$@*XC#WP|ArL$8Tp6I6?|ms8}1j6bS^mkFL$TI34zw9>}&&@2xp@KyOnw@jyJwepTGMjlM^eIX_GxO?Lk-q_P(Q;SRWpnweqi#C)<%V97Y%stbTk>6aWrQOZeFBe-xdbA@SxDGgjd*h|9c_(VArT+Nki?0e7xo`Jgy@D<4(c8l}FW<ai)zhQ5HJG2Lhrc=f`uLE&+WYSC7#-*i-+XiU3QED(7kkGCy!0AF6aUehlO<i~_-=PKAG&ta4hjDS%vjjTu%ijT8&o|Uh1UVT=?F?G$XS*QL;#L`I-2~vHrMA)-cs_O1*wHqztdbETJ;mU>EQ`AHB)YAxwb^cplKQ`v0tK%tuS+yIg1?i60|(w7I)4r@B=+Ys12|W9VItQJB*0pyWa#^!myRcA&F5=i*U@S`^z|y5O!{OTkJ(5${FT5R&BFaQ9KN4E4Y&o_T*M{yOB)L&+`+U_><)$mvd#|$-n+~0_q5bwr9PnP$}~c@tWRLV0%GP4H$_1CTvIA!p`6uv1Ngq%wpgG2IhvE55?gFzR?7=dP8{5d~D#`2z>h!0dH?2bo^TielfSG@b?z46zQ-(`mfj)ns)IR2j*w1xxt5f38w(A+AiYZ1=CEJ+`ZF`&N)_}X7(`x24&H9nnk1;+#?y11XG110Xc?87|v`uVupmd#EsK*Oz)>8{9K?n{UO1SX$kx3-?B6uC)ao;FbPKq8=!*M2bH^uCkM4A9?%7hN7Vt1nT`>%5UuMhz~v&TgDQrRhlT+Q_yGg=MBv^_{La_st9y-zF5>OPb5hBc_Z|^d#n_MVrLSzh<Pt+chT0{#u}v(Gyf{Gn0?U5-_kcPn!ywlM^<rO%2cE8x($>Nlcu-&ExM$-e$%lAjD7dCOcKb<2>$V*7-+Wi%g~x;83Pi?(YfhUCExk9qlG8vS7XpJGXd~|~`BdAw2aw)9{T;W;Zb>`WsiDg`>)F%R)Uq(R*@BQBdW=P!uuCqXTP1V*BMx^yI>+bKmBR9xT(8*$p4`#wgO9|VoS$Oga}<7ItkkSO{?LDPQe(_7bl0TAaXL*7#6ezhSCwcTUq?Ro=MN?_HlQII@c%^uLy7T3JIHtyjUytjJkUU*j{~%5jJd(=qm!7LpdE?WRQ}niYph!1;PyNV2BD(Sc|W|orw?PN2}{EGBBI9=*~v5=V5o*u86u*52V2}5{26^2-8+e*^*{Za>o8hyp2F4k2E80ux)W`4HDswhsIU_pM;GYru+H|;;t=4yVUYc!V3I-V#S9kzK`<TVu&!{E!dgMzL6n1ZhGAs+5LAR@)HjU=CiUbqi1G@g_^IFaDW90~RZOk2;8OmmVmTBSPVr7=W!L2U;)zMnfBwh+D9Gsg20%gkCK8X)eH@OWaG=g%e9p&nCN@jr9tg&(rxl9b*UVs{ew!wf;F5w1R?$>qO?7Otc3aAw>5C`!edMHkzp^sFd%Bn$Bq{gpRLyNn(81AC`%#3d66dnS?g_{aR8c`orxb6aT|ZI}F2|wNBMePnL-Z(5;=a*L0q$Jp?H=$i>^TS^yt3<hFnVE+!eDSt?_g(M_<H{CEBL`q=*Q9sdMUcdp7+Ah$dAD&u)9yc*gpPR8VAn&uzx-Y^PmKYSz`A&{bX<H=hA58b_X^uV=oq?z^-t3dxpQ3#*s#oi6yxubdj}tOrIb(<I5F>AtB3|kN%XiyN@626(oXYR0h`dRxMj(<x<mBGoaZIC*_;VC1DVkoChL+&WFM&b)sJZQhq}hO}rY!(m*Cdx?J;NK(aigE6eJb@gsm5NButX+(!UK2dd?8T$7A@*GpUS_(I2`4CCPBczA#+07_`7k%f#KBrt5Kh(E$$KMle~Meu?pfdzm$gcV9mhvqVuZ{{1+OZAMDG@TDpGQ1$>YZwbuZNJJ<Qpr+5WNVb>w$7fXQRer|@vi9~sE;h(ieUdlGynM8kcG-i`Gn$q_y8Fy0Q5j|=J&4MpXRgk-mG^Yksv^1!yuiM+!|XB!UsrP0b#zlU1qwAy`P8+1{;%W5GU)5M+;lL1z};#W39^<*&SJNgAhMRRQMqL(IkavjEbg4F&ctDF*(5-`6p)+x{tV^u6%&B;Ps_`M8h`{8o|AxiJOk+qvRsY?hAyR{|6!H6ul6%liT~k!N2F(Rd{n>03Sz&bWw&xm%%s!>G55X4Wlt0FWke3k#H~{Br^Ok{%Ar&HAj*N_qaj1$?}gRHe@sZv(_&}Cq6)ANC+RcMKht?e}ksrq#@4J570U!q%03EFT?bMru#;dEE^~W(cnp2?t9Gjo`CT|lf4AUA8oc5?Ew-Q6zU%QX-#<5(*LYyyzIpXOnC)@41{w+8LS3JsU7p%wD`zu`9rfb>R*P!Q}3HFN-}g#+lReu9<VBLVXc&zS2`(k&&opdu%z>p6%@~V@Kp(Cl})21Ml0#%T&*vM;PaK!pVy*8|1j>Co%7p(=t+mRyze}Rk;1TS@$m<B4g2$hp1uih*a-pU0cT5myp~@Y<{m48TKIyVgkXmvRz3TIo#MWC&XJ-FYyYzzDJrD9MN7%W^)yMjdlK)+y~3mj$D%>dFA0p};nHNXQhEOJ#(B9-!8<-L<P!%w>>v%IIJm?CI-!gEb4EzLjPSD#QGs>$SMZfuJI02G^bH!0;R%wJ{f5ir?y@qsFDO^p#p|%-aj4pa;Y8??jORpp1$k@9T7_}(!o8w+^@!F5zK*gjAKlwg0iNsc=(;+}ddhp+qKLfkm$6=W8DLyB_y+qiwCHfZJoFmn@ep>{fQA&5?<hkrM)tdDc#(ommr&TXB#jgH)8Av9PK>0gdr{uQgHg7;iMOQB%PpLXYA%Z0HK%?G)9ai+TUQ!0?2qh4_wbW@(M6zLPtpBegg$wRzoS$|KLK?fdlCo!3;iGHbR@8=@GL*KZtkCr<krjsx_qRGZiGlCz`|dYdoY)}HZP1DgT=(ymB|3c=qAS+UoqGZQyF1#9A+5pC?oG53=m>EMsr=JI?X~EaOtQ=(HPOoF9ZRBu?+i3R%_l*H|4Ev;z=F`p$b>o&4{{bG(MjncyUhU<?e6H0YDDX9|VD}W#frlwp=$p=I%)_4XELGFgpoznDoNK48=R~3<&%ZHRGdfqr_CeCj1HQqn1?uOYiD_8;QW~>;!hiS2OEzYVF#scsfq>!+5!_{C2i{`&SGouZ2ou+{X~F^u|=`xq$zVfAg>YvMdUX9S9y_NkE6>)5~A32`Flh`9_U<(cQV6sj;s40I~Njuzo$$=pwIs-W?C<y6u1RHy%pyB8STHyZidNa$76E0=x)smX9cA+J9e;mx>&E9L|@+tL<Qo29TFKc|)bevssYFII4_2=Xuz=f4bm$@soAVV9vEw{DDtD6z@drC*uh;fgL2hD}$j8PM*ib%zY@){|?A<Ol{xRr8kLN=5^hUzWA1L{>SBd>m859+`c-ea~AeLbF)0(a)w+4<r8qB_PmVbJ}EerUZg*9Tq$I`p2%Yi@Q_$C$Ut-*QgmC2YpH-{y)>HSyPs7D)0j)&Du2rlL+az(Zc#6<JpPQHn2xiYJv%x&J%79R-K(R$1NM}ipC29X@11|McXD`sa{Beb%cFBD@vD=gH|OV6Z+)G8)Hjs@Ub~6z)Je=kIPgHxFo#ZHDI8;r`ZxIC%_zF#kA_z<m;e^TNNBL+4p~M8o0D1X6SR-h=~pM`2Zzu1zJ7(&I^KJI0>t8P9O6SAJIr}{txlOrxxu%~Tg?_vwS!adP>^(yXUCt$SCm_3t{(0gAHDBx@LVU1^bXtFmQ~$I(O7kBo9EiWpm*4IN7mHiJ@2p$Jy`~D-oeXnJlP1+3@FT06^5DGy~#6yHP3s~46SDq9>4>(<iRKlMO~hDPEWN%#WOL3&yXyv3q5>SFOq;5Y;)60gI==khMD%LQ)e4(Jq^3SHn1wChzvLSF+LmJax&#Pzz#mwCPvG!2m(nZjWoL-43SK=t$Ro!SwYy0cLdWxVd-56Ny0xz5>0vs0$1t|(RC)zPIg!qyQ-gk!T@f_l%gkXD5W<CKubpg`eiwBLIo|2dt;huXa!*H_mbq?!>Q;LV^&vGdeQVwbE`-u^9gjPqm@)%Ur4{rR*|EQRdwDY>K0urCMj{A*4t)FB&*hwYlXM*_-3B3?Oh$X-(LkfxTTje{7|5MMUL%Uf^FQ;dZnC3G(K9~DRF?j+L&~k+5lK=<>VCXwXJ1YC*Rn%hgxUEc{U$XyUp?-WmQJn(BSK5f=0`nQ$C#FIz5ZiID6p5krPzVz=hbTjgIWYXIf8+2plkV>4Dm?FE4rW5_t797~KT3OuqrD<E0ym^n}wT2n=y|Q7_=TK}{>crjc)4lip!wCco^fLv?Hl8ht&t?KPI+4K}U;8iVG&00$IQ!c>|yi_!OwePM5f+D4+e?iFL}*hy)MZR<nEck%^l-Kb;1(kwP63(cb)z6);~TMQZKv!q}F1$~Us+s^SZS$U(5kK1RG{oa#Wr}V{s7*6&_NgP&_iyvyDV`&H#V}@#A6Sf9fSf#J1PsW$gU`AzY{N-jH7>(=mQ4-|U>tKW{(BK>V93^!&j3o4Ez^Z5lNd|ZU1l2cIxkwW9bg!`A|6V1=)6q!(4FV<{03Y}D#7d<mo6E61{*12_sKyOIZF@5vUxX>Pr}kK(|D2~bqwIMUgGyZ;)VyFs((51}Hu3dp><Ir6#noX{XM<8Qyo~>ULj?Lk3jl)f5F}5YLDzJ0EJFs>m}}V*U+I`SQ53d2g?(mUvS%D9|G8uI&j*#WdZkv(bfRSjw1hHE$Q@T}%{+OP+=S^q%(ki^EC-iyDD;>v4wU%a)_=^<pSSp#XdT9S9&jYz^g1p5N1PboFalWdvw%%N9)DJ>M$U+vV;76vSSW(+y(P80ng%y-^Gwo5a2iN9j28(+D#VJjm1>#_zRr;NK++6`jy@F%=mr1U<Z2Up!a90)2&c~RB(nO@inDh-8Sm0mM`6w)NNhcZk0&NbNLpL72OGUWpgb>l7QK@rf`IOhgB!+Yr=Fa;$=EToUkJCxzW9O=$Uf~p#ZDCpjX;1!&RPmJlNczyt<vAK5Jr`7QL6#C;Aq|n;)shM@J43|lI9)z+z>Bc%H$pK<s3P|+mL4JubV>MD*wh;)$zEbpvvCS6V#M?Z;Z>GCeg45su<5swd_>S_R74w0Wp}9o}w_s<KQSR<|1dT=46@;t7l3c(!Nv)MA}vY)LOlenA=8)PG=K;BZhZ1eI{Z91&W27F3M#|nrp_Npw2E}fMt~cScf&(1#%F3U(;(s5@tTdO@WbaHlV@UqFfuxX_Jg@rtw*Jrh}|&2-@%7`DS37&p-o{cLq*!C@sJh^N;6^f(&y-GtR`P-fn%|Cpjkt*1~U3SUYTN=yRbcwM(7V^VmEzNC6sjsNH_2O;s@|bufg!&B?yW9so&1!Wyq#(`tWK0!21~b0IZZ;<hGC!BtkX=Lk^IPlr3^5J2M(Z9NeM=Pf8``lFS^Tt>3A2k<amlVkYH6k}gf8tCHhb=eO}?+LFDV4CVSWdX=YwjmmsHfYeg1!#^$+}P4!o9Q-iGuMU=`*#yM*&AHoJh=om&$L0qCf@`tcKt4JnNb2>X4?p0M{XjJTXYwL$|*si@@*WKVPfJ?CNURDkyV1FC}5-Mr?JLAedR!B@Q+IN@sG;1LBr-z1I@RR7GRO+11qvP(9fj8freHL|B#U=6x$9gZrEk(XuX5~Ivbj{RaD(&Eo?`T@Pu`12I#IK`X^()_MecF%+V=ZhO@$3*{-dlHb<Qn2(dby%srLJNlEAC3Eb>f0Fn9I#p5ntZ-Q}X_5;oP-X2iKj(adb8L9_lf2jhcw_BuEIOhbS4MIjrq0SE#RFjmoqS)bUJ8Nu>%BhQk2G*s&n=SaL$@=cWg9XMeQ0FHTtkdGQaRZopQei{0OVq_##vFL&0fiT!UZl>CKX6&v#=qN}wZg38oQ7E7oDy|@UIHX^o98<}@xrs4w?z$WZ{pua9R<%laj~G;1?v1r#@jgah{gh>XV&TbhBexxaiZR7z$nghJTPQtoep~#A3_a)b@HRcg`KaR0a;j_5_N8==eXJ$F5i)nFe)G*H@nXFxkY2GL#2{kEtgfs_EcH)JO@LD#B~eQ>EwuQ0mF8;T0TgHal8zaEK#R(Cborx(9&j+b>?KxAS1g@7D`UtEuEi?11bxImRG04D^Gp*D9Zw37Z5-i54mKZkD@is>6dx_rRmef5e#Prt|T-?vdsj1mm?0#&Q$24x_xkF#sz}kW`v$PGo$UmZxQ|mt5U?8cTM5(naL&zytta1Da<~%(;8cxUTE|b)ny*=77!AI&bHA{^H@f4m#D1g*6A#;i#+Oq;NegMM!}zWde|WyLx<w$2?0Xq2hI(|3+8|o=T|NOl_@nGeV*|X6zj;+g<%z`;|V5q#ScdwbIyUoi!6XcN27CqKz;$C*c9sLQ1)S}J019rW!`k~a+s)Aa2Osy$VH^BFCyBZtYQyQo098zR*SsV-Zm@g$F?5KD!0xLb#X<dzmKfpEe;S}C@QmbSt(~w0YYQYtvM2_oKFQDollhr?UD@jjjeOk><%s8E*3+JCga5;D{5)7LsJi&ku5v2b^-cJ*7@N!*FoA2#jLY##Xth4kqz{xxv*hMIrmW9ZJS-D&JWK0+@PJJyO30-T)sd7B`tIbMi3xYWCYLgyvquFd%yB57u9rL=**er{`EuvvDOnl=eJtRttSSIVm;ZW<z&+W;y4btJ+jNxxpRSkz?G+g3rA!XB1lyC4V2F(!5t}XCs}!<L^WL=Z{SGr{Xxg>k?Gr@$Sj~3*^<f|J`jczgxegaP@NxhGtNLQd%7Er69zqs9FH7RUKMsnL<Y4V7D`j?;C>fQ-$SJO2Cwi4|5tPEt;Lq1aL-T%2$@;xnNe&?{6(xDmiccKV7w(PD1IjoO9%HAs&h{el!(OKn(pOy3^BGTz9KOEd_*>FNXm;uBaxnC^~vKV;q1Sy5@KSIR5tdyUY8XAR>_1%BC+l4oxM&h&X^hb_GB;dbFmubEmh~<Fsw@xZA)*M>m1_>A#UL;7ecz@j2doHsmOyy@L6QnEVFUw5KJ=%^+lSAYPyE&_~W?noI=FR+iH2;+OF9X+jioy-FWmdAd{_ecgtw-rqy7>>Bog*6p-Sw?e3=+az6)GHUZkmwPw?NZbdFYx0KNR3F4Lk(eH`m!t|A^lgE-UBp6V=?n`1~ad>VCAvnyVFLmzp2^`ovO?EQGtAcc<8}fMdBNbu&FuueHpVh-#yjAin${T|uZNR7D#r}4d50m)Qxv(D`zUUm2mp>gmzkSKpaTmr<>3EUTZ;#F){V9$Hdmzi1{$Z0OgLMxNmdBQNShX6kUt;PS{(*1qQ6CrV_%t5|W)9M72n#)oIevibxV6sx@UqHNp2-^Y*(#1JDEG-zJhy$M4li%nE-%Nvr1w~Mv;#|mIhFk{IjFDRN=!AN58|lRjAP6x5C;EMVZyV9pw!gk<1|U}qG)&$jfTlI%=7Tqagt}%iR>e}hXgm;`HRPFSsXgkc_*7#)=22aL_6-E<l15Xnecg_6X9B&6+heWYTEg~b)YQHHZh`sI+m7IodW{f)#4di=snf!lK{Kkw`e+d>p2#ByWX3Syo;=Aw&~oi^(va^Y(U#l4r;9cqMOZY3IZR7GbNw+B?O|@yFzN6Sv}X!1Zs6bCU1H73<1j%dGzx9{sOgGPbL<|?!6Of@1#4)XQJ`<aS(xO?)g6^BD{ruA^osFosd_Ef>W0u=lg>c;JwZucfaP&SZC2Y%_B+-v6k2NJBm=d&ggHMlL%l~<RJn@eC{D7z?ExA`s;i9g`~e;#wmoO<}M+3zb1sG&LBoJpXhF9@>r7H;=LQW;f3*=;cqpFbuTx-;Ij7~$3h7lVRF=_5WCX&@k%hF<nh^3b=p+NTK84qi)l3Kzs2|KPA0hdsorMTA#?3PN55O;4X8-PUFXUu!~yNVzdD1B&Dm{+L)L(F=mt=!k3<AD2fiZWKse@`RO0xD=rtJLFjAeiHn^kU7zt|}g!jWy9xN)V=GGPWcD#Z?rhNFSPpjeC)jR6;845z#@+-xugp8M|&a^`K{T(isLseMsO5fW)U)$Q{ZR31O`1wqFP&8*3rIJ4Xgab`mX)@HaHT*E<xGLF!lA?^NV3q8Pjsw&+sDRzY@9WHH6=oG_+LUwVCkLm*X)!C6a?o!fzN&0ci}wK5Zq;{^)s!Ps+B6PTy>!96{gz(y$y1YTgif_bb0AeU3M8U3I*HIK8eC)my#^zpes-HWwwi^<%+-0O&sUMYxroF#mYgpN`oso(;<g+D@x7x_N@g~+f<|6P63z!kBVp`-bm$n*rDF+pFGb^0iV7$-3$3S!N!ys#lzwcvo%p2JkmOar5LILs@CnrLIv8<z%9Z+z#44!snqNO3##{6q;@QpHOc!J`EoWxrlt^MxmNyPvYaG!m{Qq7>@j{*d8w_pA#Wb>kDr^YwI^Sw&x*(_CEaS6{Fg+mAD8*vS^yd{s*vCCFdCKaD5P@nJ{3dRHC#YB}*goptin-8PO}r!36z(U5m^V}!0)AD9y^Ayqu6&AvSf;LuVH=)7?RSRnB~DO<lE{cfXsIw9^m7!zIS?;5QoESiv6F|bmJ;kxq#?K-3a%ASr=n;Zi&CLZQOJUZqNSn0ttoIOptb}gGsNg)YaZZOW6w}(v`HLY!5=}FzRChrvM66W*9fquIAyytZ5U+3?$_N;6;G|A8T`AelWAMuRHEuo6(dFr6^*AOsKI_u2jUMm9&WX}kGil=cMHvUp{=d$&empU%U|e@7ixDNZnQgF?S~J2rLa|^+~%W)-R{N~l%rB0)OKOX=2WD{4%wgMA53m{YfgRvbZBCo2WQKKBS#BZZ=>^Q<I&c`&ZAAvEGCKR38FVil!e^`A<ue1>>d!i2gFu~3^vvCB*(i#h2+OXVEmKm*iId!;qP<@X;D&7606=(FW03+Tj58_8j2up%rWFAPDep`A>);JfT}NPdV`D*-=7c)`P1EEVd>s2@Fq6d+(qFozc=${-C@?9$};cJ+_q$o$hcU&wKnI`%qlRm3*1=+?rIi}0X7@$IDpKoJHS@YFlT1xV59Fa=dNXen<BUYQQ_7${0!{oPZ7g_=rVH(+g+I=(g9KG&MEA4E92ZCN7@9{Ymrpc1VjrZ1pc|hoBB}KLf&gTHBjm-s?}<H@rbIWxZ0(-7SwE!eD?Q?SM~R;J-2V=HCyfW-2TnM*={fFqfy(a9^cY%&^WFk&jCNs5H%>xLKfe)dFi%Zy3I?s-O@x3qNN7A&0)7)*t~RGFWu&)+ikbuG-Ij#YsmjloSN65Gza*s%}clS(rsSa1^x{QRl>1`^M#7fc=1^QoJ-%erzA%oP&Jt)WH8T@i6nv_kQSkp!<1HY)3lk18<>PZQw=#-p%bcQ<ox`_;nC~E)8m)>=f65RKR2%dC*#R955<e12Nc_|7vj6NVxfWc<qm`0)bV|=JP;o*>dFJME<7tKy7F;gEI|EKt~2Hp71UeICxr?n8h*=jKV#>C>C(FZ_aNNHZmtb<>ZjeTgDR9{4LG`P>1&u)yzuI(5goUzs^qX?Vo*LDR?%D##4N46wQwUS&Ogk0<bLDSQ%*TXJ*y%bD#c+)mBtA*OWBMEd?4`}m%xCaILX$<ISY3lu~r00DjWsG(Ljd8x*Dez%JsZm%@pkrK;fE&;^u@7VG7eCo|CNc%Dp73%F`iGf!(TNMB21a<<4+T@W`Obb7`os<r3kV7|;g-jxsByI5~B`P@MOG12rb3x*er6HaW-@d<{Rne2wXg`1)q#VOOl^_i3y7hLK#<3ZBB+hWDCPd>q}Hg>4r#dtzLLH)aLpiB?<0-&lGH{=P!hq$&;sft!JuZbmhYpG`bhXoTdwe!%2xFlCjT6BbLgCABkPT)?`9u-14NALuy_Gj^<+4X9c3GL<>(!197c`2;}vB2(gmq*5@UQ}Zxhl14h?35UFb^&r8^dYHaYr0$W!TrpT!Nq42QRgQ0fC4HqOtJ>ws5zeY$Img+o#(mz*IwH|ttZ_zivG;&C%@SA<!O=ALYYW)`AzY(mfugQp6k=A&Pm-vDVrv}w1KC~+F4mp`Tn+csZoTmSSJJJjhE6Et2!IZH)|j1jEwXIlC4*dN(n7RW2^xy_n$G2Vfooa7gh>%8<VZeHtzMI2m*<e^1nl1FV6x(aBAkZ7=)g%jqf3Xzg3}?z%juZDh|{yZ__E+BtYNqz+H@3rZcF8&p5}Gv707bi{1m&@)Hcx;BEEwrxM~+|oGYSdB9xHPL$GAwt!T4UZ#JR_sBu${9hRI6G~ck7^WLrOATGjO@goiwFs#xuov#*_=9}AfPDoqD<{?a$H+uN^k<;Z%$%LB!2y#TMczuV7DO03*S=8jAG8VlI6P-oXouGn8u>|lYe0W(E)5}?vw@5+N751vGr-OnHg=)SSDyiREJ`HkQL!)W-0w_m;P3Z1>oyFh7zf**2TFz1H@?4bX-waDoOe=T%y>)99x-HT$7ztiGQnRUpXvw04<1_KyHgoJvr21EROFfv1bO&2kcF>PeNC1IQH^Gum#OrY(HYUZjSEFrru=~rzp(8(SjPJ|>IC%3*oa7;q{0_MS8C#)Whi>1|>1s`PFY<+yiSPW53)e(D4jRM0@W4(SDBx14Fj@+#P1qPUPpEfi5uW4RU8_Xu5l>asIX`3L0pq$#H=1qCC*o$8c)3BEd?;umWZ63Kf<=NKI0=4066ElylR)7(`vDvK1L=zh(bJwQ^q9hJR+%f6ahsmZ=V&0a&-V#T6OXs}x0yL%$a$xI;5(&OT(Q*X3P5}m$_~ZUNcogYOJmkJ-M%pC>}bWblo#|T=7s-aB@>e=$lfO8sU>Rc(w+XIKrjMDpPRF&;FqjgxDE0;HP^c?ze)B)MK0zEj6rO9wO8+)bMM!j`4@QIR4;GdVl}zbE~{NvHKC%9aO9T(tITDbhGIrqR`6J=!#q!m3Kc#}a^25}caWa|xAo&VEJ#bYn#z__qsOyA)Zsz}{UBRZ#c{nPlL27{rYwo96rLtH({sIjsu6yOIftl(P(uSQfW|2QsF@E4gQbw9$&FwB*uIIyd{YpX5<!Nz!|rJ!>9McO3t7m!sf`~O&#918Cte|!&3kNki;3A}g%T2~XD?6E!ltB5e_~42fRfs5GB){m(_ZMAN`nk|rS&3(W2ou%jizcF<6<I0VgY`Q=`*zOK{L8v*dg_v<DlF6mC&)CE@v2x9joZ1S!x$`J>(ej6<>3dDngeLIStl`Enz>EI#YoJ1sCc7!jRhBZP#<VgOs2<D~OxeXWr>+bfHaHCZXW=07=uolZtc>+YKevy!Sw~H9<l1i!$yV5cwuWZ<><pB=5659pc-($W@2bE6u&aMusClO>s;byuU7Mla*BzT5}5_{h>*i`vd^inD~LVD7~EW!4dhp6nIk=9!4IIN*@7<avh}NE~jRr@yDj1=)`;qib5q66!hg36hBHSDDpW4Rbici7Erv;Q54+L1w$#V=l7pZE{K4fliz8GoOA=_d(X*^gnM@m8e6u*SM$2At%?k_Ow@J3u){x8+BttxPOMF3KB#gND6WX`y`a7iyc1&XzPrE`c1s?2B=a~y!ctcV?vxXhrs}xc4h4B#-_qDeR6nDVKTj=>P3`c5HSrY`hZ3b>S&g3LTA{_;>y6apZS~!@eEHQ6O^tUnkPp#5$}|t(X28-x{QCuGFZB_34VvyM6msQ8_f#@F*RoAjeu1him2UyeoKqi1^_HLw$R+x>jCY5bN?QYzi?uU>WmP3j-^kc8rOQ<_8e{=!7-db@o+hTbnfTaW%Mid?MI+s+Ye`^NCR^pdL604JI~TiGyc}az+OZS(lH&Gc$CGB3H5$L;PZkf<2yc}g^^K>y2H_n~nu;F(3GP&Oo9r|V;%r2({$#BB_O$Wrn0>(x-_-E=VtP=Jy#^-3$C^Ibt;ttM`+Khr&ky!a_vn2jdKyV2zTMmZ^$9+Uqzdo7dGYn$i^KERho^g@iUy!L7Oiz_;Cn(&ZR3uMh!U-CxlmZ-UeXWcJuRcX-@wPSuV3vQe`ht}I_U)$XkeWcbzZi&-ym0#o<cg9yeJi4PBCyLOhVOAQz7X=Z$`;wfuuluCab?g?`#?Q5^-rcPuUSgwQLU3WPBLsX%uEvkraxbCIzz$DrPm4Hdu7#T*^74WOA$)?L4bYqn!##6rKZLD?3^W-dTdy%Hl?%`XLq@8Q9(z%J!A$VU;G0?xxe@Q7c7=Ny?_ckR?$so1hh;xUH_AuV2<#r2*woXUVJUXU%`|ZoQ_iPf#>#gsv{bsxd2qk5wi-fGB=qps_Hn@Y*-S2o~2WudjQIdw@_Og@t%fX#~_c{LpYV2qh(|c$oAHFSWgl`{C`;fJ)(tP^oy%QDi#}Vvm58k=A`&nScc@M^QFho;~q7HEcqBX)vhlmEr&bD;R*jmpA0wAjPN4t2g}9y3L$S(;iYs<N|*qQ2A?;b2fPVVa=zlmuNf3_^xL6Nu+DGP8lkBOwRz~d>3=@Dx75!Ud?2T&t-9Kq<^e<f}{&QHW-r{duEwQWz@T;3ccj->TiEM3mSLt)_(iGwr)*$*eT@pmT>*giwb|X4r)i1^KvLP2|d3LiD`ln+ZZ(m=CR_lYIE(&TII2BHR3r`NzKKx=7Y5_|NPH>d|$2o{_MB!e*4>ZG&z6!+duoFQrM4b%^wojK2<7?Z71)c8o<Ya2Qa9jz4JJ{JiMJ$D}RmxNfHJm)Sp#qM$meyp?9Bl5MeeQQ3P}`%#xm(fq_#2hWs!9l!}^|TxStqT?7>VMRgg57Ft3<Z=pf&D|OxrVZx{tmxVQ&aS*=CBccE&fHR-?W5KWR*;?42g*|Q6Gv_>J!ZfNq_SOG71}2)qA1h3O38MOA7GCaDPQpu6XtPSa7mRl*uPAg)r9O>!D*N<Adp+spJC!4T5MFs-J447c^9Y6P10Ud%)4kJ|`{#S7r^hd!eSJ!+JLh}VMtoEtqIR6*7%oEBb*i$({iHX=W;K5|4b$04IHEn&-e^><oY6y+u(F-e_zdX@O8m)RheX=FgQdb9YD2(llOMP(#fg7bA;=iIQiF^?3&@psuGNdLWT*;*V80CWJ%AToz`mi1kZYzjSgeW;o%jU(F{T(xF~xtv+B@{O&T$Au^u2wZ*<FouK~q6u)uMvHTK{QvM*=vFD*B4kOo?%-(4@8)PqT=8j7R+@f$7pu(6o_-d9&Gsg;3S6yroo{Q<zl-<RD0|U?cqsH+4q+Q+ofIoep6y=BbTdT4|nr8|A}l<?9%lQAO#j>YMX`N>tFdsluxJc{*DAzNUaG<DUoeakvOFmM|cHXF)Eh$dlDDb9xhdWjcHDbj~0~mG^S9C?@5rmj{Q(=O=Fu_fJ#^haXYQ4ngZEo*@Ux7R5WP+d>g{yMrOL@dd+hLQfguY=`1hF2pAmPsuU-E2>_RF@+RZJ6?u_-jUEZHs?Yo>&Stq?*VVe)mRxm#p_svKo3VDG4P1ngagBFOC)HfP<VzW8crm3Okf;TPOJ}!slByaUw90W^1isCHHyAqcy7@b46HG)FC5MMzSsdsR_zMKA}Q~Q9-2ggZm2GFw87Z)a_od*1eE6p!4F)9`c?#z%`PB!N+2IcWA+TIyO0h0r472X;Swa4fZy_(j9WRYt*84@iq{6paVXQEji;@RZqWxD(Xp!TU~qkvBnph{O*pz+YIL_13eYnomObI)bgV$lMI)WC6dpAknrLb%M4-V)MBhmFEen%1$qmD(O|Y%`0)*-^VH{-70fyTb&6>IzbY!Ucplxfsnhp<@2&8WuM=>4#;onIdF9-rm=n+whtdkxhxn73Kb5P-w0&%<GF<-Ba0aZ9)2Uy)hEEkdP0<P94#cM7B6*r45#6FDuIL=nUWwTso&MdXD9Va)-q56P9lemh}T7*p9d9XQ9o2>INy&cjkB1>Sh;)gqeP7^={!k_-ino)vDP6V*kF!PAxt73jlwLT0pO!ZaK(yHOXS%Q?`VRI*+TL0Rc^H-_k=wjjA6G(b|?`O`q_O?f6O=BHA?HO71AdIsppVby4Dz3t5I!UY0Nm_GPEkyY(MsS6F!U5j5+b2j1v8qcSt1XiI03xS|hZFx2Y2*2TiH==!Me|&2_nql-RW4?F2_Cv^_5lp|E!1DgfgFkd&Y46h^^JCC?kcLZfNvF$g@}#oYK|JXJ#PX?I=-T+ixAmY-Bx5poM>U%Ad<d@+KbSsi*jn%C_1p*$9P4RF>WVVcM+ERvLInt$baI_*#~go^Pm^z3t3R&nWuhi&6S1wSd;NPT1z7;(>*rlqEbwL8lmZK31rsAx0PieZq1hwf)b&)nl=xQ%X6Si!K%nB&S438JIlip9VH~@^TfV<Xm1f)C|t&sEqk;!TFb}?M9RpqV|j$yT`!4L@qKGKLCDcYcS~Uvx1ZD=-rfrrn4qLYbr9x3G-A?VyiDi9uy5m_kn}E|U)ahi#sl%NhcCi=p<iq$4s3S(`b9yx6N1EEq4O1K8g7q#!QXABDCAPxw_O#g?@2O>`b^m1J!Tv$$aT@9ZI1=SZz+P|Kb0UnRxda7yBe8h%Y&p-zB7J~w@v3E^SbgXF)KNH%R{+h-FO|`vJ-&8jsy%3GssZzTFiEb-R4c%1Nn^QS5Tj8xNc`mBpwTxTsL%%^BJiKNx20~;c>#f+v1f!z~^D^v`{hQOC}tE3VWW#+!P|-i2LsJXo1=7gumDM62qUfeF?}jk2oqLG`t$9<;*4m6`JD84ATNj>13h+?|j*9w&pXsz_w^o35;$?c^Bo@k|-C>ErHV)a^5jSEyBqMPR#<?m>|N>D8}-qae>-sGVV6U_9heD0@0}!9%hB?3x)?a>vZ}8DZQ&t<^hE#mHRo~POd&XI>Kj8zk7AGcYrq>^xsW!qKQwF;NpfZAM^6nYq%=TKpraBIR40rQJvn3r30~k(z~MPUHKO@`oe&Sck)K`^oHw)BYHs&6C#@MIEbggNS5HItN1L2yxXl;!4f2()2J`s#+Zb0A4G=)utQf}c~(D!9ZeecW!~45K6Fnn5d#Ti?s53LDeS0`7gZm4`gN4Sknc#pRHsF$D1qnD^3?=<fB;a*vh<S^Zp1~wm+Bh|(jdJOq@y=&@Er`{`w?VWbQ#M?f<GEg1ZX!6VLn7X);(Zvc}?x9LfD6&qfDg7(TvoYH<iM?kkuO$CaF+rk3ig>-=Tyx>cz?3-H5-?0m@8~PO69g1_jRNBG-Hq2Wocg_dq1+1VOla4G&$&i=gv)9>x3sH{0R&)S6Mo@2kn`qSQG*{mp80)z_aVqMHi*UzQaU`8%v?Vl*a-e80WGYfVJE0KhwYCwex`!gN8mu!s)ZmrfuhS7FL?=m)Y^1#pXj4SIQW9dcwZ`=~wR)5zzEdKy{O_dCa`=J0$RqmoXleCMfV(P!blbRu4Xp)j{Rhc6$Xh$d4yj)F-_Iywki`Gfr)RvC~96(Lffmk~Z@R)JXu>M(G2G%6-ocul(P>$$~lf!eQ00BTLagYik29tja7L<zP8zkuMxOK7YLqTps2#sq`G+K68F6nbo$3xe19>nIp_FiCr1pCz$)@<&S=47gKZl!k+prn}Y@#02|+*lgc4-@A=qoGLRxpjia~svVbjR+oKOXO%n5`3knhcd!&-9>_Cv=<S8<dk!p3vTT2vzwMDwL~yNU6NBNQ!-j(S9fLBgiqYqe1_K^k^p4<AMcNEP)y<-+hV*-ZvC6|B0sywoo+B-}%2fMI#^HYvCI>+t=+YaLpCe)R0~|j+E6QG?&_H72N~DqKVw%nNXgG}IVUp#?;Ur0O9ZYW&g>n9xtn1p#kNpVe!dV*?LH=i}^-g<2>PWpl)hgc2N@GDt>4la?xtRi3GQA2>;Dweli1O?iy%`0(qbG7=ndzuhz6ROaDWo!KeVEoQWHA+sVyh&j2Det~7-rz`XbObIJpt@gw3UGJNIT<s+nWWBVUX<++n=h(gP@_GY2tngY7{9@g~)=1yGT+#?uF}CcEV>Ba32R=wOq`&Z>E?MeC@r%b+^hh6p!MY5-lDBLsTgkAEVlPUX_WmeJ%+y3pKgta3H3r(4ugN=1B#|Tikr@#w;o&6G~Gb6+G?D)9O_?Gd*GZ5d|_OS8&UX71NqwY_tK3p8=3}R-BP9wVWLWA1?OGFn>0C3wwcTa`8i*b_LdjI&@^hTTc{9hx|?}&59Onn_uRH+U1b}2!{Wm5^)id*(0Djp&UaA4c?L@XlK#8cOExr$oIUd<o1y~<vwjkJvWHutxweh*=-!yd^QP_f!RYE&q_ktX2tL*G@&TxW-UCye0mibcAE*Fh$cjI<X6^%%ab^mWJ9{$g>5#RH7~-;D8~KP3t03)iWrmbbG^16Jjj6A55vj+D2YQcl_vU?&G*ir_LA{9%9ljRxufv^{?*CR8$6MP1t=QKs%BxNxmCbuQPBgQtmGs2%`|`+PKQ=$LGoREu+;&T4WmI`RrPtc61%eQ(<1uTlr~UEk7v_7Cm&hkVFUjFS`TtT`w@aHSiJ~=%Y{BEyY26^8a$(l_AbQzd%vjfB|W#g7N*dyF_tnJ#osQIW$YGMT{gKxuQDmQ{^n3)l1!?yYUxO3v$(epx>=fxvgc_sCObz}Ek|_W_oN4#&MJSPQq<}V!~S#>eg#_8UL1^Oci|iYp}E9IAe;O?0+sT_y$Pg|{EtPTPhhp$Y_g-Y7m$vVvTwtSZ=&#~!=CXFan--LiJ)sYP1tD!(C-X%T)NWr7odLsMH0(jpW+=v6!jO>jN>rq&rU)LVn)PzEV2Vmq0?wgu_~n?!7SAIg`wjFM&flQ=O|_hThMDVDQTr__&A2RcQO%JPdp&`IJs=aQmmq!gnao_sze3t3mS3pr%~P^IoC`j=88|Xi2J7ra!z#;%tlEOa9RYj(Oas8_)2HmVqSt=L3FN-poU&VH|o)4nJOr!_MHRJOq-CLq}2+xLkum`J4o3(Xu(a>+MJ6hYK$E9QI2JF83(iuPf|mEOj1p|fgh$yBd--z424#{9w_brPSPgbtKqi*<<3Q3MNgY#OT*kwr-iozpGUW0zuGA&Ih#|mK&WhPgjKh?dBBqSjlga$Xn-=wkwLP#QIzg_N?V3HUZ=C5j&8maSd1!E<DIy9_4`WAJE{jWpm@|1gZnB1U8}ehBEkpU8j*tNg1u;l5bnG(AD)_^deeH9W3~d2SqYHwoepHP90-k5O$?L`B#L4G{+sU<C?L<pZ5>)@77K2LXS;z?3kE{hA+$KUV>=iKhM0kUxbeWI4q#)`0w7z~U>h~-u~j+Yfjqz2fg!0EzrTauGi3r0Fm}{8%_j0aq~2-2rO85l)$+InL448D_owM~c)X*<%rrx!bUK^-0b>du&8yc+Um#4m!CzY^s{Alw9~R9kI+)srjW>wR_;qH88?6}1cfkOL%?Zb!Cl>~%;<m1mbn0FvMO!<-^6<543}sI=0xxHB31_s7uOBh7BAPeMOtRNME^j&_Zn&#z4K|t*udmg<WjIc>XLL0@#fmX!eb$#7u~&}BqN;A+fxtK%QNW95vzPs9Ma;Jbma7<>AWYGhDg52+L6fsrQI<D@KGa4P0Gd*<uEZIdL5;saj^C4MZsisAY;7V7b6KT$8q<s%Wwj^`$H{f*ZPfcZ+vv3Bt(uy8pqBm_9pfOl^NDpTBrW+RnzM0>&(K1A8mu-cbe+v2oRP(QVrh5_NapFH>ZE|Aol`B-Lsq=Ij1S!VY<$6FGMc@NdkIXaOTnyFLCv>ZYpO#(;sh#$F9-W*@WtpWWWC=L>6VtFS2i>jBg3n`I3k12F(SN{?o*JAHObr#iSx9l)(PW}@9SoXy45Z-@^E;YuZCR+GfpNRX^PrUhEWbpgup?*HFbk$=(?!3V0>>Tvfjc}`ue4{0fWWo1^0@d&E1-*v8g%(iPBLtmKJmGuoh#1Ossd>dMzu%t5QY42}k#<SOF)vQ13w{QU|TaT%vJC_p;F&fP+@d|0Szde){W*jE+w}pN{&9w?KdTE4PrLV%8MQ9T9bQHDHDsyb?x!OBEE$fA~9A(H;Yzr`fit(s-;$l?{`d(*%~OY9TRTkCJ1O6pH7_X|QLjX`)%XYmfT@ykqa#A;`1#T1izLBCM*0s#eG+Vm{ebpM9Bgohy<0VGi^4W&8uVNZ@XZZXFw9*xZ{wwf3fk$PxQNn7sQuuvGsfpN;r2MX?!G(noH=4J2}D_M!P)t=sa8SiC(T^_{BpLzz(|vyxU;OM&ZZz~>xF(P#SIBzcug!Ze?KL$~D@cDaaEd{azeKd@@0(ZD@+;{sN3Gop;qGyvsAL?I+F1X}Q>&MxJb3;soiz+e65l>bG=4FoU@Z~5EnGRB783}HP8Z<Vd{sS&o07?O@E(kukU7K@7ajOhy=dKyt|FYUr@S-9;MzOV~-WZ{loSbMuyYwhk+wl%-8MU<OPZDC_Y;SOk9wS|opg*WQZ1iP_i@t})Wba700u#xrj@*?>1x7FWf52|Os?Kj`8)!=Kr{O5XP4d1wg1Qb5KIxZfbwt6k|JMa7*mHFLwwemQj#K>GW!`|mPx`Kq&l(^nWzVs(w)aFdL5xv=2Z8baX&K7LwQhFKaVS5wbqP?Uat%n`_ae*-oJDZzDh*243WICpI$)SqtZzZ3G7PhT(CvsKMr1zdTVB<blhNUG9#uXhD^e9u~?2-@ofe1Hdh)<Eu=P*A9s+5`UI3zkTq5)Fa924ES&Jw!)+}u3y&0uz^iAVh9Q#~~`35qnaG;cGG;W=qN74!TNi;YD5WntU*yZOme87lnL<1i>8*@B&p0y1%4p7cXn2t7f7v+R_6-Z5%Aem@Uy(Ty|W%NF;!`Et(Mx?`}WIAB$9HIF`wSZ1UXmzgt^w_JDws^VT@ry6V{u`(87QRU}PWh^H528GdDPkmZ)P`vWKLIdi=`NpQ0E^k=c=f&qqR|iLS<4j*cK@_X<axF0&?_5Nh>z=@(S9n}TcYZ`=kzJfy&8K?V;Z^~`A+gVRW1F59@4^`0Ark}d#mdRHsy)mO8lfZxy|81zE<Hq>w~L!|#73S_+!O3H`G$5;=4#-?j5np3+!OHKB|pfy@0^gYBWB#xh0AJ*>Fe=g)0npNmuFz{<xxt6-&fmdqtr@5n4;vDOI}(N3Nh`n;PS$o`I~MWHT}uRd7<-T$d2o<FTt-S`oAoacYJb~Ob-?c6Ramwz=lyXGmCM`Z7SJIf>BY|02hvrf9-Iq>DU*@iTAoVu?=q8T;ndY^<rABI=@44!8vp0xXIXZ<b_wi3P>$WdYt}^t(nZB5fa~@Xp=?1RZz2Zw8D+Wy4c_{y(myvp3Dl?P667^<8qy=I~+nN;7@3()=6<Pavt@0@6hXv18+usyTu~(`2qnV>)Rs4-@4D8)+s{nnx}65J04$_jgwS3{nfbmFrH?yy87N;eodNd&I;}`K626(40W$A00mUSm-D-`qjzUP$MtsmSyewv^p{X4qOz-{!(d`6S(i-7vtY3?P%f{cEFn1PgdvNva~?@k35}H8#cfZ$!jW7oM!cBmLPydqxQIqkKKp9gUsY2fwa!&k3>P})dfIt>9`B<@E~mWt6tq$=DAQnD*lAPPWy5lChc;SqKVoH}kJ_g}tEF}NRW$lJ%I<PZMrH-cV*1fn&JT};8``sJHnXTIf!X}HBu6gfNqe&*qJJBR)YxeS>I@AG&E(2`%gLaK>vbE)AOJl6R|^f?=Gr9UDW|h%5xpqvJ6fc7$``t8DUUeIS&MXQ%b885i|glR>QY`DRmZlZA2w@8q4EecMfiA=maZ#l>!uT(RoUB-B2~?Ew!9PC(X6OfXWNCs<IC>0TDD8|C-89GYO;O0p3}g1gm?iGs5NBIQ24;ctcqJewpLsfUSs0E@*0DUCBr%TDcl<iHiluzK^>mPSNq9`2MxBon<j}Ki(4G5reh~9xgI)c=u*!U`NgajdDLeiy}OJ$A$8Vx^O25Jj0y?f<)O<y>la#Gx~a{2!8M42b@C5dmskDyTQtDO$%Kuf$vR$X>je`HPt?D48jDxhM552J2<Whbf8-e%&|nAu$luWa9sHyDFyuS*S3URyo!g<m>iTH^b_f5c8%+`3JHo#*<(i@=XxFQPejjhOg;22&6}NRZqlchk_!h(07@uMm7rYL_%R05=C9r)a9`=AnxXL=chmzwvBpmJ9S}~`g=iHlF;L@f$5P@eE*tJ|B3D4Eqqh(XHbQNs<rQzg>Zkv>)wc5GaqvuiF2G>nAQkQ4mYh*l4Bb|mpon6#f&j=OYzvcL4o)65oFj^<!r7;|Bpb`ALgMYUj_zwT>I(86xE(6uY$r_Ejps^o-M^IYcV!`Z$=I}uT&|w!@9m0?dXL!b&{)Ya32fu^SU@yJ|Hso`Q2ehz!8r8e30D>NmPk)1lUo-ywJJVkR-}J&#@JEz^KMfr^Bx%1M8&|xtp7WsC1s<57n;$iyr(Hg}fIZ(SJsXMsbJfO$Jg(1vm*!OjR?~eZR9|6xD4(@z;B!SA&f`~DibS18pN9JW&Uq&BieGoS0>~Zs@V$`8_W>O8*_HFaUurz$ZW^IP3FGm0Ux|K5cZP6y9$@hX4G(_5H8;QNC3C1D9x&hbJr$TA2Z*$q&WOIlTYStbz2!e<H9W-v2=42FnW!h4LWPUg5Fk%o(w49$HE0uc6#}&Tlr>}m<v-ygZ?>2zcEB<^-1jA>p!eP<qzDT7WVZc2R-n(krE4LmpTpd`f{ohg6c(TnK5-(}O*xxjsy<6{_<Nd6@Hv?Yd}5563}zmDkYwdw$#az9nHmL?ky6^6iC7Ti3vy=1ctIKVE`W}<pj8E!bU%73T!97B!JOKn!%Zu(V=U^_NIdb8fWHJtnj>pl>wxphI~3R(jgp(N|5d8NP;m;h`MoVE1$;q1*(z9pSxC9eYNb1R<)Swaib+yDUZ<eNg8ZFYjetDdGX0Q;sVRUqG~8Uy6r-j0(}IFR*CZc*=}kc%^3!3xYo0vOy#_X`fe}4xzAjt1K}?;<closE`>5kW9Qp*8C}2u2sfuA|s^aPP2kfe*0W|E|Np`Huu{5z?VTNHj*5w#4VHCMYavn9uef9;i=sLG23lzMvT9BpJvV}Llk^>)4)C7ZHUK#!hpBgYoks&EmHCrH?LY->6Qrnd4C54~^bTscQ>i7-C6|9t?JOZ@3#sQLBYT9Gd!dc<=B|X1MjJk&W1&jHujTY_OSc-CIPVOyll>|bK^n>9AWr3N~oEzR8YSjbIMh%Yr0kMn?@n)u%C#G7H<*~L?UNn_AS;N48`carw6p{jh)(y$DTxnAaK~w4IRqSG&8ZK9b7X8;~(}&c`QESzPUvm6BxKN<Zo4X8TLlgL1Ta(Q7RL-X*J46c{M{8njoBd&GHZI+xWkG8%io=GHugR=88%1d8Vm$sMz5^gOmbi7y5+*l_`1Ilp>?GN58mMESJ>v74{R;C9PUuFpe_OCne<patnX~cDtSBwGhe~5jqx3S&0=V(dOp-z;!V0j6n9IO=Zwlp{$SIz~EwJ#-AwF*{Rz_V6-b2D>IIF7}J`Yu6zw`=Lt%I;_tICOYmc6U1*>aY}#;<p^6(EQou?27WspDXfbBQoW{<nU_rfb`>Fk=2owb?%(#28+XC8QY1H5xW&*~)V&2c=;coXm^17f9?vp@LA{f?{{<0w1Bx=})`1xFE;?0P6B7f5Xl@Btki%*~=Fz|0>a=87oWp76m}C9}2f2-(2hA%<AFH(#2MzJ$K3qz{mV>^vw6P`!X|VbuDF{GElCz_>_Zk{e{V{mCO6mRli=oz%L|l&36cTFM2MNNgiHRd{UR)=TlYvD0fuVj$FL#%o{c6m2e;@$oxgqRF4NfojK#%%#H1N!aSR!D!crb8AKb*Q2^8yr(i;T<5MtOZE5x3{p#JYhIG)YL!(Lj!biamSo@vl!kZO=37KKSpH$h)zpvhX6O8a}>on?j4)9^q(Mwd{?@ojCGR)0we~edose+6bq&P&B$EUujz*(z!xRb+%lrs+fom*{JRs$3m=Eklol1%{Q(v=jkM)3C#1OD*R#>=pf-oV1UNGp?r$7EuzLMBL@sK$18i)Dh^NDYHh@2Gc@Fobzrm~qMfl+dfh_xk&(lfZBUz}Ly^qSM3Z9lmx>-$%(i^KEx*n<SH72pJh*8W)ZQwIEwk3i^agNLAzjCY96h6!(~#dc&}HwHMDs2r>~YYhrQ+wz7CC-5Y~Tkg1x>hc3c6xEOISI%NmU?e|e?<c8kbL`zWtfj?8=2Vg#L;jb@a+WR5c4;1)esL1DjAWleoKa}DP8b28Kxh4rm6+~{z%OCIoEv5X8osvvY<OmJlcX*hBJQXn9Adm2?yiF(QY=EyKi~HQyq4lD%6lS<+c+dF^-Y2eqb4Om922^Fd1K~SqdLA1CsoUAEDMMFzu}-Ju!<nyuQ^cMClp7o6C{?M>MoX&j93@Uee34VUbI*?>$Q1&}DQTd-<wkQ!9^hqCDBip~2N1?VMn2T@^I@0=P8ke89?2r~<MCpdFEZ(5epr&rLu0%ilWb6NGK{WA87LJay2C%=?uvz%T_qdB918pALn>lCElsgEzOs&Jwo3v_Sb;ifGE#>Q@H)!ArMQoHiYpuSB{a$jF%APfY5JZf(81B!@An!k*XG<dA}}agp)DAr<xiTPF#a{KS$bo$3{ZEYUNqKt+5oZz4bj5eEeta9IovEf8Vs^9{|)J!x%N=D@CLwB5lYs>%!+}-h_dL!+kn<}aaRVtvETYcwPmYG;Uim3;}8LnzlsL=_xC_8;@Z{}y<rlThHl4as+)6ytQXX#78-Ia!xJ8S^_s4HZEbL;sMwsHpc~FFrnJBxxEA;W+P`!7G;QD6>DdqObQ3P0bC6j0lK?8M5Nf4%A)(N(ud}yl*yHy?S$GT5&2U^`{5=9LmgvGA?gz(VHax$?pxFWHqLUe`PA9PAXBavJ?;PVq$%Lh<2-=dQ;juZTx^(`~X>MBaT~4krn5tQ})!f`<{IL(cG`02xmzqdhLDV~w_M>DHmKX9xh>Y*7n2-V;kn7rzHFbvSWZT-mL~k%KycVH`>!Db9%_-c!J8?C_O{ozQs6r{E7QD03#m6K#%eku{#p04naiUr><S76w7H6PR{@@-X2RA1;0CZ~0i&2-5MH{jr^$PhD&tQojHW(Vj?{z9Qx`y1OUlN(V*QN`>WEY^uHZ%$UKs%gA<LjD4^FVyjy)|CO`iQ1zyA%Kw&z2O2#>yE`#|-@nDh?f=t&pKPsf|=RZ;9hdC^;XfPX0#6GIk6r7@p@5EMwx+&B`c7iT*Mk;3dQvogHFAL#8~|i+*Pp{jQ{F5xSY&AhZn`#%~s<!1_K7gE)JVb9|1PEQ%+=c*2i<wd`OrNt4?>P#j;6I}(!=YV9WDr)%WEM(=q@6FZ(b=x$+H3@P=ppUo2?c+CUvnKEHNSjQQ$s`N;cn*t4}lig0qELDmYjNjuwRRMG_X)#|^{2+Q){Q+7@HheN?#JN*YbdL(EGWG#wdT{rFLI*%l2-9lOXi1GCg%bo|RJltM=M~*HkK~Cdm;g5w((=3}pg)icwkfgVnJ6!p^M)!fAXw#bcyLbA!6<ayIs17PsxcnUCP}V2#C?NNmO&S87uUZTws`$1RnyXDo;1R&l8sg+*TaL*kOb0}65+0r?#)s4C*)AGVH!JCZN3f8bdLlxY#FK04c-xQ<T*He(K+5bu$_4X#9duZ)hwaK%aqpK*hE!T2{YXb(JHw~C6#>BOTKq$QFBEe)^JXZ9X8T5boap6WFjY@B#nSUinev41n3&Z7T^i38#TFl*!hp=*Cx9ErY4t~1+`}!+jlj&0Nu=-5(M$Pnp}}?W>yEdIOdYXwWGtV&%;R}ZBd$#sME*PTx!-hLB)dbK%Y+>T3w0;0wx5G{|t;T2z-_IACuxCDf}~hXTL#X1!pqhWzlN39ILXvvT-$lV>9#s|KjBdi7v#qa(FHPTk&1mP6;Bzy>!bTVn@W6n!?i-kP%1^A9$#dw(+yJM1^)y!8Msnh2mT31`At~1h@K`<(Z8G|I%1NjnI%l({<L_Hoc-`y<g3#mqWd7r?zOPf?TPZVUL=wO_)>t6OM`SJFe;%0gHwI|7GvpmfJ|O1i|<GiV(`C3XlK@0577zl+q+hN@<F^7|FaS)f#pX2oO;M5hw&e63o_Ef51Mj*|zP=?kDWqyzN8JpY#{(C+xZS-8}*UN~$iK?y^cT5aE8@{rK(NPtp0+bP9=M3ysHvfTkMKv;@>t!@{|~QLutR0SobAV)?&n)Rb-_tkVnFviFLJvtHwGgweo?2q3vv33#sndd~u1jCQ%tdTp6jkmU~+>5j^?=#LR)Sx+ybr^#iaKlW_89(XCvsrSVq7YWIbsM!2mff`NmXU*s@O(6wrG(0YhKD-)UA1~M$#nx5XU*)nws)-S7eJ7=q5I5dKd*!W$4PKEGhU^4YzorKbOu}=L15r&f=#1h;gp4<Xc14>wMZ!#=h^?t8+F~xhBRO8;U%f424X9x<5sJueiM85f8oH$xr6iG|5&PDfPBtKntx*@>-KHQwEuf-(R8Uy<Tx+Q1>;|?hlIt)M8nt*}!W^GfDM>GoE;<xJPp=AAhFimJ><8!uYf4HP;9|aZUcQ1hWiv_kVoFE?w678<nbH!Utuj|sfJ1AAnK!l4OwrB18z-h*;0P~uC06ygFXR0GLHcCeg6lHjm=beZ;nj8x3((f?7g@~PDUr?Am>+CP+GaOjP0bfpmd41~G2RvC@0)q5++jW!Teusw%ydMb3TSU#-0;^iC~x!o-<Ix{WOQc(y4$DIU3viT`onY<J(*4^%R1is1vkF5Kg1%%2Z?Q%UtU&7KA{hI{0R}6E%DssW}7M5mo#A^)=-~P`n46wWX4>u(T#@Rt$gO&nVcbkgsZ<;`AC}SNjf{FvZx0mUExlXJYOVtt2VyV4ZK6PEzOvt$r(cFavX1fKugo$<0^de7nXZX+92VkN1*Rnl6hk}6`xjfWp^K>jg^r;lOIYSYo1GlZVf~IR<%0qhudsShBMGJIDLiRk`Cf9i#y0)Lmkv>$L_3Q)8_TZ*i|JxDmm4iv%COdEf-_0swn%s>5?lv2t%gO#&T)e%LfleW3r~E`fd#ztD5z*1c+J617Xe5v@#T@n)AZfD{r-<r(|UikwvztegPhinLOsu?(6shCa33Uk8zo>v8Cpl+Z39n&Ix4sT<CmslZ8+t+*6Z(>$Oc&3A+VDq1P;EOpxgf%bR!BmYy5Zgv(t}my*qM-4%>rJ7wOS{<Ui4mbS*K-v?-*GB)Clyef=r0D4?#X?!{$AJM|khGj>v5K=~`Y*_$*(6iL!PQG*KE6X|9I4y*e@Qz8osI7g8e95I?NG?;##Ni+uUi-Gyvdk>YKWxE~a*6VhM`01Q8^jG3y(ClSaOY*y=(k55I7k;)36T5FN{pvNOk<3J4LN|sESs#(v*~?|R}XtYuI8W@;?X*0$@WY<`bxZ&*?jQ<?+mo?toO>P<J-G$TE>NAM^G?_SaRnGWLA)5bzDJK<<5Nm)|9q`{-!hdsrROmhmi@*crgvY_l6o;@#1J%zw8Z3hi&>lnQyYlq4-x_<Yx2Va*+p)V4u3Oy>iT<mJ(QN#Z3ibrp-I`%@@5h9ZeSr?u&BXa}Bg9zp=J~%bMCj>D577>VajUzO%uZqL%nZ;5VK{HHzwc?knCYe+OrGB!~1LWm~Bg+tf24j{FLDhgy(L18>H2i9l!TX*+tEp=oY(Ot#1orC|q(GdrKhvvE2=nNRB=o<&Id!r~gH12i+0N(g0<d&lyqK~PZXprTU&Im=2y*Co;i@l3a5bDx|sVSE3(A_q*rCnXyd8(PCtyPlX|OF)hYE|-%iCrM$1ST-;MSG+6utJ)3~hW)iSK)Ck>UXgz>oFdEC@^(9VJ41&KT*cBjdh3~tk%yu5Y->gonxWYXS-%jI`Rl%4;yssm&n4a){AIuZ-jgzt`ve=ZJI6ar$?N#qWP;21XSGte9T~?&LAe*@ZOTxGAwQJMgT5i+d2*s{3K#LT-ev1JsUmRflF7BFyXU^OZ5S8m%j0ei9;|jzD0M|JlYE(mN%t__qM8+s!?S}TL38*xX5R?}-vaq-q<_7u#}8{!$*Fy9h!}t(LGqB->#LBORyhn!va@({a+T(bqu2<GJZtlp(*=Gy9VX`ujeFmA)398CnQ(M>re|M@W{x;nrpc*N@3DlIgq}7^ypklQ&BKlu<fZ81v=uDvM<ioAZ+q5mSP&~GWj|oTE}}?a_24Y~%Czu-oWEIkeM+krg~Rmu^wRX)kkOLvMhnxTG;}ZmK<{MK-d~pU^Iynk^i3d6+Q9ZL3HaFOQ`@t|Dnch&a{X-XntX~AjMFxq;?_GAKB5#ujmP~s@@+sP1Ku`@c|}>gZpd#%c%uTjK$+t(huQHUhPkfaP_P#K{}}&+nRT|yUHqt>Rh!QDMmS`fqmWP{MP59l6IDy<9{1jYl&zsOg;D_*qItAwg#rdmp`i_$^rNMY8*&+I(wWobp4en=#EWsQcs|fJi{`OubbM$*(=GhvHr-Jz+svyG^<5u#BJ$=@YDEq-PCPD<S_M9@IlThbi<|EkhnDcRibF*hV`3wMX5_w_y6=Q}=(->)>p&|o;rHvHYg{Yn<|`ArQ*`=uKo_<cj7DK!jZfDw-p(5C82=ZnU^mQi=P%aq+&<*c^<-1I-7w#cZM{y1>o19_Yq;WxFAZ<beu*y=x{X7Qk5UIb%dSMQLE$K+E{Q!N>);+}*fhMSYTZSJvUxQdTVCT}tuoWRodV~SQApfR%_2fWjD5{4eg5uN_%Ay_N;kPU!u+kSKe*e`{L;8pGX=nkzLdA}R7)4k7CV7ss<Rf@3oUH0SBdj`x)zL8)fiUiWAN3N0i2ff&ppO?1tU^`werc=O_>fq4^E+9wvh_lWKiwnO>Z*MMGTzla8JZF?fcN)n*@@6+Z5589k}~NsXwjW`S5;S1MkZ_<gos)0g>bAkL2kbsfmd=ct#$@gLwu&g%dT;kz(}o<pouTMvhz;N%`&7)cRCO3}V5(S8OO_wsEga24vb2T?oj@9OKOD=-XDK=oD$I-?^P>Q7!C(sAPDFPA0E~|F`d6N?+q^`s$;nsx|6HVx=o#VrAOVw~CER$uEhje6PpSu!ePIyBg{mkM;N()=;e)UJg<>C9G~%kH&0Y`9JTQA4OBn$IstcaeQ+Q`XhKQyr>Ie0%>PlkzoQ)oM>hwNRhkcJ101;Cml0l(pqvc(~ZlJ*P0(tT%~=4H7{-3dpN(X&;b~D<mYU1aIuBwqU{QH*YG62XSH=#8vMiZ?shs(REs2E{6d}m5y>v2g}Xp_^tP?&A<N0+NJWl;izl}Xcz=ktF@i#a;%fL2X57~@){PT*<sh98o>HW4m6+QMnu1yA^Km>&R5I@DFuO|T2b3U^?-Mjzz!t60EKu<<y+{|ozBi?K!N4ro#&tuax-SUcf@M~+jCIb8(nZb#P=oo-wqka#3w`o8&}+izsqmaoR*gnAELoxZ4FQ7$8~WZUt-Nw8d*gdaD+VJL-xPy_VV>SFs2v4L%r=)C&~AJ!E~-cBd>Ez|c|ZCf<24U&lr6R49NRa4sH`CIeEM#%=m$LZ(Zd&Jpo<#-)}jsoaNjRX(O)D?^qH*&Q%4V22NOn|_X8VBjf1yj-`Ji_ofQ?=S6@Du?|EMO#&gp=RWJJbkZ777B>067iKcr*_w{4bJ)!&hQB9C_H}{?2Rw;EC_nqIelzYPWy*Dzs$9HBzxqR_sl5r+(wW7$;qtAcT9E|xT|7{vkZTj?Y(+FYHr+-y;8oYh`{HN)Lz~~#^R*u_NUp-ma|IJ0dygmBrN#(ea(-)XYg9z@292At|u<x7N$wRy!xfXXDPJ*8aD8;o6XjZOoQk-B}xHVL+AWB$QUVb{iXy{x*d;*l$$S%hXGuzOb{-8UTnTn{qIF@MWbuh#*+FaqMbQ&n14zC+#8l!iWkc1^wHKju=s~b=>nwVCf-xQ)e0Kvq)`uw(J5&|&H+0Y{?n3m8e%=uB@j|wI#0Kl3t_5D@R)CC}zb9hd>9{(*$Hk8v90LRjk1s}`x8;S#rq_r7`@O&6O^3O5DOyFFlYc&#l8bR;QF`8aM+`F5D33P)flL8kisI3m1NcGUV{gE97q*Mqp21nhxf`ZFr)rHG@lJd-s*#oywm=R-9g+tk<)8lNC4yEg@8vgf)C1D1``Hfsh!V3N$8CfjY&b9znhOHG53(4J9HtZ_1QvzZ1Q6@ntg=@R=da%X(h#*eczP^F<+tlE`$=Sp#$(X-q789%|0mS$bsVUUCLe>%{rXi>2%KrM8W~U+N$PWGF+!nm#`f5~igWdd+%_l?s9+hXqwttBk$n0Ccng(|I5=X}E+!qLvuP_nE>m;7`4Iu$yisS>T(5oqz2~MJ}2<WuxU2!c5v&AT<lrfrI16=m$U;QS&?$f_ThYSTjeVNVEn+*8c$#2IKIL+YDs&9P8Ak8i)bimX#@OhX?u69$?A8rUbki{4y8R*}_W9ddlTQ?3DLW~23c++;riIqo*55s4tX+4!soc1?47vYMn6!!Io?UeFKo7bah3^Qq)i@-DDdPTwnXvokYh!w2WHh2_c8<niEvae->Wh;Qg-mfq`+%s%R2>sT!Rn8zv>V%wP3kO^5*;-jzHc>`Z6gWIn!f}2wO|vT5)n*m#QPclm6XR;}i#z&ix^X{^Du3(sv)+nTF0j;DTE>&BwkfQF8k)4+$Zs>wsya`#2{%=hkE+Z;Rp*_E;&!gSZ;*xfK|A^-Is5UjhsKjXr^yxN*?vAfPp3&#=iEmpS6S;_oMVQAXXrhGxy0}Sz84+DlXRBM^KX%e7#Hn1-c<62B_%^Hdi#j8smu2m7WdseJ9mm>w5Y&qEd6vj8esrt`-|dy)_exmDY>=+XZoK{C^@?EmC;rVTzxNqZhv>dBfrdm9k}=bPbd%ISuzY(fcL@jX|P+V-I?#S-SkB=*D|S9eAP#9;oUu6{j+p27^6kz)-JyoiWGMJXlqNwe&As1{pf=Zow5i2qSq2jU=%fY5iho14U_2tI3<SyyfB$Exy8D>;@G+P(D_KQf8c3HJ$3cVu6S#nN*6vkiXC{poGel_>&2|Vb|*;tTha}6P&0W3M>RftA8pfv&yi8?rZY?!0r$l=x({^C7i7r;FMH0*9=_aiUT!HB8uU_uq!*8(81ZvAqU=xchi!W9((@h^xr<HUk8Y2?Yy}{3U_XS^H6ZO6kRDo)w#p#&7*fxGv}-`>a%Tmk?J`JP3~9@N^uUDFH6iVokgQCx05rT9-oX~1C9IPhWtXd?7<ky2UNvDMU=D&&JhxZLNF<`WuT8hv@J9f!2=u8gT}ODpS|Pyw4OSgugjV{<Oo}QyNqI7KLD~l+{hRkl9ooc*u?ddlE_BK$K-1n*;dJQTHdSJFaYSk|x9U2?9%k96CyU>Hn$?q4(iBNmB_1iR*R{&Eilb{qP!1ln0A;k&1-i08*DP?O3-n}x-bXvPfE`9?1XTBE1^?aHF@#1GKWH@B$5!Rjjd;?k_vP$Y7U?wM@x6ZhjptZ1f65;l8^RnU4<A0%hXdEe3ZkwO5*cyNa>UOFQx9U97Ip_8-y8BMM38um3gOW;7dA>zIuL%1YGDEHSC5}HP?Q6TazIh;peQF4<$#!crJioYlgZmIvEw<mG(vlc96LB#nN2RS<NO}uo95S4)+&J==l7Tro1tA>&G4?VZxm<0<k$QBi<Wb~62I_B#P-F{E}d4bIyJ|O5Dj`(;#Ze`-H2bkk47W3bC$9Z+IdUa$U|ymsT$ehMwV71ORJG(uo3PZ44!`N@~_ptvAJ7-J9FEPtTskg8>3(w)Hzs<{Of`Bi_ZuBGjP!c4*@hjPbWm#&Et#u`Q%^$E9){po?}if{9~W0my~)1OSM_-aXgNP$($>;e|~;+^8DA+<CjmKJ(qbn`Abg4j<e-_kkl`8(S%h*bVUHX%uOi`mjL>OzrKs-9Giha@yCO=uiw2oe13X-^5o>F<A#071FO(Z=JRY`ul;-+(Nn)BYbvm>rlagIJIA)QRMeGCndU^JQf$09dh+Az=WkBd;$xIcTo>bGR1F`ajq&kfJw8TN@iAit!NiDMS=P|v#UdVz#mKM{u7`CcMs^8cNIps6SRjZVQ9$E|LGky)S8x8j7Cnd1OaMUwu*48`U>%OcYb+bsh=i@zik&)67QBpP&wM7nZy}ni)ivinzbG#N40(A0<iyKMAPZhz0$A^Gfg({f>Su^Cl^nFgfehm5WsKWym<^WbB!jc@d_w**Pgk#o_1gKQ#f56-k`VRat`v`0?;x9^(~Oh=i<^sBWv@`Zc9oo+PkOKleve|f%79^y(FS0?1j;F%%*Jt_Iq7CZna%i9^x5de`9!ZXga5{I`yu&ZX-{t3ktoRen_WDg5K^xf$ux&Ksn^~<KR!(u$EU=ko-WhrqGku&<c;UxQr;T4u(vwMX#L|KE`gfIsm9+T0yQkQc```p^*B8r&(N$PRzkCM8eJxXttdW)W$(X)rEa{Wn(!9Zci=59>cDGU$@2AbngR=XK~zh$JiWM_8C(yyd1-dUcx&_o-!k+|vn%FnvoGfRd^sP*gXGBQ(`81fi_&S`lr>T}ko7XV6LCN2wb7r5`$4ab{zRf548`bBWOszVn^?ltc`9uPkcdJ=p)FxD*sfEDLcsw3(OMUyue2^ML+j!)xGpY(>*6xJE`n1bmj^YnJOwhX;0sz(9%PejUhtibw1XwM`6VEHc|Jy)?4km2tHqN^Iw<-+hBNmfo)vw*1{M}07ZiOTOw!r9??1<rqR+E9&&#S$P$_pZhJ(e~OWXJ$Fe7&WB25g3zSJ2C`2-tV0*mGGD0zZL!0-bN6?({kKOnch?Hxm|t_nZZg}ZxLY){0FbPJ>HUnC2|@+MK*E>-Dxh0&-l(vTlgu^v@XVgq?}!Z6StavSw^N;H<DhZYQ_$(;lS9ktk0_C6Igf^HPR+YP`2Ksb&jmuiVdF%m#0423g*7*M!6j!y&GWgrhNAfgVI^xQ_mXBy8cE-VhY>1ABetCDzjN*k(|TJ$}>vwb1OLctW=kF5IN1Lk%b<V24rNE^9WwW!hRvaWt%h7T%p({R0k3GnwE6VP_~g)f76J}mOTH7a*;VLG)n4p1`H5@qjm*)U8&KNO?M9=e0N$Bd5Ooi0k;d~f2$8=8?1<o^BWcm~HdV2zX=-F`$G?ns*$M8CC2e;*w@c@`a@n@LORLJs1YGv7uBL-XAY&-WNzv{8fr3rvjR8e@9!Xi!SlYj4?z<Xs!jp13=l&yHRvSlT!|I<&<f(s{ENDt$mAY1~5C3<c<b-N;?V(e-x73}ly+1a^D2$F(>UxxMW=LTehQxWEqrc!-81UB_u!Qf3vVtk<`K*_c6YWMCT|(*{G_6i->f^x!DiqC!s2%Id5rB?3lp7z-BQ;)Kr0$-vnMa-YZNWT%qM>Kp`kg!yju8fcko0Fb=h@F!{vgV%EvIPJT8ji$OXI>xN`;63-66Q2fpNHjVPs=G&{>QTNe?Dt)+TQ=*WYl76TI>9umHz>g-jc$6A)QLc{q7cG>&*H(S7eMhqNucIWU(8{<!f)u5eG1ER4FcMFv+p$Zv(*%lNfPnyHF?;zyM;(?!BqDsChjiAz-{mBHoR&*zZ%a@3-^(@zr9*pp<10Co;!|P+^`~Q@tPWqy6m`9A7+dCn<n(S;YZ(+WqVH9UP;+4r|gz0Ywk{^IX;=k(|oc-iF(9J<@=mpL}-vB7MeKw(LN$V`*AwNfE_3e7ajSz5m>sTd6G{P+!yFc&G!-$B~ag>M$nd`8#r8FUR&rtL<P~$fp$=B@~ddYK+el+ft+TvgVYM`vF#lLRid41*dadD>nFHn_PzVf<a5*=W4{huGc+%+%sjK`(;!l&uw8zWLPg4uv3RN^dDKGxIG}>hC)pL{B|#6E`-2Ql*gF<@+K_2ZhGFj}@iY+=^rkKJ6}x-;Rs|Y5H7^3eSe1XU@3ieLagM=FVSU(PI@P{=<U-OUyIe}Ty}Nj%?KyqA=3~?-6=8;FKKOQa=-|W6b&qd9{@H6-FzA2x>|XBCxv;&9YoIQdB_Fw{3ZV5v;g6hQ@EY)OgWAC!_hJwA7z~k!Knl!#PsWm$Un~kt(_PMLdQ`A(FeL!_u0*hFVGCpAQCJv2DCe_ivb;#A*)op?t9aTv&n82<7D9Lx2Uw2@4<b|c7$-Q9y4Qr{hD0JVI9Q0#RDd6fbl~D6FlcXRoU@dCieW_gMfPbGC1}Ag8Q#YM!NSLb>?(!9zYr6L!#~%7{f*^Jg~f6XuD>4?@x`l`aIn);%i2EOA8ZGfwGe>_fYn><_4t;NE3t1gkvluQof^R%p_}0y(cvA@vv)*q{f@x4Y4!#2>FtOId!^fH{X*!9<!>wmYmfEzY<9#sU^T5EVA4VHVAnl}CBuVg?sVNvbFJyIYodSb<A5fix7}zezUeNVMn&5nZx#N*k@nFEk1H0&OY-P%y7;&=#?2>QE7*c5*lBD+j4$Bg0RAd^JB$CiOrm#Bk6MT6B7qOfVVcn;Z=MJ&37woJLv$}N*E6hEOVk95G$5Li$GZ@)gvbO1-4eo(Jk5-8Q_g|j_O4Zp<Mi{7rY%<yx7K#U6WkbGQq--@43~}8Yf!}6dB6*9ui;6RjG1JzV-l~Dxd=~#-R0fX=}Kls2o~Vi7VtFPoreZ6(GS=$3W`f=zwDONRDz-!r_+?eJMfqu?$V0gCff)tX!PsBF7E~?v96-T6yyfEpkJ%&2!&`&BH9f&Ex^&5IxHSgI1b$oL=t-ZnhY7TZY)a^%(+?-Tl9YGfmjMnYQh`YoMbDSjx|R2vl`r1yT?>!ujk?&F>{jIec}^9t`{wz^+bc>9Ffx-)#U*1(SdDU0$b`5u<wMez_A{QgPA(U=Xy6>O5lnwDVBHc(Om#|ak9^r9n5khB-6lW_h9Y_YSKBF3wDeIhtt9bsQ_vmuyWs9+?{tgbG3CUh|ByC*6vqUO%-d9!ZOdVp-K6&VHm0j?D4?78v-)<vcVV=;Q$KbA5}nI?s%1+#*4)~Jp&RmfOqekp#jq00t!O^qp1(_zgANhUdHnkGI+j@%K2h+Q+^3(tK3g!7u|3F!BmJFte?NHN%>D@;x|+#R#X|9>M~Q&Wy$pU8r$BkpdeeP8??a}Xazt2FRUaBsKq>0SViU6=Py(hk%&7!w<rfWCl3TiA-L*t=B>K=Bitk}fIYL}y^2j%5bX=&98;XH1^2g*+gBAT7mJH+L9-({4r$Ja`QJoVYf-&FSiBq4yuFTHM$3zK3*|+E0NAiAEMDAZ@|}|W+2Tc^2HM^!5HAL4aDftYTuKPCA4w4hOE-F^bi<NqgjVB#v`d?;KE*9N5(F4{Kw5x<t}deZa&?i`wX9X)FhgC5p9an<z!odUk&P-i52*tmDP)WHBNmSsKPdoLl3HxW*?8_s5a5sj!$(_8QHA{qtpSEqjeGh^)O$s)sVdP}!Y6Ie;WEa^>z0W{S=Q->;a=(4-Z!;n<`0I=WM4B$R*8{OLXp8TK8kkNT-S_b9Q%4Uon~|ig}#O{9PNV{HewcC3OIz8mk&63mR7LbHqR%H!7-OH9W?_*grzmb!+4que@rrr?x=iL&eG{n+9f}~Os0#x&epjN-;g;3Mck0$HYQ_a)uD!U#tP5GYct}`URgxJ>tIB|vsGmP;gE#mYn5L3?ArRU(jP3hAr4(gVH>}8AV!S)D6@x{zEO(=qiX=N9!Fcf4nl=-^YahU7KKzXyuNe?z0f>QjSxq$tH;+(7^jy>=C2se28-UMKVEPKL|Kb~kPf&`W$#lrN!0>>_o2}D0t(B5@y)$QqL3R+AU7la=6{_poJ{uEr&fdxMc1w!AXj}%M<OGTlM!5F;sXvD++rRFJ<5z1#qkeTRmQjS#<waT->+-Ohb~g9(D;50jE@HQYcpD@@i{NN@yXaq)AQqmY>poEys6FE$tnlBP8Nh;p#TtZ$BJ8@H%P}Ts<>slR@r(^VI#sdj3Juj881f_Q$9ut#C(Zr26{=>uw^y7p_+nF>J>-FFj0>J`4+)wMcbmuDDbiobb2V<M{pJechUH|d=ELRe!Mc5{CKtTdLOUCs~z5#u5}Ydc(mw#n7_&}t3XkG8VMuU{;7%uN`(vQGOci-R-lxE?B+VQ*1{eYv{r)qsu76M9NPilq`NhN)_1uXTmfo`5KS;WThdjmjd!-V;NjPkqoXJ9PoMtu;>Gi$rltlOx;XvDxK@5~XaQZo+UPU(>frR*(UV^S7yohw9Uf}>1R%nnrVhK(lu=chI%rChW1=)U;z?7+Gijpj(A7_Qe4faav~Eb$T3fU0YsO^sN;jn(p{g{cB@JtuQlq|QLt4?irXd5Xw`_`n&{V@8Punfqp%^xm+7atweLK$&pOe#Rusw`~qaDxT7e*T~Nh3k^0|})ThOw#Op55Kq*)r_hy<Uf#4=m?>?I9>ao<QxN-W<RB@y+vRr?1|e6nMl{YEMQ1>hAKfA=+<L@4)fPw?`)d?@biDz<JY`LlW3&Mhk$^SHM1p&V?a*2rI7U$9F#kIRcOG32_DksGp#~r8sn-<@`vc0Xjdm?amX)ZA@xe_#9UlWMx-KC~~rU0D4fxxK!L^?vp-=?Dz86u;1!E?m(gaXuspVW51ItQm?CL@83LmEspi?jQgwr8#vfDt%YDQv81TfLTs|oJ%POJNrr3TJjp`K!Qik%3qh@C6`C>4Um=?nLo3sBV1S&VMSbTAvv?_#X1p$)Mx#Fpd7;@m_owbWG;inbq@BAncJ5D?8nro5R!}855Oa#m_)6+KPmXrcg~r^lz9`lWy_eeuW4S{SSHR&VHJz1X))$dz`patmor`Pd`x_hW&eyl@47kwE$#A|Mne!3_k)pralVs3`;n-h{9&^5;a2POAaG|a)=Z+`|EvAUf;9*?t>egbWYBx6`$%@tOUqWtNF|Ue4*gDZ$p|e^f_Jky?xga}j=lMxCc$aa^3iR;iq8Jht;nbyQvKiG#j#{%MK~VP%nFOq_3lyPO_bu5Ctgj11o>%uB8y8gQG!*n|3)6%3weirYHH@=BpzE=9Ic`dSQ;lRApG^`DZpmF>x`bOWOI{jf-en{(6Q!Eb7I7ah4&OdGX-W@&6z_X}_+qYZ({WR8Sl;nBcFBT{L#fR=jtk{B9XHKT%RBzoE?LlVC`GYBD|eh$>8;j^W;WI?7N=;@YJp;#bzV9vY}|Q+gIU-4Bd2IV=doDD&fkvt`K%)=zJ7A@{OHw_!_#+1&ySy<9IF_M!e8MuPbZ)H5m5c8j^yBpJ#GEFyM^iTNO4Ku*dCQF26{Umk!xF?Q)ou?6d>~&iqqJMK8v7?2_R>XEf#Sfe;Um^cu4jpti9W_n_-)hEzy|S3|bDTW;#9D%tgFdB&Se4zDNgsvzdoo(hsw$@PXY7s}9*1;epl6?ryM|K{lHu^V73=HoZx#W`yrO_q%I1v&H7SLM3k@&1~j@Y6i^?`dWf%&ds(~c|Pblb7OR2r)M_PHIdfck<AFjbwAL|ju}tDZpQnjnn9xjjkFzF!cOE(yr3w`;lU)G{luEb++q^#*y@iswz?5iX5@!QccQHS9$jR^q|XKym!db!uNv1T2FDKtdk22Pd#A(c%e?Sbj`W`?hPzM!VIZcwZKiuH4Cfx*<8C-nm1O^Ws{ho&XZKJOm_pa`gC%BRLJ@66G)P|Pnv>BhWrQ_|vt%+^oeoouEJbN@?eCZzy!i7p8GJH7v#r1`dI5F!>~s{UxPQ;43!Ls-SklNu0p3U@3LE?11u)lDLuSCAL&{4ao#!MBdV!&{>P4I>>6r0{R5*u)6(VL6YFz2r`kLpzm`Lt6Wym8=^7TtP1j-lM*xj~ulTh(xSw)d*3~Fxg*)@l=xvA&7f;%L;Y7di3T!QI!GC4x>kOC_<qn=gu%4yNi3(!FBB5*tL$+)!2OS=jgc<?B$XyBMX;fh5!^p^Jyy&fAJrdh?vq+wTrDi#-nm#_@8#lg_8nvo%7rSMU&<NQ+{BS`7@e97a5`|SC<lb5F_&yP=xT4^pnAN+K9c>3bW!SmqPr-#qqJTnPyUdapcwWG6*Y&vTeO){7yF`Eh1r4#6$in^ffReZUjRk8Ds&gm{)f8DJ;tLk@V4I0MV!?#C*oH%{@>LmK7NR3^;ZCH|&L6*Oh6OW2D4&vOVV9nO@KnuG^(FZkQRE(oFb8JZQN=9`?Q!a#k*Mq%^uNuuDobGx!sOMV?rx%9f0^mUs1Y1=<n`eI!@j%U(zFVAp``Pm!dq+>6!779k45)ANP1^2x$vtq*3Mg&>TeG)z4%f?>sG=fEV`rKK%$Yej6)~_MG2+1sdEdzzM`z@LiqegZ_3@u3PHsQquEFWhr+?}BB|X1vs@D3t-OoDfXty0bo5xqe4e&lYFTP_#iU^gdn9nDAk<Ovt^{aWhNOBJP7M&%~*+hg0Kzr0X4YkiK&Dmpz=wIf_R!AM{2GuSMqF~DB>Gk&Lvd)aPK#t<9WmVv;$wI5vP-Hy(a#NBl7jH*Tp*KUkCGOM%IUd_GIVK9)3O@6J-!Q}38IWy<8##{cQI!FZDOatby=(=!DtxEhjL((MvM=hz7RR?>2jiaOg6KJBe?dcruj4L<$Jj2goB-Ahjl)U=Ohy})fN5hr?K)0V^rHf^DN3#tQSj9TJCWMRv5SYV-aJ31Lgsd|b=k0kdtwJ;QV4YRuHTC|FM1<Fp`F&fX<=o_j+8XlEq0_K>nhuk8sJtnP;j~-DEOmYJ0$_V_;a#S#J@5Z{~@a3a}C%9{sIM)d8%DMRCT;S9TxoqL;Z*(k^8M}vhBAXkg`0+VL@v|$=@D7hGDY=$gct*yQ3-)l_QUYM=x#-PP+X_X!QHm&;;9z!0LCLiC1U0oNzuFRTWqnT}pvw8f9<V0ofY%z*~4<4qp1j)EfHkZX;v$MG%37wE$jz!3;>}lbU1Qz9}5-P^D4n-DeI?MN?swgsI9@MfF`Nr^&n`MdTwK634r0!I=*y<xmhdh<JAEkI?5LkD!CoXoPMq{6fUQMJDDEopufLR@97)<VB2+)Y1!JiShgK(ZT7H!*?&A&^__?&GXaOuipH0e5&5tbv5V2jqZnAHTfg6#9%p@V4MOh^Wy03n-d2*Tqq*uF<nI`a0tHn@er>geT_7=zLW2<q6VHmIr#I}hF`z~+NPT!#k$m`hU8rOgO(P3&%!O+!Rq$=#SNJkUdX<Q#=hNt2?9f-ZicJ}Oya|GkuPG*iy7<!vM>;51o2P_*e2a@r2t=Nm0|BGsw9Sxe2EbhlW>H|corR*u~PnX?cILu0n%S)Kzb~!kdVj8McSgkbhCJlK`hMJkuqK+Mv2rxBdysmbN87tQt}u$r8AzUfi?T5C~w9IF{=f1{yd#Vp*!^rr&gOgyOUgeaeUd;vF7slvIW+ww!mC7mJQaIKMT!(4TrtD%1@GYr_kq6!b4c4TWvVf5FM~ae@W-b2t_mz+P+NUl_PMxQr}@E*tQtrNVt>c(pF?CBtrGZzn|2kWC7lO@mWFw^PH|KE%?sf!v@t&POq$MDJ%4FuS%g#g+jd^725Jl)4#c>!m|$gJCjvd%iF3D-eY=4ZMUOCSobK%Xg!X4&p33m2s$b@R#gAP<*YT}mm&>EL+GGTqa=!p()GqS&Byt)ti%6!aq*A3*Z=5u`yanWCQhYbL)kMND3lHQBs(6=lVn=Ix`z2#!GAYRmL6+qv6BP^U1OjG=M%g_{}=p4Ir^?v;uq%>yt)xTyLQgC!AgMWS|D~T5Dy&?TQ-Or0itJt*tI}#7C{YS+XitZKx|nc9@rqdHi(^%hN|p})Vl3%VHWY}kOIjL(0OQZ<$OV{>R@GjakA`O_oF%ixU0jHp`w;1MwD5R3;#~kVt{vzGA~s!p5frPJ|YZTDoTBWTlOFx!miD(UMBIdKEPaDi*)uY{retR*>wIZ{R_`<$lHrzO8!##(HbPqGuCsJm{6ai=WdHHi|h7Ta-L4##fz~@Uk)!XvdiQotLuIk-|(0e-(dXM48TOl_pm#6QJsi2_}hE^4PE)Js=#TLz-jq#29pf#VP^oNbTX+o3i16cTf(_VSZ9o1cbm}){=4qMU-(Z%5*x-ja2PhuDLMOf51lW&mVz0vzQXq_`#pzOF%tP<hVkLbQ2vT2DBC)q%)XnpZ-{Fd%X#VghO5Ar7>9P4Oih*dgZ567dvjNY8d3PlW2A00{_@2<`;;6nR%AzMc)&~K7JR}<{Y5CGyY1Z_V~hfo1U*^c#r6zd)jw>*<@T{rZ9(!h`HP6B&FjB4BC}1|UU>V-#n4)!$J=t%ROl?PCe{wt3RJ>Q%z=x_=1IxQe1{8{zzy&}0E6kDn$cM{9}0=Gc}Fy(*(4q$!>8GGqO@J12_0o*Wn6pE=>VJ4-kV)Ve>#ZsK|D<3=m2P_KQ-YGra_B=+W6CPa-Jp8Pp{zZMK;ZV#~UP;U-m2>;t~76@;uM3(Kw@L8L}+!;Gro@;(R$zPB5DlW#D4V1qT3{g+P^i+`!$aXC(QwJmWC{zgpU4hSB2stq4C2uH|n&oDCN!%Rhd5+XnNJtG%S`CO84|w*n(+qaT48nk3}-2<+_ycfy22O2il>g4E=B7R_Kn^JtntIdW2)09%~IgK?BC#v)`pZV#f{+G)--qB*Gz-%FN6qvVxLPn6~upKPaOEICdWZpJSI&L;-)2_P6P3d3`FZ^KiwgdtFL@eiLq?t5j#NO6f=1N1XW!*SNeiQPu#ihknk;P1!yy$}Z8*DHdtA{b*#K8!F{4C5vJMi?tMevaw|l$Oxk5W~0{>MOLEJHzY{Ka{NovkTi8(#BdwXYG|y+=)TV6QQ%dd0AZSxJ^*J5uMGG_>-%6H7APPZGT6K1)Yie=udprC%iVJai6>LIpk@JrcgU2M=tgOeJ!#PA6uwQKLXm7#V7L2G8EfZsXDthb3d>X&1fDr(cv>OP{T6IaqpaBwM1=xeiqkzJ8%H>P(|M3s80{K8>o2XuiYJXM;1Z8I*nS0YzSRv+eP=IaX5#rpiKwyhwgSa?)9k4e;93z9*oY6KH}MlA;ht7c%omV!{H=x2BA*bCT%r5Oq+Vcn3Qe7<zzZP;`);Nm8#;o*muDdniRSWpp)Bia<DeNqsOQ@X&xmA&h#jL1(Q7*4KFCob)a;;)*IRlU`EbBio-#CK~_MP(X3$?6tH+yRen&9ZTi$l6F}LQYDSO+uwI5>eG|LL*)0qsXScA7lta<RkuzZ(DZdy7k~7Of(yodX_q}h*P;zElN(Sj-sFu{BhfV6H$%Q2GoDM%Wsx;Vm!`Sgonv30#ONk=;|9Uppyp(xXonzMCrmkzQf$Q^O$ei1^kW;Hih2Ii<Bza&B;gI?n2nb0Qn3JjRB0oe=nzLiF>O)l#yxGFdt0`FwQtl1`?}w-ko#I)0U20B_SF};oORk>B7qdwMczGf=NL{vPZvT9;`2+xccrea@F^vS-i-%bh<M3hfX9=oAC|=Sc69$ZI;W$Uh6p&|_9e7CyhC}`e_1iy7I`ch!0YEXWAYtN%<eX^g$@H8jRoHdHF-@C{0?oily<g^8urlVwG%vU8ldOi&`X9&pYm0^l$4ws1X-CDA3`)Qihkd4eZ$j<F<GSNHlgHEZBe@qdRAJP0OU;Ob<yfZ)R5(mV!SZ_4!J2=O4N)N?UFvn!{(V^mFgAtj<G(~xi@pAfXw|7qZ^Lyp_d&^Lj>jnhP_7f3PX~U`=f1Qf4ZUnDZCcmNS7`Udj=rSsgM8ASzg;dqFup#DY&*?BBWS)7qBUnw{Sap;B>t4{yRsF;;72Pq5n~lSLtrPP7Vzz81ibvO&C;qA!AMs%hHBKip}u%>SJS^-58<fl5EP=!G0@8jgRm=$QK-td8ir+`K6!q<SVMevIu9Q1o-y&+9VQRYb}hyqV7$!MQm{h+(dh^Zb`+m&cU&NpzieGk_O|v$3}knEG#bV(5X$DX2FhS}Yt(%pyYis3y;ajpywVp+%Yku%nbe4D=W{pZ3jyOQjJ2V`BD-K^_X=hJ>KWlw_?B`50o<HiGXq$!!6ANnb4t}}THOrS3SFo5+V3}?YfW|YwHMh7Aj5|BZX;NDHdtVBE9#!Q33cQ&U%bQw8d39@KM6b76f2}y!sK3Z-L^>m^h|g)DP>DNk-5YvFeO}9XTXAs{8#tI<rV$L=+kEEd|JRMMtjc1B07h?L%LmOAL0)y=rtWOSe^KAF6x&$5~Yqpr5uW{Ko$y6%<t!u>@1!bDYSOXuQm(WvjCeS$t^<+TELZCqEH?wOr#icW8V~rs;`U~Qy$^KIFc}qLNJabj3W<*En@XZBYWL>0(ZNEvInv;y%23{2;n^gHR3Z0F)jBKys9;fU2%zf0?x)EfPJ0BQ*##;ZV3);DRGBvGk2<?J~1}$aVHxnYJ_Q%-PwHi^x7hq;8S$lKr<UyV%|>rBN{f)ad|RM2cIaPkN9R1sqJ)1wo!B@x*G?s=yi86-$JjZx4DE1>aM?q*Ir<r9v?<>RCy$~xr>WxSGbI;jm9v7rD?&#4hCfkCJT2BlyA$wEBbpRejnj)aXB|5$D&3!CBi3n<BTZ)Mrh}}nig%GlC4Ai!<|DNYuF!F^1}-8hmP~AM@HAnH;-YNCJ=ZOxGh3QdBI_h8_O=@sJHwA=8@i$Qo)i_+dgxxDQozUgXeN!40Xpa@_^Dv+T0~PMZh(F%8{Yu9HoCm&nua$QG~6}3y0Tj?|#Yf;Dp?DE*1Oxy=b=pj)Q^#B)5bQD}X3LM<lGi5-^}@Z+AaX=Dk5IppW)`38H$NAxdwIqwrm$FeDd2c&*S-n%vvM;hS&$J6aLc7g|<hI@-CIxq6*WpW$M&gfehu;0K_y2N!KzUGU@eg<m(mE~pz{8+GGrzwR`<_=P1>muZgM(kz0!HP)o##EutC;-Xkc+)y&UoKqa?y6Q|zjj2HqQ80Ku9xHV4W7>-1lAS$Uqon#^9J2WCbPkt?N$@*#Je|8Z!XUx#6b8;5i_5N5suEvw6&^_VTo0soEgFx1X}FyaWsdMJ4&I6PqMdEAhEcWF)U7t<5nSbB@Ql}<W((ldB4!gk>M5#Yyo*lMZgb}5-x{Wh40SAryxivTFik&nK5Fs?Lwi^ff)|rHG`5B?5imEQtn4c52`T}FLUUA+Y(T#;E%Dz&zj+Qc#PTs{j!~c<sQ@00Ev~J=(9!xRV%m%wz5-XqouO+<JgyopWKj-!D$C*Hs(`yH<Ry1*(Jj12t**J9;!^jVQelWR01Z(LA~;M9vC2?6ZO7zL-qJ?zUB;hFy;q3|)F9~QRPA9eD{|%Km~>jXHd-<7?qDZE3qg#sDF<>37F!|$*06g}(@X!PR-3I7TP!D{6=BwE(a)yQU{md(imY$g6bf(fc|3ZD<SS_wl-Y`*Q2y%@>K&0@*$PmjE85Cl3!pZ?5P+Uc(+e{G=7=|{9V78txJS0gK3*=e<5@bj7!X7MLUclB&rAnrjl;F^@I&zk^abq3M(KjJ%_rH<oJ`|)Ck{<G43ll5c#(%mzczjf#`P&w)}K!tCB0D9NIjl_K#B@qLyd}!A40)^?gxwaBg@uu98X3{Q3gBvp^h-(7BjrYgz_U^#8XZ}fe$9AhP=mweq^U9hT{bNfhsSuODmm-0j24*E9wHJ@+3M#9TKjwd^S#iI>pcy5!#Hcq<RppPvnl%>0q*?l7nTAv<=+bz_6lxbvl&r<_X|v6p;j$%AO^w3|YZ(f>c_H0`EMXjI(93fEkZqM_(op8TpZM7?yka)3dfo4gm?Y%pE&cSQ{TOdK*1-<wNgd!&Ed{@mWw!ECNixKVvTU(JH87%$Rlp4>%_XcjCS#Dg?^0!EU>|)3A28xxM`Gso|tPV)x)#1P9^yxwr4x{%%TcC*B8Cv;V3C&&pTt`PFwubf$PXq=pY+v<dL#a9*?Z32dY#9MSqHLRCV9nRF5?|125B%gLgSxvm=PK+f2aWSCt|J&^jemxDBo)AR`IN&9RGRP>Y;h{!itZ+iSDM`G^JiN4t-D&&FktNG!*@!`D_w+g68;Q(_G&yZF7p$&ZyLwPkcj>1ZV$9ubI@FY2v7-%>N?+j~iH3rle;JBPJD|0xa%=_CQ!jx?B4ER}Q;KMOmp=cey5tRw=neMjBIFma5SC!Jl3HuZ*{XP)K$|>wdt!j~#`d!)DUDeZ~I$fvE`wDe18Wq{R`$awG)wqIXJ9H24c)%%mm3iQ_x)e52o#Xt|Dt(W8fe;_;Gy->c;EMlj>to^DGgy6ij;z_67U3b5Je=|g-1t>C%YLP;vYf$25q)Y@t1`fKH?gXf*Si`gR6aQ1z$s_bxba|-DRZ^tdIn=1CX+?{UM~Hvu2FoOVCG(PZufTRcJX%;x7RQXeL{2Eg!37#uhYw<&l6SQbQ+#bVAl^mAu4PN&g5-{4en8rr#H#lvpkuj89AD{)qq||M!-W1YhFsTOk~lqs|BgsLQ<6ZfZnr%CDeUBOaTuDovJaCwKIlqX2s)O@U5Ku_E2jkvK;`~(t8#iD_SO^{zlwk^zj?u?{Deehj%>p<j>P=@rv$?77?Xne~)J8_6H~Ut3dJVcs4@?zD<T`*R61P%q`nmZtND+W}iLVD`OT9QMR?!!)!J~RH&gk1|CoJ<5LuV^lW>-Y+=Ri#8|~}xH35UbJTDvymTv!x#S7|d1{-sCOEUi^drc7qDhmS6ovp79IEfxYKj4lMR>f!^a2Ryx}6U(8NLK6QAr4(DsKCy$?(_rZs=FDt73&e+|ho=5)=}fon2*uQyL+bEv9<m!cMr@va)XMSf^~a3;p!vdq^MuLjD>OjoZ5_<)!8Jc-4=tB(QNm8aEXsI6Umrzs8#*dUIsFIiWWv#+#?~=BavvJ?Qfv^W95+r`#sR3h2uR`5vdIPyZ?r<4N`_X=D4wZGxI_IW)PL?!jwd8n7-h3WSq=8S<Iopk#6#m{vKM8%)7*lD#*<+)NEPwC3;0K)(3tE)U%Ra($8=nE<Yh`Z}klb$!u#j<4wyIci4rI*Q3epD~{x^%L8ojyH_PRwvnS*lDxDRj5JRB(N*eb|XSoVlQJuG?s=+!W-}hfc<Km+%JJ+1;*8pSj-%Wg*K0zVZen`W_wQs+iS>a1d`k0%PCPPIrM*K+<Y?(E;GEgFF@hv0PiW8Q<J9>*5!h@+c`ZUd;1C4#(q@eF4S}Y?avKAG1B}EY*=;Z%)I?;Ia$a^u%Z(k)dgmI`wEI5U|RI)jN+rHsTF{_dMx5(67rupO1*5zerRh68o&6kdj{;Q7zmqU*!(#Jo4)w4w+sYej9-97_*C@}n|`%zRjn)VrY|0PL309^N_&#dPDhh?o?sMi1r^@b#3X(UduaBay-ug;(|CBElzM4mHswRM6j|?+x!dVP58K<-T{81{ini4AbX2>wtL2q+wCq}h!5K-!cf5?m>`!^+-^7$|nB64D*4J;~S9S)-K0`mTEBFtC1+Vccv&)zIl!@swe8_f$`<V10>zO`e=s$-3Fb_Bub#))I?phzRGAHJO9{&N|#d-s_aZQrZ_9*@Whp{tMYLJgtxr<n6cUbI#<LI?caBPz5j)Rxs-L-*h*KPf}zQ834ZX2dc!(_b|2cy6f3c$3lLhe(8ae1Y2g~;-Qg3$7V;@I+o!r=0Qujn&Hqvk*3hT}_gDB3Hq^fqyHK2L|Rj{=(-vxHEp`)-d!(A`~QPkTGQ^PpkDMfa94T!gsw0KsmFu*@1Pe#49_-CYjf+_8c39{0ea?fb(A!V16BIUB`0RyDHaIxeU?*xlLcZcB^zhly)^A77@6)eG44l}6LqEglVivx1DolSyU3y}e?<TMn9Ng%?BabrEdm0mnpY_jcTQ?IPp3vn!jmZq4h3kHVdJclUvC8ra)?2<NNeG(hp!$*8^HEEg-V;11x|$_YPZC;SwH+HAvL)9GHAty2_xplk&Lkpi*3%@jSnBo3mo{#w8}Y(_!51U`6LvbiI-Sb?to=Jkc`4ON`_r3=t`02W~LX5$&Lz6wg|VS5LtBuNPc2qEV}6J8O}Js|S7*#mmZGs8Y0W+}>77eJrRSG3V9Mn(~5LP3}jXmPu0XcNS^WO>zW`;kt(Vq-m9PfG)!xP}AwQH^$uG7YI$J71>5gcf#*_(Xe#@f5S*1%@^}y%vHdmG#E>wi4fri%CNMo>w>X)%MCiyOwTxSVA%UvT9=!#|`r|piEnI&Zxs6FnzrZT{1*(z3H<i&?*#|yh@fI_WFH(8Bdmg@aWya%UACV&2IF^D7gk^JDQDGIqAglfWA+MX><nccT|6J_{)>`$5B4cuBLYyYx!__9ly*blMD%%nIEuo4E!R@_?U`VN9`nDCG(e#vmubuZ<ZHl$=q2{RQOb#9poqtr?-<8Bo}^Us!Kl*zd4zlE~L319z4jTib$e352r-fI93pZ7COizFoFCZ42sK=gv_j?jU6L_lP04>t9@mb**AxdsT>MnVX8OPX91E>lA{ch5qXbq%7!<J->kq-oIOqs@4hn{qhT8o3Q5r~#X{~D1^({YJRp=j1{T^bi6)X1k#W0Y(Q==r*&-){!vrJ8YS}%C$@BWm>O(#gTnpvAem5AWvtxQyCot`6;EefcWmDJe+Kuh(+07@gS;*<;$WpuAOg%NqThz@$X>JvEPYg?x8gHWX&hbf_<&k6NBd*4d=UjV(am=8C1LCG@PFh!#ycZ}roR@X2i`H(1Upp?W8;hezTCncwH+V}!QIg*1<zd&%Co@ZBx@GMR`ZYv>>F}oExXSBFVvQN~0PQWgpqdf=lDk|Qlm2zSAR+2K>cU<8x6#n5PQy3xczK2~n&!y>_90w!bh4yy_%RI}A)!!wI|oTLv9N-K+6`_2xdD}=SG+)E66q!&IM|%Onu<x~)mitJ*tK^JLLH}!Bo(DF+Jr*xsWR`o8C1<A@<@<kMpn}wKl@10$RJ~Q_}gmz&5&XfMN*1SNNIXV@Pt2wVFQ(2u*oL*;vK_>?|2+zc7l7+_D*Y<oX?X)#U|%y<+OUA;(hx^VT*n|iO&j2Om87VGfW4u>ke89WlOlh*}A>;I9g=0FIce#{vGshasmdH=ihvBDnzlblSCAt2eBm9+~0H=`-_xuW3TCT3l?nzDg1*N7*lW@WdjB_fpy>HG#L2kj9zy7i`U857(H##jR#MGHSEPN=9Krq7ffkr@t1VFU@Lr;6UUIA6rVSkl@6oE<aDx-7vDXx9%k8Obq>S~d}Rw_ihexCqe%GR--8PC3sF3WGbmcXm1y)Zo!QFs6&+XauHBt0XWlCNG+X#3jYNLVa7~$xU4mqShNMDtqNxNPzce)oK}lgn+bvbLVMRB!7{QQO3PVP6mbWca+(mLimI-e49J!Py+VAXFASEy)Q;S%?eR%$!Wu6%2SiZXVD0*P)KOD&o8lIK2m}W`IV3La6lp?9O-a4%$I@pqd9}L?YmPdYVdg_0j+sT>CwdV?juxk3-DTL1Mm!R|8oOfSwsHNBFE#cXRf|A3BcX!X+-Hs5HT@5*q!vXUZlFUQbx&v`xIlH4=u4v2mi%y)ao&Act?OPM-{`PY2_}lC?+0<8JR{q}UoXTf!AR7-y*G8hKHHc?)+oQ{W@0lSDG@}r*l*SWzz<PB#E;B=sm^^kEwZ>wVsv?a2!)SE2)#=oVo$_`I<+9rw%4Kc#kj4mefx}o&rxzFBNJPuN=b=<psmzXKP8zAg%i_XSN=_xFOGaU|CafrA;--^0h<ke_lek?ti95HLL_ySGoOKSeRY8M=KBK|%8_nNNTg2C(93lrmbptn&_oM&$FVTzTJZnbp;(0QJi|561I?TSSx~0Sny~dze2Q0{TuB?Y!R?%yY;}crZPO&4O;4#bLx}s7ohWR+^?rr8b9lD}63webBnm1Vj*wLnet<d!2m<r2OnsPf{4n|`loj@o-bx~q!3UWr1jnx}Ujj+C~QWGFsgMKmQoVf;QdKB77R%-{vD=li(v_En?28v`+^ctR=O-_5mg0MguA*SQ7tZpv|^_ICU%WWSv6p6%?iUgza;*P@Ok0cm5Y9i}&8+Y0}aHi!Mi#uBMWz43dh|pC;W+Z0J*y-zZXiBE_ecowziH+N_H{dn)Mue%XNC86=4If5ecUm-nS8GLKOsKmKZGc7hD^iP_5U-`_H6$LIs$+p%8)BfrGNtrOwKeQ6SUmB!x0P$Xo~wHb=Xwn)d{SsOe_e+omk0%eTGWOXtBcw$4L`5AykBSui(J}MSfx^A%X`$8v&;izRZz^LLX8y2S-#+yNT+qFmhN_R)H~6+d$Mg*Fg*wz8wK$OgzE8&4~<=sSDhT=FmstY2rxDP9S`_I$_On#2rl=i$OgSoLLsZFtQY~VVLZf}TNM0|ezfW3vCkYqg|;hy7<)_+mZBd{$rM8w;g!T}lI?x;PyZD0Yt!|}4kJ=<%f|CTeGDwrc-0h5`~Voota{t+J+hau;wXnKQn`{M?kU-OfIu)!WJ4swUOCN)|Em?>>!m>^EEn)^YOflyOr0n35YK}3P+`LiTcUW)@ft->!UHUj7kQ4#){KA)*w9lEW#E7)5R$UGnpw&wV){EHkTxqAR(;FMdCt*kXVMSiv(?LSx;O#s^9Hl}NnE<q)k=1=8*XOyz&lGQ{Z^~%zI?`cxw>2OcD%**FWchkG%$90$zIpR?JckL^mgn8ly&1~MZ^2C86c2yZDG0`F+@8$nKAI;zVjY;a8Z&~wLY+*Gu^idXt37dmxG#`R)itvpODA?Y(d<X+9P#0d~8atnAZBN&p2e08SIGUP*7BaTF1xl-BiVvrxC9ZygD^sP+IaaP!`7QU^bthfO|Zi#<P43b8LbzX1EM85~y(Rk{46ApbmNm!wQQh=}q#E-W0VI_G=YBg1%>~_NXFjons&|5-*)`j(YLsBzc)(_?>vNx=GvsIGcG-7Y26t&(-svtLL_1QE>X~FekTME}LC!lq9TVZ5h48vX37{RxWxX>~InM2=$k9EA*#38&Kb!;51j4sTUAt!|*I?0tiG7GF41pAo5>LqZjie!Q9irn;&gUn-Ohz>=<ge$BD3hK=0NFrZ|scig~~$uxJu^#|zU{cob0VKn&*g_>svQVbHjWoAG-~d{#aa8+fogiiyD_zL)`P8MAg=`tR0hbu>AaKk$Jh;&`~{2X^s6puaIKF{r*pe#P{U<x}jznJscRteAU{&^cmMgesh^?!ygQ^?h_c<=K2;c<IK?=*;j#jw!lKbOwL+jo1^VXPI?O@fTXQIgB=UA}3P@@C297WQF-2FctTZ){qrl7D=B!YX=UMbtj!ZLmSG64<8n!SnP6&#cHR2VcJD)sEGk-OMrd&^pO!}DAg2Yc!M?v*ki=6?E3I#Uybh5elRPcdwfvwZ+w7QH-Qz={PWj~0rf4;@i`O`1U_vrOQfZv5^U4Ce(fqpZ>GAsy~R!9Lhyz@FT%b!b%t`cAo^d!ki~eM1_KZRXn+zfEIL5$rQ~7BE;_$OH5eLp;vPKx>;FI%3BDPMHy0PRU?g{YfqidZY~p%+RgLx%7bKRx;|fBojpa}wSi{^fr5D)ebywL&$9#oLDi8^5-8t;tIdLwAI<wCl3vtd?f8-DubYf#LWH@7t1Xk9k?nnEo!Br$Lm~N-+h7qpZ;eLqz`@In#M4!5TpHzWx&$fGOufD>L2@2m`zrntW9eSAY6nwBN!A#Hy?$IT_<7dRZd6@<)-V+sDenqdaz>zwVpfiT`J+#o|1E|qh1Ev6zo%NV3iq{5LF>w^6854pRlJ!Q**$@_aj>&?C=m9gq#CMx5+Va3V)=2cp*Nh(Q;!t|#nkAiH#TDBv>x367sIV7Z-ZW+12m&`Fa@f#mj+?^Ih`q2n?Y*6<<LZ@+%Zv6=Jg!|n5q2vN%MUbCFsxk~P*;X-s5q>xl3{rPm<mU=*IPHL(oSrL&I}4x0!<QW(Gr@O(*70V(2RXz4}#vp9>$Khx)dd^w__NEn73ZOnhuV6JHDMxR-quqVd~9^fe2UJ3`buU2r+QzI{Uj!))1ymot)?!$5iAIT);J6z~+6i9Akr^jV2N|joj$f{Z?`N9=4;OUXeNEJe%av)0A`(&FI}c0iGa_evBs*40!xU_%wkp%Xkv~#0UR3=#cbb!xem#jF6K0{j(jNkLQm{{E`lVhSRaCLYji(!&lFqADte*dwy_SrY*$C(NN1Q?&}P*+|m;LbqSa`hQ)~iDeHgw09c7z-1$efKcOca0EG>{z__G;s(t*EEl5Xj4N{AyQ)J0(55QzVbR<H6MKVL;yWNd`h*0%cH(z&!Lfo|oOsDDMX9}c^N~RU57R@84sk^6HZ|qYW4xc=K!#T8TgT;K(nk%1SQG_(aFHc?{Mvv6?`P28q^fIE#kGL8v;@V?CgmLKo>HB;ZPpwiD3|C)^7<<qqei6dp<L~cdZ4ac|?qxh_UCm>!aV(ooXUm0Edb+%*MHm3-QEf^-&o$)1jrQReHIKpC%-8WXzs89$-qXC$2Xp~X_>1tS7L%fxH=O4Nm%bn9t%s~704T)6eL#fuGWg2EKn7=yShErdoD=68;6ScOIa+7QQ@hVeX^%_H*<IA@4`vUI{UlNmEiWon7qjfur*&5Zq4vR9pdV}2b{3Tz5{kouGm0rQ1MOa?X`I%=mfL#fttPorLsSkn_!E5M(*g_WeXft#4{D1c>+m~GU!VSM${Fd)hbE)A&wrY7sD1g+6kX}B8%2}Ow?3b8pDhu(Xvzu($geg~8o2t^V!3ZMDcNUJI9c2sT4W_1!Mh1F5s1S;0-`PANd@)MN5;j%kL(mp?Q$|SzLZ?<CENl)BqQW4Yh>%r{bqDoNYz(YDd|jL^NXJ=UN`noX*o4`RWUX+k_f7EUYhlp3w@T%fz%w5ZB=g1Z?VAAnO8y6!zq=Ik8o-%%GaJrLzii-99JP#nbciFx2~aF*U+w!j*3}fHxcn_prKKv?qE!3a=4-;Qxub}vB}e32C`rhWGtK!2gDdA$?RZ~0eT7-s<Q!&1@|9y``v2KS?9EMiXjQj;hh+UC9ZOn;XHF+u$wpE23}q|*8&YWXj>{w_E~N~+zmoq^N`@G#lTMHiNZ@@nqc-n-%4zx?r^%L>4LV{2Pop6Ht?#g$g)QQw5^{QwL=%Iel4oXN#xGCBJ06&Ud~xK%Zwr(avhZYt0?*Qb~bzAEG8ui<qoOfL=3bMN^AJp8Mb%qsF$Tf{%o05nR8jMDaB1qiIh0DyQpoKcEy{ukQ~aX;tC@x)bRv;73#QBs$dnN_k|C^d{=x(on-7(CHBMZcTKfZy&$69BQGGDQ^KFG@2u7R>^huztH`&6a&`Ss_z9)^{m2UGi;b+lZX;c<5f~s$$1<KABO7Vx7ifr0?nJX(3g28KA8(cmJe~MYqvV8A#<(5Y(sEgm1pw_lNXn^9c<s?VcA$ADsE|WDZQi$$vj1H*MT8MWQO7vwghIaKj%lvVC_ue4&aJgNh%f6vApb#W4?^04P!Cv~UZDp*z%@Mx2=>3I1A$BpZu_3P*OJLUwq@I8!h3N!l>n2Chf+P77uS>dJYE6oK!3~3OB!b1LUPdcb}pV3b*U-Ohg2vV#b7PDRkfrD>!GVTQh4f_sgw(EeMgB|X>)s*g?|u+)JD}dt`FQlM%O|w+>{>lKxqH9(2F*l2iz?ff-M-n%^8|<9s!ASsj7G}&n}J;KwZ%%1)PDGj8gzBW)(2-=1CUki#obdE%50Spe&N%sR)E=xl;ixlb}bHpdjstnfMX?e`@b!%|<iQ-SfE*OMho);eh!-Jia}{q|oh8$qI0&ScDR9DXLhe{RpxfxC<Q($mJTEAFEjB=_PT`2Enh@9kwCY^^?T{?W-gUgG7)>N?>y}$c#%d{SWrHzC4UB8-+|y6(&RUrm4X-Jb;3o&`gBGLSO1L3(FWRbeQKnPU!hyxsVIonfx^WO_Pgu)B%fbUQFMYc{0KG7F2Jc`EF}vXM=@rzg4b#W7kcmv$Cr2xka(k5P)5CayBWe37`F%6sZ_S+Mw~W!U_dPfb;Y73G7K$J;R>719-D5{YI63E30JJfxa7B@9B(mA&+Q6eu!#26qriK%%B3qP}aH~`?a&)7=Rn|p)cnc#|+B>-dSGoq-!{v*m`*EuyJ#1N=Czd{K$?&LE^A8S8FiI26RFXDN=Xs?Pyf<EhGZQQ`JL_7sa@+<#b-h+-mot+JA}ahE*f58np`MOhu3lbhDunOic(Gq<!^jU~g(`WlKTfmVLr!lNEg^+Ywl(b%v$P?Vzf<XZzGMM>Iv5(LY7XE>D4QFf>I0C*Wf-=f+P5>3o2p2ml%C9YH%CT`cUY(YP0l$U0^M2ikOi;kD!Dk}c?)KYAOAMgd-g1D*R<r5A8<f&*U8b@VODiPN5^XJ^T<olMcK885GU_v`{!@nw>ie9z|Td3=$Ulo$XZxCFMKq{w-avGrZBj6HH^=5Thnz$ttvot;5&cAyp-0wC4#p~mQdDm5B6K8OM0qZ|o7t1j0*7E>h>b{S!Umin@sXOA(6=fk!37`R-pAgiE1g)A}fbAzA-E(L*e7}e7(n<TMA4a<e|;nPPoJt0J<xrhwq*#<j-+BvrPC1wtD?q&s`^n#|#nW1>My9yA$9)buIZ$rqgEA%0|7R|S^*&_EKROkah;N~p|;`-(uG&DlWFLF`b0wLpUsmC=0gbza^qM>op&e0hj6V<}*S`mF9kOf4-Xp&qLoiNR&a$W@>)fxF%3W(|>AcE*bZlP5~M<W^^x5zgOBf95!2#(Vkh8jg9U0}p+ZYD`IgPVxBxM-{bj;f3?YmZ|r#B0Snja7ZUoz*Mngpz|(7c^fplq`VYp31dsoLg6)YmWFJlt#c18fd9O-vuuhdMS7>cY!asv35I_KOl@39Zydt6KPUHh~#NfHYK6+QUNVHFt1oKBe)P%1zp%-0+Fpr&z8V6*W9LSngX+GRoNQItc9JR{G<;p>SBZJ**ZHR<k7NxnNAmLS09yZ;o`L@Az9zW4aKvt1OH<v*>Iu@b0vv17u!A8U?|IIioM)l0V3GP#C`6N>uDrnPkoi>RvX2)vJzpCT(w+4bT4B2>S8fxD^$Wmgc`q^xBwMH-%fF=nTk<;E+A)UY8t^}6WZT|``{5_6itU%RA6h(p3i3#UufOJ6?Y>=-|?2N0mECo<1b6m;+luT9bf}Qv-}`HzAcPx;DX9$W-vDUMD~)Tj6;rV;_P~zPLIe8*UZNP>k#{j>79E!rX<*{9ABH2DO*Rc({yvYNLYJ2jSw(n1_G;442mYNcpY9`&;<fmS-VWvqAa{FVGsxe{+Nq0RPqWCfkg#w3(CaTT!v8S#aRr5HvKtGu4dVM5xts@GR&edwIXNnNceSy%^;`<EM0Rl&1g8U2I%#_78ZkPr2|Y^S_BIj`s%Q79oV~6L(<#Sd>gnmFVj2)?!YHXwa>-mI36L%6=XEv^JzS}idXq*HcO_0ZZXzvY3o<<d}=g}x5ypQpsoLM5Z>^nz>}VEuYorG|NgK4?VpJ@{kQ+~|E?7QJ)!iVh91rNRtO%qAJ2!N2v1S7t7H)NCyMGn^d&NKMXTleYwIXpH8FN*3O5WL7I4uZf})p6yg&zInuXj9Dmaf<PZ!g5Y}Dnfg(dAph;I&)^Rl{Fq%}#-lj+c|I{-XYYIeY*ad@xsMYY;v9=BV0O|M0*V8`=h0(dRmZwVX%0`=xj6R2)ToR?9f_O8JScv3YSXfTY1oQ2X|x*i<QM?=g@IU6b#SkBflbrTHDOM|DUl-jm?q6tBXI2Ir{)5k5)sOeAXm~Y<%PjN#`wUTr@@ZgZ3Eun<m60TrmixeSF+Svng!7e%|15VnG7z9I42rb*X{eTdJdqiFf!Qo&iRiID|IU5G`_-S@sD(zLyw=GG0=dH8s+Bq8#_&U;)qu9ALr;U(?gP=A1A5Vo3jnLAtkhErlxPT;X8VXAR!H8H10l|o2cF2fnXdHPW2n7aj65=ta?CEHp=o`j(Z!8EiL-l;RW-d{(HJr!kG(JxP(lG$=CR>!QCRLkArYV#*r;>Zn5IynmWo;7)NlGot#8jeV4cWs28IC|8_UcrESK=FiMf;<cGFnz*%L;geQUjpPd@RC;Ux3;vy>7U!pz??|vNKrDj;Tb2+mb<rs~^UzHE|^^Agu|Nw~kdpMMI#ZU_#UBV6q%0qRS=IC@|BIDDvRdLjW;Qnxt3}`q?BKd<ub=!)_=9lx_JyQw<*$qfir!_WP;`NvFu|w?cUFK!%iqxiy_+fdC8<5SU`cU(QZ>?oP#fx!UyyRFBn4EdT<BEtYN&4N0C))+yOhanQn|<}%`{4FSTrouzmOzM0ps?L}@;bBlxVC(DvO9X8R=&lOoDWxY*@7UPjX?PSs(jFZ8qWN6&&mx@smJ}lfmx`%us<&M%y1@$tn4lfKt>a)TiY%O0Hf>wluVYr&WFcd?F76#*~3&U`<{;dd*uT(ToF!;)X>UBiB0@Iqs3m{FV=CV^z8X91D@ddgi;Q8YN6u_Jh&y)2?qGF_63*ZS@%NBCdQq|>Z6w3H*6HdHbWG#xV=1m)ZIt7f5(sSt8DHjTLg)gG~BFh%z0@Vh83{<925iJawg#J?DE?|*UStI~MUdV23mq-Xy6^E_72+Iz3Ysh@%!JK*H<*VZYGvtvT^i)i2!*aq1_z2l&>P7r1;V1?eb^ZAAyv~XaHa>LhE&|qxR_Xn}eXisMXD{xGlsl*lqUeh6sPS4&zs5k&_FH9DhY3d>s8j>t%uCqNn$%=e#LM$$8q6Iv%hJBNiK*U>(B7~<XLI}`%;D7SwL5-3s`}OzC3}Ld+>N%-PADKfR%p4W!mp$GPVIF>w|#UN)f$vHYKQU@W9uduihzceM62SIx&lX4(pLU`<4Ud-KoucI;iXj(FTxGzPv7U4=MgE$9@VxwwTKlC@Vr}#F4N=+=+#HH4ot)r{D0Ss#PFx@$*odYWa!D$eT)7S{Z^wq(2ry`$nL{#v%9;~?6iBmMomPpe^mQJr*k%ncjSwf=uo%4UAu2Jc^|rq5eNKJ0&@cAd{7*~xpJP(SM_v}T%arKgyPL8`V%iT^^yreN?jq5qMgR2#BO1j`vJ`MK(s&>!8OG8VRnV!v|Vzbk!6l7hHOPrMg;IQ&40=*(%GpClrftf%j(btc{=BH{#+x?j{V_0o)430=*u7mjLrCq)fZvtjSPeSsqT=X_s-oC7=or|3I>4%LOqp4S>RJVAB=;8o3HXk<+0hObdNDsRpBVI`FT7w$8aY&2$al+x@tM$$%SUGWzH`vBKQ0V#E-*4oWrYf4ubEzyoDvL><L`e_BZ8sW+)iCf6VotU7VrWH(HOC7=rQjkBeONy~x0Up>fPwVFVBSWqLlX|Ngn@gZYqtY(~FFVvF<%YtiS%x@3d`5MJ1ebov##WJ7X$MZN%Lw+j2ES}U>tz}1QI!$eWTW{&2u?6{L!U;Olf)^4LPJdta9H<%|-S*)dcZJ1ta<%>3~lQD(34KmB43y8K9=39Cs`GQz@kz%=5B%2b3j&!5f8cuf>>4KA;7)K&hV!+Y^gMLuS)7ip#kxYe;2Aje_BewCcSJVTh>h3#nobo|Y$MD-co#Ea!p_;D+?4llR0zsn;=VNUECoxBh@$%w~Ztnm=ZJvzK$nT#il2It;kPjG6^te_Q$w`zWS;k`@X1H{|JPQ?;eR7t~l;Z^vLfmLIX7jG5_H1o6?1v@am~w=Z3olL&tszTWdWI$OU#BF_sue27A^^NVw8O+z7do4i1L>Rg{ahuuSK(9ZY%#5Qg`G&l|MUL{6cM}Av8R6qSX(54_5-0n{JavEwktz&*~XZ8@8;PoK1Zj)Y26E1aVLih@+3otuln!gUDTK3I~{Uono&CJNAf)S+^`#o{5wWTGR*6XZ+;_o`qBuTzC_3v20^r9M^EQV-n+-m0-ponEX1ykXEUgKFa}n$&dBs*uyDZ&D879n3+MFKL#>*;!Z=u*FcP$u8oub#-ASC_6-6^lUPdfdK&BnJ6NDu!W5;nGDH>HOL+WSQ0;#ol5(xrY6u;95c-a(Dv;k*YTQ=>*nKFC-{Cb9Y(`1)~6olq4k5H}ympS%uvT}All>BqD`eK`Xiws#X8M0uzeFU$lkVQB&{zBO9W7!XjkAA?K#b86@{e@?}uU5stO9`P2^B0C?KD24*Bw!QNYYAc5G#0VLh?i`|Qg_rZj5eyTYe8n4Tbmpf_Dj8t$lEkNODE}K^>XQQ0`p|14laz<c9ftsjK#WMgo9Jq8qbt=Z!i)TP6##we{3&yc!}{Ul4%aTCHv0?IdVF0f#4ZjP+$v3r1kc4T%k?nJ4)VoO7;oo{JG^rD%<u7QS;OszchPsMY4_`H|s`{FH*F37@l(V({M)u#i%QyO|u&?A^B!~fEq9qpjijma=Hk%?-Zf7u_3eJQM$;V5?co!<qv479_k1XhIg<h@E74@@l!aG=n6FVga*w)Su}L<dy@uO8fCTNnCFw3XE`@KUJltpUS!a;79!dNzsx4ddJt5!#mRg3o!zs(HkPvMWtZdi)s#NKs(N+4s4!&0om~-D!1{`~OdJE3bTV0A4<~h*x3I9&-FQB&GDY(#tOM6R2XzDM>`$RkE1o3tMbP^6j49P>0Hl%VSMm9hPBdbXdQKk4<SQ?OU|o<+{p$<d0loHi!$_H{3^OonuxoEUa>0m{un1?X-3y72jZQg~KlKSE#`j5PJd!_EY7y<eZ0sF9GUKJkQ*g2p-A~(n0lWL)f!$v>tBDDnjRpqUB%4#dR@)|ay$aCqt*Bkb^Lk4zU|fien&C|$K2wa{cz`)(T9n<SQL|({WMV^yK|>r04h9UL5)n>{1_-<s{Bb{a%RZ{q?${<BBzgwur_(auw+>?e_5V?L<vKP-#U1@P+S&0?G?=H02Fh^is?_#Q0U|X5#p~=-qvrX-(~;KTlg(W?|6QTLcg_*_X@i%_xv}x+tZVR*=lKAnx$vY%4O5+dlLxz@Z0Qh4GLaFYe=O!1G0rKk+#Pv+;w@%ecJR}{W7`Vrg^97r!0C<vgEymr&vwTYUkfS#uSRjuoX4|M=+UQ!8C{EyYP}lxw=D~B4r|sPi9Wy_;^flYiVpq|vE4aNWcJB$FcYvnGdzYvjuzC)DM4&lAdRnVxFt+&#5<!MV|VGx05Bnrb@xzZQ>}vekUdv`O6_RTWXTliI4Pk-2Lk>j@Z~hQ9wZ4dBnFdXcx#+p8~!7{x0!I-K}gq)MiGovRT!&c7&ld5AYFaaXoM~C`I^H!-gFej-=0>%jJ{I9R7g5tZ7eLaaB=V}an({x8eQHHsGF4BWmRFgsT>&^!9cFs^t)IsC?sU*rN1SyZ!Hv=(0)WXmO?9)`aS!@8QH1%@5h4tBcZ$8(zTk`je@`-zc8ZeS5^fvtCoB!y(|vkRmRl<KMv=|Pp{nA8FNi%aWRV$oePW!e9w%?Oh2LoEFDB!&mtA1$v$rn()qxui(4Zf$FuN^F<FOEGDx`M68%heG1TuQDNzS9$GNdZJCr`Y*Xx9@^_kdXRA{H8C?C0N;q1HxNZR_hYu6m@G`q3<k!OZCp>QU2%Rfuc(?xD(RTMz(!ZjPU%q|!oV9!6MJX?~~b)Z6%jCHP~?rPOwgJa0p`pfm~i&$v^-etYHrdik0Gw6&Y`34ZEyu-D@7To}X#lmR2Q4+0jXY>gvOiArSfH#?TNuxS0QTDI@gHsQRjUW;d;wv>z``<bFn0O$%b^aY}-2_;njbZ{wYEc$(I(Zk*X-$6EtPM-|3TuBh&j#r8jL2)4pjm&cj~A<8!+|nNCo#_8dN6iL1;?wQPT|_&OOw@_dEUgrnb`E4<&6VW@Zm3RUDJnNxzKx6CCB8EheB;+cK0t?I<42De`1TSTJ&%K{J&G9<RZ>%`4q*nr;BvvnOkH2k(6#Jl+>n!lX*PNC!{QrPDbj!ftzZwIvK-Oc`_Xy#+dl%Tw7$T{Ujg6roud`Zj6Nm0#Qbe^h<QCB9w_~);ZAzoHA(%_w6-c36OR8<js#iJ^AtZ>FehwPo6zFc>;?7j!HQ$(ySQDC^kxxk_g>|R!UVJYKlq(t1~}XKig1(UAvH+m@MX&<BDwLEE}%$7PMZ6aEme&g&M=o*K*9qUaYrf#!{`EikUsrl^X^i$BKEP<iiWGq{IqS{dJw#Xc<)S$K=Ih^hZ`~C=fx91^UQj$S|INLPv$#zx~Vq%kH`V^3OHPl-8lDtd35zVNxlIN!s0;mWD4ONb6!fQK5ohCD?+kRR7e_6+C9@Q!uv3zhekZ89GvB3bJF-ug@DKgIxwg1>;AV5J*24Ck0ZGGeu$`163tS7z*`a1zIO@h7{%OohPuIQ2m5ZLq^<=1}$GG!T)9A7`G*vw6cD&oJ@`v%VC=R$U4oH6RK2-MqGeuER!rAzE1M-N%rHrpU{uN8f6eOg<~wm%vuC+ZB)HKC36ioV&HP!2?B(2W>bZ0-P-1fu0naH8qpG+tXL1N3?9%NU=a^K$(+Sxcdcv9VIBIl5O%nh;}He>pPt09pDy!N{S5w*!<VLY`HIWY<mW5LMYqz?6%&Bc!wW%$cRzl?^T!ye?uQ~hNQI7Zgiq27Qb|l<jqY0m)-i`+%c4u{^Z7iR+p}HjQN@9Z9Zd$=y(Et1X5z^;;g|Xph=GSaF?`}>-x`5Bq*RxpF!SP4qi;k5fHKGDY`HK$h&$B86RZPSFl3oxH9b!-r@Ytt=Vr9E+vx;07YQxI&YUDiF|6ndpbqPKk_>^2mCfMfk)l<+M^g3~uD)q@RY%VA@nbvh!W`{3!pWlu4)L(*#d1>5qyGkA2|{<L(FAsTdv~wb+vz?;`gW_gySu&j@L~6X)rc|!7BzwSz8`J(9&SI}eb9TTgvFn&F3qhDO|oV*P7OkElA$d=^t+A@2K8|Yto8(sJsZkwT|$mo!2RA%b~UrqUr{X|CllB<(iK=13hQ1hgPB<%rk2jFHm`Tvdz3ae5M_VX7D09jEBCnacCfOSX@unw*d|6%>cLd%hDwu3K$YDdreE(FHOkXJ%!2tO=JihdA++6XZ|}LFoXpI6kif}NqG_mNM#9qQEzJTk3+I(Uu$<`mp$Ds^Cp(<%x)bb4c{YeyIK2d+1d$7))S$w-8nAFPdeGhp&bMvm|48l=3}M&X1Je2fAbuCBH={kAOZcz%@dI^`G^%yAuXY<oj+R;be3G5Tu!66s_Y`2oUK_10hQES;aEI?8gdImfHTWbeIZbV=-WRyS;z7jq$zKYsCyZh3_|+{pSgUroLT$$Z)~et0i@T1lR{5>Mu?f2tcUQvX>>6vptu;($ETgcG52&@(-VLq@2Pp*r_7K2c6#&R6!)Q-oK_t1?|1DfmjS?i`#pJAmIqEwf!v8wDV!#>HI#I=4;CVs@u1;8g0AV5A#7{CJd>z`fS`Md5PL)Nj6_TR=J@W4z&$UAA8J6Ug_@hYA%rL<>lTxz}Vyb0v;zGqtZ()`P>-)<34zu~uQe~GUL$T~*`3t2&hlyDP6JZ6fVB_BW201o1Or{}L4_x~qDo#mCj2NYMH_7vBG*LWWBo}p-dzvc^3CgLF!%b>-F5^5iLc8Ao@ZbL7>K|I|=;OWn=S|kz%+rgyQQ{wR{&ebiTyYBu=C@4A-tDv_GR}^EN#|tBhlKay8#Jbqs;AT8Pp=9xPY`cq2YW~^fkPQhze2zV&k$XL-nSC(Wm7l21zIor2||sC!yyxKu|AUaf--^$F`iW6@lqf!eWV6}7NJi+%LzBka<M;_?gzV5VnHu5HWITh#BIm0(I_7+&^?yQx<DvrYmbYxowlZt<VFs$^vyMZhKX}v>zh(~)Ib;K(U}F4=NRR2gjimU)H+5CZL&FQDBu{Si`F7*$y`3>+!Z7;Z0Jziza{ewBM)Dsc}|)FX^Ag9)FJ_vPSWUV467Q>I&qHRc3xyCyNza(<#{@dfc3m%3)+3(3}R?WbX1xX*OH{`I&^}wELd^Imh916m4w75O=<xqiKAz`;wv~ifHS*8j><C8Pt7nq<^tZZxJPmvMwbf8*J~pfTVCj*QgIx?(7nim9>Ez~?2u3cjua(|Eh@`~6P9|y2(zT1X&k6`)zMH~MP+JE#PZz~A>Cf55F^IS9wj+kyl>C)WR5F1FvF^kcE*jXIDeTAhshN8iks_NC_v(~ql|OZI_(&89vI&|O>%Qk1Rjq*g&lTJ_yyIBq+{H-%8mnNwTWHFb}ka_;mE|Jlv3(9A37h~0~VYekygmG8N!~0%e6@lYMR81i_4BJn={iNg)F8pYDW*dKc*+A3l8ob2P3Uhw+fcS@N$)xEG=WN8CE^&9nE_?<GI#b#a@H*oF>_|aXQ1P3zX^w60f3yEJ-43zvNLuCGDb8%(w2&mf@~k){3t{f<l}&GFc?9>sqeXA!kFgZ3Nt>f14cQFz**JN{%DqX3luZ$*xS=`SrY-0$08o^{`g;hGt*tH4{_~4{KZv|LgJTv*$0K{B(G7`tHfmlh?;iMb}}^+6zv6)8JPTjTilh<|!4DvVWtDOz0NXRyF67nV3o+SZ+QnvPo7S%crnp0t<2_mNIzO<e6&pFp2I`=o6MgsCiMw7S&YsOv5{qb`ejP@kB!6OPsc`c^XQ+Egfa#rh4xlSDz-=3t9PyzdNf5_BN1mvJ6!HJstKHs3!KXuZQ<pC2I;>l@y*EbZpenKUtbm)Lht26r}gH1w>Qy;?(RAo*zX$*Q?Rnh0=7TbQfy(XIkRWg%dVDu#jz;C6pK`Ovv~Y%@pWWCB%I;sPkvp;1h?aKZ(!GsNHbrJzc90L?f3^EhtL9?j`y_0WB;c5+70Cv#Fo8>MNp8g9%tez*nY1Yh;I7vnd(Jpk}QhjT|?04E}8d9DqOZ;6DWh|H(C-mOcMenm$ICqBWq08}!62)UOw)(F3F{EDyF^i1HZtv_FafPn;XcUij4478aA~aVilDXK{JD0}ZbQMcud(6>?~r5bV$t<mM0u;y|GK3>_QbqcIyuZpP^pgCxxoD+q*LPR<&YY7#KVBcI@7TqHA1rknE87slYqeVr^LL%O1?5vTV<yIyP{?jBVXWpRG7`ILPT(!a*6+oCD#4kJ_G?g!(!zYdR5h!w_eNFp{h40dHul-F@O-8jyy40D2&8v=-$ezTQzkvI@tnA-%Z^y%MC$zwkr2Z`&gr8z_!M5KpLQK+Sr`Awsc(F5~r6ES~^z9dusi;Vi#7optDZ)?UDjP+3xmEf~`9N61gnn>82J}jqGv*D5LpKTjK5$J4vzOz4wUBDIcNCZl0;Q?HB+ZqjoZ(O6mZEjsZ@)eTuHq5{k4AUyEV2lD-erJY;;N6>MljV1(U6SrkyT6-8v+%D<t%75E>i8;M493=>Yh_2MA^~5QsKK&Qx($Q3*8Jp4n4_vZkdyME0%HE1@M00@e-pHb#e&jz4>>`VvO(Ibq&+8DHo-f$uCn#q<3v6Y5P0!C8KQ&6!INjv#f8l5gF!`QBoCR{r=fagrJq@=SP}ssP<&_Uk<1J3g4r5Q0OXxChQPoU&*`<`Nexsai%MbzFYk4^q$2Y2yhImvuP#{pt5Uz{GxPE|gBg1rs3{Mg606w)(%oA(GMQ2(Uep++lhJ11+jD-dn-a{s=v*@gUv>B@sZ%AY7B&~V7&>`})`_O>K*jy9+HbjHHl4YE&S1*HILcBIp(AC{%EXI0LD|-1c$%k^PvknTYPtd>wVbEQHuh_w<SLz4l&WCK(VQvuJI*VI2dR)|gxa+kMxYPZC+Sd4uD=aJ!&Q;tD-76`w%!T6{?Z$(xQ{XeOQo*bNkJ-P3aL>J5XwKo?<%gUO@=W`r`39oTI=H(@p*UbH=D03YV{WDO19YWk7e~~&8`BnfaTRfvXfiUw=bSn^Z<aOrRM(vRDu5wf4sf8?^8<V;s%@`vvE;#BrjYK7g>tDfAl+o09>?JF)AWkXotHm-_4ME#}T!+cJ~8veuGU=Dni}BXr57+aJLE4g}r+f-37QifwnrgXls$pHg2ig-rnB4B{l-zxUm+r*1H7`Q^sIPJ)aAEwuDPa<iv{(mY8rAy|xy(NPh-unL<<wtH9_zP`NL&d3uAwJ$OBdrx9t0qTd>}v~0QH3}UP5+=<drJt8fY%afESvJ4oeGK<WP71^a#S>K~7D?n^nim;tdn9P#t1LGNbZZ#?$u_dDAYInLq=glqAd9xm!Hvx2NoN-JdA8Dq7&`0BA%9B9`!LO!^IzWh8ez7JX8x{M_Xm1Berrp06)T11d`iT>On1>hi5M<j*P+x{Mg&mvOLpy)K$`1WC&gD{6l#aK6WwV!kVQ)J0f3q)Nk^R8+J&q@%FIe5{7pC#%5$<nTnYbYP##aC4=nbDz)EB!aUm3aCXjF}CyNxx#zr*f?i|a&$D}FK<Wb+}0Scv`@J?B`=EK0PJDsvd#mq|RVM6h9CV4<Yrnx*8M0X$5?83n$8j7u;Jj{_>Cxpn(q^Q?Q_^a>S%BV+4cbYxCbJRdfUBn-A^rx*P=XdsF9;V_}0ynoQH5khcE@74&=ZfC)yBRWHq9}T}C>6NOEM3F@Bn`4!%0^LSkOcw^3F5P)w8avwX|I~9A$eAePgExxHs<`3&P*TzeEUq%|6qhz*kE`dB@@7s$GbPZzCC2p=60Tj2w~(e6=PN9f3Rg_S_&1lzyD1gFA+iE_8LMpHucUfF`2er^uWM6S$sI3bGup9iMgvJ#zsm5*=mislqg)jz#MS|hKKdn|Or*@D86BS-MsG0}=4*_T8y&}^WU+$#`bSCvhE5CCl`T<9Jda55ys4I}EC}*f(04gb=3a#5+e+OwTXTdUm0$D=5o9~ce|;Q<9Pz&`nshXFUWrx3brh7H)%B%xpA9)o`q^b}PyJnSphIHNUQDuhQTHJSh(Tj0Xl2oBlSBR<I<2%#zVcQSQ>6)Z>V#q{;Mo3VX)hc<fN-kbuYXGw2Ao)XKb7u~(&#@`SVTX?@Fsqb!3@Of2j%s^%}~5aAFKq%w`ki-aQyWrKkOL)x1da%?8{$&Xl_!XFJ94KY0zHY=t@h<)enB7q4?|HOjrF44xgf&*I%>>9UAZ=p06SiEbEUE`_o4vyjE0~I)>foDUs)>R9Iw#Y|=2UYL1lk^y|gd(g4G^v;Kbjn>i+dm<=g#6UV{<)8_MIAp@+T#p)@X5;KhMIIlUmy+YB-kdG_RL1$%s6IQTJJ58(18e>tru-Gf7ytw*mA%zmOo9X5Jq<5jwx%awlN9v^ddprOCySsMYwqYQ=>sJ__97IrtZgi2rb%MZ18Wgnyw_XZareL*t7#4%VL;id3K}nQICP9F9=wb^zzI7yz;(Z^Jc*$!IUN<$`vWk@z(x8_mqjM%;NR+!6n}s_Qyr%6eLZis)$Y&Rxv3*mLH2cSgA|0d8$1ofg`mu}YJuS4F*tuMd#`KS`N9ALi%RSZJ)DE%=%jueM@)6yUQmE<QQ6gP=JQN&g5TYVuC9v#&q*{aWp-SvnO?~!1=^dGkX_fCB(}V5pPO<qt)lI6Nlehm&_?Bp+MtAbGt?)DCau1m#PYT}NTpjcC&FF$3zBdoceU_^8&1*aZzvO9G{Vrd2d{i;oM(uLc`v?lM2U77Xi)y10MXGu{99pJ)F}U4<a>w3WJbZav(Ex6PRyW^Pv#&QZYwwE*p`-+w3Y~&!WQ6z2-r=`tsvoq>MbY0snPR6g=#gug#!tDL4Aue})!2`es{t@Jqmfn^FlFof>D^U5y}7E+s&%j#tx0`GC1xU9?Xx;Up9E%4#gA5@F4RM;DtrPS^)*=3xrDHp2HgugDD3j@d>1w}YUlAmcqN?faICN$>*|=p5L+fki2w{&D8~m?ygtFqlO-CwexDT?jvS95Y)O&&(oaZ%0?B+5PDilCMVV9uj0G(h&d@M$<LZSYjN|&KN`zO!>2^{<*DT7PH2dKUNw`Yk6L2c9cz0~rf0lI(`w3wO>Aq?ykcIIab~IHQ#T2v#YDYr^J499^<8}{&kfNEoctjXf6nI&W$4jk0SMU^uYr(v(8=R`A;S+<sw4VY?*FaTdVX$NbT^(*+8tkhX-DCh`Bc3{JjjNPuH!40IYbyvw$69W0?;8*KiE)hLJii_CJxzmGLALMX1@qv^_2P?N&ASbQ`nazI)8P3Ge?MOEmFAc5gdkS@->V|O4E_M1+8aC')).decode('utf8')


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
    """Full-screen top-bar tab (`Gerador de Vasos`) beside Prepare / Preview / Device."""

    def __init__(self, controller: VaseStudioController | None = None) -> None:
        super().__init__()
        self._controller = controller or _SHARED_CONTROLLER

    def get_name(self) -> str:
        return "Gerador de Vasos"

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
