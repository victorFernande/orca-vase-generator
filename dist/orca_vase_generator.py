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

_BUNDLED_LANGUAGE_PACKS = json.loads(zlib.decompress(base64.b85decode('c-qx{X_Fkqx$a*nh&UG!)(l>b?*|;`M2toYx@hx^z&2lQRCi~07pksm*D}%!L4-!bCXf&YBM_SqmXSuXSd0t;1Vp&w{t*v7BYpDy3HMzxv$CqPs(Ykqi5mf$uB@!AT;6=weCmDX!G7}Kqt84TH@l+e{_h15#a<XZ_~<XTKiCXg;=xDp{`Ln0H}Mw4{|?+9799$sB<-YwD>2+^d68%)^w5KT5<y8AwM6vbqd(vNU=q1O?7Mh3#<$F;Q9trx;q1p|=t_v7<xWAf+aH|ox_vC)9Y#GDt`Cc2Ng4@wQvP)DeZO;k-}xWTp~wrM=MV1fK^t*A_)7@)4#7{6-~;NHDs%S0V<K9FTkuOnp6j%r8!$va#9BXd=G_H+IsWh$TpWii(bqG+k6j5{^u)oa;|5+6O5oSvBlt<hdqmh1NkljB_h1z-=++_M4HB4OxHId*eD?>}WBHmEl<gNOU3z{uOhu9i809Z_I<slS-GFi^cA*rDT)2m|eXqq$s$bh5+zpf3hB-8!=12B<3z5h@==|%2*Rxj?%5V{OMsCOHx<ShqvBPWaFFIl1BwcLDiL>s8k<<19F_ol&aAMh3119+BG&DXF!TLchH+Ecqa0&hdE<H_yf|kP6ai31HN*FuMFi4^h-|047?^rmkx^g54li2y^SI(^OHIFz=?7EYLj@xR{J-oFuOdGzKYGRE?BCpd;__yQX{Cm((stHd;q8Ba*vwMAbaj0JK$5dc1n>2a-N8lx16KL6u=q+jA53ymW^++R3fCOoRJZKl{a?=rZe7}gh&YXxtKb0GWF9w(B8Q0nG`dyc3s_8nrdLnZDmIDiZ1Q$g>g<UZhx(-&My#f7gh6zmFtnVUO&x&a9QO|=0)IF@X-^G>rUDtzup@!Qd!h{Xn6hMuxvjcW$6FZRL4xA19eGx%n7%U+{@DFD;YyjEpiksnr+roYJf6xE<Z_e+h=G;Z+5r;P9w!^g5)20ZLhv7-8G3R>W)bF9nAvY4R-DIV~H%+e<K8)jq2?E;cIFAW8>A8Jp+dn_Ur}w*k+MoJ9m0R9h@g}PJ#u=yAb7o!N>+=qwqFI=i7;bQDf7P$xmW=D|5B}@aTh8xbLE90tJ-k*c^?%Qw{th?=j5neu;p$KXj4tTn{2UNKO1P(Y!Q^_!c+%!!LrgUmr|>V_+6Sc$Y)QUJ?96R=zLzW#`%;%Jmxe=={D`yL4?}#RoKPr81A2b&HZZd^={h^Y2wR8i-DwoUC6UWcuO|ZJ?6I@0*TX61lEFWOEJ0E^X3mD5`~8Cp$Kdv^IGJ{Kdp^tsF<$jEbnp(6Brw&W<1@dGJYb2Pl$q<n6t<mOuU*IBBEU|~x(hH`;Ad)7Sb*cjA~~+zK!NnO2wsH~aX9P~6Yk^P9k2ny9ule><IUY(;ymezqcrn>Ox;#QjQd~jop5HOFpj6@SyTac!$zqbWSMY?Fj4rqzO4VGh!WULK2~+M9g4!X=L_c#59c1!m9`xc5mdnYNE@&J;5-&a-V*d3Za(DzV{HQYqX2Mz{U852{>CqU{`3FfZ30zy1Kqg!2dFCSZKE=*K(GMJw2#xX#}6A&@$gYEPH3?D&fzd(w!&3tQ}-HP-~vZ<EE3h>+k*=W!o#(i^BN7&B2r74hG*RXcm)tEl!5Rzg&(Zx0=0G!gm~;ILFjT7uLJDH+3C5xFldpS%t~Bd%~|35sSo`05u8yN(XVzAD=QUZ$66ie7?(ULJk%&2gulS71#ENZ8O+x<y8UpbCLHXGz(WSYR4@0<|8Qm+uyinfMf`^&VD*oMJ_sx4NgyUHCyK?VpdfS(HbdaywAS1Ryp^Aw?|axMR3@BlzW^Z{2x4NOD8Sy}n_S*?A0|EGsJj?DM}+7*uxNqPqn!(6IX!=PpCgX-fw+hZqPTJzu!TViLVw{;C~w2;VCBNw8>#2FKx8@~UA&glz=1UU5G3ExZWyDS>^oj8MHAd#Bq<&vbw<v%>0j;N{qVH&IQ9$6lduEZnI*Ub`bzT%JOeXf^fGo}))#3M58w(rxj}b8;5ccIx)5@2n(5Oab|Z8KtK1I|1x_Dc;k0oZw8E?-Fwbs&xK1ok-Q(E^w>v~eFsm@)eiSBxDW5e42US-0f&2_TTAmrulpK7avrWze&rXcJd>G|Cy_lMB!iI2;K0-vr?6$DXk3x??K5+A(18}=~VBE696HsWogY(dQgcvqcr%O~EA^AS)%u~1JNOn-i|8@M&{QOZ5NS)`&nca7Ae%DSIJFPX2O+JGx2wK8bnt?f^nR=93%GRsrHod{6kXn|@9J^jLxB%){Pj=hcy=(TdnVkonKCTW8O-TW21SkAoCtq@&37&O;t@mRmY&*~RN1sJu3?oMQ<bZT~#%o~_vQt@mA@or+0~s6DNr)NMW#hdbRcNE&aJJFA+{I~{(gWer5>V|kLAdlRRM`g77KZlB(ViDP3(ORLxW}G#m>rmH!F$^%bhx>u+vDbTfbu?0W7{8;+ykC@=BOMR@{H_SQ=(Z#&AnL-#!DjeQRkTjSq+L<aE7{&>fv<etKp0pb&!V{6_|Hb+=rp7ff<vOf5cWt31Z_tB)^T<kf2k7@V}gAmSkJ~X7X%N5<X?AAQ^gL99jF^fx`PsGgX?XtcF~gSyV!a|DcR?dwn-!;am*-J550E4}-SX0bxoS`8=}@VBxVKSx0rqoB`Hl)IbIvEO=~R_QDYOzI^lV|KQ9Ew?}p{=s`>H+-w+=j8Z-L{U6lZLFe!FGxc~Lg+J<)UeBW!svB6j=c10%lls#h7p!yUDPT{5UeG~ts5ROD1-GfNhxY~jB5T`CGKDL9^0AQhJ)BG0y80QkEm$d=@43L38on2_U|WI8=OJ_LMq%3NDt64x!X5?{>`~y8FxZxQN0-dNqh11bCbR=LkDx@4JybSv9g;BBYz}4j1BNOImZa#Atr_E<c2P}<2VbCG9i!!iocdAN_}G1D8H6K<7zZr62B?m}@~C;(b<W@$wD27uDwE+qK!ll~8VFXV(_F++Mx+wz{)0IT3KU98D8X84>?mWq%ryF7juJCNQ}i&r3zRXZ>G^|e)Esoqg{MI(#V*oyC|MOUZx}=$1fNShn#IpAr$8`z?GTJeFhpF?gas<-dxNH*qSwPsnq8biz3Ozwi?j&?l!s27fNc}fhkhn&qgEiG=RnGuwtRoliD7}7U9_o5I!b0pmap6ukFbcERtnY6n5vwoQ?j^Wrh#e`n0+@-v@B_~4o0#uMEdH9*p-dCB+sVV;Dv5bm!-Cg@7E)p6Md1uNTvFV>q#xc3M(3)hrZG{vRw<>ctVfwqP@#Ka&dIjLRJ&CbQZ+OEXdkX>I+_HcTsmU?@C>cIl`<LHGT5hzz@`f;T8y`sXgR7K=FiDW6Y(F+eF`-yg^FOwwTO?V@)AI8|+6O>yfA&qLfX0pr=05IQHz|t!EmG^e=JShaaFWHIcD~sv?k=$1b)IwPpKbY<VRid*x`RW+d+$d`Q!Tx<0vJpi;aTG-a>NN$%@srRRla8Mb*7Y(V0NMn`CzrMaJnmO(|6ZOaBh3ZdWfS?GMr>&4GLoOunima^Bh-0}lC1G?=cs0SvYs%B2?19{V$B>?goH=9u*AH;b(G`IJ_;h7!#cA-pq<M7`72a%)9%pKT!U=PmX;avv?FAi3)barm<;k~mnNH?={gVXT)Ao&{u(6X^ZefAlE?z4c@54_LokXC*mTnMo&qzUwTgKJ<dl5*Y(AILnUG5R4N(7sc+_7_6pDlu#xn5+lLnB-mB(hfdc_1VYv9&)tXk=%*Igt;<l__&s)6Ox{JfDC#xc^?zV8gaxv?Mo^}frCRqgHbSP?DPg7p?{V5o)j=U1Tr9dCG>zi9qLN_8fOk&(%H+hTE7DckW{{J7A6?#>v|QfnH3L!)l}KFLn3a5pm4KW116>qR<}$38*QKBFo74lvd)~>b9M+=Kb&3=@$D#lMBP6W`imW8b{@*TZ9o4n<|7YFXH!hC3_+$qrBK~}*m!U*1gR3hQY$5doH6+1tcyGvwGVXaz*emEX37dEHk5OuvaYI;DHe)l?{-@v(}cKorcvNT)Yc3g=^&DRlE;KkJyHG=?IfWaA&k>!*N3xH^vSA2hYw7KngRBF$U3tyO^LH@Co+U&5vTXJDa;So<zoE#u&n+&uLV5)5oc$bEIPA`%-Q$3Q3scIAx2dK`ps4p?l9PWi8J4IqrO~<1E4as#1at}xjAIRm7~HH)2<q|Vu!jod7!G{j>=XEJve&QGrhj=C8#5yr#T?1(#wc7eGzo1=4?o;ge*T}8P&`7g$>dR_YJ;ipc4=m?@6@ph=rucmZ#{=`@LhNe?UQ7M1w0q)5B4w$cI($=8up^ZzhgC3az+C@2Em<XxY8pZWGv;8rvLneu3vkIiO<cfr_1(2uUBuHCRR8Q=GZu$SbBN;jqWP<QaGcER-5MRf3hn4wy^#B#0G!Vc3YI#GV7KXg+Z}9cBk21`AwT(A#AB!=_`b(0%C|Go~7AI`hysVRqk`@63})H9hj|?~0+sHJ5IufU)|ZVkOe2hXp>UsM`*LO#$MAI0c3iB49CsT!Zt1HMDJbZMeeF1;%u5kUCHmxxkd}ob7scZtNrNpLBQD)91CGF4WE^Bk*t+6bU)O&=&lVj8Z%QWxM28uBsktA2T|>=iRn2z29U>2{Q)40jSLEVK#u<bMQ@1AVU{qQpW5G5S3gXE71-H4SddRd1<UA2!=7R$_y9`#GnO6!DwPx`Q8hr1T48PT#Varu+;Ck4sD=-My1tQegXwXQMej1Mb;|KtF*7n?Um=0O>LtlcT!IluqvuX3`zEsjYW(oX}&iTH8D!n#2)&F_Zg%G8gJ4IO|E5Pc%XtH14Q=m7*IX>6`;M8Mu@cahcNDXJsfVeCtBArcO1EpX~#9awlH?welPIAz(UD?IQ2b>L*QR91oR!3sSlmwFbWy*)y9(%`GploIBF~nAsIS)42;<h?BJOA?UZ!KKepJ2ycTol6gFkTOfJSqiDLBo!lP3t$sHYn21dFVCo~uq95AoQ6VaKkYU3;29uP3R<tZ@SvLIm=P{i{6V8qh`P#{~7#(BuaXyHB@V?aAylHnnkikR!}7cE%T2*_2qfdk#|!t|oDdm?C~`mOH6TnJ*?U^e2;Xi6#3l|nA^`hD~RcmZ+`c3uPZ(4bmrfVwuAZDAAN(o7=^7sb;YnSkX3xrpjGMU`D{6Qw>F*=;a<aU!{0;yYl1wut5gJU}hMqdhl5<`qv9qxa&zv!M8@o1@$|QZD-|9MC;nvPjxsK!V}m`y%0vf))TBjk~ZEM;#y7C3TjFoT4%dO0Gc7!3B_fO>|%YPZNf=0B`<d3U5vZ*NKpP(C<U&bsY9U-e8xTFd*#l{81tLIIU_r+b~{G%4sI4s~9tACtytAB!V0Y1E|%cpjpg8vuTp&KoK}K<`m+r4z2|$_Yh-EE!o*vdgP(SkXwvdPvc(Aq)8XX0fZW}<b#*Dc#}Gz+@ftHSUH_dn)hsD_lf?RBz9^3NY0}7siRL`xU`%~;5)8Q6pC5^s9ByL8qHyk7g%6}b=bshMRCn87&cQaWdIT_QYdNxgHSnwL<<OM28n{aT@i*^!0u~Ov@A}-fDRjQ*ecZLMjYsA_5v@XMh<Rai=HAuEOMf-34(MX^_v`U!+st@br=+Z03CP>9+FpfHbbp3%rS`Oqh!8d7dtTjz%trsc7RQb><ot2n>G)efR!Q}g(=6065I~Y7?5WJq!uo$)CM>@<B$PQfie=hOoy;XT8lvUz--}t%KIhRBy}?H{8P>|>}yZ?ty;hgz&u5cs=Z0Dno-I-5WQm9Gx_>f3hi%~K0drwE=u<Ip`So{y_z7llaP*V>`YyMszEkmS99dPi~^IN5<7y&U7SQpqX^`jgGWAiQiTJ0AdoVw`%%=Wru8WtSMzY$yU=NX`KdM!N>gCFQ8?9RkqKSG0~0aq&<44)$cdS9qv!$XO*PX5wq!rsx5W3==3!R=`z+#ac(jRXDiFsJn${K$6^2g7cQ~d`ojn9^@405PzS~F3hG&=BM#l#0p|H2mXVY~1xCl78ZC@PY8IJ|;chVZBj=Hq=N8N@u6~jLcx-~)Hq18tw1QRC(66^_L`ly+PSbzbo9vx}Pb(JU}Yp_)$J?e188gx$zGD)%yhjhq4acJKRyaAMwX+Dh>^&Phfo3DjO2Kp%UVrGfF+vBuB%bW%7kthlxsv9EBI!xh#oLF*6$6&pO%q!has#vBQ3|4_EyP5d`?@7F(fRgRuL;MDkOGu@}-uD3i3a92m;Ce{4=w&3|m1F}6GESP#Fxl=jqR?$2VWfUbMB9ldh_XRwf&Pzl&E3X!q$KUo3nF|0b|{9elE@MCVd9DUXnwalD2#v(fJQpRyKtv^F8a{|7N_%~Ln{gIhz07|+7bZENEwW9l?HgMK-(uERLE>W+I9}`5uF2JkCavz^V5RV%6&+mu-(zhgmt8Yg-@W~PsUf<T_VTfoS>39krl)uVRuF1rhJTq%0LmtqgZ?^yF{l1MavI&1@&Zx1x@56g5F7Cn>o-76TG{}16zRn+=B}s|M<+%QDs&g2+<=cRLF)L>bqpT9rXPcJ6J&@L{D_ge8lvF)3g996YS4L*M8>aL)YW<^mJ~r@CKIg2{h@C1xbV97L;`k9+v|#A8-g94OL)5K1efAUB!YYjy_Df)}22LZ*I4xK@5Vw#bao@pwCk&|KeDL-0<2aA=+fq<M)4XTE<bQXWVC<W6m=Ta#O<;p+j7{Yy0TZhZ;?)LBVAj13Pa+AaQ8R(m)FX6cl<WJq(&OI|S*m?2VZV{wY+^Jgm^rFO)V}?iq5x`)q<fRd&Ja_kkkHDrl$zei&?bpZ(`&RP8_T64|Zu-_Eap{m;)Ho_2QeL7;~$QN)KFI-<~mDFvcs?^+AJ57XvpuqM5dtX=a(7=>b%t6w!kPWXpL#UvlXgP-`?C3%d)@Vfz*NaQ&sitU6g@^x1Z_rIP0RKtw1`@m^JsMW^+WHSsw&+g;~)1wAkrP1hip1@-wA!u5truuHvrK%iAB-!htx)kHdQZoWc4LjRFE$EX%py+_tnDl*M#jT_Zuh<)~0_(^iZ+3IL1IiIRP3i{7VWh3?xJX&7ZC)x;GTer*#R1NFF)vXYor&lUl3_~{lscdd%mXedw&fy?_?f51Cr^!}Nm$ENs&-i&*O0N;+;+W)(#fFa3D>umwq!g<Iu`KoENg_tQI~hmFONb0=}<>Yx>Rx-Ncoq98kTzAZGusb{eT8Q#X_nzHxKzd66MIq9`i6d4eN=z2I@v2(9qL~C%1F&&AFcBT<Au6DINnx5y!)pZIB9z8eg32%3<tE?2Dj<aaCxynK-DF@=+Y%oiWB*9D$n`^-esu>-CW643>-ih0OvlLyv*m>WWxeZ7jKwcwuc^DS`#;%3SlpINnUn2e}w1$2_qf`Dp1)(>kJw0im>sVWM^lO0x=~(ZOo4Q5W>NwN@^qr0Y@GHL-?W`9MzCcp7G9Tl_H3J;q^GSV^+uTre<uC<*x?)l*PBNQA<x`=H-EOU^Ef5Y_j$Kj>`318!4vOb-UCP7IM1gYJK4n|VeLf66Kk)5BTJ42DMs{-oVQ4Uke!?yCikv&Z>3`!v6y7)vY0!?WX95y$#|Ms|$~uTMX0ViTM>FyBQxb1P@|vO1|uVne!nX^L8rJghGH1qDUfRwt(t`S_$wfD9xA{kFr7DdD!+Lmf-cbC2u5LUdjBoYO*+FW&TGqwPz#$TNh?)^ZM^Tbf*y&|w#AwaB|p4P^)9=veS>G-^aou?F(Gq8rIU=PSGMN!t#|NyH9%K47{JM(&Y=^)Og7%*{gC1kD|?36d)yf>2Aw`I?r8X{CjT7Cx}7m?UmUXC|avjcK#G(hJn*StiM(tQ62gsd<qxm#lSlkOdfPi}WQhynr?%LtHXFq-X^5!jW%iI_rK_po`ycxcbon+oQv_$`wl_NUa*x=E9>fp9&XVR8`3msj}3{hjYvt(yuRvFb_;jhNIA{EW>UX`e<;pV87RD;bPZU2a`~EDh4~UZo+{@^vi-#_*;+<d}5z|X|1IV%r)kSL7U77H*Tg98-VC0pVV*qfoCTI8m>pD;%8c5Li2$R`bp;#C~ySJq&P=2?Ms&!>@#%P0dD~7oLqbnbu9*R!6Uob3Evj1Z46rUw9-^aNg=Oko;HEnoD{u1pz#3dY6IJ2*FDPl5S<i4ds=9?PFpm)e839*6#Wo24<y>44X<-T`FdpA@<i;ka}YZbYSB&Tpdux=QB#DM!%pgl0UloPNE?((Pzp1-)SawCWw<C`Z8nX3<)TTfH4gG5qiakK(9;N>d`%=D(9r0Gi5E$4t)-fZ1G2R^_=rTSNkFP|(gZdF&B#CVmG<FrTU;!8khb``9v;R*?IsLKjRTG{$Lc<l4Ex-XX*Ihc9v63|0xEC+k%^s*7J1T4cNLFwv(D3rfTU#8q|*Pf+-Kxmc=iFCNP8}~Of_Jp*Z~K2G*P+iFDNAu&^@wE58c7UZMEu*G_IU;T1U*RnWH&PkNNC^Nzu@GsS;_GLh)Rs`69N<2;%h_?_ruQqO1=ZWC}OXW9D?x-GiP+pd{S6U<{+X@He1Z;aMT2`8R<YaRi~Jxfy5z-#WO~^n_Ym^e)g0%4TqiJ9Hwb<^D#&>7>fOopEeL+tBYgN5i_KGCTn@k8Hr?E0WdFiOm=%pY>FjdoKchfj%-XFxgF?t@~+0mqi}zZ+QaB<AaE?YMz#4Mo|(SKEu^PP^Ubs87l4)8r&r`xQmNDkf%iY(O?zSL&;@a<TBaOtDfo$b;5HDcIB~eiwtX+es<~7lyuQi2vdoG4QV^(XP_`-nnSsuxRTqI^-0!S+Gjl!?J_WML@Pi1APOna=_G?Iz3hEp&cFhvI0fdg3xh=#%B!vy8x6C#9jSBrxb!Kh>=e1d6I&qI1ghhM3z0`Uf|9ctH?s)CZ10yP?zj);W$*Y;kraOR+3gRCpdP&}f)aXpSJ3gjxLXHZ{>50(WqFkWm-(*+xGXHd<=o|%(B(ow0k*s#Owcl2F=QG4EdZA3R~fC$zjIJ!{WC)<^WS=?a=CnbuyVO<JiM~lO1$zGH8f$^@&p^V;g*XfcF1zM%m!F4mQ;b2ZKY+Xa{hX3h;mJhYIw4}yat|}E33vPn?-j9PtLBb5M_B~0F>pA5;{3|Sp!c_7R%t|+@%$oY+P4kle3Z%HaT}$h9>8)OUPvTyMRkJE-IkOMu7=T4*4Almz;wo^N$=bS^pe?OD>g<g-foyy?I#jI9104CFkx`A(CySHav2%#DYf7U5|nyV@VAXd0Z&6rLYQxY%3iBL9V%32|%_Mj}Jc{uij4!fc(?x%cNn)lWcuLxZ?>ldZ$?9acWNvYJ7KXS&_!2A}iQ<eq5|^zNi9eoGU3IjdPdd;EYGru%L_!1>?eut1A>?#^zNSWSqaYqm0c0JIc6Rwh4%FZJip3v9-J&TwHx`B&xXfb~UQlUVfht#rNT*6TlX4af2g4#g;o00u*m)iz9KwwYTdr#MSrg;Nd#xa20Ske_cQi(=Qu#m@n=IIlS4YEWqJH!6tFTW7XUQP<YIWcLER|r*0k~oc%U2!s=H6AuNB6g%BQDr3NHS*LMaC9;b2%Ae_4_1BCO}7I1K(paL0eDYT%23k4OpU`t^c7@WT@1A_C{WiW95x)uyvdCQIjE|*onfGvepC}3M@6$sc?YQ+GTiYoEH*5W(>IQv}%`n8qTAbu-u*Z{x95<A?tTvi7A=C2EAU*n<*=4&f0qkQw%R)lY<D39&UeitCU#zhg(YhIOcyym3^zgsA<f_F<rMf9$DWr6G#3MwGGmck0muBEU7wrdoWFuS=+J7Tw7Rt43ym0D1`g@PJ@Zp95dNVi;8h0(Q@mSMX2>k5c&sjLQ^TXDk<&MlW!!*lKBH6Y!J8&zOkTWKXk*IHag>E^HN0lL-qEI{2tffcA*DjEUPt+_c8qg#7>1Wvc+W+hP9T3n6NwU<{Tb?xO_kJR1T_9ltaolL`9htl1eb|!$&-Qor(g3aCXCbu4$yS4322$eg5MkfW!okXjX!{tt<-3g*|C)DsHA-a=ldD0l&Nw%H?>gt~cT374;O6yj7c4nMpR!JVWYhL9ryZWa_?LNUD?a_!`d8OgHBH1idH+NY?>Y7)1kgob!1<<vX8o*rn!-C5#6x@GMF8(_Tjw?(!uGW<A9*=vsE!-I>ck|EOOEB)edehb+ZnvhLpDf<?C)us7z}DVv3wMvQy}Rcp4y~PN^P|DF_4hXks@+888Zd3ejd4)4b@#U#NPFjvSaGzaA}flvRAj->77B{+S@Wt4oHZ}Yh}ryg2`!tuEJ0;+mt~l2{(7<~*~ztCg2(1AZJ^j<NeK~~yDURt^Vek%Z2r0i0$XvT1_fJjqY4OXE42V&3k4YlmjBiRV1)$$%V!eqEBy67zPyBU&0ShSuBD<P#?`#Cpj!(C7F27YzyfG36qJChxyurQHFr4){OVS>IBC4<BwOD)i0am~bKjAu_x1Jn1ABU}-&g}Mt+-KxEUmav1u3<a5|A_=0VIvfKvMh^>*t|gha~;wNF-?(A%qv~hda-KOW#y-g#1dFH~1pR0ZJ(qhp5hlJGe&QH|g1u;qFP@sAXou%?j$$;a=EWI^6xJ>k9sMwgQ>*i@5O`pecQ!bWx^gEu_SykI5}z>NQcH7Z(bAuMt(@OwD#CnH)Dl@d8RMC&a;z=un1Sogi1H6QN33f?O|X6M&PW4)-8QE(YRKBTH@*%v<cLOp{CBPZ)ge!hG<1Q2EBDAHjbd{DKrnQ?4h_jRw-JE=z6`37Vn%AW7=7<ciT*a%ZBZ2dy~C$Q-%&`Rfbx`Rj&HIdXf|IdYr$b)W`D0ydKzcM)b#=d5+MC0TM@cbw$73;3A;cx60BcHG>nMrOxFtXE}%+$Ys*D<G&dzT4xiWXqB3^LH9^338vV%a7|@^W*NN>=T|$kXw--7q7$0^tdX+N<9L#GCi)E2B$Z;aLnt4wHb2pQ`0>jNHI(91$&lU$<mMUR;)>u3%su#*5=Bc$IpgvBN~{xSMrQv&fMlEa^@y?mNQqMo7mRBi=4UKRyUV3cYIuG=r7R6QWo*s$|NwI&Y0<PoBFmLow|#@ZcEv6XPR!{O8T`Y%nhZetVo!v^OWFrm**q4Bx$bvMjIbpfZZOUS-&9a)8@i#xtq?K+f4<2cCpXo9E_1MS7aG;G5wv`e9GK_oaHKSuE&XU{hxH=++BYDLs<L`A224c7x-Om`5BzwfW(Bcq0GdDvQm8FX!&DtvE1vrPcuzQZ|2JcxlI<P{c>hqo~Uqo;=om%Dp!t-`XU<?dPFeH1l5GBMNoKhOFGHyxHL<;hiXyGHK3-UW(%|9mZyJq*WBF9&Y9^u2B`K?Emt25&1J;ZnZfQ^R@~6YiraT%PKygOLyFWL16GMKY;AH}nE6qd)xANfo-IS}<`d*@Ha~87C;4$%>W!Trw<bMqI5Iu1nyFDKa{I=YcQ*rHot3u>`EmVC<i~Bw{J3JX`Ej!^ugesp!q@8bxH)pkZhn-rNj#0JMBlH^kqh#@jo;VJl2APTQ%H~NQ8EIu;9}n3&_ADdeKtI3&WXYvT0U^IloeOx<=6DY(&GBUoW6XDT$B)GBRWmA?ppYHG|ZYiST%-3zwq;N<7LF9MTK^rPDN*exo{=*=v=s9LgBGaSB?j@sJt#idqgF_jm7}1&h+spu!=NLBZ^?hNO(&c1b<~&OfcQ;;2P$;#gEm}=l%0JZ+%<NTdkK<i5p|=``J5&u#&0dN^XE3e#GHsUN!rJ({<@@Y2vsAJ~cl+nswgDd}}r$hgw>RO(wq$qe*1FWs})Rdz+g|essD3Yu&pauJ-RO;#x8H?d;yc8wc(t_wBr3U3%~ZD$_<1Tu(;Vin!MO<OOv)()&1l7dda0M~qyH{J?Z&!rP=e;q3+a)lu>XHmY;p>UzMSQxWw?rM(5KPo_~epRlFC&3e!rD+R96vhjo^7jC}Gz$R^}aQiA1F4StEU)`Pyx9x*1ovSoDAud$zn;CJNk^@y?Vdv=6$0E!>S)Uh|O)ht=ytrI<VN_n+og!Xv1JMLBCjXL`xpOSI*kbKCa|l)E$7P16)4chagQOx&E`2{AggIzMaV2Kf$d#$;I@?<E8=tlC*_oi(m1!m9ljzRm#0E0rQIk1WAZVmEb8cz8`Qccz=(_eSx`jyz>+<OC3xf`3+*K9LwXaO3t5a^-v9|lgQqy-;i(qs1Q_2ET%BM>iDP;5~tjwpY@8#jQg;C0MU{)k93j+Kgax08%Xxszd0%>+?@S*~dYpf@zGoq6UYf9a=>^Fi1VjD8o?0d65qpnPpE2rG3ZH4F_c6%5S%$%HA{Sr`@ez7C2g(tEI_*+h}OI9|q8y6Of2;GL+HTDO)&5Wc6RcUrn*N;__-7Jh$nP(RdQ_0k7Ba`e>U0?gAZSdWq3mr7$4(G-lnP@juwv;{Dt|3-b%_=xANGcUz@*OZ5Jbug#JeEe4*j{)oeQ#ce%V>@K(aCp}fU-R>a^7tZjj;l`$Lx^bU5X#80f~a4T9cr+7mx<d?(W(Yy^-K-hVE8m=w-Kdb7X>E)C+p!r|4DDXtcXIl8wn!<m8RO{sKLPPvg9~GC^h_ned`1O~y*qYvg2++?94xO}1VRS1zG@+y(yQk4V?M+l@k>DXUN9A!OpU%ACE+oU^y5a`s-BSk7KE#Vj_VWLPc@Vj%PME>fOe&q&le;XJ*1uVeyC<>GB7z)WPe-aw`afV%?Sr5<O2hyHSg-k7qoc<z>he`kCO@8o8W6NkcF0gII(fP0ma*GLJZvheC8ylRr9D2F;QX8PE_Zg64=cx9YhM!uY1?JQ6hH?oMCc3o<K19c7xYB^UENVr?dw~O;5Ehw3<bWuwWej1sZ8N8VUmREB`4(CN-1MK^dI;T8w)aYW~Up6_!?ja5xxA46shN~?L$}oD5v*s%9ZM3VHx6IL{P6g=HxVWSqHFaN-<YF>c*nM&{@(gkA@Ys+e69(KK%6I^@j|7fP3OmG_7-zxFgbAm{4q$Hi5Y#=+g4<+27iGbXR2E#~WuDBg2OZiD)4;iJU05M6G?f5r_FMTg%%N&YO*cWcGMi2rSL?>Me7KEBYMN2F2vTBnPTa2B%;&_-3XGh%4PO|gIjF6==>X3J0<s`(XUV^PXSs1x!O3wwc^IrFIWDmOzQ|?vQ?7z6J+3@}R*@f9O&*_(+yXT2p;Tt+F@3%Pu~K*tnZ&jQWFUOD7OjhxfDyJxxyk3rWjAmkQ|=+$(Xgxdgg{NgTz{()=I%q`Zuox7X>-Zn<OVu~ur(0feLB;qek|7RdoY1z^4$A_(AB1G6Lz~bU#_y}vUIuZ)i*kCobjXVY4j>OyGSvQt;FYMrue9gxHDv=yQEAuQWUv({LceTkvG>*IxDV-J2Wy<V@Q4oBNwij3Kz_QZdlBJOTirWu7JF7pQdXJnZoj<K-d%lrM9;QeY?w-{V1ijm6Q(8(?KVB7Go=MxBFxcGo#b7k<S*zuX#r09zt&EXgp`KT~xBxeN?y0r>2yO%nzb2A<X8-$JTPf+6a$!^I3trO<7wJN;MPK#`Or>S-V)<6x5d2Rz;L?vrjT(tt$-&X{Rs=@i8`;tu`M3ugO+R*4h~9YROkRX0BRL;2QOrYP;dn)<m`J+a@C|0&Rs9B72@%+%N24smxOw)a9vVCHN<ks1{h0GM(GBA7!#yArHfemU@RP50xO}l{yQ&!;-5uP#$jfii}8B%l=w@Zq=Txmi&@=-+4J-ZDo~GbjV(<5G^sQjFGQaVkgGWSW9$*UQfh-jFGigz94@<(FWX|<s6*6hB0{^aye{wgm|cip8fwkhpoq&8#%@oC2LZS792UB9*TLkq~npuxetbN!!^&~f?`!Ty1VEwMS=BVka$2K018l38e2SmV9R1_hH+f(kR9Z^2c#~?1<Lixscdbv%yhQ!*Ok#>Yu!>p+uFMMthO#EwJlIp0S|1%c8XPWTH93kD!F*+rCW#%-ltAo<+|*UZvw;t32`&YZ4<YZ6UYHz6w5~^YZ$PS+?3nu9%Z)O<r}GOk<fGfR;~$VxzKINs+E2Vl-<gO&s3gU^+G7>n3TuQZy|<wpDXj+dX(liTWcrr(36T&TAl2clq;9_P%hsso}|<?e*YoH`!c#(bmW0Vcv+C8yJaR6noKCnF(IE*-m+#37wk5We90xgq)uK@7ZwHK2F-c6PjF*n@RaOUX1m4Z4GdHpkbRIM@1TsgbMUs<Ee{k?DSG9NoVR|_Fa;Xm@ypz|V8;%=!PA&7XTNpF&wX3u3^obAsmDw5e6uevNOuG@dr3W@*-J`*=Dnb&dM=%3ssuFuYAirAdaMYmG!oA&>~Lm0lZ_#$Uf(Sy#|7mOQ_C;G>%9t0vyVHFop!!gOq1)ADx&k`@}&ebr=U#RQssJ8xpKWckQsCg4|%53_gu!{WjS-<Mb!8hS#yOQ&kQwz^Lk@InfW`1HY~GjV=^#iFhSxbs{9@yggu~0pE1npd4e%Vq7&kYRvaaDCdNHCarAPjcM87Dy_E1}^jUN|UK(KVlV1fQA<Q9|(TnErS$K9ISES3G^Y8*GRgi{K30?;FC9%t49d@~s!!Fl@mtDp#dxTvM`z|$V11~SZ9D(JSYzn&!Go%5<=oUtU4v#O6gf0_yx#Po{H(Y<o8w0zXe^m{5`L}79puDXCFVE9UE0D``BB3x`Mebar(FJy+YxwefxDdgZFd2Or!93G$)9fc+8NfVGtc@-QAKLNDFqV1%bAKEFvsZy%rkMyq(~aX%=w$*gC!sZwZb<yK1YJ%j3WmymWis8thmNp7mqQb}3<gAK!j{!+7?|a~!5;~;JOZ*jFL)Osoib)wj0aj)59*U1&NkM^!#e{mtM>2-ene~nySz78@O)IN9Kq0KY>H3jiV@glp`ptjtyvkmd_bV~gvjN2KFXC;AeXWCRM-`DxMgn~%rcb<RSdIQhg%L@4zqad<MPqW0nHViKw&L-nPjTl-z<8$=`Kj{vSKXt=w+9-vy55LP4xb68o>;ju;=&>>HY>VO%I8fT)j*^KS2odK2o>}GmyhEH=7}MF8mFs;_B6r*Gr*CWi3|dUg<eOU#Ed)=D8p_%##xd31-Hb^QP}n5?=AB8Xb0p+bfUHLqs$1v8-L{WysAZNjNz`GnfuERl1*QdDLon642}}M6h_4m6&~O?-TQP2WO_k=AHu<n+ay_-%~KNXM&j#c$j$9;1eCho)j7s<Aa%Jkxz`3dsmEuWhTiPjs<1TRkI+O6R~M1bN0wYvCK*kj*Dha#NET0gRmaWJlplsn2y>h4t__7<~*R;f5-!=9oA;!O=I?LpxwdKqIxhUrrAKCGNL(CvByZy>k*<EHEjj?#h++_8%l2#u6Z|FaIm$q=fIxQn%#YaH=`J8dIDq@$WNLL+V3TBGxr!cq&&*cC}-l=8s?lTl(Vl%V<He|n#!gpn*uWxv~yCVn##r9L<%L1pa5qkU1gkvyk54bj@v+mFqt5**&rb~ny^Hw<ZS2B;gMGoi*B}Y9x*kaagfe5sO+E&z92`)b$Dk~uo)cffwB=IUDv^#xn~t<XLYjz>@4s&I$@m|o>D|Rli6qiI}28W#FjvvJ?*DP!XTq`GbrbloA6S(@?o~#?f~SxL@TBnQL0{X{>M+;t6Pe*S0r19at39T22b>B%%L6PJb!p*|Dl;3drJ`K!@CYVwfEqGUAFAK2RD_xH`D;<Sos#L0O!016{d$AlkOb@oe6%LA)S$^YM{;n7n-on!U}eFIrLPGa+VeP6jiJNIMa(X4p~>XpqpijATjD-&H46Z<uamKHim&O8<u$<7KkHKctR<(0GUY_2=(n+2r~$VK1fgvUS^I`g<YNj(U#ybc=qb3Co93rhVPObJ)C#A0=;Zh)}E3|_%c}}siZ%}q&5D~4q~=GqYac1P-c84!^0R3lOmQGriblU=>XyQL<N>PrGRfBIOZfIkQpAY1v2k*qfVEoNj-^3<~f%lWnmqR86FvpVlE6-_pS!Rtd_O}Vpg+Jk6=y%IiA)-IRvw?L72mar(Wq*pqD`&3g49<IGsYcy#=^T#-v+~TCRjF>lJRhO}Lk+$+6@QX4gW;qp(~Fv%C*6%f6?F>(xS*VS4(W=yXL1uRPy&{aEfv3}lEZz_RLjQ#sA5Aj|U#u}lj~^(%7<XJ73wJe=x@GGsZyU!?5g)PYtVS~1J&&^++UumZ1~Z3A+VDYd#1tvt`#J6Q~#W)_|et32O_zi9vURm7kYs;sNl;gs{Pa?mH5wJ2p~3+<v+WJM}VaRHSp0m_mwI1yVaZXiYgllORGQ=b0_!o1>ZM<vrLkifCk9yPtTXGTqQ?io8A`G97tJQ7iy%xX9?f-p1(7Zxz`F65iA*^-dIBe*p{WIxPp%_=Z5T0olsBa;=?;2MZSHfL@G78!^FC>E?y1w%$BxG50Efg$6!aMaz<;F|SNWH*OIM!PwwLn6yxr0zFeG@6)M;)~oGK=Mo;kL*qij%>(O&j~5u2ZTvH3k?8z+!1_G9PM=iA&ZG(kmoZMMYRf)K|z^JCNU<B;#FRTL52>3gd}iNfKmCah94)n>55Z{JeGm4L_Uk%mKtd?8SL@ADdTaK6aYCUnVSd&*#lBD+R<||5#X_mVIkl+qaO}u;j%z)5cIH+@{=%cU`zD9WKxJ@^>hJqj0O$}@TlS8ch#kIaQSKEU@;jolS3S5;Wra(ToS6(vX}ERDWBE^!N)TGOUL334x3p5*c*>YpV+Q!qATtJ@)$a%8x|(RCT&(d0evH=xk4U`dkH<}W24vy)CzbPGOh8~_V5fqCOE`|k;lCK5ttpzb#f)}nDl$KmU6dx=<O1!1#z!|$8_qAamQ1HJJvi5$*kQ@@qA|zZilI*e!4wEB%1~;HtyMx$DRp1W{ulG9{)B)Uo@XrDcS@!<gvybcVu|e%<Jpn&kT1w69g#(dKK*0>kE3jMjd;2$S`4mK@oJU@A2u-D#WoJaEw2spF?}5i=g9h0fPjTqNM_H+>cmyp&)_bvi2-+;|jDfIy7_6xh()3gFcL~BepMdnB#z-MsL$Lq-OjoBFB*em;@7R3>$;Iv55t1jKq}G0FBLKQ(FKw7Fi2kHPkpnzqa(?ZxPz~Ay*noMGU6rbM^ZNHkS5jlU_(6i#*cUm*@1Miy7LO-RoKB<#9apLBLx)BYd)zIAdi>b91G>8YpA3viaml3ZxnVZ-enm=jBftWE@ji2hSS7-eLnbizj0YOyi7kJ$&s4$-u@w7Bbk_BdoDnlaPa$p~M?|5_+UUe|L{K-sc(}(w(-Tjvq?-$ixI7$BFUA!DT6b*%#MJg>jVR{$P%Ywo#*c)LC%Beq$OfH-`Q7AHr{JtGMMzz_EG4EArB~>16?{&BBc-kco$;H6tuxjXNlpy^&bsvP9c7(l`++s*A^eCWbVYp(wN()Y&SehISj5D-s+XGi?RX4LuO*m2hJ|S!g&w>}cct<mlA9x&m$7Bs<F`w6RwL8^ezdybblx5PrB;u(40JA{7f8(ineuWY9{eK>=n=XSqyYYYApdDlemqrS6vp8LKnW#u>~BBaQd^>VzklM;d0F$+Qe-Y#j0k=_T^CAboHw$^<78MH)!=G@k9iz^15x8!N9n!HxAvQ!Ct<{Ej)tcL8iXhwgoQjZzH9TB`&#)-^^Ujd2JRrXLe%%=O1a8DnMGc&=|i>kMEq|DrkcK;gv%NjX?C$eJ>ySd7REocy#P#Q{1h67p>e=0M~TpuzH?9ke7BSinP~rTl$9Npa9)pa;mV$-6I)j!rw)Gqs{j(WuPF7zI|~VjxrtxHyZsAnj1+LOZ%xyX$QgE%4%UB@<mNhwUwC$}ZN<@Wr6~q=B+m>{W~KVj7P@Sw(0u2V`318VXsw$BR7cyS5lrjICuoMdb$GhKKnzoS5}IpopN*X+*F#=@=XOQvaxSln$Ct9$38B1QuiJ58Zp#hgjGeY*}H7@jHDg&?OxL<UR{cwbr1wtceN2iq%>}i*`tH;{HbA)U-xiL=@-f`u>B84=|+&jV2CNxU`-D;eTNiat{Qtpnn}dm$?L5nkS(Z=j<)^!l9Go=45#H2UxsUZ5E(>ui5nIfDHOsfD8kQvXaj+gpC|5iQE)a57-fk4h(d0-W+v8)gg4NGMsp9JaJwyT7~r3kB*5VE<C41H=>5yQ9Ww79hFeSyMcKPF1cP@2OIv+k+9*EV8dbwY>6UpSXhC>_C&}bY=A^2OQFu^(ZhpP_^;!;otk{e{M`W%yo1a9C3*usyej}=@Q~vfIg#^)Dlc*xTad(m<WJV;u*8E^`86YX)4&tYy08*c{V*{zBkR`<R^u`8#OQ=cqlT~{iUs^%1u0e!)uu;Qjc_47vX!9XorBfB56pkb!It`=*9iuz2;fg6rwlGm`EvlWc2jk&=}omz#H5o?l3eO<pkD(EyaXlCarfzvFq8RrNPIC6al+M*t)RQ3DnT+(fV^^Asnc^2AKVdDFyjy?d$5Xysr>d>HO^QN%or64kIqn3;EZ8E!B5PRNLiA*qApGH5;eB~bi27U$$?H@47*$ANk*)(sKXl1N=uOlrSF4{I9{S;^JVp!lEsKj$@A*H6?kJr*m_l&lIOz|wrpSIk|p;V;oy^mrmuiCo*i6=(c<Ya{85!KSptq%t$<^gTgDsP;l>Bk1;T2Hdc1K}zGO8SKp)3E{$^Aa;+WGVQ!mSaW9G<3z%g?DV=yq_-SRk}9do>jtgy{v)R<$~s~T~<6MeR^i8<cMY$K04o^@Ny?CaAc!}^(NlEt`rlJU6`;P_4xC1Yb*RFu)ij;!a5&XtUJ`XoXm;CNiT@#tL1vo0P4psIKR)(fOmw?U3$i8+=svJ!M0j|)2XH0s!^PnL`aZq#S>yewUEyAE*7T1cq2%(#eSN>h{`Bc~}gF&c3!@?hgmAT|RwCR`Z0sk5FU{_`PW09k%wC}SDmQKN2xFcAu0jHd!XnQZ}~qfLT44;oF;s7-LWeUb;TzjaS&0+zD$$h3nMxC8|-cLL`Kh=97qQx)GcaIwRvUD=fEKMe@DSs!x)8Y9ix<!(~*pzunTKPhxEO`GheS{Yu8-(dHs;TS_lyLZj)ADndD6f<Ce27DKYVr2Hc!R18esWBcpm=W_mOpz=zB!k%Q3YjB0jdRTnRyUI%d6qcA)`5z(cyz`97F(*8!NtI#HVZB`9@zxA*tvs5$td+o&|=4qErwpzLW@Tti`8`1f{R(TxI1XE$R$f=UL7p3!CV0@-si<JJLZ5k`E=T*pv49V6l5>yXTGUakDD(U3m?r60U{(VQ*o=X#fKwMy*Le(yaQ&A)ZgwSvUoMd6OkQK3_!bMQ<HbT>YzE+80#Rem}QV^IwfsJe&cYGu;Rn=0o5AnP?Q-NwNjRq)Me;8#aZD-QyY^`TSTCYj{z-?cp!3B9X#m(!w{1K7w2e*z{N<LMOt+;vsfxuQZi<nM>jhfTFgU=OmJ~4H|o*pl*2_DIUjL?zaz6Li`s0;BB}!z<4Hx_|0Q@anu+W_vLTFRI%W8KcOYYQh2Xj%g(-;aLz!=Gb4cTUqF5eh@ZCJt7%FrT2~7OZXr=trX45Ilc4GYo)JnGuYaAoixSx>M3n)g-WPLv6nH@H;@!`D(4_L6qzkOoYcwpoG>=mWl6nIBYBGv>YGa&b>9d(>}Uh%7+%7J-@uw$Yg%F;y+%K8k;j{#3W>0AptCQTBDRR=wml~Rx-LE9$=Qw2d*FO`tt@>5nMvVK7`^qmNu!h_YOR|QM9zC%3}$LdWsl(P9E3r=}(5?7ZPDAd8z|Mr~AK|3OgOV_EvE6*~^!ODHEB@}Ae7j>ZJ08jj94^;w|4QD8)YxU|7%SP?75X(T_smq?$EbtB_*x-DZR>X4EGhJA?k&tDlOF1*c!Kb4^%SZ({;Z5yPsfI19tVTv<4P9Ox30>wlWzS~VWjk~k9rNgSquxb>D~aw})v!zBDB_msZ*GZm$mJPKww0tUcK+hz#I@;{QyS7k1k@OTT^4cn+N$KsuxJ=dmMzAN7DLuuLNPCL)F<E19F&<yYTmX2n$_wPe1s?10%uMs9D!N4fN9zg&4ZH(#>Lbmq{k`{&E}HAR9jLo1OIV}(_@tgrbCXu3fGJSXll1y6|Q-3vf1S`aB2;hR^-^Kb21~A&hV!e9<nE9mf3GHcZcVfLC$+n87BscN3hy8AZNK@$Tv3<<vc5m2r^$XW5R}V9-QpE$mCO%9GI-YN~E({T{mh)I~N@FPCWQFszy6&ZjuyDwF<zq60|WtQ4f12iH1QL*iOh2+_Vn){J%tsfjMQ3qnprB%Prt%B|xn;$C+{aljF>O;Ym9PTKU9{QHkOl*W;iSE0r6tDlId*_FW)$u~lej&(Ck@Dm1h(u+U-@7WxnvwG4$uyZLA4{EdJ@&*QOgHXoQPV?^APG2>-qHY4?t+mdIs3J9G=M>8liPx1&PG-(Naw~u{B78}!RDq+y{3#M|gsw%)+0#cPG0ESNGA&$I)Vn{mKDE(wE7RV`wRiYRT;iD&;quB^9<r)?Ftj*~$c_1xz2CEVvjan*(Z;-Xc3<uuY6wMxiq)QVRlT!$j!g3%&=V-<}W<cwnm|TkHgc*w;#;Co-DEVN7(&RiwL};|p!)(_uO%p>&Q_xL^+OqV_OjD^2#w98biASduWK*!??iE}bPgL|%ibA<;w!umr!;Yav1UJEu!mx9|O^Jyirja?agNqT<(v6q3k@@>fznSvVO&Tsu@=kK$-rx$3m0F4kHci`93nAWp#HW$$?@z*J)Nm;TsB6QdEeg4|5;Yx98a6GA2GN=3@pj~eRstnvnk)1c8k~I6<`@+-Y8qr?fK$V2+A%ze4!uk=VZgFL0jDu#^Zz-0FQL=iP6wSMjGZRxqfLVFX-BkS?gp#dX`WM}_=p1)Os9BOQdFdD&Sz|9CEh?zvzA=W*et9Wo5|S`g-?s5fSJahqJWvsrD{fN1-4i&S@U2O5xO2~Sk`>ax%-q~Clwa_G+GCOgU#K+Wjc~sMp3ixCG)@+P}JyoM^mgr##1Gf`e3?%*_+W)0}@4s(UK<;OepodIvQ62rsi49ypCIuycvDj5e>nHq;8^z*4c&>I=GZ7By}!pGwcF#D3dy8AgMunh7Htaw@`+p7I`GK)^@i7NFAF^l#$de>AL6ekP238S?cDlw7m3lEgdRw?>nAaS-^y-mLa-w@@BC9^2wX|APIGzcS1<+*j5TVYiUw|YHh8DEu!_B#Ld{w5@*K^C^=T>wUnFqr;VtVYtTl72C0Q6o*J1w8d|<YQ&S*bVW|fvu?R;g7Y7uC?fF&Vz%4FTiXZx*QaNZ6vs;R+#?F;+)tdHYK4&~Pvh~1fJUg4^a!%0jZpu?mEz~A*Cu;67wpuVlKw*pab%@*lQD_l!zIBLb`5Q#EPalG(p|1kFPvQ4F$?J?Xkb-n^?joOaxCr~r8p<`YIgd!@yt5$UoXvu(VOcq%Ehd}BnZj*m0G%jDo;-`V4b!jy(IR??ldQ|-+|K({s^Qgby~`_eIZM_cE!YykdT_Eyj^LO%NlL%%C~NYR({SOPm+eq%O6trGa0$aGrgX-wp0O$$*qRk(LR)hi<&@3>y6G9mPbUnv-Y1mB-F6X!;G$`mrTPp#{fedBp%-ADEv4JYTd<$Ws8et3^N|<!mydzEmcCMb*0vII9h+YGBH~)c9&A-gai?;XLL4TmFdA;X>To8NvGLZ#NqUGdPe<deSB)rQ72cWyG*Q|B7HQ(GqY!DIkWrh&Tyr94@e@E@3)9b!5n}Q#5_e*+haR~+zNGS~qJt88^CUjo_E^-TZA$QK$;}3<(@yc6u}G{$9ph1BFR0JytfN3F_sI^q&W8vJ6&2(fk2|FD2tvL_hPQ^9UT|?+s_=cGW`?yMoWx_%mDNgVoJF3Zia2W>3M$r6IO`q2EqvaLg_mt5&{|{%z6>%zjR*0{jJ1a5GZhf0JmAg)AA=WoF)NIyb^K9nCNF5K5X|Jk*89})nvBZz0HlH>0b-gj&!psuV3KZ`M?55aByWxU>-ahLC#iUr=I~pMy5=_2nv+c)6Vw`~H^W`iDRn+TB%I%5C_dgi+xe(Zs@BLL@t;68XM@bhT&A@n-q13Fxg$AIsyf4mN)eMReF-_nWOjwwQf@x(S61h25@@M#q<XE@OlTw?e&jI>n#C!w44Hh2box(OYeWXyiF4<TSR@UOqi_eugI}9+(k`^ee6}RN$9ztSa>QTb$)P&@HGK>}kH6k2(gYr;Ltp=T6#9DbUIW91_}-uZzP4hogEIE|cStg*73_@C=8+ui`pGatb{yCc*ZV0+bBA%)g;dRbf!|Dx0wZ0sQN%dw8U9p#5ogU4VoTY~cMOd6p*H+p>WKE>;^4fQvU!h)<?E91VAeSLU+$cGobH$~>-lEa6EMS~!~R+u)*8w@VR<|UwVtCEs7O`YGMx3HG&q7$BRqi>VMmOSEqMYc!$GGNyaV-E>Ia6D0|&!=_>nLXOdMM+`zX5ujnFJWpO4^^P_&fxoX5OiDQypKcDM@WZx%jPcw|mAyGcyHsp_sEX=5}Zu;Z%_h-Ar4+y3CoI1M@#uxc!uLNJ2cX~n{82`i|YN{-YfZRXOW!UHmN9;f0X79{oKX&?IB;LGuG)PpaB1ZM;*AzG=GM$Im6c%X=&RfnV|=72Yj5Ttq}h&unK8VvP*7e`u~u$kXIxX2d04Mh#~)=fHimO8Q{sh^;Y4l79&G?;pC03*lG?nGrY^#Rzd=IsKQnmAm;jgAN}DMP7gdLMCiz-9^TQ0l?ib~|8#DkG_98a)IGp;}Y{rH0FCM=y#6NDYh&B<ICs30)$(JddW{iR=cpOc6{ylfs$=M|t5&DC)<;t{=Iuagf!i5h@@xu=yZEQXg#4O^u_*WeD;p>KPb0>_^zX9BLSWr~YjU>)7lDu-4-Nsp<9+*Ow2e8g~Yy&Z=TmV`^TtIcDbO#|AfjpLjk_9juVsOJGS`k?1ld*s;`)Q>h309d%km`j*kudjy{8NucO)I{M<V+$w>om3#ySL`>U?rj{kJy;EK`JC^#Xtn^nPx#)v{q6$jA3+NU1l_To~Zi^+k9Y(Dc3bkFvLQx}y3Rz4oj7r<g#bE3sESQSDO<|~Y?;67E(Y-0@VGi4EQtf=6!JiV0dZ$pxHXgW$mPFb~91;f3lQ6eO246<NtA9hvfOKjLmX-;r0I<J-tD*!`{edl!CQFWc1hiAfryac=Oc{*+F(jGh0|?w}B=;~kvoRV6v;x&?aZEd5+Cb7@g!wa2)YRn;@za~YPbY?=1~!;dqjYP^>@%<z)o9dm4(`}>z}d5Fe)chFb{>B7TX3^KaK~Wk9c~xb9aqYzuPOVUz^F-@a9gM@!-R-{8r(U!8IRST6-JHxVCzuSEFDJ!sDoUk0(2VL(x!mZ<^yBGrfD`e4V%uy+UT6j#9S+3)4ZA^aMOWV#Ri#{yTRC+n}baog~Xi^nwc|L>XI^3K>*4n7IxtE3G?wf#I)ARKzr=q)=`IHfPp|4IuU+&E*K*tGius_aS!ESUXiVWOwTmhej3MMvrt^l>uEjhz5u4@-R2S17cx0Wcu<#OwatxjhQNq;pwNC3RU;NaObCy|JJM((80n{EE2J3V90J#&m=ATC@W@@iK~#-wl0<@!C+GsvbI?w#2T0S=AtF9w6^Rg`8BZWrnH)~KKs;b#g5@Xtz}ys%NTmg>Vv>4t$blT%2xK(g2skVP-EHSyH@FF#0@i^&Ky~ow8S}`%6q#8VTgUUZ)X5S;nnbylfVm0`k~UNzRiTKJ-a~JQoX5c;ii<$$sa@pD%7LWm0+pOQ#zhmGfR&F>e@ckFcDN}SRu#|KAkhK4+K@mp18RIY^b8I`lxG|&WjJO%Y2%`ytxY6%3xzg~VscPr6Se?kD4)Vu0!{>JLM9@5=iC#skMEe7%i*E%*Awt7hlYL}e}Zx~9vWIX0;ItKYl>opUta(~OCKmQ4&_vQV6)igy@AsvFCkT6N1>DUIs(mg!S5|#pV`pt4!-Q#fX{I4#l+%pdReR#anCz2uwbiG03**S5HdZW-dI98Ga4_*H)usS>jvc`s>vdp`7to?^UW2}%yW2}Gi@J*-Nv?d5y^}d+U)bM0Wiy3Wb_1hi#SFVa#@x|P{J>@f|h^h1xH|<rjOB%S603Z5Kd-gJ6xGBrF+&*<A$%;rv;}hD~F9@-3oXz7bCEu3mXug%DFL2a55fvL8OXkS7%Y?I!i8S>DzXaI#3Hi=IRY%oN#XjMo5QZ%E;q+bZx?RBv)9Zdr%w=H<%kj5pT?E)bBEZ<gmu<K~W>LV~n$v<J!LRW)=a){2q*1GAA#Ci}&EisgF`CJ=9dVzb2}fUxAtxcPR%a=9_9Dc_^_wLZ!!201!V#kD@mDM6d1U=~Ur|vw`kHH&0-P5AP;_h`A~`?C_lMy0jj#n=IKN!`KtmNh?g4r*R7Fb)vzS9MiEPgR>6jE0++#To4|?>!1t<-jAW`XbJ`qB}Zkn$btrzN-TMpBnejnf%hXGVxg!g+i<{Whs6m@=8@V=$J~&vXG8vyUpXe(gj$>7V76m_XL#G@4Gs(HcVAc(AXdb$WcLvrkc;SM9oUyjfJGacX59CLUjg+ss^I|;B}}TYzDD(<xe2a>_!>_%@^fv+_HzGqapcKuUxDY9#YZs3E7>TID|};M!S(JD$j*R8azQ<)SKpgDSpIaT0`=k!Iimf$7C3KK#QlTv{%Axm#a@%J--gn>eLE7-3v#s^kuk=6jm(@mHI21^US@Wvn3CSlc{8hVyn6&NE4+iC1QASSvAHT3?;g=cHV5?&5r~%z914z9VR(&lSvm>yE(s72Kxy0SD0$=rE}6JJ=Sj@LNqTpHUbjHb>3)G54L{fOWsg+wiQ;x2r=;}@nl)#1PHPPs3h29GhYZyD1jj?21aXf{Iq-?QZY5fmqG?BI;Br6lUL`v>c7ry015nL_<?cD?$pr;<B0$|Id3z+n$%kiXVvgXv1=-_MENCZ$(8chf(IC()#&VdHRCtHhr6Ia*N=}j|Q~wBIi$P@zCIZhrqM9NGWE@|>`Jt79`IMgn!M+iT3g|rGq)@r@6gDQbSr`8p3=cacNUUf6CZ4mtbQbkYmN+?pu4JY1m>_nm&2gZPlp=v-tL({<GZ{$sF-dIhyhnlf<`Lvpicib0+yorVna2|s!4%EgQ()n>-Ke43m~2vGuvU(sZr~wY{&(2$JpQwX4-y$P7dR|e(A77%*ik*_CU={Cog7q`xhk^+bBQsgjx8uLFe^d1Q~OwA-2-&)p2&l3fO~cdB@A!g46-Zx3#E8M9aP(Na30$h^l4IzIpXnTT7NmFIZx4L8K^6A8IBFTI<M5`p}Jb{&qH+&Ax8H|LdWoOK;8L%gn2tMr0(3{X7fk~?LM!Q!F7L!Nt+||ss{#O_o+0(+O+9|GG6y_`r#}UY8BwRvZKn;TLSCO7-0$A<J5);)fFjDu3^yFp}JfE)QTGJ;LCP9kn<!#y88xSsxyUUjIK)`F^nAP8ruSZuHniAS=sQ&_2L9{$OLQ?l09HOI@`c1U=5wNFZKYs>81u$cP5Q<5M6#FedDeIpPN@-?;fK2`#((O&I09|AXcng$N>daOn>>-0CgWjE6K>ldNc2~hIc+SwTEI__X(=|IKC;S;F7ji3sBvN&%5bY?cgXJ1?SKMP9APP*~p$SaxS0(N_;U2wi2$pA4P-LsqC(9W)Gqvcc69$GIDUUi%IdMZEl>k{D~rV=ldXMI<R%R6o1T}utD#sPvam5BF38kTXoFzjNnSKmk-bX0T~9{)wuu+1|3mrhA}E``sm<dSMmM3hU;<*zR{t|Z2&FN5e3tyy`}J7!^2}fjIlbW1!kJmCze3_Q71X>A$%7W0FT^*ZsWqL#10?me$?6scC$ef1eTQBMsGYU?@>~U#)9rf?a+tq3shj7d%05tZ*{b>BS`;F_^E>p6!W4U$7@Q$O+k1$*y_;vK(<u29>cpEC%yx!0jP;EQ?WXFM3%laL<|d;@0by0szUS{C+y)Ba|*a=LG;d((8A_=<T|xsdfBv9%6<vXy8~AWUEs=Fo`>;1PM1sSkVg@|oB3yUfZ+x0H~4%<R0i_$WrM1fLA-1Ok)*KTca<fqk0(zOySvj>lTOUxu%M4FvG|*oE_vsOI!~(jCmnIlPL}c>#c%qOKLNHgEf6%62}=uRmoJrDz6{mnR^q-o3t52a^6iLR{}zNU-_FHoiU?h<qCy*$@LVoY%ruopk}JWv`RX1cBlhEBRzh_1kAw{o*dV$)VA>_J@M2<sb9V*F(KKq8p}7V!7Z%5Y%%#%^_Z5~qm(mxz$k7q=>8_4p3!5iqq$hzxT@=hmO&sZ1ai%Gyk|T!fCNQGuoEm|{EK+Wa=bBj8hmj)wqv1vtI4;h;j=orcxI1$G{yYE|?;U{-^?EwmnFrru1wFQ0oeXx1by}hu6mF{s7~am}Uj>jY-gK3TT7=hP$6=0z*A|n()*_3+x8R{5rGa#!aBzOw$vQ^L`jWw7&?<+85v>R{Um>>v5WcChO%_j!9nVoDcAi*WOuZu$0S3cfhG~a^0;WQzv``+Bsgh;G-Ad@}PCO+CZvhSxsk4t=mrrQpp=CTEnBdt6#?SsnYRlW5#}#>UPsz@Z#Au!qy3deVx#1-kg4cvLu*oL!T*7&r4@6HRt^=ll4_Hd3T+KFc=~b7wN0>Pv=?*UXNp5zeuj`%zXK|%Lw?gh2WUSC3tOQ05kj4xcR5gpF$<)gal%VWJB82$_Pp}I*^an<8%Z=Ka9%_NI20tuG%-YH}d0G1aNlQe*KJC_{V4rqNDA@J4{<{9&-)>#`pbiK7KS$wU*Op&iTmF7+`IWWhcQ^ige*LA_3^eTUyN@<r{xXk;U0Zo!?Zl^RC%#@=SzcTDOBohB{LAv%^5x;_&xS93l>^1Dt-Q6ia%Jtrw`(gaYb!6=u(4|^AFZvtxVCb2?ZhY0_}a=UKCyDsgvtK<<|{w`@c!`H+Zjk!Uo%2>ZTZ~V^4Dw2ALn4Q>+hXhUp>F^&T|Er?C|UFfBf#v;kA$XmVuL9zj%86z00>xeq=yo`Bm#TURqoJp#~#+>*kf)E7xEiez|k~-M?>q^-c~QOS8AScH-jN%5ff@4Ig{!#VZ?s{(NouO1X_3M7Gcx-O~?j8Cdq0JJpzAWzMXve6hB2k{0T9`mu_Odg3#j`V+4pIUQgA@y07yIp4dr<x9iwKe=_~hxIqFuPwhtw0Cap_=!p5Xg8o6g|4oA%d>>#K+#BOEBFI@_3^DAz8k*$A=DYZ@ciwS%P<ht0*vA;4cvSLMsa>^`P1Q<FUm~~PriKn+(jN^8F9O|a)By;wYKutTbKSaTsbrR=HnXR?b?aU^vEjq0fvJQVrQ%vT->ZU`Crg0ey9ZEZk+pWZTY#il@EAp-ahx`@Z4n!68HAY&)+)vcbb4}NCGFm86S`Pdzk8f-#i2C;omo38lHan_VF|8Z@>EQn<s04xN9eH_phzIM*kAkodCY_!tlllH1f~S_~}YuZuZI=Oz!a08|z=Z3C;C-y16ne*V>Z`fbQDLr$p};sqUL=D}SROAKKBn!!tl6f7*EG2NSD%`^D31%h!+&FI?WZ_)QtGyMFn~k2gMETmGU9)@9avdwF&J_@y#fm*yX6>`e<&_x9OWhG+f)6hHj_IcM;;6|GyEt^!tf{k`MEi<hdVs|eg(fA#Y4lXq~EPB6E>K%C{J+b^Cez;}PVaq`xs*Fhq!zxi1a!aKZpme;rh-`!aKX8rmHD355s3b?y|?Ju|A|41Wuf4uQBUux_wROb={ygPjU@{ixWp%<hMxVwJ#8a$q>Is&;n{NTjKyVv<SnA|_CpZ$9H+Mg6bZVtG+{@L~6*IzuP8~gQt{QJ8Pum(3*4cX-pvebt;BMN+b?Zl}{u<ph`o&z~JeC?&R6K6ny7@qm`)(UWvD`h32jNT<Kc@}7K{hRkKs9i0tp}F-hKC)tV*I$O-y}WV#9LkyHzXQ94zE?tbH?DtnYvluY;jebCo%jcl<n=1#uC72c@yYFXUbyv-uPTANtn%>gF?L2RZ1=|-*MK;o?OQK@zVXJF$P@pvJbd*X^>77vm*(_O#9mked_+6!Bs~9%;h!$^v*RLp@oN3u8*9s_hc7}`-daC*Vr}^<j{{`g#+TRDPc8q%fV@=`0Md8u#CKBkqFj8P)mfCm$CooL1Q!;xkW;+pp&H2M;j7<jT?8f)I|&mB5*xdL%b%YSrQ}?NcY;26>)Kav3+Q$D^4C;|LVs-;HpGW(%WtAwCDA`w@NZ#S{(bWuY;EJum(59mvB_aCe_EQ6OFR)c@Re_Q;Ggoqd5n`n0<V8@dHuOF(BZ-m3VnxVkeyOPICcB%N#sw<=V6nsKMxCX$slHsD5p&Aa&tK0jqA@rW!O;8;4M{?l|dGb6M_eW*ugh*Yp`0_htDtalB}(~3i=jIjBE*RqxAgiWo`;syl#rQfCU>Yna;|$b>QIA4*RwaBaE__rUX{71|+O!&a75|2{Qw%s$fS77oNd6Q?rqqj1pcLrn>O5F%iQoR&@n@Bh}#d<RQb{yK2xdccKP0Y!F->Y`CywyhAchHYRxZHrQ-GTwo!PRRG=wmgw-6H*a0O2D(}efVj|$-~VCbOOVX3ZoK;m^2cxC&Pj4KTpfWawknUP{C)GW?#%F|FK?fFZ8WZU_}=TcUcLd#y#DIzpckPgXz1HjkYZN<faUO08>`pv7n&G)LPm7P2!SEM6s}+U2)P?*KdaYaQcy3>$vR{IE`KsS{q~PHj!XMJlVT{R)U@O*@h!(1GvB#=5~mbL1grS>tGAE8!;*CP!V4SMUPmUbW*fR;+QlS-Pu_m@ELb%8{%3uzMj{VC{eJkvd-7Fk@v#eJ;!gyG%sQP(Y`8|RostR`?KAQ}XmNFJ_~CWbqmM63WdlcdUh!*lDz2&x@Z$QrKNKcm1ZG)v>yv_hj-AsT1r6rJ39ueP{*C}I8$1G=d`lU+FRd-#;4xa^%g79jfm;#G<vK+Wv%ycU009+Y%xo)KfXqLB`z5PtcZ_Aeef&c-kv@HH`0n44jJ|w+ZTTfq`JU4%q~%%GC~dgrT!YJ3wK)a!x+#3~#+mPj@1d*8SQz%XA_x5e*M_O^z4My^I9IiSvXd&~c&Rpvn$5tRxfu6%)g0iA;#T0fGcnHW=U|&NhjV6)G7odU{o?82#Y^LXoXv)Ty5z1g4T?gi3drYzqZ^)NuW|XwO@X1QoSnkbaS8Ku@#OlMcgqbIK+#~>-@f{`1rN=FZsXnSpk>&w(6?5u-(I;~xL<%Ra~)j6t1!ej*FXKU4F*jH5s=U+-Ix^vt*aH<D`KE;e|*;LSP=jX8qmg#Ws){4U@3r{w1A*>C76QYnX_D}1`a*E_ztrbwA#P_X8q02fbxI-U%-8s@NJ-IcmQhuc;g1g3#^c6XaFn?_V{4ah8NfljaJSg%L8_JG%hnNQGx4&dUNC5TNggFqoh%ZtbL{eEzM3O^2kW{5zIjWC(XVeZ0xJgVTmiT(p--xdid!JFhri|O0+aTF#P&?^ecV(=Z#liv_hqapMQ?a{>ruN<;7v>E*6GS#7eVX`r~(}H{QKb1WT`f@sT-3J6gK1nDET)H@~ugr3+L7_1F_?K~3L2{(@PL`tTL7RGtnKJ<WG-zyAR!NgJ0wQyyajLd`Yw`0^NPsU)ib79iAx9uq^n%AGDjsf)Al$v@=i%6Mw&^#iNIT*4ft`qqV0v~urA=VcL6&0R6OZUt6b2fz;SDui`m9EC?pIO|)hUu<0ejOh9$G<$HXk&s2t=*cqhdj0Z+^-FJ4!(XxAs{(pmHUdCkz`m%&Ut0|gUV{==n9bTc@HHE@6|n2!CntePpkKE(R$#|qXEp+?9(AvXzUF&cG}xfmQ04aXr#HU)gp8w?p(0C}O6;|v9)E&1`SNuc=R5HcO)zx%>k1sU`6!4R7HTy>?A)u=L|1~abG6l^+ws@3-^!?E23L*09)A1H#-}IQ0l#tMWA@S)Vb_{DqUM3>I4G@ej6h!xUpu+}{-20Cnbg0)J}Fne4T{a4dvwJcetQcddu`?X+R7^w#=J^Vh-I{x@D)tbZ;e7{>xh5BPcQ<SO+50lmKYl!o&ZDd*5#LmAG|UOm<>7wFi{kklAgY%S-Dz`&0fEBih1A0$It6PZ51rr<dtj7C%~duKl9qg@~1Vp?BRQ#f!VqKkFSUwd_?g$u-JjfS0{kahPnFj2JDE-@WS<ffHHP<<Nf37xW=y!zh`}R*$`(}u?|q%iB~kWafAk!fK}>A!L*0(zer~mJ|R^R37&Ta_WkWwH$DP8^~&vYpAEnJ9F14>Ph2#&5F0o$6tG1=?e+72&TQc4uWIF#U6e?Y$Cr%>10(eX+!pznQ^D6SxNlpI;ntH=x9{0SNRx&qN4~lE<2SEs4y{9bI4Cx6wjSS|Mf@((`K9l!4qy6Kg%QqgfT{KQ=fl6RVmFV!ukCZ_?8ensVEf8NrZ}M#(rg=UG30w=^~~Cd=Xl8tTj_F{*YWD2fuqUs)LZL+yL9^_wAG|DkjZfpIPl>o=WoCBuIWO>S*>uz4NsgSAIf<;HuTc)BC>BCA<eilpA(u0CVb<oRXwp%=e_YVvZL#tkz+^6IcD-FURNhHsLS7+Lc)bvec>|gt{*hJHDv*Je^StKeG&+U0Ue@qI>loZND$w@N{#|_!VYh~sa<S8-dNH6W8)vMt)KhS*liO6l<NaWB&^Gwy?T3jRe3c~5rT!_P`k<av^@Ordypev3_m>q|1yz-Y?Kr}F_<}vQ@hwg+vK@h@4k5J`LA=FZu#=Y*Dn)YUE!k|%DwiP6k!uZpEE(<dhQ*ZQ}m8JcMF6&@G;e=wG*e2vz$0B`Ixaihi5JhpTEJpj*e(vA*%Zeg(t5O_xV6hy_R(uA{`HIo&39rM+XzbK%x(izmkKY7Yw2j9R0`d-W$HLJbdkR9*lnL@^L;DE3xRq=T}g1KyH36!=mG6$K|-LN*RnkeChr5_s$QGU(7#}L!{sO_$(g=l$B4NE#uMY<Q+~2`{_$~bm_!@_k&yCew0U|ub=&lX#P3V#Iu9Z&9fUyNxLe~SptVT3)|z22~Oveh&E_?!DR_^x~1TBI!pwT;IA8BzJu;KWQ~0881)c35BT=RD}Pflgg01}X^%Mr)X7eKGlx-MzkF`}o3j~0on5siM%~onw*sNAkH48uV@F|BMg#;a7!P9wTcm)8cPBt~HX~&}R1cm)pWV6FDE=_|wf7FR&dzt@85UEY-^mA{fJ*SyFcy3z^qgtHjQQrz+Nk5kWj7^xcChk|cS%;*PvvYC&K;GN%dcRB8m*?fQOfcCr#Zgi>1AM!=+A%QtKsSERh|8bqTfrtrmMH#Id}W)8!*a^Kc6SP=@r5mfZluxkF8w3q8(%#m%fFSz5U`DtV|v%?zNs8E<|RFvg&nSZjc+e0ZzP5XUt`x3YO{vVW7dk2z-XZq%YN-$+`>JeDTl{^|r7r^~oLfN#(ZZ@+ZF>9zR{POYas-uMWuMdi2ZTpDqKz<$FTM*>0S^_2n0e{&F3eFsdGOkK1p4g&LkbetL=Dj6wrcD+>J6nlIC8pNAiX`14s(qdvqffAPIrmtU>gMWZnHIjO3`YC71tS<JoJNf{N-w~L3oh+}|NabxYoC2|D4q-9?v{=P=|V`s<3<3k6`69-H#`UKj^t%BskYw8b080QhcR%{&?*>W7BBJ9b%wZQZ>!iU5&^X510IQ`-Bbu@bnAB7F6uN@K`J1jx<Z~f^c8GtX4D*Z+otWRr9s)7uuf6FevB5I#)2ADXq^G}ws`r4Pn2Z_sYeK2J=uD_xU3=3pmJ3iJwyg9t~+JrIt<`N)a<}b?}L;CT?aS9^KU60i?gyO{Og>&W^#OT|z*3&GkDrSdqO`j96k$2wRxJu+D&lgAzSAh8EyPAcH%3%M3Piy$nTO64vfc^{BZe2K)ua<=#bM?$)_{FaP6sqblUFG)xWF#0mdGjld7*~D^0CwB(;wOdL_HO{lSg}#B^Z@{x%J<|1y|H}jiz~)g02D6kO~wW4PXTECUVaJy1i;4MzXwr~{~mxmpGcsx`~6V>3iUsyeODZG8GiCL`XYcH@qCv&wQS7DDe@*=QAQE%0D~W*Kjwq?a36g1&8;h^t%9xkT>NGGE&*Zx-4A%k8u#33ZH&pSkpF@}Zt*CHX!(plt`a(H-Yk7hAXnupu&z&Y_}unk0kf{29^2Oi%!)tWyup~L(nkhzwG97q`HKT)&Gq;G#(T8z<pHw}%{EN+Te+HB_z{Bq%gnQYr^u{2O@P-|HR*7t4b$fwb4%WKnbvGmjwbt6g8Xhc#mWZC^G{ife@q^z++Z~7l$B>x89sW8Jhf_6+{h?HZ>v62pcmuTh0E%U@L%aL)~Vaaj}K3sEi2Dxzd%0?dPg>(cRc9+8638<=lAWy1qSt9Rx9_Z?ENyZk@Fct%fU4+mH8M0;@}oAG!o`@3~l}W*VfOT!_dm=X*Ny_CV6W3+EqILoWpqB`%f9rqCS^r=GfKs<A1GkcjWzF6;ou+43N$b&)@nOW1|#2c^fgsd18`o13dc;%G~?%6z(X(s{8<gRuc56O4>r{8B<#*KW6_Ff>s-f4?O$qv;PmpAnRW')).decode('utf8'))  # Replaced with compressed JSON by the standalone builder.
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

UI_MESSAGES.update({'lbl_ribbon_quality': 'Ribbon Quality', 'quality_draft': 'Draft', 'quality_normal': 'Normal', 'quality_fine': 'Fine', 'quality_adaptive': 'Adaptive', 'hint_ribbons': 'Round hollow cup with closed overlapping ribbons. Check the sliced result. Spiral mode and other textures are unavailable.'})


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
                          ("ribbon_nozzle_mm", 0.2, 1.2)):
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
          const tangent=localRadius*Math.sin(theta);
          let radial=baseRadius-localRadius*Math.cos(theta);
          radial+=0.35*g.ribbon_overlap_mm*blend*Math.tanh((0.5-q)*7)*Math.abs(2*q-1)**1.8;
          const radius=profileRadii[iz]+radial,k=iz*(nu+1)+iu;
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


_STUDIO_UI_HTML_TEMPLATE = __import__('zlib').decompress(__import__('base64').b85decode('c-rK>YjYz>k|6fIe?>HArw6D4Ks;G2R*`)yl2u(ZRmD1z-96nLE;k7zh-?Cxn9KxUJtbSa4`-6u>0x&=?b?~l_HHGa?9BAxOefu%txPAgt$#AVV1I(#Jsuem8JPfBRo!#aOcw#f!#%>o!^1to!{h1adk4G6-@V;u<8(UN{_H7!u!$F5Y*o(AUcPyG{Bq~j*{hv5FV4;?Y#79P^4`nC{oUi22X83POT9)q_NTsH<oK)o*ZYu-kbQ3mA5%Z|*kJ6%iJxv&=IN-hQDJK`BlNKTRp4LGqByOvK@_Hb2nDZ$VLIL#`d7igZ_tlA3&J1`yh$S&coToC-E46{X^>9*?SpvWv2VP@XGiIL7(`Fkc=~5glk^rpH{&Qu>z|$I4Ig^(W#yFp_!(o3#`#6Vo6R=aFWT$vjrQP)Oq_Y4Kfz?b)9S3N<bf9tA+^)*Y;;>jYGWK-`7!1Vx~;CK@`7+SPZ7|g_T#p%l4b83X@uB2-OeKopvpausBWj-Yj3FB@f_L^Uz~f@POr{7kLs-3t+Q5hW4$KIMDfs%8_E0}hynGx?e2Q7W#*-E6kb4Huie||iw>s#P1=}xK?v!-KkAH(^m*!I-yeHk_q?NJ41*~oultW4Z9L-15e!Si8w_AjA*a>yHXg6%aumT@t@DxB&*vx6C>8x|)frF^{;c=0qwRhzUz~T$U7@!jDkQ0w&XY!TNq7ev{jQOI?Zw#l(dfL}Y8g3$I7lg{4`VNK#@;Zx7R_w2joA(B^x%(dfcUT3m934vVE~{KAlLfr#z>n2WglB<6BwR$M<$LUB#9R$o9xPqtD^6iT4$9b|043)*Dot|hU`4?8_8{w`qMglHVMMZ*WTcWem|$;hY_$<RA*nG&%<<HX9%^C_;E0*X}G3Q7;Uo3t_L%37<g<q8u|c#Hwu$z;w6an`D-ZCIP@>(6EB85tdh*U0kHYI&&)|T2`<KIe%9$+rp>w${m-6tqyFg8$aBv+-}7N?a<k3?WX-za(C_(!qFFb1G;9wCu36Uyrpo@bnvYur6K~ib4*Z^b;+<~{x`R=E;<X2zPUqY)@%sJs)}vN#;ypUwSa(b>V(^W}kIu^`-lNCs=L;uZ7X(bZLlUOlS!UvC6?%Qg#A}~F_Iu~9i8p+_(Q!|_;p1+r(_doZwP{%DtVeUNjUxlR_<$JiJi2Kl!Cip#7sCNb2z2Vj7f5}=J@bY`D$}C6xLVes{P325(7FUOv(@?~79RV^+1YQT?PwBRZ?bU!{1sx_xi`4Hh@*Kpl#`cF0HVzxnnbZoSByYeG!IAKG??7V0!j>I1)xVhN{VKm%L<tBenT~@N$fXIkoEkDKY+9_3i(2G?Vn!;sen0!m2yno_Cj2716WpvM1ajrSuz>K(PVP&#X2Q~ERz`N=Q~%WMj8Vl_(*6Jfz%MBMhv`ESaCd`p64nGQtI=Hs3KCh7zMfdxTHl0c#|eX0eFqmIV+vd(=-ZEF#!<+!jp(fm5t#F!ZAqH)EXr%RgAkz0np8av>0G;e=;GE!yuVWJODSE_(Wy=goz&m&L9GY1t{|=F<B{J0`Rp5>?_dDprg-V{2r_+Y-674L<eke5jFx?I)IQ!13$*(ALdCKjBXo3bK7Jj^&97YdhK(Tzwl;=o3n<RP>*1i$|cP?DQE%E2N6VZ8iAN=LrqwBf}u6)Bx!4kGRZiG^-j#=J6HyW{>>)q@QK_!2TmI{5b12C?owyO@;nW~h9GrIqJ`$c|Gjw{>3Am5MWoM@jx|x_Z;M?Y<;jCH8kqG0i$J5Q?QVbQU(}`Q#9F_sOKDEyP4u|;SY}y*MYUBlPh^s*B#==S!`PBMb}3<9A&UihNK;Q%<#Ln!88oyh8gX>J`nU>tWi%_B&evkF9`R*K7r0#|aQ!qzUW7TomyM=i@#`_5q;wyp?se?VII1g<t-Q%3MT#Vw&||duu*^iT_=y)&x@XOpkX=4rxwS+~k`!3y6ewA)qy$<QbRoeW@DUV^qS~avCrAmK5SycDFy}lG%~NFiY_-xM6bk3&3|JEfV;0yFGze*7T$&{`Dxq@GZaZh|<Hse^3^mjh2hTxXRR40TeY=FiP@TDvvjiqg6%@zWO`Y}EudZvwGOVR!7&K!ZC)kcz6iCXHk7iw?fK0ImTOS*J%`G2TL8MwKmAOt^u20!5@Ibg+@u^OI8%6O{Xd@FZ^}nkEjU8M?Fz?M;efKJo*BWzZah4ETyRJ6aoprI|y0lQDMV0|7Mlef)q=b!Dn*X^5Co_M*=W>44C_uQ7`yI+K8lAc6(P}EOZno(*927KZ#nCKTHjR1e*2;68&Dm$Q%q(e4e6)1hd8w-S7MItJg!v#&vDZ%1yMPj<0@bL~#5y1liy&#UD2~8-^Q+zU7APtfa}1+YSBoB*TG1n?nC)|=wp2aW=w^>DqUUOE!y}a<SzS*M<LCl?o`&}k2qi3}V^qsfAD5w)lRmCReg%!8bn#kbpjraL$^DDg6Jzb@;c8;7Fqo!udut;p(Xent_zJTbMrm~u2F5#|fFLQ>w5(OcwJ6z^rohA35f`HJWrZrs3S8$w4Klq&4YJqK$p)|+-UP(9u*k7$BLKdkY6gQmQtB)e;S(d*=^}d~F9W1$fg4GgX<-t_u;24W!#lkx%MHrX?Gpn=t#mYgnFdQz;cn96EdVN3d$O9=vQW?$32dWX<#JjUU4`pSAg+<aO@r4k+1a;Id`Yv6y@)}OXuAj3D(A<{8kQ=K6zb*zdjTLw$iXKFl<5rTMT6UTAj`U4v?8H8C^pq@k5t$82u8WP-Ye2>a1;Rm-#@sIO=+}r!PbNeJz>XnT32afvDz;Xz@j#l)~l;!e?e_too{L_90l3<29QQ-`$~Yw)nx_ZX&XJ9U-qKGC3_tWefGw?3NAdXz>dB1gjG4YV0FZ`-v_i8KAS?x8Zp!mDmGFqXpEn-|3315kzw5li;p_fD_-bj6B}~H*C?&v0W1mQUaPbvPYbt7S2h-%>bzrNMnI&p=o*Q>T*Fet*JR>dohX`FSE4qQ=^GZnre>x62}$OnCYJ9`!0gzCUMB1dcH|2^R1>90fpP`qBklxEhqaF~^*5xx!4)V_vOmR6^16Y=+M~0TP1nX9F`%Z8&1W+oh9~je8+d)Gw-z(;{Wck?{pa5BBH#X2@hr_oDU(%8Z$vpK$-Oz>>cB#Ve;fOWpC*~!Fr$RVD3~D43%6{E?NFcJWO8>Plg>y<0bno=W~LV0m0Ga9CD1P>a1k*-%!JBzZ_6ZgP6WR*I=8e0tSz@o>eTbZs3Z;4$;<&+psmIJ%=gl2r!F<N7T4Bl_HHU}Q>mkmR^Qa*9NLJ~o;uk^4l$0BlCwyzN3joW0vfG6EgxAH_Ik!TpWeXEbe9!(TYI_P)?Q*S+^9Q>4ID+a(sRyxo4^_ZgH;!-!Wy1sB$mbi*<rBQLF%^5Eu`+cTZ8)uXJT42$d&EK;uArmu-d#`RxK+zWpQtvuC(K;wG6n_ZrJ1IM&atGq}E4n#?YTAr8=9~U<`nqNoit}%TAX!Oo#^YOP)JfJBe-gOzxSY-DO^6UOpQg{txEZdR~xgE-FPjw`1EkKiNM5TUvB1o$7Y8UF$*OUHJ_GQ~G=4Ofr3!vY^RQnA7N)RuLtk>>PT@*e@}Tt+q6ynIF282CHaxv})PI`eeQ5scX^s)CxzhJ-3=7v{<e@9r+hiB;}AB)JNArIv8`4!M`YTWcXPQlRKIbtyXPpXqmO#w>8?_iLX6ze{y@c(DD_1TTMfA@3M9F*zP<AAiG|8<t6M{bVK7jz{G|>4ALkjb+|<J`SdDF#zD?4xL@$r4tN&~#yp>Z#a!a1)akU$lY&7UCCS(e_z*<%!B`yKNd6#eitu4u07+g>eX#9mOxBH6{Fan(Ti~?hGEj=yIP3Eu0$7b0%<X9I@IG67KI+1?k{wvkj0OG~yxKSj)4csF-DdLr9|lupP#yt2VQJfinsGGY8z_S`o-8mWi+3=($~H$RFmRuC0|SvvymPTlZHoTxV!g`{TK!f_gL>snG7+(o9b}RqoKJQ2x?jflA7M@DSw<M{{!0%c&7vWlZ)Hb-_JVz!cUhl5-1&$g&BGuq+S@7OY(p<;%Plpc?MZq&gLwyQ(1l+)Z4%OiPk|pbA6{<;W;hfYXpMHI6^P&ds?JS0r`sIK9NQWTI;1)1(r?YuyKgtUmPye47~Tbv(>sdOH4jPCAF|EQ0&;gkdWPM95qsxlt{v^<-qh0!0d4n_E>l(8{2~n(tH;sB#l%!G>Fdf)l}idlwQrmf;s(dI%*KvzuCO(VZqFL)jiPfL3uR^}WasZ1+?Ed1sGqsByDior1T&=A&REWGeMR4ijU?B?&CPQkhF$L0iczUlo)k7*&K{ehJ?ZZ{N|m-xicV+QX{Ak+LS{F+pbygKVC)Yr!5VtV@?)^rb$=C*2GLx89KWr$*QI|TP9G5Fb11$u7yuFQ$n%wVi)sp;_uzB_alhb%$5tXgl6~gfl3DDUE8E-j!^}fv>9aMO+5XL^I1n;!6D;L^>)K(@b<b?>(wmZ4i_W9&sd_yswncLu*%BY{>{TqBf0oiRGWD@=*5yY12H0^Z>7rxIyZJrVy!^1Vx+|62F;Zi<!N<<_XIs{6D%a?R4^&ZS^39X`M|46<<HNdp>>F_(kfyJ?90<5pIeu97D#HRd6r9qa-Yb`=K@bmMx%N_&vaH)t4p7!DN8LBdy5gw$N4c%}i-~T^FSz%XxAa{`yRGxQ)3E3c*?OsSU>M$@s~HrX1T&OCS;H1DzAHCf2#SV(1+-4G#;Y4eeaS7~;*QYqI2c@pev+_%I)`uS%<~KO){ld!kNor%n!LzJ*HA-lQQq(LQ~3qU*}`WY0anMM?mf@mhGlGZGh@qMy???Z&=vPCI-k^^MbU9dXO<<7$(A{A(=mSnua|-g602<aIGa~`(!8A6%x477l%kEH-jbVDOK{Ss*w=A89~8`|RfcoPgNM=qvk1G;VdMEEg4Ha%$d<nYzQ4-VSdhVK6w&2b<?dK=U?<mi;mcU+WMs;_Wp2@AH(y{~7*tW9vj*$*JEWOw^13bd$)NQY6E8`MmGJR=s3z<%j%LD91s8{TT-^|WKdKLwzGWaz=&~E`HPvwKrg3S@7s{%SeeTnDUm|RmIovo@a_VH>okxTI=?^$cX!sFMlJ0Y1O!zxV+I+k<DTDb_co<1sjhooJUG>^u+3u|lx2Pja-Jc$fHb$)$Yj^K+$-#9G8ik$vBDC0bYbLWG2BjWdpd06282Sb0>?QJ5Ds-lNEfkFFLVh{#6ge)?xmnwaFwr$dZRd&Y!rm=e#Fn_YS)`A@b5RfswInzf?xFX-{ObmdQA%tF{f5gU1Pj)jUL`%?fNl?1p{D}J6s_K+4RCs^bP#%{!$J45m1E#d)#0d{m!#W#e|@RtTDL`9YwTd2E{V{sAIOUnMfg|s>63tp+KMzzN;&3F!=b``D?#f-=0jDekp2Yz6|I$4{z6}}ViV2k@iL2IzSal3ZAgFxr@6%>So!v|bfpH0dFR0-NN?F!U++nM9F!LA^3W2>xHY}x<?*g<%skfO9;|w*zFsinu(5o<^y42aE#|>{-Ue94F9SO!#J>tYVfgJoDm`OebQ9naKkB#9G^0!Rf&e;4rv-mDc;K#$Lhr@svgQQ5V6ACCdMwT|JFP<4VjXlqN9V&5=$YSTr?bfKQWAe<*Y)-&#(%n1nH@_a#HpXg!C*C~l6QL5#^nmWwbIE&uYa|=Yfrm*pXe>J%Q#}dvB~{CX-rT5$DJZae;p%D_F{)1V=-GV_3B-~tL<(rr=51JHQUzV%9a$P1IshD2w=HLjno<3_tL31gR&QXICPr{ON6v>NSS3kbnhFp=AGSew|1`FcX^>ka_vc90I@bbHcz4-J9(gEtyHF?0A2L<hYfGy<N3$^%&mS$S69UWxBGaw(HDlKsfl(t3#-HQC0uSe2erGI`^e)~tsp+vf|ylmPsTJ?DZtUXG*=B&B7$SKj`v*#nY_DG7>~gs{0CcULQWIlQIO{K-i~%SyzJ#JcXZG7eyv!v=mpJ1)*h8*^pX|BWY`oa@cMVRw%bvP<sm7LJ0#TE^C-geD%36c*&VDkl=7qNy68vshFx{Nc~lyb1=gTAavfb7olq0e2<=upM9b{wt{%G2jIZI^U9wHL-1O}g?KX94pX%C)J{L_+<(uX*5Lhm7%e!oViUU@tjdwCv@OZV_ZnhrP%<3N!eT73P3c=Fv>vX&JWROn(hM%BA{hSH2oW`ldrRf?x_9u9>4P9|u4qj}8EV)Thp!L}HZa%0?j`um^;lEa{10Q3r%+}pnnzN#pr0h)uY#9uAgb8x7!eo7E&sOqLaN`e+ji>e1R&t$(@U8;)n=l*(i@XL5r<eBn;<JqDuy+5Lf(08Fh2fhPhkRUgK4ngQK@&9Htf}8g3{B$k<Hy!s_2bsnwQ$tS2GUR!6v5jo3|Fg`2kOUhR2+UVr+)*_ZGFW50a~_u@cQk}?lC)hxwqfgJJ|gVdwsCC&#Hexo58qAwN=3|6P3SU(9+P0QP@cTorFEzVvjM}Ukzb>%(mf7LJz4EyB$^pxq4wKJCLfSU}FsBf|{<lsB-aEZt+ExodJnfu-l7UWxIZfnb&9=H<)_;qHD)1#-=H2ioM&X?!I;$!Qvii`^VynM-gD%_AegU<qoXgl{H^Ki&&|iex%?C-6M&ci{!Hqs(asDyM>b9z9|`@f+$9k{RHc@N@2)YQuWdjcD$%;!6}aav;Zjw>CpT0Q<!)3ViKJLLzI;)B~(d$<&)_Kz*8i(w<@qC&HOxRmTXQDv|o^mmI#iqk}$I&3K$=)g&92F#w3`Gqd9I}*Y61de&S|F5QQJ7UHO<I`o`dj<V(4KeWFi~4{4?bPmXaAa#>KnFNh2H<D&%qKt_Rve5`ItV7!5Tc;!!`*$Nz@*OvV)=-oe=`uI#tRoCZ8L80>bz}$|Fw|7|3xr`TDRGp1h7A&x{t_2Hhi5-e}(72~-;ytLRYvP3}@&VTfkiBMwT9|t4%9aRFa~NE)0s4?Zn)X}+WHI*i^G1UmAG~E>?eFaEAF@V+QpF1kW-Xpb)u4z5RePmC<ht_lb%6>aC2Ol<zk{XfLCxgqf@=v|mG*i?s4M(CDmKreo2^O<T~>PVUj?o1$yNnNq{7fw=n}w#4U9*?yQm_|)P{iBX?9c+Zgvd3*;a*&79;rwu#IGT);MV1%uB~?xK(+*!Mfv(Nu%BDvtF}5=)fob>%zaj`2M)rZ!{m_*G8w=WxWOzO&Yys7i%^8jozTqZuD5I!OKALR{-^{vgXFP4j?g#{{a30gbnrx6X3JmW-YxEu+P<n8j3X-i{f$N&l>0hkSikJDliEF%pN*GRUD6;VNs(l*Omk56ntwaExID%S$Z|_4c#Kd8C^lCJn_Q|9L$XtFoidnBTI!tFJTAqg%^T}om7|?2OdA_-m2{RNpKOeH-y6=lujGt2Y)t&+Ng^H*%Y3w8f+EeT)sOAem}>sk+H{;ARNR|7~FwM7))`cNg_zbdl()YMhuB|GzkW3hUI9ig`=))+cf1R?Z!4Z!5nSmIr;I-K`@3TpR@hK2c<d~;PsQYJl8SYZqO8O-3^;(ZU4jHVVs5cf5rdwTWmUIkk)GUrqdh+mZJy;|1Q8uIm9*mQVH-|Jclm+@t^-+Ch(_geDsAV<ZP1@i)Q@pii@#uOAZ7~q#A@;y$qGC*yw90!K%AyJbCzi4c|ND+keom|7f-(4?Ol40YCH=@b66Ef42}g%=u^vW=0MJ?z7lzy#0@V^WXgM?m?oJD`;<o1mP^1$1pGnQ2q$N`993-#?&tx16R*Mm0Q$xECN0K`y4Rgx{Sc^*-7Ebtb@bF;ufJ~>O-5h%A`RCwwx)0UIC!Fci}7iDq;JK9<%&<=f(cn!CQR0^62agx=TolI!NAk<sIDf;!C#1UXg>|_8<THKRFo}zi?h9CMK02+uk|ed3Ge#g3wdUt*l0~k6hrZV4+f35KXu0k`2qZ!{tkznc|`|1tgydb>?{#Pd%#}#n5%IO8d1TtBh@aC)P{u1)uAlHgKN0{gO-k_y1FLPuSc>$wTMq+u{P34*cmF3|BUyuXkR)Vco{=!K<%dzhU1V9RB9$?auDL99rCBwe&ru(8^InFt7HXA2SYQlf6CMKiWS&Vh`ET%U53=e7%2sybnJxG|<<F-|Vyfy_d%aQmLd_#ZT-6o-F>gv>cr3V-_n~7b(~n6{^#lO#Jwk?k+2A3Jgvd-72nF{lq+TCDf72AhAXXYh})2yc#0}-OWbm1)e5@xiR!9G}a_a^6R8yl8X!AS(Grhtd+t@3Lo*T)st)|NF2yia>5osi&j>)VIaN9l^5IcFsB_E#I?emW%RYut*)9npkCO}IdT!w3YEcium-@|8u;UA0@7@&@+O-4s9W*c&1Tck{ao}0={XAGX(_?^QALjAGU8H>!qFuxWcMJe5qDPCldN#G6?d0JaXsp+A!`R77*!r>t6F;@@eI?pkE3CfxY}EWK!+T0MLY*xrh}Dm@&0e&+lQgK@FVVdmP3@~fQ}kX-~T)O{$a>~xlmoqp_1v_yWU{z&))wZAA|*;zRaPZ#O>GqJh=}O@hvTjg+$`ERasYOm85+})|}e0V_&eB*kj?4tYX3KQ`ol>5u9!M{iIS@L%WT=m}4l^FR0NTwB9L+GxH&u-0}d@6$2Gd+TIP~0X`?}FncUYntf6M5i8{)X%<H#5g|ugx<rsdV@C7-;`Y#)EWgczk1gOw0~G~4vk~Pn@M7DXgs+0D*e603@@CP<+Tj9iYKVLD#6eoHzKYx;>b6?h9ue4y$j`ip1t^D9i^69i)kohEHm+jAG4r;+N1qY2Qs4hId$is}o7Kf%dFqQXgEik81Krxt7x;B+fp;xFX(UHVa02_|KmV7U@e6n&CrS!sOBNc>qR80RgfW4)Bje1S7&L7VB~ij=&<XemahF6)&S=g&bmO7?0S}$$C(Jwdf}5yWz*D4*2r6b%Ud%E{LAi-b$2HdBsyJK4vp778tT<SRdc~2TiI04DHl60As40ZK*c1NI!@#5P3JE^s{1MvZYSlRi>obX{sBzAU{$z6d0W}3VVsvm>y6UwTB<a17@|yQT8v29Fd*Pe}v$GLMd%tkd3-}-h<=nsWC#9@oRKZo~A_9FKekLo{p<QhBM|0F$X7zvVCu4S)owhBov$Au!pLCJe&~Ed_zW-mr;D%!CwKo}ig$r~U2{WK)xLY&9wPLkuu*#&tz?&2)TDc#%@k3Kz?kVCB?C!rg-ak~9_e=b>vwQp!tnBU{`*#1?i&q`?&CC67-yR$u7h2r9V@PIeYfG$(ZIfR{^<ufWHhS^TG|oAWW{p>PB>37((fpl&)`ejjvS_Fo8|l1Y1#K|)60@y2_}Z8Xz!j~k+^y4hrep(5_KRjj9&v==PeG-f3{hRYG&LU3z(po3q&{%ee!_oxv~mA*jRPuy4cI|lj?&c2LDsUicm4SN-%f#F*s(}m1~@=TK_!D0O)X0Z;ggShW&3Ru4}7pxJoXHOPkJ;aO8_54c-idiJdVOUKL?!WR<@r}HjL{zXoCC6Ai4s5XbI?e4L%2y61V^HZ~puLjU9R*H-5|3*jo^~L!VWT$xrV6-w%ReR9gapxX+QpA=9^Cdo$XW!Kfi)nB=Vb5C7f)*xrxLD{xo*QoqiLWOnN}{*7i_%}RQjSI->y#4Jo~oHiO&4p9B8{}x6mg_(?s=@K{;0n1S+dO~OZ7e&maFkFMOvj{wu+5Y3d_$w*Qmw=mib39L509llRcK_G^H+zeEL^zICfDaPpR<{Zi8cVq&rvV!|uX_fIbLxX^*@t-<+|bNf2LCJw^JvB9|IQo?i9?Ea2Xy<J|ByT5Fjjh!)?Y=~4t7LNb3B5-imCH597XIIJ)>laY?8z|Kf7${&%5Bspf(lPX`Lv~i}Ldf7@B|am&NCMW(|I@35}0H3{lP|n<C3F)Qj0{jWxTkpQC}+JUV{Gz~)W;3y>vju*RN6AQpGdVa4|B)21A;4(4eC%;j@`$R@Z6BAgLj)UhuUWtN?tVV{}(@n8R&;(lkfd7t-!sUIfq|4*=!{F?!YkSUAU6`Bt|DnZ$)^XEC37H{G89N->tJX&z%t=;3vnVpb+CTnl+pdshQ?ESw%P10L}5m9a6cYIzUX^ng2UohTJdW;S)m1_j|P&<|yit;<vr%2|E>S99u^j5$2?Kmjct=swVOt?N|EggD8zw9L3x?fz;@#?p-argM(H~GVEQ<bzD&Nuc7^z7`mZkeL3-wCeRy~Q|PU<O4IjILOh*VuDB$u8eY<4(JiNrTsQ;JT`8cbYwb)@^p2J11`C`{Q+O3gUQtHjZ#K-~TmqDvn4jEbbW9Y*0;i#{k?$|7YsfFqkHWgs4uZwZ(m+YVO{&+w1TDivL+}{q!A*gn|LHL+Wj>-~Zd2#a&Vr3%GBi+53lo|I_z}Uty_iKMy7zKB0rFSK3@+I{Ai(GduHN^fuVVPv4j0IKb2NIC%fJXfqcabsF7Bu}T4>wfdI}``{9Y2pjclah1EGIp%0Lyz{bs`)MGH8uz=EMyK6#`bBFrTpx7M{tdQsD+5$N1F3+E;QkGKgi?$YtPCq*9*s5z-Hj5=0aqz@y(?Oc*caY(_QVj=%PcE2LMFvN4Ix{DjeeJR=a2u@|J>_4XW>1lbdE;^1h&`z<6r)({zn7c9ZJAoT%=E2a0}_FU0yM`UL|f@yF;Yem`c*Fhg%TB34*-^Wuas@MciVk<aIu$aRkM;DnSxewqGVCwn%Z^Q5;!k0FZpfQ@5X^bFP0MuxT{Q0mZa!&=~L4PJRm~2U8?(<GJU(x*s??4{2cF{eJEZ<Ge3`LkoUJjbM9oFvf&O6_{b@8i|Lj;#r~UH)4Mg7$F)36Q6y@9)cwo2X{bgOrC&bAkR|veXWE+#C4?wYOx-Ftite6W~(C3R}4Qe(cIm6N_M0v8*HZwd8f(TI?-=BInFt8R|72PTQF|_$A89l!A1pZRnnsR){lW0?7N!tNV2E_cSQ|wVZKAV^k4oz?75c)o=)-a0X=#Ic&z_R5IA&8-oZqcY%twn=ru8Hf@+cWa*8y__@gR#nP98ZB3GELN*m8ZlhmKVSLGYsGM%2)$~!rqI55fgg_PLi?v3ksV^51sEiToA0yY{gGANOjV{bAlJ=2tt-||jN+x^xr7w?D+$RZ!*9dJhX#!FpuPSnDk`ootmzRFzWzTJ8C3QX36xBG8izInl_#|Lj~Fh7s?e|!A(;XZq{^WFX-I?(OE`DXtWl!C7>b`JM=>4yxr_z&J3E$KqXt=-jp=-N#?B>WdJW5JSP2Qz**sJcJ#uRMIy5tLGpvn(2k035q?H2Hb0)aOp#QgWUJsfAU)(_9={^%J`3;R!W0QyR2fTcXXNdF(A=FOgv@wz-O&MGgiL?mVH1TVe%%pvMTc0qoF8biK60h$z1Ojh93WTY2b{80EC^r;NJ4j1viA=NoT}y+}kkW4n%3+w4^kj=kCn?j(dgx)I%OL^JgB`~)ZdwDXb5xw7!&Uw=CRb%adYvtCuG6nTd@x877>dqGhR7>NBQm?Lem&)^!dWr3T_V&DJ<<{LF1io*rG*95h?Cp>39Ht-DuzVV5GxBCbk{}zH@%q=SXy~Qh8I@m}5C0oa>T|CBt`Ppjr_;4@b6u?#6MLfJ<nu#rU=QN{pj@74`eT;xXSu{&Ci!_5ak|9YjRY($$V|av-n@tDIkT4f$IL)W@eoDm81qSmUA`F=pvG@Ou#r`z9!ZU%HKZ)1~6}%y++*Ld|s5S9`&SN~P4rt7DjF9-ayUsjZE}}Z9Vi<X7>@klYFmO)<?!CnCe0{#U*NEsM-cCFtm27$M5m8l){RCh7O3Edd7z)~`U4k3i#PZ0CBivtL$@~8RsG}kba$Qg__7!;G=^81S7RJDX`YOjgnMP4M#v4Q472UDhjS^b7<&gjOy8<sf9t>9?G9FyZwaL)Z2jfdQ4Fqx_FzA6c^6rvPwXHb->D|-cajR?>v~!Ibx}39~J#9@b3xk_22<f56Si}jt<Py4GFt<PAaHo?qd`?{{EU(G+nw{gx9nC)Yh|J0PDF!}8;pc}+&HDL={-cu`V}7B#CLNB`X|g8{^0K?CMC<S>aJfH!Fp;qV4bg!AFA^9^OlR6b#;af&5P9W+1`>Vh;f}_XZ<u{_5>pejBN3a*KRI=cRcq?qoF(4KS2Q{s`WN@~VeB+vNtm7o^mrmWn#Usy)o?6BL=;=F*}cJ^(3dfPCsDNi{lC5Pg9Ya)Ty1aA%YlWKXq&4cOWB}epWrY!M{kEUwu?Is9^M-U*+21S38bFi!s0*j=93iG6~3kLFeC3MNI^QoFtT(EDnc|FnwthD_2e^%@(QH*so(Y~o|y7gOs%ruQvRr7F_b)<?48WYw#oO|6O*9-{15+8kTLHY00r%vNIXXOp+5=ykvfNQIUkoyY!-zB5R8{w6^h;0OkkmY8%Hzmf`SWHajV3d>eyuMwp4zmFP_-<k(2WM%1U|nbTK)KV(#0in%kJ6gQKPPqX<<c&SZ)0Baj`aqJoxADb7ac{YV|Sat@^qVQBgqqDOfY4vl6CaAz`adyju%&p`m;mEF7tqZ9VT_eN**4tC;%ujg;Sf*<UNek_e(5TlFi*}$Jn+!%}k+q?9O?c%Scap27Nhi5ZC^$L)fCAOc_Pxh96E{#T-J7By_omh+l+rr`P8U9)tM;y#%mgJVuMb`EqeS+K!FIE_ah<46g^rxKdUHo9LAQ3d9BCvUH)uKgKE;UUx1DZpBR%~1@34^%g%o720J`_%&6a5O1(rdbC;?y9P1~MDd<(hIJa+f5A1v3iowM(+@y6U5Zrjn2X!|&%F`o>k3P&#>yGg)K%kbbj&%6}IK%e=TOKwKs(^U^Z*M&>c80C&c7w)gO(c;e&$h8P@T;)E!&w%^d_3NS}O=sO`&#`bggy8<+C=*@B)@DifR+};u2N`ywi{9clc1s9a=BCQH+;jZ|q00;AUQZm(61IBNA&OTP#k~H=~5j&d=(vJksySVV<a#;Dz(EKe+4i8q&Lkhdk_b1q3K4YLcjsZl3+Pa{|4A1vO4X}?;86*XrjP4<WmV!Rtln&vzEz3ZIW)YN$nF_Dx#Xg&d-jx?j(70;41>?O%E|MApJSeA(j{s^K42QTve*{qEep0>`;K1m*_cG(C84cW2U_pYB#8Nzd#W6x1SK72b<6F8Icv(bnvIhy44CVo5A9Q@7P&AjhzF2-FS!k)nWGjA<ndSshZlf*OtZ*A`1(hr#PPRtbzH97x93*bv#v*qA5Q}c{W)AjGH1p@*$XRIq6;CqWhY!#~1%Lra!1Ug=hjUnx2e*U!hzS8A8GG@p;NI<W5I#U>6%fi5)@7!<*gX@G71_7m6^N5H#^Wt6-o#;k$X~1A^V-kLife@UL88J1;b)T+qA@BSB}KXM{>0=2Z{(lcuKIn%1$E^Eqy?`pEle7|iO>@64Ncq?Kbu77esW(RbbV^%gPt+)L1VeOFC6@PmR$PR_XY5AWJnifNO0jz1CSoyMaejr;sNbFwt*uK=7U6r8^+HjG*ojWiEx+DD?ar3nZ$-{=6}}uh3Lcwhztqg!#250DEHsuQgC7)=jjJ%9THNRHM;C{?=@*}7{wqS8PTTYJ?8pA!1$oaUI650o9$V9fJ6p`x_f_G6JE9SKkFGUd+`BNUV)$^mXcsFtHDufM|qnTI~^?Vb`S@{3t#v;f8z&Hg6_S$V9TZ+s}dL13YmE&UxU220c{-9iS!DJ=RNqUfU{QLg;Jvx4N|Vw7ejD)8|x1g(q_LO4omm<H9+(zPFqHdC}AYu9~SQ$I>KW6!}74vZ~SX^L_m4S?gB5_<(Gz1#|%&lU(lmEY+t<g!M<R}X!n*lWyps?ep06lg>*Y>DP0mcj$-cM$vbkdKvTjsbL0&RLW?=LG@7kcp1)mmR=lU+9G@5Rk(f=k7kfeIUEly6QRtJB5mIl<{G>yaVcq^Ue5KY-vEe>_gN9>(muTgi7e#V+S(!T&l&frGKmqdER&Bz7OmxlA;nTB%ytQPl!nk<hUQxU{MC$@?aoLuS?k}zYmwJrnoyBE6b^pYoh`chLuz`Q!VPs192KE^4=y1<w^t<N~Wj5J}h7^?VAVEKH_WQYi9)nI7QQ*ob4kPyd?=jLb#-i5!(C^^`E?eHjI1^{ZJDiJZE{c6vQa^_2b;ck5ER4GNGy5Sw`s9Ad0ch8Ayuc)aN4><~L9F6OfjW;p2|ag6ln-><6xdaOtDjmo|E$pEL4?HmNE6)%GEabo$34FTQg}IJVdO0=CdRHv1~5i<;U4l8gZ(g<F>0rNg7M-K@}I;IOXk%QuFF*Ci7!Le9SkU*E&56OARsUr>@Z4d&HL%5ywy!S$-^*y{wmgts2c~<v+~fjC6$-E0apTmu9SQb1PW|{CvwSh-T0W+lVBQ9!|`Bt=BF^}g^w<Zcj6fk_yualM=_(sRKO<u3E5FgD*uJi4!#Y<(-`asEaJ;sw!?2aKj%+vYJm&H<C~%%#@nC8@h#-*>0&^6EmRuAAqL5&SNdW{2$O&On}7Y6MRC0Br!)|j1hh}LBKX^19>qN~U-`<13dvn>*I3tl!rd87LBHT`bdlFR>rO`$u;4$r8xN&;k$rV_ru+K2a{Mh0qOb^Wl1?b<<bPL;mx}B=uIwy_SF>P^2GBhr@+Xb6hX)~zaa0L=&hxN!|7<~khNo+s!EzV>@drMhlfAUF8%<}>1hy9qE)9k@IJu0AS^lY6_e)C4F|{4<fL?WPnE?+v`r=!}`5%|-t(TA%bNlL?&RN*~P}uT(%NcSJluy8g+5=sZ`=sDhdXfG}d?l0ZdLoa~!h;IRFfGBAPw~MiGOz-g4B}vxZhuxC%|kAItNb-oe3S%V#|#E(<q2{+^fO7>vx9@<v$s3ny*k+0V_WR(?BH;B=j@xEqy4j^<FEH#9-L8$UmqR3IXk0zYisPIzDf`9+D*KW5`{bn4iB{tbLa?`!YRJ;!CgLsJCAn=!?9p7j3r4faS0V{&Tea;pnaT9zdkzK+kd|E^(&;-;m+$LAQpcm7N0uWWVy#H>y)XKn@!eUZ#7#y)ei5!NzY7(JUfCvzC+(KbM=7vo2=FB_IPeC5dS7y-;h=FvG%d*`UcOn!|89bjgG9TN6g=3Jv~{5z~98{!#vpta}OxYR29gc+TG`wz?x@+d4juVGadp7Omc6M_@XXPJDWv8m_o%9F@sN#EUXJXJgsL*Kn&LJn`zKX*6o>Tk2`hNYwKy)1=ho=lp-?n@#8mHr`O75%5#8CeDG3?ma!uUB$YJM_WfXpWU9Tpha{2}#Gdh{U^*x)y$c~p_~%HXN$)`5O8rVnoyoJ4P1eP(>Sv!YfIXR#^`s4@^yUC)=}17oEXPi$prvsSO*0L50WiVxUWNwsRHANIAYXM<j&vu6;u~3N<`;~mGdP-qFOXhKrjt=5ZeJw|2X3GkIfcKIJi%SCGO9CX(ORWvwCyz4vt-)ef%bN^lFBWO+R(~!)VZ%dIcWH^G03C{O$}{0nk|v6T2H<o&c@@jsIInmb>MD?8tCA<UdnKkf%auNw)YFRv8VM)d9`SazPMB3gnP9y={B_iu=qZglkxwCmSr8yW7{5SozdAU*JgRrvnnI?H2C_VrO~q7F(gVLou1iop*`^8ObjY$;CyUUuOs{Lnbwmm$P&yHdV|~_%6t601m5oVCfD9=qF?gY@zSMqdZq6IB$~LMt`~3x$)KgGZ{!=1FgBT)$>TZbP;;9e8hsrBRWz324K{9i8-wP&;|vs3(q8VnW~1*O`)orPY8#2>!kmq5ZX=hb*oHo2e5)Ztt?xQnu(T~DlZDD?$5?(h$dG}qtsX3(piePC=NY~iE-y{<ar;cN-#gMfl|no8{n_p$3jJzy{zFZ43`G4r4jJmHO|V@Oze-<G;SDc>(Jhs&Jwa#&FdEnAlgLY}SKb7d$k8|WIf?3Q97yQFh*fc)CK};2Ak;5e<vfbe6~Ds%@CTI`&L<Q7HwYLX7nGr%SgF)xb2+vrpYfFf^~@3Im2c+Lb3exR)Sf8xpYzmakUS4U(D|#QniGsjdhMm-CU9mIJHmeiVRanT*{F~VFT?-e5P^Qs0)QYK1WBW3&^4VL%aB1e=1R82RXU_jWQFZcVV~KT>=_5je{LH6b3x^-Ua4g>ooJZ=Eul;ka;Mc=GmTzF*M7VUv#lx!%fTfa3cZ((10{a9^&hwBaGd>&v<_oE2RM>%dYzX3Ba94i800bgnZYI?Pd>|5quhv_V;2f@(HHSl-;&)>jlJu)X(H((I1MBlh6Dy8Wnv{~>orXaL}y5R1Me1wjy@F%=mr1U<Z2Up$~t;?2&c~RB(jFkijz~GjF)|?6F+4EB(|Qw$5Rs|Bt3j+4>r1~KzUy9Bsi5Lf`IN0y=%s2r=A?=ld)rFzYuPXeene$kbT<T!cJuhjX;1!PFe~zlNczyt<v8yA4ZjMQL6#C;Aq|n;)wGf@FHpflI9)z+z>Bc%H&P)h3<?x8`6y3bz`Vo<=^<KI-M32RN0$)f|^qAjB&ZsBpUWW730~lmL2QaPMLQ%A_mK)$0!W(ygCT8xyTu-Ih!Zr>WPwvWH>8<NOmtkt<^J$xnY#(bo%%kF`U-)nTQP(C>C<MD3?TWs_jmBb#@K|EUS3HI;_FYk%QQ~nqCu<Fmnry0wdjQK!deKxi*&5CK+9w<Fo8U2U*t;v`<f6GqBBPpn=Ib17|6e7T~h^$MYs$g1Mp@C*o6Yw?6K(l#>E$;kT!(?KgV*T*yjoQ)l%&R)z*CK!Xmo+o#%86_Zj2L+IO_?0xnCNFov*^4c}6_Gbl9WD__SQj;ZaYr<q)Wi`7*fQo+RxTAys8h>c(i6~gMpy1vltt93$lEedmhv}Le!(XNt`;yW?7k{VAeo%UkczpoVRM$N-Kt{3+(a5wxgVrrTb0p$QnFiZTw}G3vHgvGxP3W}WkO$6_3t;n18#EaCCTL;x=Yh+N0`M~1MgSJMi9nj@c?>G20ENo8aa{P3i9_w#<&k7r1z55IHkx4^YWy=)9)1S@sAL!as7xC)7>^ogZc18!MWPF=$l^dhlL`m!1Y?AsghZh*JFvL1aa_mkMfk7N)3mLu>Naa(JF<kQtXnfccMZ`$oAR~)h?HcGPVHsnR(LBrzt>SKQKtn$tWHOVTM{`b>3n+vjok_$GJogs<d?5E-qbhyf#(m-9#F<+{^Wu(R1awXr3#eZXpvfxJIFBFpd{f?oqxy^5Y;@jbCFs5nw5<$Q#o~UD#E(-x8H(~nyjBcC9%NR1?v15g>_ndBi{g)KUT4!*(K`Y;H3nfd79z`s28d8vl?8YHt_F8zm{#W<c@AEaJdq7ez*f9%s0<<*yDs}H*cL9*6!oq#~lSPe>`MCvkTPu`H{16=6R9@NYAX(VH0b#N&7?{)PRv4J~?2>%sQP+F+PME0PC1ai4HqoJFv2_<Vw`}u06-q)^NGbx5Nem0?KFCxy_q3);a+zuyDEDGE7yqyXQE?GNf<5K%I`c*g7z5cfI9;lx>t3fs!TabSTEwaS&SCEV2&B>=|Ta*J-zsQ+HkGC*w5D0-@#A>7>n3KY#9K0kI1RAdN>{GSElXn%q&Hd040E*4c3kX9lh?G)1z_1l-~gCwnI<QeE9X<uk*;!EZAlTb-G~)!?^?c7|0cK-p<ixThwvNdhmf>}CqH4;i(_W+xdMJw<hy2fPJ@1fjEG^wT_|QQRde>$!D0xa=a2Iv_YW)PRxkCmwZnNZ-(*xOqZ=(D{LL1Mz}6VA)w#9)QY}+KxWY_-TrDzM6+&6{+LtDt5&UN1n-+z~My}z@c;85+IQ8hLAh>%>%KD)M3TksBg4fV9Y~@LQs0KIvyyun!S3@1u#2dE(9iv)bR|uz0s=oy3V%g$I^wsvO;w{x^B5!Wt?Oe!qQ3s!CLiB-wjKgQ<lJ?5_LQuZ`Io_AnLgM<X05v?N{|*@g)hqpb82fG8Edc^1{RfQv1@GyeR<Xk%!UU-NY}at13f7-GU*9VXtL775d?*eZrrY%iN4Elgmy~C#q$l4o}6THq+L%8O>8b$th8rlI!R|fI_Zq%>&(+z=2ui*14wvs&@4Eu_b4+Q|&wym076Y6iZ40LX(v1B}-?qz!Y$FfvMK=E-mJ+vCa8E<cF5;VPr##=NOAeR@BlKF-=d+jck!0MINBLWSx6laAmliqnPD@p%_TOG_ryIB$RvRa+~+m$hXZdQ|I0sZf?+AJMxfJrqrXr5+ZYG2}TegR%8T+&q$sX_@2|svs_fud7)D>%iW5N0AeXNe9o`8mQ!pD7@1<TL3&N!0+RD)$@j=EQ|BHp?g4i#D*}#OPm~A})m;PSa+JxB6yLmCd89-&T^{#vq`0Blv3q1X+$b^&C`PuVa?b_A@XX0KCs(M>eJ>bipq4$|4R0QU9$Ah<jwx3kyCWil+7B9=seo{2pj_X5q<W86c#Qw6<qrWe+conUQoCX@v(Q~AvyR<GtR5CQ6=h(YB`hdz&m+qibQP*|_au~v#N3(@;PzHB>}6LG7=At?eH)T;ZPG}j=U9Dm`0nI3f~*o^VvtleHeH;4Qf`~wghwK=o!i85dRFDe%*eMVdx7(n)hK7FI(N}xU7Bd?dc*P_TX`YGx7~|{knYW;hFet1@}LoX7TGn6HrsRv=6)OXMebMDbPYG>B$kJlD@4q^p_bS6jha2NZO<~>w@e=cI!7>WJQ@w|TMafm(eiMN0#aPI^BX%0xu1h8ngHZ_Y&Om1>y`(YFC}z;g1Bx#bi2ppVY<rI$&F6zXc<tQK6PSZad`O>LU5SpvGVYxn(h2I9kFy}gvc+xVC4nHw$aws)~}3hsb6J>*BXFq?b!O2c{K8?CyvtkmhM(dmKa5GRh(YniAXd8tCd@QV5X9Z0G~obgl|#>`PFI7)t3_law<E#RpgtL)l|pHpWxz5r^$}Sctx39HGKZk&_unBvmahyWZ~-m4c=yZ7NiZJMFT#K+cR%(({U7jx~nsL`!70&bi0WBN#4F>YiP&v!*^cf_}hasNZ&$!W)EaJ)9rH>C7?N=zsS^b`m9zx_Df8Ch=1T){sf;djrgcCKB?iwRUcF(m^JtT()Y$X&c{n~TRf9B=(ClbLQ?M2Ep*3ttb7t~*fuZ6zNDA*HZ?y4f;pG{FYv#q-bhR}pbz4x)eP^1IS>Z_RY7F3hM?5k;kr1B@q)U46imj^+=uD*n=nd~>P+^LyuQ3^?O4@u0+CHea${gK>tF%8G1I(wW~t`Gb0S=s$kC%#XW7s8X-#wMvHV1Y%K}DHQQju9YVNGh_Mm!(hi#5(_Mx6#?^`?t%h$^tw%PUG_~bNbRkKgQ>{_pana&1e&~s1^Ga&j2SWQ9T!*HS`Jiq)z)H==N{)yFd{dlid7i4ml&mRY3c_NQqp5L3IHtWg6!q~l2k#;I&;%B1q_woCJYI(OFOhkAK-MwIOna{}COTnp2kmYV(8F;6U*WGWpkL5{lsyRA}A=dKRZvQW8*9rYC^8Eq~iyXh8h|BA%0J!q_ihpx&cdz(2%lLY6)ZEkS?l*+6(8tSY=2P99RB*+Q>;~`q$t?pIzgzsR2C?qs1{hqaxEO1)1dcE{YEy_^YW#R97*X>0?NW8xR43D%Ou>9U4<^I6`10`449&;tO@bXV*B<oWy-`lSid5VqwunL;&?fw=GcXNLZW0`_2BbqbfJ#FoA}EUR6%l*lzKuyGj(?2K!2UHO<#WBq{eP!OSi`?%=uc8_QBgIwF1Zu)B@8m<!&iM;jZZF5soN(g2xZGJ6{iw1UZ#4h6~gbQxLl4^VZAFuXZu`jYZteT^C{uyGwDIroNbg!`ur1qac!l^P|qIXhcU-h$qtkhWmE;L<WO`Rpgx2O*j@a-#*9{BR+gqsx!nBZ;FLJcW~EXNhAqTbl?`g~9>ChI`cAT%a%4)I#-Xa0&X{-D(rZ55GRa2hRC_ePa8)BiA}XVuL93{Do&fY3jD-5xZR*%+79KNK=b0g2MTX`g65?2LzR2hk8uSU<atOrtjz%e&+0Y6ac^yeO7Z{C%VGd-Dj$tVs3$QyW8WvJiK&e@19YsvqhP0*(LqXg!=`|*KHOxd6*;p=t>R)*iE>F2qpO9DubzZx!!-w$(T>^P_^Cr;+*{zmyYvdG2Vo{bi4n5{_qFK20z6!#HI{!BqQkjcsWCK;$5a4xgYG}G3r`~PCXB%O9K%!BK#g^%&FNm;<y9(sGrz1iHs$KA#xcyX6v6iuYFuW0Sp|hHJN2)2@Pct!Zs5AupG822}vF}~F6bG?PU1q~JK7rb&hD$Y0P=%7nh(&0rFz(%?D1cKSUTUOvF|}hSk6SGz*r7;6a6J@!nE8^6qHQcng*sUw3mS@+h649cfinTMB_Nq0Mju=A0LL18hEk(V;^-3o2)Yba7NC+v`P%uA06U6Pc7CRfy=2_|y4$JZxnFP#|L*E^IG`Jqs5(@|h!H~t)A<Byus@J*%cI_-^>+7h7wq(Wp<7;PeSM>|-tVlt3*GTT?arfKyR+VY^vG2TTP4c%A3y4Ld+Sh+N`X+@h9#R*ks3Q@e~y1Jx!tYh@-v`g6KffqbrX&pEnvM~=W*}x`lHU{K4%t_#Pq)0n<z;9?w*im10ePQh&=#et796Q>S>hX6~IjLV<IsA(R^yBj$;4!`n?BHQcn`A-oYT%r9@ldN6H$CAR6WvY8a=ZpuCXrN<2W-mo&XWMu_iE35EQbH?gqv;0AaTn`~N9Xyp%XomqF7b*Hk-t8q6i*(2JXt=?G1d2nkLxU~!1Sq1KD7LE}%8~1SlnOS#)t-i&aTRR6EeTO-BEeqTn!HtLtH}=NQ$Zq}|F^q^Vx4FW0SLTRxM3lPA70z`l;oKlc+5|OdkyO+KL<=PZ{<*^lAyC&sK4|A^pwwAZtJQYm5mgIuwF_}AsM#X<?Cuw@>h4>+v~R^VTkUpf|4MMS+Y9?>)HbSzH#8hHjt`ONfFEdx8kA-s3vb%IbXzao=B3;D(nJoTr3SmrVYl<JdFi%Zy3I?s+xdpmjHUKJME-~3)Vv0z<$&L|dFi%Zy3I@Hfqz3nm2f=7`9j5SdGXr}IG4T;w@8jYplUKp$Y7qQ4kJ(mKOikaD~BnqX5ZX16Bnxqfu<UAutFzP%gEW;i~WPw`^Sebch7!(baqBbhcBN!J9xu?8@K(V>1>|*;%)amim^KIr+%1<g$LG~I}Ey2$9D=-Pkg+nE9d6AaGItl?}whTAPr-=?wB{xP>(U6Hp`T1_^qEIDboYfrN0K+Bz(`^Tr21tRl7h7RVc|~0Ca}a*EFqo<|kJpx~^MQ$pyy5puA$NqNyN=Sz7tOp<yV_L(F>Q(3GpE+?<ShRz=*n6o(^K8Yk2=WiuY|fyCRI0t15LBwG{bF5Df*S|KE<a1;<n0~r+SYMh%X+htbH9QP%F!Zi!U^${J)WLu4RZt{><9z;o1o)&>hoUbZIq)iJ~nj5Ye9wAhDE)5m7Tq1lZ2K0e|qqdo1oUA%uD9(Gpff^H3U4qmZo6Zw6zJ{MpzQ*)Le0@D}uq#${dkNND!$?kl8Bbwt!ynKpJ`HZn!nV_&Juxo*YqNs#?W--~Z!En8e_x`iQWXb;z|Fu+*OQvY&nBKr+?3?Ke!%2xFlCjT6BbLgCAAY^T)_GeVLjwse4yv#n6YEkY(UMLlc~&M2bLEs$|nHQ7nu?lD3yW<otlI3qBzhQPaI%ptOp5B*2DCLB6Wvc5VOI;O1g8Rt%7_5Ea@sOS=BC2u7y?w%iYjsHSR@d))9&J;*B$si@gWDX_mkW2#%)7Us=dT2;mAP3lz-@Mj>XU{3MAgDE5#;e<0gy!NuBhfUDu2+pQNDdz5sms-Y7KIs%}BpNGuOx)ND7@uE?xGifGTs{{>2drjwZy}*?$V8W!pGjb#!s8&CeVwdNT=mhM}>0q+rgDh%}!RWwAI-^VfjEvJE#mVWIzKGM4o$w;#DXd{QcG`3ld~QqSte)n_=@iJ)jNZa-H8rE!Lc}d<f~%}*<D3zFJ)wjQ5`-l)|4*Bx2DcN`?63lLSaL4Vyk{@xgB#gFT!gveM;tC-Sfy`uzFJtC8@p?qkhaRrBNZ*b3F6{MPM0qw6Keh>$PuC9^-U(GOqS+kQIm&?SoFe=bQV?aP8pA43E)lmaIz|<7qcpFk%Fo#>{VS)2L&Ap)m)*HV)yR(+)Hr{4d%%Upd7_7q7WB#7Jd)^juEQ4la5-KBOV6-X6y`wv~q{vTbI+(MU1Cm%ptr{sAf|K(b5hRj?c_>ku<meM5=$4x72|tOV45J$_~0Q3JD+(>RYnpBk_8giH%uyquprR9aw{jIE3V<kKvtJ00*zU#8K)K$?uRWkg*l|HR$#oown9=cOzHisPNA1$Z$op<DfCR6OZ4<fdVdt3WFk{+Juc!^MrbL65zSc-IYqD9`RIFo%1s`9x$${bfekEd?Ien6E8JLla2*#ge+SFUa&~;11G@`NP-kTbrL8XCqH0ge;|DkAv)S~i5^sFW)-<s89_5>I~_O7?DKvC)5PO0{_WPBFyzeB-gBK=E3Q~-bOj(j3Pp!xYNTAsrKK@zoNnKR&RMi#TFN*aGt(_ITgk*^@{+d^d2Wds+Z4JZE8tB)(dXM+RPaky&D;oiom$@8F1?O+L`5#<35-E(d23(qT<%K0IrGo)Cb?eTyr6D!r(IUNiEctguj{}q16G;KI1R;&w06ZqsSfizE%=-NEJ}61Bi=!NBHY%G=dd6x-D)aZPL2*w15t+y74(a2QI(u4CT$rIW?;&K0BZhmgfl(W+ou}ghM01QN(ePH-~wof@{gMNfG}7JNgQ3f<&W*Fn9Vl@VJQ)0h&$|_CX$}G%Dj+;oJMW<BzxA0oIEi)glygu!+T83CM#l?P(24}6lZ%%YU@u-sTxpHn@xt1k3lqqo~blQk5^jDQaFa1Uf*b{W*BD^5fU@-51BqgGoLi0``JFE-g6vuTfY)I*4A<xqhW4Wbk;1~7tMRjG2|=0<|tK!u6J@8JS4URdn(RN1riior~?Q?YI8SU$9)-6g6^zXjl#~n)7R)so3OToyqi5F&G1et(kYl5N~$?;)@W-&?TI}h3{l3t1p?Qk7|dgGrR06Kr$cy?X1VIndZoFS?UCWg&tn{u2Jdg4wP}}C6ndC1g!G3dVeV4^SYzS`?nUY4luwSx-=_Gws_-~)cv!j!NR;a!6}LGx8;zfvf}#`U6cmLDC@AR5DJXsvQc&b`3aY|71udX>LnbS@t_y}jT9@~qPA-UmoRd#AM7eYW<vYhokA!=71{zzk$yf8buC0m;wM^7?!LZ3cRN5JT+ET1dMLwz02ozUFxGkvLfp<d8-Pa0S!CG>-Cz;0y5|+ABaHpK2G*u^Wb|}bex=CXnQT>EUewkVxn%dz9YvL;?4h2fXvKl?fwM>h**BhzH+v>Z$^W|1QG&Me_fqaPeQKWgei~&mraoY<yTk0cP4VvyM6msQOw<VdKYuTnMzd%)%%C`V!&Z&>1dP~p-<O2O$hPA{@rL6(V#oC#`vZ|7%8!~q2_+r(J23bHF2T3!(pC+ccnfSzA%Mid?MI+s+Yf0d|Ot#8@gC0EehBtOkMR4RXbKXw8a8vs(p2k4&c1Ve@{bampCy3XhOthPJ0xy-P#ik?8ENgUs)154y+7kXRo9Y`+&u=MjI?~iL6QAIgX1B?XV=qi5^nO{ws&9`Q&koraZ2wISA7ZDcQQ2!?Q+#&rlikC7b+EhhYX59+=Xi%+dZS0)MB>|>-QOJH18=JE&YKrs@4VPQd%b_WBdTZsnp4r*d<}dVEmzyPH6y~wt9vsPKYb7leR=cCXzw@h@$BnYJBQy{O}L5%-Z^g3-ez@Pwm04&Uz4UoTAaLk6<*9S!Yxc=)lgHV89;9)(M5(NLwq8upQ69F43Uetw45z=K;dtjqd1!GhiM%6NmV5I;-^W$B!P-a&7=($z0F<oIiX~7)fVkMsmz1T3dtm%179nfS_<BRg4W97Mxy#5mMi%JhAZavE78L$O&Z<NXTZbTideLiO%Y@Z!s9kUuR?)cT{~O5sIy7~%AwYiR@Y9N|KxP7rY>Yq*n5PouGgwD%YunjW<1g`eqt0tKdkWD*W&<|=PIwS`=C33P$7kdcu?sS)H(dna5e}fC91%=^b4=ay$px`&B2ID;hIvZI8I_@I}Kt_fR*X8IIeBL0vD4Y886SC_%I|kA-pgcRQ5`70D%<@K;MfS@~sz#II7qD)4CrW&Eo-5N8|#3BT)HkmU1?D@?p&<<4v@kV?3?deG=)~ZmEo^KBWgualVT=c<J9J5?;+@jL&6pZKQv!I9^l8!U!bVTOHXW9y}!GmO?N2yZXByPrSz6>BHZ>tF2iR9&C-&HY(TtJge|$YoNF!DKCdolhE@UmY60Ov5k?8U>++zt2Q5gS*twJ_nmkSRZ?^Dr1{|Cmw*0eKfbHh{&4cU)8GB>lqToze)nfzRI(kYTJwhp46sTiw>y*$P?6x{z=KLuamVz~zu3Q-RV#mv0!b1EB-Ec(YR2mpR73AR*&u#0pU_hYVwfd8wJi!x1sL*u4^S#<Vsf1Ye032}_!re>7+Pov#e#qay{puDFT^HDExUfK(Tsy|T}KfGI016=i9dV(3LoGG3(p^DtDZUMF%zay?TM@Y*C8;`9R65=4@?l%9~1v#vvTBLph}!n>H}}OS$Rd_gevuUxLMgnx4%j~8l;<*1AdfVc~?6@$Taf^h3o?#;G^T6<CnW<JIBX|FQ0vVOshNRd(}pKeI%fE9Hkh5Lf3Vwvc<z_Fvn&!e?Rx*+arHMR@lyDQmvfOle)07ozVD<=`mgW$=|s}+MU8uksoS9z-yBqxGknI9~FX(acwoo_%nlCInD2z@s$jfX%Oree!2tjf^)DustCDe?k9^?F-IppL4OP>?o~)Jxv=&o{jGBxLJ@suUy#nP#;KsGAhBvuMqsV~w7Me!a*fLRiqlMqajMXywis_XiF^!P|0aUzGK_F@B=OT`vk42Ks$Y3asWhiBs|d)R7hi%Y{tC@Pqy90yWY3PrV9hydqn}rtCf^3>xLWx-gl1GxI;;BTJfIR4^p2{q>TViO9)4d_K-Ko41M;E22r`y1Ab)2;E~v<p)i85<6MH2(d+~J6AV!sU(%cl2^3}_|{ll}PxBI(CDk#K{C}zPxtEk;IlxzXmblnz;xSLIkua9rB`uq)6ob6DY%K7+M>@m5Te?`?RGR~6%Ye(Ra&^r=(uU`tC_E+{qeFu0uQpd{hDFVnM1bToAiGhdXCma})Un0Sc4uxlIqTxhhhXf{vDi=LOVrs81*B2g@q_{8nU>#XsFm}J_3x?__>kCIy-WNNh$*NtU=qANI(Sw~x&<)jvjy4#5C&$hh##DKZ5Zu7!I{=D6ve_BrP66b@V9K6h^*m%_2h;}L>E#I$O2BV<O~&_0tF5iwAjXRa#W>XFqK&7mjc(Ql8_}Vvp2Lv$c9JMC=s)4;uB*}AP$)ppkXUwvm(-yGRf<NsaVb1%I5g4JQiwo<k%+#L4qz50YmysVt2V*b%LNG4Wnz1gJqH;1zG(Zgt3gMGDhF-v=d0=PNQprD#&KlR;UE6J#PNb4z=WO<rD%WCK_o|5HY?`3L@mYQMyq@t^8G;eEmn8XtPr0bA}^C*z5Eny7b88EFjhe<gSabcwxJlY>lnt2!~*Fq)L#W(7U#W04wZEBfY)CIr4|l8C!qTIF8<QOc*Lu(hLK#}%fwVaC#DoSUUwOE(ot4T5XGhoXbJPeAF(~Gz7!(;#)DF(lwi!$P>Eh)@9u)2nuf^=xNP~@DOpl%Y=_bHa;QE)!bn`1Xjz0zUGcHmLR(qNFufhq+gM9rvR=Z-F};%w-~W{*{sog931F*X=5J@LiupCw`Y_C}F0G1|R2&D+0;K%PW`6Q1Wv$&WSE*p8FPwV<$$)QEm@}@u;gHPpPzO&N9IU$MhY7wcu^3Ty^HWoxTbTmgDpj!%C9Qd2)b8Q+(p`eI5UaZ5w3<e@3m{So_&Hm!-U&P(FwwDVc|D>O+kI!cR3WpOUVw-0R(=2jehc*%av(?IzG5j+N(H6eDOLHD%KEJWvJkOxJ2R&%Y?Ms^Nyk@IbrB-_X6K5mh!f3^8${CAP<s(NbuUy68-*8_Mt7--KuC_T?jkJrWkJHQkpILL%Makd=ib0i7qXzlQ>K2bm&(FjtjYM5#HA4x=^p)3REo)u1Kej`0-1Hsb7dKb`$)?OL5c8wYH4(B=%fWW<Yhz$Pjr-!DCdb?`F!jmwotf?8;bU5^;*lw2t>-rk7;>?+SNvhRPlXlIYG$L26szg6_@>#iDny28K#I#9746{r(Q5&@^oXF&iVe(#zAjd<njE%R!%V-j)Og1Pef?ut>VCD$E{yvlsh6w>=pVN7FgG=*CTAEXgdr(ZEr=WzDLm{7&38S<k)kxqU2{i+Hh>wxwkc8_)F|{$J-HVWST7pl1}k9&U3t6U53o*xvs>l<m~l+*>1pV?}i-#46@G=hJzX8TN2u%4>@)#o3eZIaptd}KG$&boiUL(wrl0O(OIyQLr99ZYZac{dl9yH<xj~vm^;o?%<zH<f46M&*<x;bW5ReiBG;n@d&Ecl73!DxegfN-fE@FPqcYx>Py@Bx9-lyk`^H75C<062WTF=$__Et<l{31)wrElbjQKYy@+jArM7eNo37oDsD{{N0i*WLRQ?mdJ6GZqKg&6-d{(8M8<6e?%XEs9<h>l?K<ke?iFg#scqoYDd8C-rccRf5--%ar{e)ZYG0Y2XS-K&G0J-pDP|89!ocYNCj7dP}zD$7@IysNMpsjoai`72FEb$S7vPH%_N;F2CK=U?!I0tQ69_&TAtd-6_Wq8H@dBZ6s9y>RYLWC`vHfbZ(aPzHJxEI|S~4u<k^otYmFL3Bs}n{>0AXAOO@XkvdT^S+)9p?i9X5J(_%5B=ZI!J<Z9RDIy-S3v?pzA4?Xb1jNR33Qr}&#vJ68-PldrJtN|6D|tARNqjLdhw+o9X)b_59tU;B`-;Wi%<sA{L%1u!A*W2=0h-G-97e}*VG=}1v~r<Wg@+<Xr$gcQz@zu9npZoBo#{S6`7l}JCv|SJ?;HX+^f$#cTjQAAF;vtoaLI2YC+A8{h*K}ogfJJ1>=!BGiT&92)VaGvdOPyHiLv;&y>|gsWa}XkksgAyE{(=_Z9fREGj1QH(AxhXiSt5$l-Gk2pL{$BH9H2-pQ%x**x*%1>M3TI&4=ufs|Z@DbJxF$XXS^Ee6&b;Iph8*~=kn&*9KZ&Z79j3qjV&C!A+)Pj1y5o{wWx&`Fj5>!Y*1{pUMhzrs?7JFkyKpM|g8k$6UmqCE2)zI=cp8qMkK6ecO@=pbn25B3LGWk4oWgh+v22KX9c1!f(n!@$|WB%5IV73sFGON-qAwO^9})S7}`95X*Y5F$v35^M>60l|rPE?E^s!S&b=2?m3;5iglgq`i462wvmQD`DKtC?5Dj7KP%?FfC~`;vTF)?2lra?pjk26W9Zx*}i$Ya}&TgRc-}=ZYuy#SzO|Qc=lbLRqin7D=>@iU@5>nkZ0(9KJeN199SGB$?iOTJ0PKm;9AWl#)3reA_en124z?kgD)P8Mm)Ce9l@cBWDG*pepXdO`n|wd<xxNZ09#|vk(OL#s(mJ(p?Kj(dtU14(i@YXBVl$u96voPNM54QKw{%cq><=+p4{%xa2UzsC`k|fSrn%_n876Q!}K-nu4_-n4g;JECv8*&`JeUHsrCllfqK5Kl|8%{hk}sOWik#@GX=0DdKIF;3oT_7q{%aSbPjk&Pvpch(^08>4YIY9NoCUdFs+-(Vk#DdR!K_rZmiTP%)s%%90-dx0az;9N<ev}o$<VleuiW0B|F6S$LjSlXy|8}xSxX>MG90VvS8uPlGKHa%+D}6;<F04j{~n-{*c^}SWF4N_TJ&TTjd#wNAXFO77zI%s$`6hk2*LWRSJ?_E(sC~HTjZpAf~9$g3gHMNd?DQ+<ffGEGi`vN>djV9PLfx>ZN~cx@`{wisMW77A&7@Ol$g~(FQDj0zgi!usUCAIhzbV^4Kr@^x5rOum!5o`44rn3atC1=yive{3vo1IZ0QV6)o62zq<^zivwX04EH-d;@&T_M?iH#c`*|jycA5(PJ+`@htEFbJDwEF_mSK>KW#@H7v|+9XVnAQZ5-J2cIHPTvxhXEm58*>isAlhLQ$UhS~QMwdSw}Qn+cu>o<(%z5gNRUqtKfrW4g?UZ8kiM&;5%aM0@K6Eczftj7j&oUR#fqWxyQz{%m&=g}#_dGyR70yWF4-qUkh9mqf|ABfG5d>!X7=cp?i6P%yf!nuU?(Rso|$Sr2%!l8@Yx*Z^jD$XcZZ$+z*v=NzbH9E{Scs?W2P*p+p+vS4#_GN6zi&*o`L4&BDP9_|6O-lK!|BLrEndhP?43w=^{+udn3ct#cNS(N+teo@~GdTw>ikD*;tEM+o^yIm&B*e$TSY;uQQWma(8Ge?bCG^@(0g(I2VhJ#(u&Eja1JddL(?Q>Msazyt%j|O0LR{0CJqSj#S59bsAE6}2LLT_?==a&!&w@X|EvdQlvP$5s;n?M@Le=Y)jf?cbAlO4nZk93@vee0ip6ZqF1_KZhFtp3Gy0A0Iof~Da>zZ1}L>HgtgfcpIxbeETYeTrv5QPiJPGY)-kczfhi%s%yUD!oF%DRdl6DKx7TB$$Odzu4$Ff{}Qg$T^CcVlU`5Z7FG`Z1^~aXgiq*tQSs@e4JdiVkuTpPC~wXDpjI_`wJRz@uyKfM{=&2O3W3PY7q{PBjlXw%)6aLS$uU7yGd`U7SS%g)fV#t<O*W$juUF=Sun2w-R!D@a%x|Y0nM}t$x&RbU^~RnGQES8y@@-xaa=38HKoQVr#{ND3@$>C*5O%f$d6g9X*cl0RB7ZLxQe0B%EvRsh1FTyq)TA@%Br+nWaNdoNqcFS+v&9MD(my$#vfKY1to7wN@fVvo*QA+cikLdY5R@9_7^ljZOPGwWV4r*?m9|a8+E)+XF(l(`%Yjns!)wnaZT_Km6~%@_ilmW!9Wb|s{nMZ>;{vFmT_YQ#-ex<q8UQC^U8d9YJ%!b>rtB96@c6p0GZzDK>Ec%Xq;+dpll#P2=@DLzf+)qJm)ucXrWomyAjtg43t{z8@jurg^ixtv2QS<64>F!`?5NKUf%*BTh?H`n)TMOobW)N-)_Q?)U)5;!S7qO1t4H-s&Cq!$oG(Xr~Q^&7V4{($9E9K7cG5v9$)!~n_7riGa^u@)8{XsQ?ztmy;k@DXUsSJwRNJ(4<mMA(Y&OCsa-I<L2QPv6GPl+#ZbNr1~B%VaQu04w&9drE!W-&7ng`BxZoa^hp$y*C<meuc$1h*IHP5J{RoK_aeKqer2YCQ#Z5=Vjr^)w14C2db+y{H42O~SinN9&TQN%3XMMR5wsJr_s_LpJ2#oy+#dmpj`*K*Vi22sQauve}!W4a(!r#pSG&y+{Bx%zdLTyw5peYsW{-&WB)EJ#K<M(KuT6tMLTboGyR94AehBX7FSuKkFX>{c~8}+WvdYx9;s;Q|5YU#hFV;lr`HnUEJ<W7Ep=4@O!HM9_y2CGd9U1zfhXJql7SQ_2}k~zAlIw>G&=Tyt|kY&$~*IB3K+T-(Pv&rqta1g<Sx)97-71VsowWd1sBaEPe|8lg88@?E9h<5LHM7pJ==#>qP#mI1KFFBDx=NJLTP;e<o#+qcBL*hJb%Q|8F@m<|4QMcM<2HN&-($%mFVaCbC1FKQ{X=9W_6A_<~Z%y6c8M-bi6O7wtBI_+orLSLF1{f?pFSu9yZK-Ld#-^GZNR*DEv9y>whcz1uWMaM3)?;xA-s{VvqvUkIiWMD&3-tk1B6ZMuyC|3@6hr{M0XS&I{9m$a<^5k*<YN%z^O;j$@yhc1zseUfRLq)!xhaAyuLjIegIB`HuT+C#`44}`u*x!;ZJR1hr;1d`IJ!QLV413B5(8|M6qBS-JVQ<co2{maW-TxT+5;F6!eJrEv-Vm+RU9I$s)nkT$tPky*;Uv6GUvLyL>l@j%-5IU59A_&))rlnH^i`Mn{HXQX(n=nJqVL`m&Z{X9;LSveoT=Wqe}Wn6Wl-|mu455&(*puzlg=#0aCYAr60;I1@0?oWwj8vt_FP0p=5og-%XNN(aew2+ixhe!@@3Sp}DWKDeMMTtuz{FV>ixW6*t2l8BGIFPDB*%1S9@=Z|dwqemUn~bO`*>drtXZRPs?P#{Lb(bG?=UVeDpz-2?wd?R9P$Q5uOM>8K)3d{At$sCdqszTly!5w!WjF5H%d+xf!hcHxdJ+_4L5PgiTL-QHsB<&DikGIeST8!HNTK-;P<Y^*5Ut3wm)#ukM?&mNJ+G2xMM*5ZqE@5|p+f0sO{p8RguJbhS$ul3@eYk@U<(*hFEYXQ}1_U^jXYnk6Ub$3+ecTa1@VR4C(xoig8=Q+B9_|=%WK9_vqPCl=dOt%R=SzB#2JMGRo7<4f`g!QQ1$ETPt=tt{O2Y;MnNY75cpGDM_A#vsy_Z95Hj>F$dzKkyRw$5^4*0LtOb3B0@4!JTcchX>7(Lq5Ei8f6x_<-+;*m#Ec6zO~p^K+m|(e@pOL?=cxKnh!Ki|$Nk34Q<EG#<Dym|SS$5r4T<PfbmNB26sK+l*s)Mp{qBJb%Pu6A^A)?CrbV{N$+&72a|<3`$70V5g&iM4XpLL!TBxN6hOaIp&^sjGB($&-@#7;|%z+#eHtRELmGO4b~I~tO~B?(TCynjCA5MbB6Mk3vWPG+$ro-gKZ>M#zHKreEC$yV$wFqHm&v4t%8H%mF)@*XfCWhHpO&#!_qD<K1aGbII<gO`U(o7Se2J+iQ#ycN2Iy#2`qYrCq;DUM^qNs#ko~E)r$_dG6*>myEbp^t*6CS7~>W)G4M{PoNTk~7_4?h40=$?fL(ZqR%XSO9I=rn6!!!>j=mu)%3KX{Pb8SqOxgt8y5t8r_ni~+G0=o>b>XsFu=Vw1@z$7T`O7n~@ZumQ!tW|`+9<V>5T-{ViX|_t37MGAv*7Z=o4K2A95wyP$a$gjV|<w_e<;DPCi=h3k~dv)n6@4)6ed_lrhpBjW@cvNl-g9Xmjt7tt^qC_ANSgkucl*PASd4G;>6x?)8-m?nXPBjYSsDeiwn+4ZjPIbEk|B>^{e>nvZTZ5-!RQ&4vmob{#2VR`mKVRrK4qTEY`(_JkyH;+0K($!Lk&f?L3IwnYzOvgaZDArfQuOCnIOUkoOL~&N%R9Ftl4NBK<EAAhNzKLfozUJl8r!$Zhk~&3(t?%c60T3a7go7azt;L{?Yd*~_m<bIn;H|7w+-bQwe4s|!E@mGEVGcQ*CzEa<r2Za1syXNm3->O@p_wQv|rOa<$bDR~wwHU`S&Rg@(J2c0k^L2|~!zAB*+le@U>sh2sDi^Yf+GhOINx_RfpBuH<+nh#giR7kDMD=LNy9m{*#IeZ@Pqed>Lytx##LN6$D!#3Nejls%><=_tYXvO`Am4!ZPp9Za#*6CN#=u4E{<(Q1N6(o!4M_(yFJQi+f&*sUkMO6vR=Eo&Dav@LJ#)=44Zy-`*rxmC(++b)%m-(m542tBvZo?1+fW!Z4;Rd(4Hi_Wh@$IvK9?*6jEh5Op?pn$t&T`fw-P&?y)9I4;b2D`*Cyr`vZ%IFF){a8u5onC?@g^-@SJKwaTqt3+-;NZiYM!&jozRYEMZG%P$P^w|cDL2CU8+BUhvRya?b7v}1_sZ>3y}B%344aZ2Mn_+nt<$Kc2)Qx6Ze%LGB7L|&e2cd-k7m53`+{?@I1WSjV3(8wdLJ3i}b+p;$StN=F+08aV`yA>Uko+nAIYW`oyPa#!)Av&Kggg(vgZ$A;P;nblGR^T&qhrwb{VC0#UF={y}T<sy}~v3HUggu}Lsn!z*nAZ>Hf1hBvv!;uSWL=yEIqI&9(}c}4~_*u+2bH}roK|7bo8=_dVE@0&sAHtDarK03VF#6RjrQ-Jr5@UKj{qUZ_Q^(t>T#9M7XRLn%hO`YA+yJsPM3*l>sFOQ20UVHvUo!apd*gg@j&_E;d$~ry&lj5^G9PPu0*_?)+b8lvWOPlUM1fG>)*K&a*JXdRvmQA7k)yn`c4JS`@+oUY5)w!EJdLG4X$h(OK>hjDxjf}@}pwrN+v-3I|81EVkZ#aIL=K}LBjMkBVVGKtbXaxW6;NMLLzQez}j{RZ+mx1cyWR1pM(AW*YAt)_xG4J+>=I~ws(7}qVj$uf~w|K@I|CauK2fw|^XeYb?Hso`Q2ehz!8r3tz00JM7g8F#)b<4khXZlOv6Lwe%{)jU0r=dfKB<<G|<BC@@$i1I;jt3^_=0{B!XqS)9!R9-rS5nb`uG%=4$MwnY<FtyvYP!#a>MNLs@)frRzRuOlz4eBrNYrWcX{hg~xmQ6i`E{pDfZTx(*Mp$k4&abaE_3f$#y7^hZ^kB+D51PUlOS}K82WT)2#4nZ7H`n-;P)HT_$4Ubc~XTMHU2``hU;a_^w2}3)%cd^JHElU>*5>!<F<yUSO6jaSY{&XiKbBDtThD4QJ1tOtVs>(qpm`LwzpVACQ$xUKJsRZnPLYlqr-hyuod*q`C=MDL7&XF+s6v@nYVN;1od;6TbE#{9nWC_n&5jpV%?Op38w0^D22br(G1@{n!zW=s7YYv!3RlJ{*^pO8J?+8Fc~SO&6$V=LB1eoc8mwZ!FB<3WP(-|VAB2Cv>7460_k8*t<&MAmDn*Bb!sG@_(;HC0wm3mwXJo4WgAM$mv?6}iLU+OSFr{|#VOF{_lBet@CEr~t6&9YA>}fwmG0=3v)(+&CQ0^Iqk<L+@^@-A0`h3x^g|xUrU2?`xVfCkMoaIf1qFq!Nk0Ctp@KZ-r^9;J9C@O94Qy5eBYM_cUAAz8m^zZrP-?GLQpbfjbO|m|z?5E66~oR{kH0-Q16U8(WlaNU>}yBKp)SYb$bNJjhUHL~W4we><UC4w)SUbqMUX|;xgA-c;1$(^EWMU3y!n+J_;{)&82oa|@K^XQhCzx1NujFQ0@)PmR68%VO}SoB2s%JV^SMPGzoEE-l@gRkfL7NyKyph>ds|&NE8M)K*Jg=PA0mIjVt!+z#r<t8MY*@R+#B9134|Ky2Ez-=0=K#5T=V8os~&JRYH;iih-GYu*SC6kVycI-Jl4*Y7ft0&)-dp&ZWLw}g(QQZbwe^OSK8D<&{R5l6}wochRao<MgKM0^dYr!)LOOSmmFUP7YfvQbC-c^Xab*WYm&L1%K5ZphiHN0Xicnbvp-DD#-)3-Ea-Px*T7)pYcd<$P6FKNVm$sMK3X9ROEevmh)F{cUmCpzOOpMzfjS26M|@thA05BO3Eij;Z!#7d-U{Bx&Drq!HY+W-he~5jqx3S&0=V(dtt5p`gcV>BF_(e$&J@ZikyE_>oMGX{A-?7=Rz_V6-b2DBIIF7(zGYTpzjO*#t%G2;RprDxNlxo(wwxrP@$0m<0tE3RwBRj2b#fTwTp|pT|E(XP>Dsm|jFA6QZFbKGF^1=~6OxVOLmIZ+vX!P(4obr?<TB6OP9R|(3KfLn78JW<=lJGwN`Kn5#RWkI0MI<2@&^~4Ln4$Dn!S9na<38tnz6EkYf%6MyS{K6a?P~?&a45>EM06h+ND!g06yf0qbHhexY7(-T}vrb28z`dmvT_7zcAUgVtHS<>eq`G_=N<nxeh_^MbCvY$-%3NPwKM!e5$G+#g3}lk&Ba^d80;y0uJN^DPJ^A^?2mcnG<ei_BP6dc~YV(=lL%&h&C!w0F;T7F`;hwWXx7uT0MBTdN-^g9S!QxXcE8hk?{l8K6PApvm!7dGtBstDm&@-)w^%J2|nc>2gA-DzQQ|siR$~^u@_(XscH6yc$Jqb$aq1DLqvIe*`5lVw6a%bIc!Kd;m}X>)wX3dK!IUy?7AY^1VAobQ5I_ie~&TX4=-&zV+`pHEWC}hGC6okTg+9+1c?*W*!Fg|Oi&xCVNmLndM61(n5Wq`F8QAldX@N2f9!YW8IAyLzwx*(Iz0|fp>_QGBsw*$Xfk*une;-)$N<y0a4e_=*^*MwCtO0RA_p+3oQ9*gW2<Q}_6L_c;jIWkCW2+nOwPbo&YChRxHATqAX7D!4_)}7cRt}>bZQ?kwckgnksErek2^&f1pZ8c8-V$|g}c6tY43($KTzO?p(3BVf#gEkyP;%n(73_mpKFqER6*pXwD<uZ&{B%u*eS>aMUK#LyTid0<f*VbpYZ^{%Gq>=z6SV$x46!I<y)_BOIe0%hVz)uV0~ixH+STuX+TwbcOZLbO~=D{Aapw$HMP%GT&&Y+xp1Z{;1r=J0A;UNj8c{A^jcDb=O}R&;_I>aa4b-SpGJ@;1dvnGKz&P%=8`zTyQEOOd3OdNjB|{1tmmg=KlO5DF#32Pi_niJi$%W3q=Wf!K`xJs@p?+4L50aMx*jB;Q%vXz|BQPpW=?jMWDHZtAD)e=i17?Mh2HqeI-%Jph$~^m>8Qy-9Xi0PAo-TUKH?#+Y}A*~s9c0`7~omc^)i7Dj*fo6*I?zhoZChK21P5}3dUghv!)}8f6cio-Rl<t>h|hcV~v*$AY0H7H+Z|*evEv&Iq?rhqr^{tODbooJ?bu;0q{_SlJzLFV&E{KEc);^pmkj|%Ahy)yR@jatT!ooWUFbMAt3Ts!6^Oy9;iiF+nS;`Ov1v*?f9g6vn0lPMr~@LA;%It;K3K#>BiT3kNZT0=IjL3u)LU30)OC2;19U{ox-QN^_?7_{BWx8;PN>KiJ3bIpwbGVQfe0x`uy4&dmH-$el3*wHz3^%zXishBj93*?%Sa`IQ5h9*#*YT_D~g_-LmR@1_nRF$RT*;7$-_1Hmb6iEm7<rnp3Jv#}A!m-wN+?bcwN4&9bd#zt8wvA9`tO?F%k7k+y=UcP8y8(abL{<O&cO-dQ0b1v((tl_6{D47JI&WxfP&FfP0npoXiVSomSC@bK;^uMqa7LP(%8ose2^YNHDeNpKc(S4N7(C70qvwPeUc09Y(eK%@L2e~Ro~AN{}Vz1wmdNs=h|USE-gw$nn20E7!kQKTrDL`fx`rY=jeE-IOplLQh(mOvyL36KP<b!<LhAJ=Th_GR}I_U*jw!<;{vFW665zr;Nv6QHE(X*)A*T_Q3w!Xv^X!o%IeFE{~oY0JfENVr6svLcNN*C$@V5<XloG>N~OSZekxx=By6F;mnge_&DzP-mM4g}-au&7<yhLpF0){4k9*UQNsyouTSd090$Xq&Rd|?tlh<Fg;Ll>Ug)p2g62ftlo1^JWE2k@&W5)ZgeC=$3%L;^EZNJZG3X9%qB?DUrmPSgSe!tLwwPcZ}!Zh@7<#BON#2q&13~($YU73SzH2}Vj9M94!oXY>U2^l9w!%5zWFsiC)4RHzkULY<LisAY)KNePAlTeHL_o$bRJT}ju#H5RTvgSOuZTuRU`zxJkZTF66%9{xFc>$J!bipZU)%NUbkeIDn<+DZ|@(K0DTd)s3sM^iP6=6gI<yfpR^g1xmQpOj|!?X?)~KK+09oH9RNWQOzXPS5*zvrBLra7*&>P8im94M^h_w00BZ{Ac-|1u@5%$)rdX4uC@+umrYbKWIOTDAa8J^`C=A`Z`Z-M19FLaMd~Vpo{e(f5ffw#*@9zkEd~cts8Sj>Xchs_aZS^X@96d`dN+4A!848u;Hb>PTl0D6)t?N{^Sqd&pg9JNj8L`k!9thd-JbV5__vpzp*Oo^>d}Pw8*dbb6rnKhf7P6{}n3+b1PRT7Qspy+o^0SYN*e7{d!@D&0mXX1s`}f86BJ#cyr4cZQ(RMDBpt+_c0z9O1BbKL!`+cvvHsSr3SROSiYA?C9_pv;Hu9jX2g7`j`C(_l@832=GrX;=^9d`XZooZ@})PzW#Ij8nfv%v@z2f|%*KQXk1Bn<>i5S;K87#|3H%7<@B@s1S!vrK1yLS+RnGGS!VZnZt7vU##G8^Enud_ef{3PeN~<XhQ0Yrsx;myTD0(C|gP<!=*@#FuKqXKg?updS9<oyM$#f8#YObaVw@V=ftrpQRNnh$K0R`h{bdjT8UMIzg?-kbu*BQFq5SijwvIYel^|)a!NQRgwy>O4SW_)=X}~-s*qgoCveyy6Fd~5B@Ux)o=<4vW2$eK|m7?X;J}dqG91&-zZqYn1H4DFtPk!HEJq15!UGjOxe3-%vm@7J7F}iA_7S6t_8eX0=;X2FGsuFXWf>}D#-c=i*?7lv*^zeC0WldqNnL)sy}vZz8+*LPO10RDi;aK(5Tq*T*)n(lFu5^Zw;XZjAKs<qYtkJ*T-}AMX|4{?5}cJA=ktRw!YJylu$Qrpt*7{w!tfQ!qA=I&9CV|1C#Ka^gvXT>^Y-k9--jPpk37_PLZ$@C=+YeRBf@8-<A?D$*<lPu?7^ILWE+nn_{gtn1^nvMJZWiXv99XCgWQ$#@49I&u&u@pcYWsJ}N0Jd#*32<?IHwEVAn`5*oGm!HhZnR;47rKv&VB0D5{=@Ljky+;}g*H&|0rDFBztwX^CKbXzf#bT6icB*6PBg_5Z)@x>~0MFk|ZW>|PrE6r5h{JTkF$^(w@QdeqKPx><G|6}Qr@dZ+s3CGl!(+Xd2*RTR@<$jUHyqyx+VvYI1=A><L^VP(BVI^sdj2+`0VgA0EWy%}obGd=LQOnFm^r?jR*2N8X9fR{WzyE#tZplWsZ^3u_e7egI;8}l|O`|812_;#_bHC)om*$69q@0l0cKOw1h2|6bfaFi8$ZU=0ZBDkS(tSw_77`6LmC~=RKqga`f{kv(ez%ILZ)S3a3=*#X^2<lMnI31;Q!0!1V02fw)gZ?gDc!1#?{ovtkWK4m%(=-KK<R26-vWWwO@oiCFy${T_nK~lgqI$H-mo<D#&RmBRx@RGALNadjXtv<>OR(_ON4F>Lp`fn?bd@$wk5+E=o*r~!f!<fahT;D<gcL)>a}Bc)-Y-F`eW>>iXK%^b%&OhAgt+Pthp}AKHql9l@h{`CA6_z8us!*!e~s^#Js*+0mrIlJyrlQOL-uyS(>a3#i{1J@b8s-t>`IP8AN1|ZC<~C497wqOKA6WcmY$=b8e4unXs*;mYZ7?nWoP9W0@|rKf1X>s1fd|DZh1Frm2M8f^nhOC}~Wv>9OU^J8enF4QavUE~rZ>=DFSqMy#DGXHNfEHBw7kW7Y2iJW!Pw@x44MjAQ_MTxe)~+9wy$($9uvN3albMyG690DsW2)Ra!XbNDOEH`t&S!bf<^WM9<QzC^j?QV1lM871Oy5Du?>(`s2}nin5>KvFJIKe8WIQM)nRV9`r9Wd>(nK8b$aZv!EnU!}nAJ1a4n3^0o^#x>;l5z~CUJkKZhFkC(C0lAukPKZaVgeBWC@#q`LR%Y|%1l}2FDXsU)De~=|H%;Tfu>&ZWL##M+1TxpqWVKyI*4mx<{6}-z4*DC;;3wXjwH%C0XvT|40KPZW(25tNW%aT*G#$3(|9EzrMGnQk=^{6q|05T9fCT&8mF<*c4z-fOTB&X-Q8V4XQ-AoPcc!D^BEfx8EqktjHsLqcHgH8#J0`s%w3QB67V6u#pebsJ-wOP#XHkt}{XO>$&y;@v+8xOu{YTkWYQ;A63<#3H#@V43WW&Il@w-By(|g*AUgl_;8y%A^azt6!f#b~2XUTMw^-<^3JV>Syvc9mm23a4?OywnnvdI13a;QO2Q0ZVzrvmbom5i>-r1z7lZpoHDIbp))-gjmGmwrzwHYzr>LZ)^dF~60991&ctCs96<!U(ZyU<9swSMXQ09o883x84BZ-j_H<{$}_@R;}gDR`hm?4js6PrEzrcnGBJKk@Re9MpT-i*$Y{}kdXPyo?qfUmw3-5-W&2|zyRLUGLriQ8?rm(9j4@Ua%~F1Rr0f1Dcp_>W1^sJL`91d)M3OA<?^6Uh-8+YXq&=$GO2giI!;~@ICjb8+SA!_-`X~ebM)nLHwO<^yC_t;BA7Y8Ov9uN%(kdzg~RY{p-RvkK91RU0>QVy{u<d|@9OcxT2y*!|29MnK(Qc2$m#V}=$ckJ42|=%WPEa!74xISh>ARI@t4y%emWhb=ds4UZ@Xz&F2GDUcXy^^UxsFmI9aC2sk+`{4J|1>ZIpN=NljaX9WlsB(Zy*qSlSOr#&+KJtlh98R!+)Zz=T}{k-+M~S@ti}!UVZ^Gxz$GtzQ&~>GR2@>A4|;CEbnYrbTIpFaki2GHUNH%lG*=av6OS2$R;geM<r^_Qk~ZEU}6ZB}=cL&0LdDLBTj{(<yGfQ{f^?A=G%>k0Rd&G&10AqMBEf#p8zjR)jMuunUwp4pW#N_Y;`w`VGZu!T*o&KbTo(yWGW(+E=yVe2>Es+nfstrBdX@LwBNTNo{cNElBwaPE%Ye;6gM>o4!!Mm?<>0euEyGirkRPSc7OzgL`7Lxe+hMmFoFG+pL<$rqS`C2~9Wg$!)r=TDFB(Bj~#(cOvlSQDy}WG$<Yy$gBdNS5U8j_2TXKi^EHJTgBlbj4`nhK_hZsP26|FJakozl~te>nDF~m&^4|Vbn}%7-6=ZxHlRye3<jgHkH)7f1aD^zw~hY`QLqyhxr-MoWNsgF=y<ZZ+)h~T#<pH(gVl$`x@&k%iZ2as&VEiVQ#y@9j*s#Vc$!~{ScAe*N*xkA#MZ$%5ZgSwch$O$7s}?*Y;1XrgO!(==IIomQ$`_iJ~hf14Kel=v-J79FT#Hn1*zQRf`s{7U4L-5qxmKNqGn2fm3^sh<*C*#m@T#gWU9Rq*bA*}uvdxmJXs0Gs%i|Y{W19J>i|wF`sb1{UcrbI5UqUn^|nHXp9ZJYFWbljZVIS2dDELrbP?m`I?@wKO?y7H_a=j+-!??>W(V$GS>{ixcRsvdR>1rE4mqO#Ye3{E`ZIYtM`~gsj-63NNq?5Zqi~|;IZ}dtvACe>(8!VNA}PPUnpmIKQiE7<H_8oV%r-WvbU>yp(S?AV&M?fZ4!&(QicXRC^*gsSDXWED5S0us(ee1T@c;JROX+KJO<#TVtZR*WE49*<FtIZ2=$qxnrR0}HRUYcG#MZE`Y*#~F<B=X;Yz@__;iVvTGs5a-^=QoYmH+de`B60GeEj^K6~?#Vm_I`1!h^abB#?H-6$vJg;zUy;KZ@Kf-#M{qJ?)qglGf6TnQmN$zSjJJ>MHFctYvB2-otseLI+^rk)QJM!9@@0qU{QH*YG6Yu-dvS4gO(yciL?yszqANf2Pj<fNYo1!d+lIx|>$?ki~d>q$0<_!BbcUypN+zjGz!xTn#_MjQd)~x^V)p9AvZpQwr3r@^YI&Q!ojAF-oSX%Eg@@=2z+Lfbv7~d4gsO*rFAh1u7n97uo!m_ofyv7?=gyxQ<1p`;y=-SY|29SafEX%?loY8q9aL6|;L>Xv!a>*M!ki;W?qK8jWgLa*giC0tP8I^tn@6dFfX6#`ls|3<fN|DF+3^JiTF1TMCqzZ7$iT-S}D@RQrlP46=)2H~JvMH4ko-Ew$ksyK6qEq#(&`@~%JM4S4LMhcC=P2R8t$MI8X(o?n=vzet$qGrJy49X((bOc-&o8`w~49K0oWjqTacNl|fq?aCkKd!CnF<9EZPsu#PONHk0j68yqMqT!P0UH!A+Qs`a%Q%#U{Ht#ymRw;EB?>f)2luO}vy*Dzq$9HBvxnll9nsXv<wW7$;W0(J^IT-Ov{@XC3+U(N54I_ljF8!;L)8Og5%YPbf2#j6B+sbj<+Eu?S?EmT_U!ESj>X%A!Bd0GglLiyK8*)%k7l*sPshuR^yOC>gcgsoe69HwowgJt`^-Zc1EDN_-r3#{ab=Bo3vx``#5@HHaT_e97#b&ah75zbXE;AERb#W{a>vb@|DB4`%$7~WPpAD{KGmFu?wUC4*RW)^oSXDQ0(P&~?eSTAl@&E)A_v-W8ib)8-FlR%Lq-0t`qcG=3eLpIhr~m+K#?<#$Wm6Y`V9wz=?RxyTEY}c)C42$Y-ib>%ORhLA<BIr%(|tFMqpBG<&iD1LfexBzWj|R=_e&!qx(ypf3H5U``XlCzoI|+@Fj;qo`FH@V!Zd|buDIjnSVSs(l%1XB6WP+fnU7RZ3FwzE-A%{IWPe6=-@(ty9y-M^iDC-|&q;(H_1g5m7%2P<_|xaJSw5@Z;cijjFd%ktPUq1WLm0NAqjUfQcf>#=GAxcjIO~t{yhx)Y!b~PJ`T4Jl1O<oIo!ARnxE~Ceh~sKaZZ<lNUd-_ffkT?sp=bM#;2(Y4oek@XKW(+RXxt2h{Cl|Hb;fowN)f4YT$5ymA5p>thJX%h^l3(86d2HagfdV*MCV><CXM5rF&b=jf;&z^LcyzwF^VPzFibua-6?D2bQbMH=UVDa5ME~Ydaji84EVqO0E^f{#;{e4VVBwwImZ}N8+erc4^3Gg@OiJ>(2pH_Y=3NU(d2sngI&@tXat6|lk~}3y?u|{P~tyJ|NHH|?4dxDH{`u+W4~vq09XS6m418J+hfsR4hkgteYGHrmkkg4hin5Cm~x1^A_yGD%hHM}ou~i(<Ho)kdn;gq9s=3*DjA_3K7Ut9Ed)Fh_rK*Z!S$qZ);L*C(|G^U?<#E8K2mIaTTcXrH_pV5cn`j}psV#n|2%6X>a(Cl@M-U}o<j!xDP2bSF#2#u4eL(hj^I$>m*PF(H*pp4m)M0nA7k8yAE5rnee8E#K1tm3gLzKbQ36MRsdTXKo<tJOg3C~Y2&_E;La#VjQ{o*==e`38XPEb>=mu<5@ktFpzGw(A4WnlUQTB56*;YXmv1Fg9A(7a--MjU=B98H0{<+u?ukP06i%#rZR$&wS-f>Ux?{3GYEB@8K<77Vtu`C;;`)0#NLwjD2Y2o3T3+`3y$%m_r4UJa450bk**j#(Ju6M@uKJPh1q5x7j1t9eIp~fS>K&YxDjt~mMpNC!gV}8wUaGBgZ+!rW--`3{^eqPAW3-}!jW4~XgcJFpKumPAp#_UFB&D=(|Fm;S|04zSngkHdIvSAwWV3`|H=Ef-F&ymW>4hz)cruDkDUN<OZXkh1kwtcnsKd2Cc-j9!s3p_zo$iYV7*T>MN44r@CFbE$47Y_aB=Y|DGQ11(e;`4K`=;tye44tt1@~j{RrGDA?4Ho`o(>Qtr#zFv4v$3&X$(WT_7HW?TwH+=ol1X}S(Yxy^BhRk)E3{vK`x~n6&X)TXN-ip61&d^UZNGiXnbS2*-1Do35m>>Q34dxjA7fY5wqLCU{oCK}+;McE$el|K=$*&iyQ(V>^(s2M2HeEEv_#q;o4BajA0O_YUH|#d_^QLNI{0c?G1o!^wO{e=&wqv=RjiRZL+yhq0MStQX+*Cm*zlSGyvJ4^03n3f0$V{kJK#p1%vq0CzoEP>co$*{X6FNC<ms`3Bto4JRLTe~02xur&oTUYNuctZgE4f2RLLbVFQB&45JjqoHmCk}F$XHQMpWq8tI4W@;#!bx&D_gEvUaqCtOB(N-<<K?vU3%YO^)+%HjuHB)bJl7mW1B|=c9EazpUY~pOcBX9UTe4$}}S)#5~1Ek`24o#~Fbz`Y4lDR>HMoFL|)V{D`Q#`JPr8>bIG3T}sgb%#w`x4YQbFj|d<J{L9Q+_$#~%go%me^jz6rAJOc@a*pg+y^ea1m)x!zmDGsb{G89m1N|PY9S1F6>u4Zz*LrFg*x8jhGSsQN0zvW>CQf{vCX-#`Ru?fv7rLs@s|lA0PNJ>|=(OrxaV-h6$tb53pIW~TxZI_G^_%2+m;SBP3cbu{*-bu~C*xm_QLsILBlp%c1}|9zB?L@egZPh`ziT%&{o#h7zw1*@n+|G4O32cU%#LLc7eb5!hAtCZZ6~-nC8`h8PE)f~jGgvxLl^t`c&$7gH|$taj9a`OP49(q%UlGW*Uc-s{e^}MlP|G?wVfT3Vr*kAx0(D~InCG>yWwy}Fg)Bd?D_@$*3K}_AS&vFq8OD9wmcNk+U5;o<po2Do^oZ)#J@~mnzbAu^EDj^v;SZd<C<NUcl6cd*8Mc9{Jq!DYPUnVz%plP8NXaRyV5FXQkPYGW!>&7Z2e2H+gyLGd-1jQmDl>0U35j_9DVohp@qgb`X9r)-->=t&we=UqPN>mS$Z|iXY=U!<UE_CQJr(uo?PY4cS(U6>7JpxKjwbM19&4kNXFSTofYvP&^cVR=Xg@d6PARZLi85%I04a;@9{d~-7G(Milg2m@ES`$T?~hqF~|O*uBujiel;1S*H)$j|1&C7t*?x>a^UKF33U6r3m)|{4A_B-ACN+M06`26R)F`x@>#H3ncbQ1w4>`qI@3l3%j9Yo!#i#7@amst^Zp23=z81yVjxnE??%0z3f9Njv38>mI@aY5{EJ~G_{v;ygBQts^VI;vSdf$)4)DSh%H$U7NEPP=$nF%Z6@G20Umg9jBi@=+>B476u>-Fc<9UXDm`Ni#vpYfNx)t3}gqqniAl3NeVYEp<e2I*5?Ve$RKR7Qo(cimcz982Nc-eJccJXD;dD&AokI+j6l3wgb3F7B&MA>?i51aJ6L%(;R$X#p#A39z7(hET1NbCryV?f$6AU&`k^{OCs8B*7Pv~57@aAyUi%_>MehSW14-8Uh1Oh{WMq|fG3z?+ZYVt5Bze44Tm<uJco9wi{dCiJQS3jveH4U?I@N`@kF_&x1w%bpqnfW@Fsbm=<61JMcr?%iV5Ax3DW4`q|6C6S$^yoS0U?Sr9y<~>q}HZjFVietG8oiYm0v^Q1!Q+l^al~`OHl3k-)broU{^Ze73`L91t>*+FWM1688ka(m(%p`r#YaCrOf^zUfD^P|@U7#Zibj$)bx<FSJ=zg@5!P#+Nhro3Ym+;?>9rSfb0bhsXJ#1C}x)Hy$t@L903#)V*@bkU?`76({7XDNKEo=yLMm~7(KobY9ixos&r6e)}RTqe#A*PDQGEM9b{(NufqYy#jHCpfvueq>Mg7P==YqaAP;C}JsSp!7{pr`;86%L9DLQw&TDVFNjjre8CwhQcdfh`Tuz`ei@4wq(=3+y<*$AlEcHI=nWV8{9W5=#)YYpWUFHTH?(?3dztkDq8c7fbPkBoW&ej~${`%{n#5ix539mg1>HPdDPJ`_X8GcFsaJLOX9E8+kyDEL0;sZe(FKvalLi1RLSr!Qkm>o1d0@#^!DU?#yjFwAvV2Z485LQ0HJZ^3#3miRpuW3>>sUB7ok)*_b%HS#nW7A0NzNWnC7>Gt8lke{8CHNx3qyREyOf$D?GB&bVUhr{_l}&wn{Re);6t^CQu7{!&n}<9sper}fK1G+`AHT@e5;3sXzOC4hh7uViq9Rw4w7KOVe&{qEJ_^V8##CnrB1$Mzu)qCzVr%aqzr#}WP7t;w1S?5oKzKg`du?btC8(z+@0a&B0OjTc8xet7--&B;o93=4_ta(oQe!^iN}_;|4zAH#L=F=YY4#E4v3*3gpqJn4_b$gmQwhgBtpb_ozjK1twMAc!7OK;wr&@%O`5Z~n3pJ%`Xt06_w<#1M606^_JfEF0K}gss;~oH|bDyo_Yed?9|<LNr&aYsr0fQC$E8^6CO8iC33E5xlwth~D7>WvXbrpCQ3iO3;o3(oZIr32wVV-d~V856s5%F<JIJUA`LBYv<!87pj>{Lezt^QvAev2l)i;6{QAPoLnR-dxh$?tMu%A+=W%}dz8RY1_FD6M%%Lma8Aj1I!bm~l5RwliJCt}pN(FekM%k;<Zmpu7t$YA_T)=D5(Pznvy10rLhAKAofI%9_1fF#$EPXd_>_dy(?vF!*X#@lyzv}d%2NXucCU?s)<6B}61aJsYJ3(cgJ7}E(tbv-N7?ykigxIUQkrFx=rZm1qU02oz5f!Hy77`~!dqD1fw#D*1Fvx<%h!uZ1|sAIaV^o}^x|@ANIl%<rP&eVt<e*F%g`^)u9&aQzL@We#cY`L(<7r#mpSE{%_enI*GSz!(aY>k#QmVxMt>si2fa4>6N!E>6r)3t-4Xh3VhLC0skCK5CJGUS&R=PNvrZifMQ{5jYh4V#(Ym+{t&7Xxy0{Fki_7r32u_7u9@NO<6xg(qFKEblkdO0O$#?du4VK{M7l81^`3S9E%L-he+4EQ$S^M8dKyxpWY1!v%5MeRYT-o>jIGe8e{!=n8`#epGqN@5BFXc`~Kv<l;w240iX5<b)q>16smpVhCAWp`Xz+y!*OrN0FCOn{_LKg+_`xJ*|bIZ`HtHMup;m!^g+Y!P3-NNXs70JS|yh)X|O;y@nVf4a^G~@?VtV>lo+p+EH3d2ALwoSaRQ>w8HLu$ZK8r(?`(D4?V%HE@*MwG-7c-sMZ00_s?;8IP|D28rphoNxFMgt00$MI<(+YID^1w@**%(A)X=O3nNJgc~{I7fn)B2%wQlG(S=BS0^;=pnwdgV%_Kk`<I3)u{gvFt-&`)H9?YEtF!_qDD8lx_ZKtj8x_(cEdLj;D;Q<-Hy=&U;4>xP!=%BsNBJY>D1OZK+RNBl)cAg!!QN^P>v>h=nm>0F*<&Cx+rn;(8P^5G$VoIy?fE|6v#GUjV?PnyAj=RN7}?7`n5^-_tC+VXVC%11!&5<kb`9E%(v0O(0q5o^F6|tTBt&R1t!LDjX@ZBG^i!(wt6-qdDkY>C+-es+R<$XOB=+aO<Vi{(VLx6=>t+p;}*hZD54_lM(!$(uDeBMAlsbPz0<WrWC@zc?QPZ(TEn2?0zU}g0UDBYoG4e4Gh1WIy1Q2NQ8Oy3j6|w~kYY^I@+m8s9vlT*RLIF$TAdZ8M1((%JID%LoX{D0g**E|?(^iF>{QZeowK$K(fLEKfu^|z0Lh!NKT#tXyq>E7weRf24RvI+jal!)d+s&G{tESwcyt<6XNN}Br3A^?@4H;LYSu;91gpR91k<SApaxs|Z`FxGvcks0fX|Ztrx(ESKuO@{PhZSnyTUVc%BI4yTueZlZ}yy~ezKY(Hc2AhJthx3cDE3zO_=H~B{A8?q$RDb?bxf<^{eshG;tq^^V_S{3)O0G@!WBunb-<}%xh{m>~N%o`XHaz-!!1tu^%p3mhC!ayA@@7PT8I+Ywk{Ub9^#OCdGJx8uf@TmG5yvNO6N4vC_oZk2Z-2?Z?RgBP^meTy*58IIwhwv$U9`xGymD6`xDYlt6uh8$nx&PJp<+ytdGPh!;dZ1=_)DlV3zD26A3r3*<DSE#y{ck8N%ls1og5!w&JGUO&Mtv*(>}rktbB82feLn4x*$a6}@e4SK4H9GC1!-Jsb1GRFr}m9&VO7|;Z`;PY{QMTsQQF#KLW2MYVW1)er!R*+#BTCk^Lg5I>meZ}_9o>hT{PR)zRomS<?_L;WX6Lbtt3hTob^QrdPBNvip+2vBw?cGI^w&V2an#rh9DuNBS$%JofiwGZXt_?o@_^}&XFzA09b}x5`E^Kb&8mP-<$s`xA0%-kEyjo`%yas&S;O$_Sd$EJ}7z~k^K+2@FA(MZ}FBS);`7UQQ?U$?@%;84C1|rzCu!S*I1S||-l#6LJUR-38d{IRGWin}==i>n#3n9D;0@h{5gV>ZE#tBZO?lmDfmPkYa2MZCJO7KIW>0EpS2JH=vf-JDtCXA@K$UiNk6fGFWgL^n2SolcDt}+<>3o&sx{Bxa&%~;M<SS;t@`g^RHFJ8TbgRQPw);4v&zZqE8LIolKuHRy}%cqQ7iMzHCxwXaHDGu%k-3;%DHt&e8y(7A-cLcUgvoDxWZ%5qUsoYMh7eYrYe`6t7d#t--iz5z!)x3g$NrdA5wo8bmz=LRRcic^Lt@*KQ;(u&%K$Fnjj2lXBx=YlkZ2RM>!VjDp4Wp)T#nJ$`9{)`TA9uz$`NV4lTL=YP@okv#IUF1yUqx@H$zK;~^zP|V^DvvI5qr(kA#YLy)`X7F(gC^`nClr<tEFm!MH)~|N%AffEFm^QLAR7Jq)#)0l2%KgUwYQ6#&P=jp<(M)#HqCzdx{&QONzU-h2g5vdJT%;sP}on?Zlo|$(TuIJI2W}or!p&*j?UD?T!>?gkk}ndLYwuwjLP3L_c81C@3zg{jyWdQwff0lua^<$H!xOuuUs=lWZfjqS3DhySx+N#5#%-Q;=hd8FsCXBUGX>i)c6Cv;d?vb3{Dga2&oJm?ZS9G6gae-B_0<gmbkbdi1_`Uo3?NHQ|kHM!FTv#~P#iNe!;o>N1zv?YekJ%$#I)pO^y3^`iB&o@!9g5jnk4T@G-A2)1<y^wc3>p9#GHS&sx^rj9XP?}SSUT=5~r`pz9X3ji<1P*)LVITF%o;BS{Ow*@!p5ayB{Bf;UcFd-E{4FW6oy(Qgw#F?wDx`MbY4q@$n<EyFi8>Fz#^IP1ceBCgNs|oCJ-#i-vI{B)>7!%<D3gaKIfI8gqb$Xi2=d<h#Sj+(4y>G@1kp339AoM?)_d)*G^{xvqli3mlJpYc$`C@caehJ)Gxu47~y5IhTT_N6L{rqE1%70!a{(+Z?YhD?e*Jb8Km!;F^V{CJCjSI3>cY`+gl3T&g{}W%51+K-stFSdMzdnEERS~JUlXHu6kaKchNEAY<t`^?bzy1g}$qQh|Y<OqQCf88y3*#J9ov#)5U!b>NSE*dCF18iTj^;RYb4J4dZFIF3*ZbI#-I(X?w(T-nU$kASFA@yEExW?%#Z6}4DJ#3JUKH0rn_DI7#UKwZP-2ctDM9uksp4SmM%UDCSUQc+YV6bP(rs3sl9n9}0t`H$Ex<vqucG++>mq&EvhoUt1?sirX^^Y}VzCk&*{I?!O}GOeIb=)rBN2}TKdAs$np$ke*?8_s5a3V%!=JXAVjb}-v<4W`deYN3;@;Pkn$~3+E99hGbht_|^15YWQI>VOVYpX%w)YKfnfchTncUSvl2u}8lu&H2jE|z-HCHtw1;<@In@%&jghF3z3`hH5hK-nI+#cT{w7Pu2$+NP8<+gb~b_|ZWjOnNuC?YJaDIUhtbfAKh%G%jvAnlT$U#63JQD^Ji*f(SjK@lgUIE~2|S#>D3Xsiq^Wk%fDsR{vq9Si|~wp<%PIEMV_T4?6(LT9WGOZ~xe8{$~=6leciN6yDU{W9I7=^HgqF}emI>rvF}wh=0fn}0u!dK6N{@cPmn^g{DIH9{Q0t{z=CV4Pm+&%a_g8!UR4{&>L|5M@mQLU+J*DtnK*NmniKcMl3Z6i`?fjBhsfMIkquKw+k6DgHW}*X=M&*r#TM4n^0l9UxbIL?n?B$l2qrF;gAqcxkeXgC1qZi}Lsf%XP-L^v1WW9^Wr3$A>Ob%h33K35<^h_e&#Ms_{85{IGo@w$kMMI3=5-`(1Bp3wE+9fUlDU;VBr7ux%w8D`L9i6;<4_9jk1;ps*3)8paS!_KcUKN&=Q32V%a&YX*8r*05DIJE59_QR<dQ$1qWk3i&3%Xhxf&$tdtL4mv%Q?jxW@!Cf@EuHHk=svj-QB|lo;dcBX9;nfcBE7!V-A|x%kALdgPW)&!^Pa|RE+K;MOpj5b!F4GJbY6eOv$lp0@!deSERM1)p?yESER41_mz)5#&0<F(-Gq?iO5FwgidV11Ttc7Q`IN;&w$<fi1_oq*PeDUJ>QA2YBu`W)}7}v@#4lSSySPOl|ULBl1J9_eS;NV|Op~C~sp8!Po)6ij88ZxR%LkCT1a7>g2M?7iBcqR?B9lH9lNX}LC+EqiM)>>LzUoj@5SGp<X2(?aATGOziDK+XZY)D@;uV~1?>K8UeL1@;)A5YsCwnH&&)@nzri`DHsKYUJ3r@{6x5{`B}hbN3SVzNep>jxIf4Ka$F3eMT>t*xG6=kE17+<ag;?`aP~5%L6T|M=$k)emo;KRbQ(=A^_UZmsrY6rj#FlMT^+ynY9cU%ov$33zY*&f)lXBRlYQBboz@T?OoOh%OA!Ls&^QKfL=fC=qyaPe?N8L;VyLF6E*7Eayim4bb_Q6SbRIZevob!sockAS+gJN~vyK0_Z^%<5G!kxKElA+3zLUu;1!E?m(gaXuspVW51ItQm?CL@83LmEy((J#(7qP4IHe9cO5DwmK2qmi%k|fCs39>$#E^5r+H{O7!r19A*l7NLNjKC%6Bk12LZ?#TD0pNVU{d~+Kktg(`fWZAulw0=l;~4hvx0vowRdz#?JleQlmB}$_lC^2Vzc<8DB|#=gHA7y3m-LhlO&E1m4T-gUPp`h^ydm#miz^jagqsqWLeY`FAd^o$qgKv^!tlx-;NHHz&jSc4W>=6hw;tYEP2EABJOpF?!7Tio#*QM8UZ_x|}njBD9!dGK0i;y`x*JnbteG5lMF3ckd8#<BEAz9LCm(-U^-7DzPV|VJ!sPX*<u4^ZvV>V^*MtHy6c_s0gPnRg;aVMtanmo7v<InFOq^3ml<W_bu5CtgZ`8o>%uB8yBq6X(;H`7N!TQYa`LA#Re@9=z3%wj<@B%sRk!6;^3Ct1(70xS};pq8fD()q%aeu8c~m=j~9n;pPV$Lhd-+KJwJRgS6|X`^WLz!<8SPeB^`%Sx9d1AlrQPHX@*+e@wax#l8!?uiVeDU$7z**(OS{M#>&Ow6fIjVQ0#V{m(B{e?z|zvtm^!cQ?#V>SZvMCf0^*}Sw~iU{p95N(W@tir|*uQA3r}iRxuWZzrtyejX&*1!1d#GBnMCIYU|(a9_BNri%a^(_NZ(z(B1loQrqI3LNlVL0GZcNoW^$aSp;QF0XhAAK2LV>(P-xW1F|>a+q)gR8MZ0uiN?%k&~iXE)9%V<E-+o%DO67`vi`2w%!3Zy5A#*weY+XHI%H#n`&KjC+reh~`E;7jPS0lf<R-P65x)1_?~dI}kIi?*mAr*Cvzhy<88kcC)f!B5ZZ`Fm=l!lTH%1q>x@I#S6KS0-*^Icj-VHRfWyTY*oAJJ>X3*$BBW;V8uoHO`4=9RqcrebUKl06EVF`(LZ1sJPt!@OB8T#SToha+SM;G}Z-DQJ|OVOL?vzusWIR7;i>>cC@@0|{(Pfp8Df+Ng7pdd{tQ=m?1Ru#@Y+Td<DQI%x>yQ=@x!e^JL2~44D`N0Cy=Aw#rO*BYZ2=kSg7iiWX&eHLCc`EbO!C)HpAaS`=e4eEJPv&Q~71%~Epw5n+jsh?4-?Qlgb_j6BmNYU^fHzW!LOZ{R9CAkunE`(eU0wp~JR@b$3k;oAFOy8^ju{{1g>zV0A!0V+jVt}Oz81yLCXzc18S;pesr;M`fb)emwm0p&NvQa;s-nmZ4K+7+?3#n=%)IBjf-@w)Y7Np$T!PtkIzB@7kOC_<qOMi-%4yNK7odUMMc{VglTl@rmv$90@ZeEg(ZDf(!WFA-=q>LZdOb2EOtXrSNyDxLRV*n84`CT*i-VzGH6laFO5vkkC&i~aMv&6)`H;s0_u2DzCofM=o*$nWwX#BfKKSwQ@btx#gXh7oPY<8Jd1f-)ypreSYe%$=Y&vTePtqT!37ZMkr4#6min^ffReZgnRk8hm=yZpUzfNz*s`{N-gNE_;@a>UcCr+QfI*I-ksj=&~v874r=fyiY@p!SuL7ZC@tl3%~XkoV>eNYod#W-3s$A%QIWK?G~<wDqZJ=n|SDsBYfbXLQ`d%l%$x?wmj03IYku&?T;v-~#^57dn5+uI>Z_U!o&-J>VZU=;!d1MZuAlQz3vat~ay0*V{J*6giS2aSaG?a0#DnFaxKW)7$#2KFOCJa{1QIVmHFMjogr-PqVJ{?ow8-Ho_wKpl4JU;6!$e!py})^>HfGKKX$G<S`j&5|qO26&I17vHfVMTD2Bn9nDAk<Fmr^{ZJnPYVwE7M-Qg*;IrGKzr2hW3|t$o3lp_)4wQ`t&k$>2G=eOqF~Br+4bh|vd)6FK#r2EWmS-@$wI3ZD>fdU+>|7X`P<=B=*<96iSO$bX}n0$R`Qt%er$%bGa%azH*y@C!*vEgrd+jHd)W$hRrpTnJ6r8)xRREARWEuR-+~>CyN(N@=a~H!4H>?U+Z-Nav&3=&L^m`Jt57f*ZCDDXTi?^Jk~Bp>)(|#D$(1S!KDuBhQX2(!@$l7~=f_mY+)nmgHtgW8*uj_-0-e3<8__X|3vq->JAL=2m6a7cQu171up<p!SJjTx0DJ3!0_ujK;E#6glnnIzFX>V-|H@qaaa6<KH4qp03lvOenRfk9)$sszMDz~~^&_%G?zfgHwtw+}l;trF3tA&i{>$-W7&c3Q{3-ylGh7Fva^#Wl=*1U<lWso}8a;n8G$A%4u=@AT#4Fk@C!8sxssbycLn+WqqwL#uK(>ZG@D|?JgO`3WwOF6sEflQ23L=QG7QoA|m;vd0Qgf`^Zwp5|RB2Rt=b3|3(Ny?K!o12<MfF)Jr^!4bMdTwK634r00?h|XIS`BuBA(s)BlNi_Fqix!8lsyEzYsBSQHa^+^snZrs0A4*ix?lNr57L)<M-pEgVQI6?_NHkbK>or=clh<z4`I@RK2(BYRQQk-3zyB%1362{$f1FI0abd#nIb0Ck}KtP(;jQI*Lw!2)_B@5RW5$j5PFpC!b?w4Lp5v@Rx55zeEPKO*caq>+&u&r03Efw6^FWE4OS1t1sU#ZpggwLiSBG_U!g65EvSDBV;{bG9Q+Ue3@WgE?}3ig@HIDh=;X+-KHC^7U0{gGVDD?mBbK|FEN5*8jdiTOrs++R?2^_y)R#Tfb^F+upV<OB;;{=ku@nW-87kD5DPPQq>LAdQ6hEFNNYCC+<m5wlspDbiN@13@Xh`y>YH&w%xZx<f1XaG(D(IQPOUa~b|<;~;P|?uW5wa|bqlP!-U4&YSZ=Yt{8?xOY&h)IRZU4&QK8SFgom(7do3Vohz?kzKWDRah$@;0ZC}R8(or~Gsqe57Y+DRL628w0X)Cf28ligp@254XSb$%?_$(!XNvGG<7JO&#VT0=?r&qpfsVekfXPrXrH41gRRH)~frvKrp3eP&|A52$aEpMwrc#r8Fwb_aeVcnx5qxmT6KI72MBIu~tSW*2?m(ymSUy3vwvABc68zoU(l&;5rXg<!TRUQ7Pi;I8Kz5XY^+yC@OWa3m8Y^Zw%f<oD#Px9mbEKMi%t818_CH!~OVC}Ki7CT8$&@~21a6Z8+^nbx8%F%bV6i=K}@ajf9cI=#M{iOiWu|RBDARag%dNzm~0itVx*tS4$7C{YS(*|)RK=dpS_iYdz8^qQ}<Ere6u60|T(k$YW0R@unqw`Sz%K3t~s{N($#mTaBy&KgDz+D}l3@>VFVnmrGx$tjAO$K<^DDzS!;~DgS-9?09OJ%8VaLXPf1K73s)yp&))ccr=Yo1Mip?}|lD4WfGp?~2w5P5r1OvqmfKU#ytdB%F~B_`D8=((HX%lx`^mY!#mcgcLD(wD=_i~KS@$?Liw#y2FB;v0+~n*o>zc>}w17q1hs27i06zo9GN)jDvR6>yq9oc=h6bJ!WcFdL8SaVfr^<qM#DgmuRFb*B+6;lJxH{DuESB(XtKfP`V=oRYI&chUK>V_h&K)|dExX}{<2Dn=qd%rHJ!8kfH!3d*JqD6{9L?Hk})#&TY|zQHo^CBdN`rW5nZ`+jSy!M(XFLyahW6$x@T8h^!nmVZi*=S#AqG(6xXa!Wqpr2Z@}q&uzcEn|!Vl>|MV<H7a}Ue!Nr!r}HYUT;D2H2I5&r_JlXH6pW3*<N`2$;HrIpvT){*-+@Lt|rzF)(TX@PRu}x%4ccC%6x|lm%#P$KLCU2pBm9wJ{t&)vUx@{qUkv4r-P^Yb*gT=LK8a7$;!BPzug8gr?oS^j_w>JML!v2Npt`_)SU+W!8B+Ia2t1y)AKxyetZRQFY-waGG0Hm{IaLX07>k9%kw<HM&pdGWymr|!b4M-CdFcwo?tdB%D}~z3l0D@3xO&d+`!$aYb5!!JmWC{zgpU4hSB8u%?LmBujMlnXTt@`@{ix#w86aOYA-3f2~L1~R$wG=^aBV(<CGj9LA)K~P8f4Yi3Ed0&^39HM^l*4BATR7j-1rSAQq=de-!2OkqFt2+k^PFR#q^NXijSEd&!b&l)RGZ7o|DIU$#>+mK<esH{+K9=Mw|@1Q3iCh2c58x8bQ-!VoCB_=is)_q;M<q_{+`0s0xG;W%sI#BQQ+MUOZ;`1}aJm%_mFdPy*r1Y?BBhY`k-VZ5Yggt2tv=crylX$j2@F^sFBzC??;Gt3V0xN0?+UD(8sHr6saYb}l9P7Gq62%YuK%i?0kZGz%)bT&(qPwvI5IZ@<p`#W+h=uEte{=`?igx5wi+U2f%4td(5Db!X4$;CdPuSGs&vW1uFN5H$X`b5$!<6_$?RcF^`?gw_F5zWFTI!qG-H7v6n_sl83mZ;6n&ysp~3kX0LugJR`_36Q8j2DmmwX?<U$RfyBJFbP;hR|`gS#~}e#5r^X-F6Uv>TGtBZkM|Jr(th+e|To}5osre5XZhDMZd@fgK_E%LQ&ZUZ8apO4ZUGZ&bH)mGMyiBeaZbwRgo_4y5LGp3S9xv$?Z5kSef3@6V#kEj}ioDdK6E=WRFI}b4qg^C|$302X+IPku#9uu%BFz6_8~#YuE(^EFM*r$LeQ`KJB6jpzO<fMvx`2UWQ=(A$F0|FEEUpet~7A9EvuMoC@nm`Nc4hoLUx=c2%sn=Y3O#l2hAKGRPN0wX_aBY*05%DI`s1MEuyO(h%bfW5@5aLhOb@Y82W3*R#3irOdPHkXd`1x~{nfuFnS{b8g>4POTmleoM%a<bgE+BJ~q65Rxr0CsUtAeu$o|V8>+Dhjmr(W(zm3CS);4xjO{B$59<R#k2Oh(wrQRXrri?T)jvxrsEXw@<eQqx@^zf{>AwA69D|-!6*m8G!kqt60<15;lt!lQ@j$PcuDhI7%;Mh;|w)Zz@A}t-~}NVi2N1aZ~r9u%=h#K04217goz)rbE2sylXIR_Vb=*{nl>2)ngL3^SLIo-H0H%LFSqQItcK9~AIJMklZFT6rif;=qmpqBCE$p|K2yFoaqYz8`rdOUPbTL_axdn1g;CcnH6jj{V^I^RaF`B*<@Kn8HGh*0Q6XYo>UGurJy``XHi6^gzeE#Dy#7tJ>Qtt;;ksJ-pyV^hql^G3*NNLt2Y%3WU)qs|UbfV2TF1;+X!pd9zNF5BV%(a&UCci)zCMa<JB>giXucBSHK$Ph5N9Z){*>;!vK7SOM=LfFV--C^U?<}(;M?I4Wcgnjl~pN%k*;bC)u?wveev|JrhmB}!qK`zP>3?eKrh!Agk4#TLRJ2vVOaL*<LB4&70hS5egDDs88e@qLHgiq+Y<Z%#>;#q2Ri@|?Y7`xhsoJy+XX`T%U1Pdr?)d?AlsY6;UIB=P&TI(Q2N`wVduW=%Ki3cucn1~bzdkg2SzDoQX{FI>2Agc0>)JsX+wi~e!-XBOPB$uXM|JXQ_2klaC36a0${xcMEvyTl&aPAbu%0*bez^}zu$bWHPp%1n&&To4I9)uaj@{TKgZ%$)ID_)>d0xndWjh{;^r}b5_Yg5R!F&q$vxycEs^@^neb{-mo4>F<`SpClyF>~fe0@0U)>XjSM)2RPn)STwE!wcd(OooI)}YOzFlV@;txycH4z!CPI5RG^-CRzQb(au4#!ub3k4|V_w#XnmW+)QT3hB<TZHUdfK8QT&rpMwNadC)lt&5^DTW;HnF>+$l@Vj=BODk<62?&o#*u_^<iW62tR8D*uRBlSZg)`jKsKfqqHPT!yl0?Baz-Jh<$i)!wb<Adm$)Z@HVy#n>ol2|yQp+aaA-@3I~1F_Q?dHQ*xcYw#;9t9X_MW#{qE_uL@vRn=(d4oHn7CJo%ClkY#?%ZGRpd&D4&n`W-_U*Y(lnCL=)YO14s0#Gnh}ISCcO}giGqKK805vVBS4GjO1wTk$lNnTvmIH!+5>X7)G!(ElBKOP^MzCbk{)nmi)V<zenQv2%p8_+=v{D8sU@(pWKZzq5v47o%3o^ws9)94)qUr4s|THKP=^kCE^bq=T(o4u2*j!!!k`E@F;Lvgh+V_F~^N%7jdq)`~oIP?@Fy;1=Y4`t~F(`4>?Ge17oN=hLH!9M$(op;a3Dw<EH`zO3qRGXY{<1xf(^-`l57ro!0i(3=b&ewsWZ1-#4P|5;zVD0+8GiKCA$u1Rs&|^_74DRlD1Jfimw6W&wS)_bL$8y&a<T#yAR}H3~y=5ro$Y4W+@oEgio3)<2^aLw%ujHKwDTi<zs}+2k26HcKf3Gy^{XpWVM`;p&2i*B5@><hrD8a&6R2uKl``{NiWUNL^+HZcDQW%GOwu$cY^<nAAmy(72&yd@-Xq)OFRFrW#XB5m7LBK9Ut8{Ft_)ykvXFzEM(rFo-O^JDtJdVKV#<A5U}_M;K)Iox&iQV{zG)wW=i7T!jY`rt5+9u4Uu#4-L2Tq0AB9!NEImBih;&YZ$NA8oJenB*E((44(1Y(|it+TEt?a$2~=LjCawFS}o4p{A+Apk>MT7AuqRCGRU$I?T?zh!O$L-hTz3`292#?Oa#o^a8`De)eMz@LZLa<(QH7!F)i^wLce(qG{ovLXo*pv9=QM>jjgU-L!hJeQ6{t*C;S>x8Fz+`CGm3^yO2dW=&3A+KbIxaRjDkw^#$F+W7O)J+bJ%!;gkwPqycD%Vi3V$YKZF$mD6^N59KLs^xhTxxzu}=m_QAJPEOSx_Hs?Byc&~EE7wLV=Gh(WL}($1Q8wg2zCgs5h=4Wh5^8$sQ);!@))I^5L^LDJdM*0dFdA&AJ+!9i8#aZ)6MU8o-y!=-Hw(&a#kf%Z>jLT>(Y>-2phj1;FMBP3+WbNQdNRo_$oQKh-l%qr#B1Rm*(&>FG0%^u*~Ah+jQbbj6WTjwIyh?_u8oHuibtR?U^h0*=6u_HlK;fXG=6vD(1gP<*(Qn?MVR$#;iq6+pVG_v^RaVDFRp6jJ)VF-7Zv^uHC}8y4g~|c7c9OTS+<s=WIR+CWw5g!=m;ZjF~e(2Tz(|;WWq@(@P`R1mgktbAK7Y%;W$BmpvsH<(n=>{KxsJbin_q5Jc-Wm4hh#-F&(AAonmN<2yMoe@_G=CPn3?cNq@YclKn-2ybYY&Ah4o-buy6fW+~uk7?B2+%ATdm97VxVid<TT3hyEtkMc!2hZ&DxM_;B98TpZM7?yka<Fl5@4gm|aC>%RhSQ{TOdK>-d$RFL0v3b#G#b?25Vi8~h{uyz(k5)kyW5%=-xX(F3xD)p@Qz1}}4R%_ct=QV#=JxW#r-qaIh~0y<2ngZ%xwr4x{%%5UC*B9VX8%P8o|UiO^Q-TS=uF9AKn)+lXj72OfnKxq32dYVkZ4Vc@G2p~Ogbr+f0hoD#du!FTvzcbkW+Rf8RS<J52U8{a*(ERnjT?2ZJjNEi=OZWBFatHn=Zd8keT~Ss!w)_3Q16YF+aRFKD>A0Rsk0&9AFNTDT->3ThIqFlve|T6s|RRJh#gRPnuJSf!IlSXIOiyG2o2>j>{>tG>0R~y#EqJn3^q~0YA$Od^koc6n)2UL}kKrrnBh^&U79Bi%MzYgnbH@ejkWq<rH?KRyD~={jO~7uIg!7osLuI{Tg*J8Wq{R`$awB)i{D>J9G|jdB7=nl}T`#9SR$%=r})Gr8l@22=V?_95}-RNBn2|J{G<`gVl$0WX0aJ7!R@Jfy$?F;;*w=_SV`eiz#dr(WiL5Dt%mcW2;(qy{l15<%0tbP&u2&P5Sd(nX9GOQyA+Y9nX{Za_M(;jq=k3GxwTvyR${7i@%$=z1T4H3C(E(=rdYhXP4<NPt+RJX>c}%UElwNsIWOWQ??a0xJPM`-K1~Nigbo%<Y?wr1AZYLf($XJc`40ukwwR@7UXVASy7e)y3Y<4Q1|&D13Vafs>Vp(${D_y6_0npALZn?gSTcP+X1jG-DlCU;$<T0Z^Ru&AHP06|B>!}c*b*2{xZquujssJ5>ra{_h@!*e{h1o3KYLirc=DYx7iTwx)lzO*|V+XMs7iE_Sv<)GN#D@bz8kIX0sXKg&JPRz|Rx?^C>Dny0*PvKDXj_Vyt2yt_+U;9K~*hmu`g-mptJ=Pi@oI6la!%egwH8nl#x-VF+-+q57UJCm7&ZgvUF~E`V{a+xZaF!Asy0m4*PS;<kU94t{y>hJH1>DpvS|E$w$KK_Ro*-c}|!l@VguVyYW1?1YQ0D(l9Mb;@=+&`)2#hy3x+<gX#oxVf!TURrLCSG&=b1UA}@Mh(RY4i0zeU*pXYy*V=8oY0#S<IPig^HjaT9_;cT^W95+r`#sR3fPrD<a?Z+UHVt47*FzF=r(rOI8E^8TMkVwrVV%vLIc)CL4k0xCqq6n9Mnv%0@JJpbAu^3PV)CAn45_Kht~Xt4CITS?()zLAlE1PkqO}1sIPN+TE`cy=j58G$WbGz*HKL-`i%Jmsh`*ubv!m2Tb|^<VyDdpm!Sr2lfaHh+l>fWioJ{t(O6=Ygg4+10Q=RT+%G|51;N$PSWF#_g*K0zV!(w{7JE;H*lXx%1d?0g%PDav1@wPvoP1LZE;G2c4?yAP0PiW8Q-h}x*5#a}+Zp{r@%9sljk{5eyHL{sv_HpwVx-v{*szM|OuhYUIa$a^u%Z)f)dd!NcNG*rz_jSo8O29YQ!4;<^jHLC68fJRYQ1d8erRh68o&6ky9Vs51Q?rg*!(#Jo4)w4dj<k9#xKAke5!hgO~2Zvs@4&B(+3Z|pgDm<r8Ul`r^9hFOEC(!f(mbIViG@wJv6(|UT2f+X)-uZE4?%^oAM!Bimdj@+-|p{2d&NZT{4Sgg0|GNY*_nZSIaBuXxXtCgEP{IZ+RJs*`M;tKZz;bFuO^PtgnB7U)dQT`wacWuHZim7QDi%%r0N)QzoX%@FCk0?qkx2tZVv^q5l~A!`$as)a(0@byoV2RXH)2^!QKcF4pa{jcb|?H;2hrIE<a)r3U$URlA6Vc84V{IF4Sc6vrm3?l^cE-d(qF?fO!`uCH*3g42fi(lA@^#la}?gaR<FtC0Ite^gy*v_@q4eo1KgetB&9era&|{x|fQqEYjoQSA5<9g6l!EWJ$}ozJoX?4!V@#w;O}>b}z@6?A9Y*wfyQZ{LqCxai&zhKmq;_YrJQgk{!X@f&7b>1=cO=C%!#_qYcZZQmc<7gqS~_SrDmvZ|3S*KtYR{`OX{vneg!AEd7FeR7%2moH$`uQi(XcKK-Vn-ydv8IRWn+}$Y$+;h-GE4&<Xw}W8Y_c<m~tGngSYX=3-t!>$?b!uMEeH3mb+uQer)4<O51E8;l(*VU^C!_WfS}s;#$r-?}l@or(PWTxHwb_KfrqjJJTc;@Yz}X4`A_Hc7lR0{LNfN}`_tyf>VIvCKB{1P>%I1#TVkLL=H?J>jZ>aLrFCBo+1F!&_CmYX*^;K|64_aHmB}q;wzz8`9n(&H%?g5jx$sW)>&kXy3gr%rhUI2eOThc~fGct;x2_<1hpvBE~Lz^JRrO2yh+mCeO6&vZ<dRiF(#Wftbhu3J=sMC=5YUhh=kkZ1gP@ibeFrH#oyui=~r`JN!q_W-^-<IN=aWF~94|#R7Ty3xXvuo+5hb5H2FRRA4aojMe0cF}EI-`g|VEVeZbjc9C^`_67K&wz-^47Bau-EVN%VfL&gh%fVUcP!~-0Vhwj?!xowxj82S<sz066kwGOrtXpzoYt-!=InLKaPq~el__%UMYvm<M?Gh9_PrwO#OhJBajzi#z$1dBDLdWna*B1&W6BBzgb+Ir88$mQQ=cXJIGNQsJD|9q!4~&s!NYa-W-ol=hEB{2@eXXB9bW1!znQ~juix<g$S7hCXoNw;J7SJ$kZZj>=+4>G#MRQ?JKj)U32J|%Aph%rg~F-79a^F1?n&vksEwc#@;A?wE{nJ_Bc7bd(LQ#hHXfwBt^dz3%NZC{N1%>Kqz?(BD7r+O(ZEI<7V69<vvaFc|it;DMpUfx_eZU7xk&thhi$E7Rq`3u0P7A$MmXBU|QE88S}5D&0Vu=H@355H=n|0A*Y)o>)P#R;$5S>#k*N3&8@=jNnnXm;|<i_IX+3#B67@p#L?LHoNI3|ju}*NK-_f9N$ZG`8-bF8Syk6MXzf<|we7;Xu_TJL3G1$YgQqkUCGCw~9(K)QJhiS&d)D5drvWNV2RE_fDz7VvHD=TUv^V8~YDDxTceyks{p)N_O4JSN!d?6~j`dZi;hT88IKvoCv$PNU5Dq$`EEy0#=7A$*6v|KMAd4mzR*+G<!7U&+pwje;7l=$^-2?;&o3mFFF{!*d>)sN(_KrcQ<CKxCqEtqkP{=)1=6yGVs+mk4DN@YHYWm}6A1N9cWDE~~o6Wx)Qf#J3YVipv4G#&P@~1Rxpt1`##Ux+7WBBkLj}pvIun}!;H3#YWEKOBxa*kF`tM@6Mw|^G4=*Q#atdzy{79upmd=R_tprug0fD@dp+nbM~c|QG$6>H$%LH}(iU|@Ov-4~}q6#F_!L;-pbOJdFaU6--HNEtWwnqIYF(MFKMKZt=b2ggx1U|?fd_YF>ifj^zm%T9mwI{6l(r!9Kx!Bb!jd-01o<vs8fQyN<Q72Ph`3g3j{7}}F^dV^W%FltOel!d(bHpF_E=Hul#Ff;I#Er==l@d!zg@WJ1J3bPAQyZ{;$&EZHidYDb^%kw3Xt9RG#&XqH7m3^Ae{gOr^KWDh6PRA}mIzdBIAv)1e3Xh)~nuVaGu%hjzDjQqTO)Wt%q?W>vk(}kNXR5nMPslpKUf0n}d8+;P-Wsd~hGc4z=(h*IAF|F9qa4du8~f3H`~Jhx+@RrEwTNk!lmaGQv71^X_10UbYpD);GVp_8d&Bz3Z_Q8r&vQCClev<vPzbArznwzp?0gM6{}_7r4ToBJjD8_Jn<ywfe0X<v&E4%NLD|)i134V9Tp`&!bgerO2bQxts`ZMte!q<3^tSfa+--j}qwa4n=Zyc7y(XLbM#9QJI-j#P?G0q(;pp1P6gB(Flumne`R_h6w1H+6Le|oFDi2t%uEb?#C=!#$4x`pstWxVJWB)W9p7q-8TDeo+cBx)=^Oky9TRfyO!d&1mR`coQ#c!peW#98qs;W$8M=~dkuEMM0!mX8@N=%oG!e~ucS;)lOPGUdl?o>?TX6YnueZeFOrUv7zbC9hyZm`g2G+6#t^S9L!@ii!i$N_NOAdM8e(f|0D=*41|H==jREFHkX^I|a><ln8krNj)q#-LaStjKnbtOq@-=rzaj39V?S*pbihnB{O?QK=@wd=zzdZs#{0I-+hD@(Keq-)0G5M;ivVLer09DlN0tl-u!gFd7rx34{_<mnEjAAZIk$SUpzP2&>DgYXTH&&@aZEGuHr3k3t*C>f1r_N~>Bm?~l@sfg)KHy@tnU<J0b-BrK3di0L>itJ@1gy=7_3a@&UuMJh3MMS{_IaYrHfBMnA@H<5KZjoYm)plL<U>W(IT8L{aoB6Jy%8HpJ)cJewKn3`#Qp0`^a663b)4S0>c5n(FV<ba`x*oP6=ofZ$^)ml;*6Y8$R8(`7BHMzyxFt3&AH6$Jys$+p%8)BfrGL`(xdTZESut@PYH<fF>o~sRobG-%?J}EStzplfPOT-0(TGYlZRtImpH2h-C<^4iySme^4z$%q0Ti&C#o@EwbtAc746>6kJ&+-*yBAe9ZwRESgquz<mZOFFqg6V#UY?Q<s5Lb_1O*FPeUUhPe!^~xh5MXQoA`kdN>If}A2rjo@W`ka;p^#NoR*ZnuFdE>=Eed|fKHB{9$QO>FLd(@Zj69(TOVNW<GQ&_tcqFlyWP2a|?QapkHeHYGFd`+VY%=TDM<7CtmJQLwW576O)!S_CkiCQzM>%AX%9RvzPs!c`41#GQ8)6xDs(DWQU#<LHuM9F_xq$zn_NpPv)LEJgkQS_l3L9q76vb<f*C=`t9$<l@%yU$>W&~WohMtNj0|&%`ke1cGnWbzZroS@+Y4HWaa@X>5o^f>Asq};RZ1r-K%})UPyuqw~l9cXrbuGKuTW)6dz&lGR{Z_N%zI?`cxjH?0I)1_SuiD~@8W=mhVz2As_Lf)o^mgn8)OF)#MZ^1%86c2yZDG0`F+@8$nKAIep7S1ea9NU7wLY+*Gu>Yj&|sy*F9$U>tq4QTKOv9(>71l3wMXi1_}GkGF|GAkpK{11GuRR7p`fS;wT?d@x~YmSPa|F-cywyHpt9s6;4F;U!E8Q1g7kPiNv6dJ=GX*b%y1QCWKiMUB`>B<NgebKh832KvzzoCy(w!c?AI!M1bxp|?NLS6I>*3bq+UAX0`J8a<Md^Y;dhep@+Nfy;M~r8x-_uEf3BYYTs>bJ76qrz4s-H_%jI?l8zl*=SX)N#u<WD#$jU`ej2$k5AE5qXW`+KAX9McH6Py+5F!ch$+%i1NiU0zUgG?3E7nuB4ljy}PO)>Yh@a9L`(ndrZ9y^9N+@n-jKcIJO1XEl@3B^2M6Ie6}{N4-GRZ0pdb|40Gd$e!LMi?}1&CU4GQlC}N#4SA7or{V7IJuaDXqoWsxb)wx)9Pq&EPs##NyYJC#}Dk{gFt^{T4GSWM}EchkL6SB!I{nrH>{XTNQjOY6`=}etNU<+R(&6xPeneP8(z9eBRVtukQ0h76P>}IJtOu+B`vea6n~**Tfk@wCvq}n08erGjF*`20aI}gXboA>Ws&vyi+12pS$DF@Gqj<6@Zdp7ip376SX__#m!@6RhME|VwgT9PPahd!#-*C#3~$ip0DFx1m0cg)?5WXx+6!hSbjb%5|APsLbrM(+%|Cy;7*Kx%9iKrF!Qj&dvs79-D#0ev^=tQX^k$-~+gsdZE`)68%OdQHQ)ei5OQQe9hAzgFG#G$TKm(L;VbK9{FC`C4cG3AYs=?5(6C3dBU;jH^k>Hzwcyn=43r2Fc7uZAlU=zpVtMzy<aX@0}?_EWRwXqy71Z$WZrt$#$yy_^s6`5b-kP1WsTSbSxGbbs;P^UJ{u@L8M^?irQAc~E_kb%Y+39PJ7osafWgR4j$Fr9YQ2_sy&!~GEb_j@Bgh(2}vKB)rXo^5tl9(|=96CA#~euI4#JM=K;DfnPlf|;NZY|tUT<!8jbd6@+(ZitFazoJ)I;7E}q=!{`~4=ps90LAeNFeR95uf}9qyf!$BNur>eF`;-NU2n9Q4q%ZNm@H_39x!7}e0RG=TOD}E8i}TSjp+V14y9|ZS-R6(bH#S5I^l&1D(yvwH%(PHg22s)95!^C<A(4vVlS+AYiDcSadj)k<wg4_AJ;ZhgzdG5<p&xm8P+xps3Su+tU0V+#jv~pOr@jR>8=`8WhXX6G=qYbK$FB;G{wzKW&cWXXvRLV2SIOP4`auh9g33I-7<_q%u}yePWs2Z9p6sI%TN&GF!$!fK!hW1ileUzgcu;Y&i<~_HH3LnCnx%?V=D3pF5nn15%a!Uk8z8jjV2Or8@bV|`$xs?d(eu0d`0GvvwU1cPcyoUXhiR3DaZsx^g}WpW5DA-!>2KPStR4=M<)D#K!>Cc8?NA^bcmeP@1O1Hd^~?t;^%AtJe-bI6}l-nK794;`O)d|yXObTRkwv0IT~u2#r-?Oys&PG{<;9n9K+(ofRyz+9{?*!lRLj(yMvx^02DU(9OIJSseQa-E7B2MOxL2>1Vu9212F9qABhlPkxY^KZgrx^5nlb(&DR}qA?{iPW|M6G69v-7OQt1VEt({!p}VI=Z|qYGh)+?x;T+nv{(LrW&XmuvC_*>HFHc?{M*C{}+<7?2E+eYE&(&ZN*B${P45D}EVKGf6R;e+DtFJ|jJ?Ij@2x0Ki!+TiU1L?MVnT(rPv&3s0%Vv}5Vs4e5EG}vh20+@cO~~iDhBCO(K0HzL7_7~Fom}&4oCxDR%?o`%7x0w72ybdJDOz~Ld5*dCy+Ch0WGw(dDIV?tBCMCeR~80xpgCgAN+fVjoId~uaz)C~I!m6~eNLD5xWt^@MZNxD_R!c*A{Ei%Vy)_8mc9D4?#dw4J~#{XW6j#mqH-*uI3hTsm@+fa?sb~RX)SHJrDxu1k}Jica<IW4;S*B}ETs3jCb1vX7DLhDcbdLk`nMrxWLN%ZFp78iPeTrMSN>>-uI#QFMT6+uE>pSBmI_@oWd#G|SGTw{aPL>k^}g$A$v&IP$@1>dBCF^Ko=upEKoA27h_;BQ71X4UjEjXI*(sXZ6=Z09DW%*?I0b-7M#w#DWUJ_YBf2c*>es(g(wV?!7eB3e+}J~<<rMR(Vr*z65mbj>n)O)<eU{FE)f|v*RbkI>xx&(!SHaT*l`2L@I5igMYtN){muamW_d;rIR(A#8x`K0E!MjE}D&`uyiI`Ud4e>g4`y-;s;fj_{QB1bRCQo}6$dXBrv2cbQ5Mz+0(}Qsi=qX*O&IU9V+<(;V_eFcoqSF=?Ll&CDJ24DPUFBYe^UQt4Zod6C@bc2R7HB9z+gf3=&vFCe-XhdB4+)N14D4i56kY<86tn;NR$@bShSMoc2ec(VKoOVPz^j&G%k~9m`+j2B3LUWewWum5kvr$Atow^uwPfKeGm3b~bx`-OqU77#+3bb0n3O7%JEVdWG0-@a*6_14Y>(`ymz6{QY?)P=b6Kyci<_EKDRFFfQQI!<syAyPJ(N?$RYtB+$5ZsJQODI%1*?dAU-%Hrcf~~NBxk28u^+yC*Q`g?OCs9sdjZj$68?OBXRYpM*Wt`tWxgeptLt&;C)DomMpj5)Y-IUu8|iqBzyM)77RmS+#Yp3Rfri-NPBf~u@QoGv@kX`6(~18yOiw6fjN74}*2{`40BGkyT25ucYmerU1I?qLLJ#e<dCx}5-goO=L>N&Nb&P{{DC9ftn8wPC0@OQ$Zmqn7___`R@*h<8Aaq+0>H(|M*XV%{a77OSiv6$ZKp<0t+rD?*Yw6@4*}Cm2<-ItZDuBtxL#ZCkgX_s`mMlSZpubh-C9&DJkREikor`BhU1`emArqI4Vz8FpYQ3ZgtD&noQh4f`sgz4kediK$t<CKn7Cs>iT^p^paed%E8C?mzbW?iJ1EKv_LND8J9&oo{2(}RTZZFVO%LvGv%d3hPv;5*10n`<LQX(06$v6eDa!~;TZ=U2yF|VT=)f|7F0+e|=I2C~~Eq5y5Wm5F05*(x*F%v(c|4;3mtQj{V-92CWu<q~dEF3T&h{v~Qm=wD8DO~~%m55N`EkzZpZa;$J2JS-V2IO)D&yQ6sdU{FHv%&D|>kiwH>-x!jj`mejgh3`qBqgw=8WhH*n*Oo<ZC4Vb%eYkNSx3kay=iE0u?J9y6IzIHMCeORv#^XILWgC}<CK0MEaq~7JCmOkziM{TjyhoR&GX6oDo-Z(-h}E+G~aD5?QF2{?bo&I-q>}s$+W5}d~Q;#Gz4JR9G{J=YQkr~CPgZSk;XJ$zOX{Y5#ap%d<=V%ubyE~eh+xFEB#89eyyrx*MYtpx89Q}-G%JagglOFTNIc|$IPGtBv95mZTq#e-WY%z^I=!cF^(CQ1H7}m;OVa6Y;51dV~35CTXQlR?xTG>4h5;h&fHsrao#5iJ)lV4wYS4z&9{&U7*DMqYP>AQg{`OaI_6f}h-&{OsvA~~AZpasFlQ=*Y@nMBm0)T@$e`O-uLky}wo<ngRBqW6J|8dXL)DJJLd`QQWo`#m)urtd&m7TIWk!FClwF<z;b3Tj3QoYse8!ER_On?ZLlFQn)H{N9I=q<MN275r8j*EO@5}7$ET^oh`&KWp3yWEbE|NJLpS98nx)%>T>;FJeIE>(|oxn`q8Rp{w9^C014&6I@UeizW>-{oZ-#N>#n_R4!Pv^xQh48wn9BVkO0v%#8StX2rxvz)z_|9;gUf<chGs!2Z-3Q7F{SsJ%@=lE4Yg3KQ?1QQt8-OZ$LCx>pIfIq`DS(Rq1*GC^zAW!ak&Y!g{>o)Nj0hO94U%c!${FT5rvkQ>4LzOCN8)JQU(W&~0H2_sg6pHvZxeKEHMAO&G_8v9s*4?mEFUl~AMRj{ba1C}=PJ2O3;3JQvh(C3gI|4+02Uw*-udWmSU!%*C!s(3)P%7$?`&X024_;|nz4X@{iY3Lbli`p!okcBMmZ4HihTe_KOOsA+`yh$KenKix35t}jAn!H(+OoC2r<QJLgxtJ>4@q^2k<z*^RXenUyA(gy2N3gPYWth%xA>viU{pc<S9pZ5G9Yrce^lWV1mN0=|^?pc|L`b7=OVl_A$U*?;EW3oxr-hv*GCXk!gI~QZ@z1LI&&#%oS-LR#Z6NHLVULs~m`_!;BA9TzU3zNm_p131majSU_Q<uk){~W$vC!5-%pJJ#X<AlC&QLh>Z=q0Bx;`?_$eUl#pAoqKJ10S!L{zJEtd}kX+ytK2)BN{on}+wa^#~CBF|fMh8@>(YW!47$E+XBf;OQ%e9Z?lA(lMB^;u+lq~1j#PyTeV5LnQE*C7wW<Z}p)^PYaCTIc1T;Lo=^)%1NY2s)k<ih#z>7$yS5F)ceMCbGTGn`}@oZsORvo|{OkpfUDBpH;_ldx2hj@1xEvJM+Ue!WH?fNSCAiEHs7tkDO6z|C6_gb2kwh&4j0g(*?o0wH4^s-G)_I3I>YM67XQpVuU#31oqwhDSBYYIt<lEI_I=@@FL=s*ivOq7yxfRuPd#bO33Re=KIzD3Az_vMGjpMn{QglHc6GDKiCWfHY~*NCkaXS-Vz}V=TmL#iPcmzTVF2l|!NA;FOTWtUe`dA-Jb<EgN*}>T}Ie;f7MV7>Zl1x!rZa%Y|ME-pe23E6=Unj^z&s<7MRO$#^Wy`UsIcP0Fq>L@yQ4DuQ{%m*YYcq^e*T5tu+!EoEnmIgHY6x~8RItJXSO1Er#{BdVWxr%7Fm$)>oy6+#{@OB5znu0AT+#Kmh#qq4q>8;U7pCttyE-r;0J=1LN&hBmvd(I&Eeq5O*hMTC!ud)y({+f&5<`z8?vZxv(EN=8I?Th&VXjfj0*%CDN5p%NY<)cDoJ1-Kacc8XKYT#V{-2|Ghm69<cpX@3*$gCxQznhmh1z}AXAUrZ^++p2{t&PIxW<}F<VhPQY}UzaA!HPMGNzy^q}Q9*!wS{U2F1yxMVfS5K#_7YW%Le9g2cD>FfN8}1&=EQ<^h<&|_kwdr4+c>v!a&1<oj7i;g!_BWHVeM?iAz;P~1XiIK6ir_FI=r}`0|c<La+$6~S$JK-AP@-rF&Aa1<P{(SiwfM9lu53+4584AbsGpT{Zp1+P4n42dNmp5n8{{hMK9!$@ar`;gWw{tbj`{3rQy8lW8{^Uuoz4;>tovJGFT|5t`7^>fxSyLB)v_|w}DghGAlBW4t%Cm`@M~ilOeKPK|upPpC;q0WLcc%({v*E7GvF3wtkh&CPveEihM5`v~3U^gvZ_#cp7Z(HSnhY-~aW${WI~V|Mq|W-?cKJCzPVuuw`(*m4e6Z$MYdL!c(-aQF>te6J=Hz_*!wfqSf;KrFoPr8yLSigA;~`1spVppy*|q%rVFV%|c-YcAX{5r}N1wG3s*K#FF+R#5afOc~xC3(j2Gf>11Hn?E{|HYPQd#ab&O2#d@_zJZ`u0ie8Ia!HyT{81P!T-%=m~0`=xj6R3_Q&a1dld)HtEq*Sp34TcfRS*YBltHJSn#A05m#Za-p3bs(Jn_y^OVxFE#ZrkpOW&|bTSb^Y7AGbiGrazTq{_-YxieoX=>bB8=2SkFlgt};yaD^aSb{XxY{yv~E7-fVq5Gcb@gJAd{Vd=1HKOh95)GulwI2@2_9VisX(}qDkewtrb-ngj%2u;a+7tOQ$+Mx{yd==}-kwjgd(?&?_AZUgB$5Y`$BecX8l2&XG7m&nFtgsYNjEI#GP>dL+-;9`8<H%D%C@^@Ekc>fPPlvNqpD@OIV?mhLM6=0?xkSy@V3uT)<U9>%#{j^ad|tVlRBd9JCQ#a(O71}{dg9^B+9nc`y4kEyQ;CknvWF!)9DzXW)u{xp)Hec)_D8K{v@CTOYv2(|^?^6@u?Qc225zVFxZ%2j%Ol>%&LTWLrV?wMmJBLf{V-Xsi0x|uX^yG9MOFzFu|P@5gl3cecri#tmn)`GU?!F*^5E4&05Mpl<X90pUEqem%VEa~0aaT*&{XWhVianI(SE-!Lb3@;`^^wuJdhy+jl!BvvH}Bv2pCMU;xDJCJa?z!y<F}31DYt*Dy^^r#)X!B241*6AFncW!i$3@7B!a<SB(V-=X93p9r$J*!*(POi<_Gtj6PZ3MA@K$zSgeFBCYCeHn0Sb6l$mAR)3WCKcxfXY`;{3lJFzs_R&R;ucFnhRQQ75xx)*?koQ?(5cVx!7=peC3&U`40>e;@JG3wu@47GyN8i6SqBSjBED8o+Sy8=;X;)yH!s^9bb_z<Y0frY}xfP8+zCPK349?TlNTOnNxfZ|^h?Y&1q~%qYd!tY#Z<}zE#XN6Pd`oZI@Y5+^beNq($4<FWs4ILB6&HCvAC+8f@W()93fI%bz;)=e8twuXIh92MFyw*k)^?eMKvh9(<w00Q*sUS+kq2|;jhBy(3(QhV_n@a@Vq?n@F5stW)6|RPQ_7KKF!ROn<$0YiI@kc*v3(0zh+C!i{{H#u=bS;lBhsGXWe`QUeMgPgYWg(><G0@`%VtdabYG==31`2<hE}A9q#|CfP19)ks8N-A(@hTec8E6L^%=WF9bq25PPf(ea{|_TJxaI-UAY_e&{i{`JyvMhP$@9bgtGQJqSHP)jA}9E?%Sdq@z}ZvhN4iSHRrNCt+~L_I;n&Iv2i8W3ZRM*qwvyP6EDIQ^UlNK@;ssovi(}GU5og_0e)}SqRTA3Les`t8z!O$|KB#F;oNyhuI<7iLr<RWTXZM-wH9GgkbRkvxAUOW=xlE_+O2Lku8Axn`?Wu{+h@aMOTK7|4s}|awR={R_n^Cv?u4iW=4CIKP#geVInQUydNxllFr2`cVty(96Av}@k{LltA0&~Y19wP`-P|y_2AHkBXo0*kYKZN_{0hNo-;h8fivmRq*^1<h2;gZ}{8(75vr`v1V|M+J)u9WLIu~{RT%(&E`@?xM8>Examwo~moAMW{FT&Xd1qS`7&XBVA&e;+eg63vQ27v`aJ(WyZ;8QZ|kAj1nEsOcuW3$bfA7Q+}(oy8I^JHR<;rrkqP%|Ius^thR7n;46Imfq%p7sMUKaK=(4zH>u2tM<QCYH1^*l<<b=bzu1;kfAhG1q^7afYrpXgyY82*$@hE^^WLG6M&O#&N@iBNE7$+4-dY`{#xa=0o<e5&a&CEwW2ki$2Gz62b~Vcwo=7$v5bd4aw~l`D2;gD(#nQt-}5TS0~1B6h#f2Ihw~Rawl(n@zV=hyK!lVIM?*9KTDyqSWETVAiLC;FWRt9#&zR1$SjWzAlg!x^KM_t1&Q$F$8xVoHzf=m=|r!^PIu<noD)tNBoQhxVCe-%4^;AWI(J^A6X7SvrZCWmZPV%%^?<3mdrmC9qF>fA{5H#`xOYvc=4%1FtVg$jpizeNu`-CBn4|e<adAeccYvWbDI+xU`)7(K7mEAl0|tto)T*NCiE^aNc;v$jmo64(p~A9H&a#<s%r-)Z8!^mm-o2?kTUibJVd*y}9A)ali<L%e$hs{(!;<)~Qxa#@3Rh+^0A4WgLF!%?I-8V}nV3FSTqU?y;ZyT$KB;+yooMg><NpX05xdjzX?g}&o2P;H1L2tb+&-7KJ6U?!!nmdHX8ANZN5}0+-3uG^eE|pLNsdmp_20?Eb61Y<bikcyMA=|BlJw|vY&R15XN=Nhn8z2N{6_wYg^|2sfsip2jcCQrV8MsHcaEC{J_kYyiCvvcr%?A`1fpi0k?F_5;(}|S_{)<CIn-MZb=?F)24QhR`OsR5ebuGAlQ_vXs%DtIj99IJLOV()2uoPTj*=o$JgU45sh{O@<kpgLBp7H>{QEfI=~%|m1_Bz`x@j-gpV|B8*Hg@0DZ3=JAT)nPgnAt~%&~{#rL*&)<X_U|SKI7cY{;D1kU87!BY4Gy%){wP=E8O#%YK-D^n-@Y`?oaSpL^E(YE|@09rHfS4a<CJ)3}p>O;E3;gk{rM#7^Z<u@x&r0(@n}XMJ1?Hrw3V<gl<;>FG%x|H)Z~zHBcSt|Tx^r;2c4yv(B%tzj(D^&%V~$iDH+X!i!A5#oekGw{cbBmyrnW>7jQptofI8Iv=;^A;GM{sjdWa#UJxFGp*%sr>iJBU<S`fzF>>e*Cg+uMjm)&GAdK7gwa~_~CZlNQ-%f_6~znu6`QsNT3*XMYL&l116-nT_2zZ3<Y@BKDx98+jojk+t`rV@GzSfPf4tUkMaRps)srPjN$j#6ZnhpvG^&FBsv1kJ)uE!U@Q$?Jm01P)<#)vIOh3e=2<Nbj}`;AkQZ5ut%Zm-!7uZ1x*7x(ZE^zjJ!ki<u8pPadimvObv1P#U{$?3pRX}w!kt|aR>10txJ(=amux&<T@NR9Q8clz)7@k?S!ar76IchXeGc9Ytg=6aLd|5H&gMbu(=+B&*8?DpM8Ap8mvo{Li_~-SIHq_dG7#Yf+0?(jz#Y(SZN^60a%Gr-q1#=1>!Axqq~%69y;e7*J~le#aQ@UM)EM6*o$*jUs`O4egoLqo^vH~to=m|BqjW!Q_XX_k{rh%*-ON%ZbT%63=i_`vIkRn>*wt5nhHpjfGMUwzaslH)jBAEBh4@Ty&XYdo`D#*zskmn8ddS3vh(Roff`b9Wr$mJGqXB}f1%KR+ovM%BkA_x{2#KBndURUm^VUJ^zy3c8uUyB*s5qk^MO#}Qiu$u`9-|JYu1algl^{|hP`u7R#WgP;36ZpzDVw`+{+mL9@0=sf)0mgaxv}wx*2PTnJRg9p5YbHVhN(`^6h*|iY-tlnGLaFge=O!1G0rHr=lAmX#8b>T?BLPBW6KJym=(gn>3abNPeucut+uJY7F+-xje^jeC(~2t(WlsqaLA-uuLgd$bpZ~s=G!CD2be>gT$)?a!N(EXo#RC2p9}{x0oyafV>sk!L9Lt;#MlC9d}YHeVQM4Z8SNOmOCJV+2|?CfqROUPCG#PBt^ifq(W1$csnT)M@`(-v{7c}=X?opHQxZrFA;<96IJ-9dM|^KH;k1L0uH(22#&TU4%W@bu>%c(1`X-LUmiT<k;Tdl_isG|(t6)aJDiJCqAFwhWp;@>*0HHW)DK3~UZz$AFPVRDDWw?1cGB5%%UA5@B{8~_G$g)d+OJd)es4}7bh;Xb6txVqU*&oixPR)Nm66_x--Q||9)x2($1aJD85mmpkDu`LN^i$boc@V`asTSmMpdUZJa^n}xG@r%AEKYPLFedOlHKODFfEuu@AN8I^Do~zHZx6Cr->QpSqZlRA@Qg8Ahmnd%x#BYY%yu!<?<6Zx2R6q!u|+%A#MgD(;bVO&_81k~YAeo1?pmOoUjUM}{+G3Dj&_pYSpLXU!<$ez6T0P}W#`$vFf-c<Aa~)Ijhbc`j1REqA5pGD$?7^#p-IL%*HLG+YB1(FUiSUvYVk#^w1Dig+FaADYuz*GtWd=*AW(TnYJ)9$3ka47qwPjXwZ@&%6jGRy+C+dinRZE|IxbW8um7FXzlx0@lEUIEHBWorIXUroAi8ya4z_LrT%(P021wqb%#&>VE}7Aq{BXNAth-lO`_oz8N1tbkon(UM`(sUBtb(xvWtfc<oWa##?2-zOS3^<Z+Tlx6)S7zU#KM`_^ql3516=Uo&u(4QhhDkRdsU^x<gth1+Q{tgZ+SMU*P_3%MOQ8Qw}1ZMsZnwf=e2x_YT46yHucP{F$Yverxa>xv;N5}nG|EXERs$}>b!xIYP>ud!B%-P85|~<eC}LZWUKuoe~3+mxvbq73v&dbj2!7nbZkv1W7Dj2tPMD2;wbLhYrqm9>+s2&AAWrD!}HVE&rhB_dvfvw76Fh-IWD?cF)pLnC`oD}bQAhgYTcn`c!^+j=CSqIf)ec7h3v$5KC>KGWFu$!V5zsD^*V%G)S)QU7<RsvV?Op`wKX%AY8F(??3u0{8-N@u=CRTb&&84wD@^s*bz-Asu!cV-FCL>mvSO@21U(k$BeNlcWcCRi6>9(XFaIyQ=l;t-*DO<7hpVzWI>`s=T2V~0&d#JVd<j8X73+x#l>{rn7VJy)PqD7x2~(efu|@tJ!x+o(y(+SroeyMn?lvcinxAJxCS}vV%M-Jy=*1#An}Mo|L^!4QVI{Xtf`*jkO`oN(obdVyp@xjOog1`bt`z^5D!7oTv)f-I&i9&uAQhv!ZzRMmiHy;JlMPK%8=Y2nop|B6xS&B>*Im4t09nZf`?g!F=-Bf4Y?jY#?K<9N=ZoS8QDXmh+$Xz|CKYq|@C@EGcwohD;6AUxqb-bD992*P{VWOFQmt3$ku+$3u^5k!=Zis>%koZSZaEfr?wmmI)*$yM0M&>`s8Qovxv<{8Ja{ApP#4<$JC-d${Y(UKICB*`v-BdrOzU@qLg!B7PKw=fsuSds>;ggbVT?2UoiFC*2S@9Hwx<12ouI`|iU4E2_T7nX;k?=ivnJ86a3ODN-6rhG^(%_yP&GS(zobz>Lq!26{NMhT8q1ShJ)Y1Geo970#nVNxbZ)?PpnKacD75MuR_;902=()KrOip>%VNpj6s3ZlJb0ZJqm%rHcR!++l10OUbgz_xRnonc<c({iVU6gxqtjTd;txO!&TW}*rPJyx)m12yXB;h5xKwS<gvLJer2k2rdF)l8Yr*=R`Lz&sxR&GZ7@9AfDVwJ2xg&a0EFA~@wHT9x093Lj2r7KG;}_&EjFDnLO#ON}l~#fW8PF)IfNYK+a2g>x>jUfobcla$5{WhZDQhOBvuw9h$8J0IZZ+UZeF{Xt#GV)tF=XH3Kpirvk&1AWZC#sKT6ltWA`6D>(yXQh)plF|+=zPH?RH@E5!n$tcbpz2u;MR(3e}4=9e@xko59H=GYjz^=l&T^`6R!pqu%M!BRlie46U}p={pGyX|S@3#kgKX|0{qc2%W9C5p}zp+dJLvR_6gqx4rK6_U6um2c7#?BgzRt)NIEfdvA6hY(Ch&-+iF2iauLinpqth=Z$ET8Dii#M^7B+cOBh}>Z2@b!n=6ShB9515^Wj?zG0^uom!XQQLPxIW7t+Q5P&QczInCG<)(p%dOEx9tlnwuG@?!02}*TSgxD&r+~vxf!OC8)H`YdCn;1i_3sb2Zs!ZnvRkpj0sMGEmHL4SEO@kS|X7zUK0kqv|ZSJ_BM0aIQGCfG(S2r7|li4wKGO<Q)Wgf0+II|am-QGd44?I{EJ=vlvJMCaks`GJ8!wJ3!C5T)Yr3MwwmW72I(f!s|aK3FPpMAMcFo0!u2L$U6fcR~w-iUT^F5$oK#}Cv&vZtu4eYG7MS@Nc>^KpKbzzV*i-cxubdu=p382k?Y!5zMZ5VjokbpMmA<TSOZdSBuQkA#TpleZ+=P8q}6@~c};@K){48nqqwcdLHaFYdazTjhJDV-r?w?yiK%**4aITT2G!cgP3S>b16mE5boa34k30u(J*TRFlDIPhml%h1dTcuBf;INq8_h>tKe~4iDgeZCx?o3T{zUaTa)f(1D{9)*lAJ7eOLUa$<}f-gUh!nrpdKmpN8RA@ldhKX*LGDzRr+k6+=9CjGL*4B=Gj%s+^!mc>a2C1$#ZdA6+YOY1w#=10qrr6L`jWgX97-qD9TbS0$G2p+-4x%mfVIlE;#GqHN$*cUOeDw2{VsI$LGpI@Va^6@<V|GT^P-nNY-{(n9Ntpif2mSiVQf<S5#ICd`aHEsgSsjq2r0xeM$&l0H<>9|he?|wV856-?wN|w^Y6@?>^%YDqw?#|BRH}fX9dQeUSfifXkbfsPQOPHku*m>`_e|@_C)aeGFclUm8bF1w#o;OK}PZ@tTG~z9J3#v}l&%Hg^kv8-nukXQrH^9)0;5=TUBQFTv`4$>eM81fV@rPqi?k~K1=}<4x7j{FLBpZNxvBFSf)qO4XahjOmHW0gDr)ZB_?!1eMX8Mo1Ip$;)N_=U+=d6Gj9Uu)bSp;AGA}5?U<wJio%P(}NBz{KZ%tmE^P__@)LTkdRWO9$@u;Nk4>sl|LuY>MqfLdciSlYV%p9DBKmOi!7f&Ym=li|XdzL1oM5kh%2Qf(U{S~ogtpa7Y~c_&XhGMgfuJ5MU<RsppCF<Pd8J3f!I4DEz64oAeN2BKQrNrUSt<7&3oiG2i?bDo0bCRog_evgxYT|IYnGn*Zmg%?^>Ejd_TXEIew@eS_a+!Ca2#+v29;z}f98z<F6NxaeXsDf*@cd(n;4#E`3RErG~cEAf*!{R-X;~-t~ly5dBY;2h~K&|FDoWR|12R&tbtUny7!EU6W<nCZu?lz?vCke=!s;!`bdRCtd{!bw184fZM?7J#K9z5LlQiROxX_T>p_uWMnErEj_Gpzck=i9jsvp4a093`+;^y|Mee})&Q@G6O}jdqBhhmCI;M;RRyRu5aBq7K)CpM#SDdKmPzvQtOd!ohZ54=oh!!N|l<sl_aw{I>tOJK~D7Q?v<Fk3r~}yIdE&AgDv!)L(Y0d7RQ{H1wAQ%$|qP{VD!3x?s@W2rn!=YP5pob!hWf!CGXk5uZNw4ClR@^0_XSiq3;_pGMs_*`3+0%Ouq~2(RJ;SrS#+cFEHSOX@|Xny>22mSA`0)rud1SPR~?;gW^wx(6E2f-BURwha~c@Nb&~oMt`WMac+5UM&<?h1iy9J2w~8=s5D#sK<@ECp1S=sF<L7bf^e4{>NZ=^y=>iAKsn~-yfVFoD7T)&2U|9Eg0y=&bI=K8=?r8F&3i6O(Ugl(70(BuV`w}V#6{sl43-HdRab&B@^h$R$Y3*(<YBP(YQr)+w6&22sJOt)vBJO4wvDLNt=hsRXCG1@k1P!G2IQN*9LB77^J?t%Rf(|KXUo;DSvNp6I<I%l#^xHr+>!do~o)1J?s_3yH%;$+&*RAeFL|R2A~s2N2-QdcN-Mxy~6*gEqXDe9fJMC*YkoKtyL%;*GgAm0e*li&bn~MU5_+kYfeceE=n_WJqITxd{m2Yw?sNWN=KJGLB&~kK{5N;ruVYaUI;F3mmO9VkuFN?g`zgMhDf{web1^W3#zX`zM>k3FBE&rrO*a?p*M6%#&D;rbfc5wW*uXHTaNJmOFsBZ$KWr`zzNy&%hKdgMJeQgVz|yYe6Ri8V`g`Vwv0Wv-%^l;?4EXCz`OCxXgcF#Upr7tCdaBJEL?=;$xe#;I;^OPDpMniIjunlrokYm(18L2<}(OuVlT;TfVdgP2|%PRA`JpYFDGXWOSQ2w1CImi2UIkgsN76CZYyJeb5EkHfM{2W&+w-AqTBR`hnQOxVyrIbt54aTh`xzg*Hu%{9ZpO^yBFkluZoURiRGrQOCy#LcYO(obP~qN$|%zk<On`)iAvP;(^jf*cz|4x*@%78!@sMF$2J-ds_Qk@9D@fk$iqWWY8A%(HYr4UK=(F*_~m;OCH5PM`PdUcj`Ur{*qlf|C72|)=60YjXXzrLFM7A0PR)iTw%_U=!UE>7I@{sj#46w)WPyN5>c9qEcG{8#+$Sz6u+FJ#<KBTNuh;1~g4wi+BN#A1%g;>L5Ug{PHd%gl>Lu~~)cd<CmW_Q>7A80@PYtf)d^FWIT`f0C9SwL@nikDVX`KsRrTfWUE=P6mKt{rs8ie_a=%NYe--IlJSwQ=45yxp#CZfGc*>#qtGdOdbDp%JoPvaFZ0WVxeV+hYWJU9yGbD7r*AcZB4kId`UQa#g>PgNS01pEuA?=(9SJ>cg2TEo+SSvw6;80hM`f)^~Ufx@w=rB)DnzLJIwot~NHDVXcMnsfE9O8ivpnO_Deo3RtemvZAN@v8NR?iSz3RBE;EqGXgtKC8a9=Il&YC6qVGSuqD29llEGR!gd7i;D*s8(GJyR8u?b!~RD5Ejeb@nRD0-5)Q>vmXHj>sC}FX2XzFxt=V{(#j{HUj!<8k3M9qOiSmuz6iKe*WlgOLl$<QNq`qT3GVUNXk_=(H`h}6nht(;1RFl=Gfor%bFGP(2o7&bL$K$)6SpGiB{7bdEs;301kte8u8GtbR5Pw#at5zAtB2Mb{9<0`b1>W;^^e3zH6}GwtU&$6*_O`5ERjeu|7I1yF(ClOy_Wt~3%?JTjv@|?GRON~O<1g1&_g%*5E>7xkUN+_pL-WGF115{%?jQUKRWMp~Z$dCccEAs}FP|+ydWR8pe|XY&==sStL751P1}4iClLVMepe^kEaqvB>_pzg`{WaRk)5XdyJ?K7qw0cY234G<oI;^#aYtS&}6fF79zJ(oKu|r5?#0(CvAl)*=Z05kEzc6VT0cwR;VDKxGa^IxO_$w&)*yCB41ZW`&KDKmi*;UT-2j0}bohTdCGqh5fcajoA7O8_8v(W8WiCu*$>qjtUIfO0E5cYWAEoRB&q2U4|yIQrj*b>!py)#{r^Xr=A{8~-UuMTn+G~<Y5Hqoeo&?e(^%#wo+!N*D7WHkgGyI7kM8w~sH;OS!!nV$TwkRJ4q*iV=MpgenkKb+UL64IAZO;Ja`?17&@qsn9am+Z@>q$nM)=gOwDy|*{}_&@E-2CpB$-_vk5xdV4sGbVZR4AwW}Okl_!S?XISuX~rmzUV#KFmcn#q@LKejyJ$xusYenbtb^d4@RSOIR=20;C}FmBe8Q;qLxyfgK)oz!f`Eu4Pe2Ak&b^^D!!4*-69+*a0f9if*f2%RW8e|+4qL!-D@USsR4}+ty|dWJW2U-+#)Gh^vF&N``qau3I5@1LS0!uS-S*4G{I*T3bge+m<l|1*5qdr7bK%n)s`qyh;E&#=oM%-YEs$@F<-j!?ur~w;y;VIb7V}F*#TPqvMOr;|4~wsq!mzkxBR7P<^lD)q&&@NN)v+hH8rlCj<k{;*U+Z>vz2<a!Znky8Y<y<Vx08sJo;{u&KNHZ7ZDTkv+o>+EN>$~=WH0F|NgV5{T09aBJLZ{9+}7BssJooG&fLY;7}Hw|FAn$oZmP(Ve^b2z+*(C&)nRw0dtC(33rQJ?ntLwXW!kB%?K1be6!lDGia?iN|&?mzUJ)f$d$d3;iI=woaAVIWukrO5Jn%IhqIYfcC~}S+1ub9q%b}Kc=KQoPNMvV30ki)cOyibXtI_hDPC4N7WB&I$ujKv4Hzm7bN~w&e_eIyYCMMoQfZ;@NFW{IVDmI`At-E@Ohpn6&WUyPte8uK`&pC<?0U^^nO!flzSw@v@o5RfmtC_%iYG$>_n3!WL{fMP(MDaW5Lipptu?{MH!d&?7~40?R%8TlxHGJ8{*>|}g;btTr7NTq)~U|j-p&laO2Dc!aeVcltR9$&<yYy0mUn)QwynJMo1c6)qQSS2OkjXA-P=}%X6BN+Ge>V|(83l=&AK&M$~5e5X(%@TbHgqZ^|rJ5VD(*0s*6&}P$ucS3l|zP;5=O31Of%^e!zhc0)d+rG^KIqN$?WIbFc>G=_sAG$WhH9&|Yp1Fs-Q2eL5HK*FTv<)MV;4IZonGM9%68nouZj8{ld@WV^%yKzWx9BPF8?hE9VTbh<2S$vTDmve8akD^ua+s}~k)WyqPUXW-0fD~V?2aO5hj#$YT*Vr;xyj=}*ydmu|-aKTwDNg;bhlJKyqCKDu*aR|eLn+assY;{2>vIu$W3Pe>i6(MI2f0$1i;H+alX9s=5m7rrX7i?nJ@*-&9zc4-dtYN3%m<Ts`2g-=$Esp>PT}*8?&->e9BGGxU<{BIX;jCfagSNjBYZ>jcE^&`|q}l%y-=WxuN;P|Xu)`FvG@qwTex-Tm`;Gap5$`MbDZ05xL4Q1$vPwo*Ih(!1d^y|w80_&MzsetjX*|hyKUM)mTt+wJ^g1c`Sj|I_jnr|ZX|LJ4pOM91SQshtRX0yREEX!kNzX{igS7)SkAHsu;S3kBdUW>cpJxZBuMVucFMP;a8nK}=qQEy10M~{;fl&eb$42JLtfHF~xwjvq$Wb&2uV#7EI18d~26V()Nn|)JhFn47%Pqs<+FiY=-BoATZi!|SIZ21Y;t+CY(>UvbGYLmx2BlS7H0l9q?)hHuRi815dKR%~2LdgjXFqBe^%qVjA92+lhKru}4gYSjOko`7>2k)F*kH7bAacg_l$U3$cyz;do_His2j0f>7*>wwMO&d+>2F_x?wft)d&9rOc+=x#l+M{&5bt}=r|o-gK!l#-887R@nCW@n@bAV^&Pa2d{2O;a*dZ|>w&#1nzhV;am<#qN9H_ZxKN7T3$n`z)yItUmiSV;~N<b~}qu33Rvk^(kM36+}*2Px@!4QEQYaaJPeXrnK7@P%%StbLFJp*qN*jfDxXkA1Y1AK<{4r7kZtBVX;ro}0A8yDh{VCQg3<?5p1<1y7iCUl%f7q8#S(1s?le>n~BCQw)ZUS)LjdVp>oAOLar0;&0JgJ4?gOwhk~+k(G8?q#E8yvU!kUl4r^|4#Gy?D@U_0t@-Lum')).decode('utf8')


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
