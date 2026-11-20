# /// script
# requires-python = ">=3.12"
# dependencies = ["numpy>=1.26"]
#
# [tool.orcaslicer.plugin]
# id = "orca-vase-studio"
# name = "Orca Vase Studio"
# description = "Parametric 3D Vase & Planter Studio with X-Ray Wall Calipers & 1-Click Plater | Estudio 3D de Vasos e Cachepos"
# author = "Orca Vase Studio"
# version = "1.2.0"
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

_BUNDLED_LANGUAGE_PACKS = json.loads(zlib.decompress(base64.b85decode('c-qZ<X>$}uy6#^o6EVjSgYb;!%>BT`IT1o)J7yaRuU~FdcV~B(sjlj&MIbqdK#~`*jq!NF#v8_F41&SN1IF0KcEohtKQf{v^l8pdxbKo#l~t8h-2ydsgpInga(y%N-7=qgU)a=*Hf?`lQ&?|{j{SdUL=ZZ@w`u$Dw{EKY4Y6rEzTdjZvm<9l{9n)RVA3H!h~ie<yAr~yh7*W-M1?lFQ2;4^&=A3<?Z4Z)DGF>abZvYaVk^^e&<&hWSo^UWdJ@8G*ke%b)=krGyNl_&{GemQ^I>r;iUR>9<xd;id)jtg>p!eRf#X5XH|^~}9bwq}+=q9E;HQYNfcmA<tldyd1heo8eu==btp;=hhUog3>$ldlJ%f$o4|m4KambY9dE9leD}IAY91L2v=hPtue)T?spOm~?_#F`i^a6kPmhgdI9dd0i0s_OE2^;9$?cEGzGYv@FFJgLh+_oQ!C=xKr$0x0cIN)wTIwaeWib*!S!`!aZ;40Oxt($fMQJX+Ry)+lu=gb5mQ_%X?%WtJk<kD~wCIh==wQaBAiqPV@c4sZ$v!XWEWQA#W{lIEEo*0W_PgtR>s|Ex<x(zBH4`BWvmmONR+q(pRJex|>pr9r{w(RF)%;JYu-S?uv$2RSn?Hu#BsjeLH{3x{k`K>kKI`tz~9lLHtzGXKW^bTK5`f<$_V|C2&Sm3nU5&yOvq`w3Gq?}MH5FLL;=-ul=!@g?ZFR{R0)`@uC$Dk3X4r|#CsFk?u`dBgKdaUM0ump)f4%7>Ix#|ErzF&lGYf6N^8_SKt54}rN#<up`Zri3cRky939TC`W!-5Gvf|DX3!_JTsZ40x|-hlqr{Rl`m;o7*YCq&Tutm8lh>K*3WZ{y57-FDz#$YFPAVZsKk3s{Y|wF7o&9Xk-=4xI42T@gT{@6F+Y;2+k6UxQ_{GpzeFb_4g>|DJ#6@76P8Q}(R&m_-|M^I_WRab0-P7AQ$MrfkO_dj_%`vI7CzO=jwSUw0b*791}S2-a51+9T|!V|T61|GbW+_uF0CpUHblH?&*Q5@mh+jMeE_6SnJgd52Ka1kfdf7hK!lk|ww&?Ro2_f4%;m^)yUqGhnud&uXUr_x$M}fm6VE11bqmhXP=9UK{CiK)_PMJ-ri%>l|aEO~Zy5tIdw#UwE|-QZ3k${F2z2U2|L~nkDw79ve0dhlu=`wafK=Y)}#u5@L_a_udC)7DsJshaX_=@VqMye0ZegGU;@LhnzjMHg`HmVovFOBV-CLm18<J658+YT{s4>cZSh6YnS5!Er{`|pT31}a7hAF^;$0T>%ak)*ov9C9*kkzsrlM@3?4k})Py|)qXmAZMuiDDUQCkX+660+S__~lB*bCAOH8<nZ+E~3@H@Cr?GRt?aw6*~M;s-}|0T8?0Wt1>eY9Xr1b!HfO|z&1?uM08I><6%(ZWRGXS*{0QzD39Gr5@6+I%SRn~p22XSZaEC7CuK5&>ku_qaCR`q|p!2hJSy9bP_X0b{Mh@<#z+{qZ;dI`Q`JfA_oJ@HT<0yI|ee*#eXm_O_N8X26>PX4*ya>~{ScWITM-2_qV8^5(D~Fk9g)w5dBa$FqSWS_X+~@$24&8R6huO*yriXwXuNc@0n49`FiStdIu6TNi#Xr!!RBK@j4hr39hPS)3NI8*9?BJHFQ-Ihm%|Jew23bz>L!>0?My7||aliIo)+v15%Ebc|D;5)Nt<o8T`nYXRFFdIt2`Os}`3YQn*;@El|yyz1q?`44Nn22%&)SBw8}0IYtG?}D(ho`S`M>9k_86eRf8!MYDToaUM<fmXTfbl1T?p)z4@{yhj;PY@FWMFI8(zvT3`y@m9MqxNiQ9TB2y!K8UshjuP3%Wcz#_gUgt7Zw+BK@?Y34Yn{yLFh01@#Slv4rb1^UW*;K0V2}^>Ebl38V;o9`XKp^w*3(0WY=;+DVpH@EJ^VYS7%^t-u8$6yS8kzp1^)#dgQlYJF^70KwqgJfige|t(Tz%RG+0$Jc2W9Wd_{>fn&uT>VnU`smIUz*bU$6Epb0U6j)to!fN6+X!vPIfX;SyxK=1o-D7I_TP<2fKvfuVH}E6DE1xw63sqM8kt~I_7bydpl7$Ugn<X8XIwAIQ3(9$Fn5wVChOmx4MvIEsZEl*kLytf{aP^=AaJ|XExMqt9kgL0ebf`Z@44YS{O{+M-<-6UQrf$oT?4XYS>%==;{-^^>o#|vv>^nHUa}vf*bB$w@Wsn6yO*l*AKr^D$cB(0zuZ~@JdY62vSx$3kJ3;RPsAC=3ZEM%gi9O?!2dys74h>C70jdNE{;yLftrxuG7O?ehX!%X+1^4K26vi-Olus5&rx%<CCLueOxo3PAMKdg8EjtM@ExW9|)1eGa6dcxOYRjJ8MkGDp&&|QAeZlkRjzgBsAZ=l2FC6VS-f>{2@WVcK++ud1*9Gl1QRr}Wb-TmW?EvL{n98<plH3Ezyl_+w4S7cToUBAWi=w@r4aQ3%bG!AzjLZf}EI9onk@6uqv)PbhS{~$KS_bA_CGTPAYG4|XvPDdJlpxmHA^EK}LxN5T!vC^fn3HvN>(TMNBz(@0K{E8*IMVvL1G)AKlqwJ^%^{~|0+mqWKPV&ZPS;LZI41-Djw8_feXr@XK$wz7KFzEHSa>K%)=?fZXMlBSIgo*SGY;FA9p4AOFI#@*S!-I@9kPo-51NB=6MjfCO7-BGXI1N<^LM(bdOVH7A9YHn<4}X@1!nHpsH1eG{<PZ$>zsKC*i)bvv``!-n(Y6;Yf9|kdqKa*+P0%q;Yv&H@mb$PTGG}{%Ajq*O4)SB2F6r#9j^h~3RFG^nQJ@n<5pX-W3CqVFsNYLfltC<8>)>qnSn>02<%L#2VNdQi5@zrY~nmbew?s5l--YLsw7yFqD8i5h<n;bH6`rbK)pId%L_U6cG&pXeW)3PBZwFaEV>$~j==J$df0VV?|ZcHEm%}K!+(SpW`t@WSeaIR7DpM7N|^K?%wbTVP*Oq)=2Bxv8QW&2(FJpqm>HU)hoLP{#;m&I_O4NN&^a4QgH#G_T-Uy2Rmi+y5M2;_Ht}c{KaY=rV04;37?EIz*q{juRM7W&bvH(@haJ`1NWx^+>5UU4CJd}RbmDkyn~*;ATbUcR0s%dTrJSrS*PXROn4o$aZEBK^k{OcaD|f|XETXn4h3dDws;uW@vbcfLuxcZqzMWmPENK!QjAWya>#HL|TUKh5Jln<wFLZ;tEVW&1KN;zi=!ytND%D?{PpTPaSgrAC=qrsQ-L;^NM^t<#?OpDXjiaL)(wwNJvmi!hLDr5^U+_77i@KZsR_b!h5hk3V?vmFAexN1{uRth`?Izy=iYK%hLr%5qI{N113sQPEhh#1ss|x|zU^j4Bk3{7VrEJ^*J@tj!vE#k>UZ~B|zr<~~JVITnBV+YdMp#}ByV!ixmd(Z3@``-+$`Pf;CGYEfN@PM^pIk7IDV+7{ve!D1yGdE;c_AvpHm`#XNc>Ri2#vEq`)Q~dR5V$)tPrFS`Yn$`=NnEZJiaCM8m2X+%{1&{fs6s&bRyIPBVT3H3HwOav}Or_yv9x`Dr7;V+o7qw2M&+#*tZj9(%Xmk?mvheWqj(u-UGXliidX|=)KZg#MFtYy@&TsjN`hQnChK|-v`Ox=z*4v9qO{r0Cb-jT>ZfNoEB;22mBcy(|jVJ)9GCUYmt=mhW|+FAq~+F`AFhBg=crhC$190<^f_oLdGQT(njLo!&#r$v-gmdxE;xzNKBYBlZKCTsXHO5%p+vbqshBRAZx@CyR<JU6$K6s1r0{QOJmaMeTM#3;(JoS>=4L+%$d*w^1Pp9;%2NVbV;X;rMaF42@sXGHvt5O{7Jr&+VqSEz-lV(+946veNedBtpSATg4J!4|0c0dahSl1ZJB4v=~z1i%pZ~$M0_*wA5-rS`R;5BnVo}jZ}ac|i}}bF>1+zANgreiWb)PfEn2}TAEb&0Q>~N`a>iiE2^)DdY9Hv-fvs5T&6F8XY$)eQX<n5hRV)<C-eosLstIxKRHHybROa+8=^&DRl0Cwuo+y7w;v}ILK8(|4*M~JJx@6U%!v~0=D8QZ%nP&pX6j_@mks(C0NZvokKp)P_$@p`N%>J~~0G|GsH5o^<*2FAx_I-BH!s(p}QI&vxvlWFq40c~+O}Fi!E2rWBs7wtpM+=MG9J1olQQ?dwt{OFChuTOyP}OiprL%+{oMhDFov!Ods3V}K*`rmJOe5xWh1a5-6F#vLvi!7ZRE_QPYor(M>)oiK6A&lwDYWm1g~Z5~$EfA~&N0$IAfYLO-W9Lz;3#9{!>V`FN64c$9)=Dbt=L-cC_`pw>APKa9oU!}+Z1$uhH0Z5P@(idh1Ph0OCQJ8TSDJcn7ZT0E0z%9u*1IOacBZ2N{yW|!OUR?^r?Fa#0oa(*8(ZAr$8&3j_g*8*?|bb0+$x_W|_W4cZ}t_FI{6AsWGQD4Sf@O_ceN_o=nQ=kY|5q2r0Hcb&~?d>Vk?DNuM4jxS*nLJ_t4ih!5fvc$^RbixK1+oEEI1ZN_KK6^1S_UiaEkhgC%`Fr_=EyPlmJ`$+pI-JSLH=|oQ#YUh&?c(@IUgd{N31wSOCOq~C+Uh*rKW%m;wGdjMf?WWMZ-(*P%{S1N+pi;Ak*#K_O-uE4W3|){(8L}%tlyZH{L^~KX@F~0D#9<;q@E8NLjDx{I3|inR7!j70@4aA3z?8ef#&a7!EOlG9MH|SYQ6*|Dmq3A$7p|I2k+}+VmG*V9z9LQ8)YfuxClg`;tD<bgkYrEUSi}>hgzt?9bv&i2V-H=;`wY?ojW_9qCf71CJWxT90V4a@1FIhW3Q%86BgD1!tRJ?W4i2~66P@JIcO1EpX~)%_rqFiWe#djbz(UD?ICdR6hrqvJ2qbT8UVZ2shf&BA-^6&*PJUqqB0e>ihLAiu+5^UH3wCfw{B}&b<M+(g0;j<oI)+UdF_R1Nq(m|Leg4rgl;l=&1PzRIHjHR6EI5F!$P>|-uX1CPb_W(PwDKGnZs{RmdZ38u`@x8(37~^)K^o^F8&3=O(HK42>2et!0#byWcfV-BtOl@Lh3#3;{Wg#nmE8reiR!m{53~@(w83n|ol%!kqAi77;B>p_2XH*(9_+k^)kA}7#2)I}V7B>nY^5Ftcw7{2<C6)PK9Gy3j?<~K&2^&G2P3-)hA$G5>m|MeCTN4!oPYvU6BO;(0Wz;}8!>t(>{>I5uiBZF+r*X2{t63p51TBKCK!-lIJmBexTBy2Ku5ziOvO>l1$IfDrA1DsGBZl9K+fI;kbHG?U;s}OnzjHf|0RZ&quxzgNG|C2KJ+^DJ0Nec%XJtK_IUcJ5M3mzB4-oE3raarlDdj#2F(bJ2_z!OA>V^sbviT)`Os_|$#Yl{NE)4lNY&moFXkTNSyMxHHk2NDsL|&dL)O!{SL1QihH=0`4O#L*;|<=VmM^zx6Bn!`XPxMtZtO0tzdDIsq94gw^ggwcn-?}srxN&<?a~TGEdbOk$Mv=9u*Wkju)#X4<F=x6%{CY|V+~~h(psdWs2Mzj$}C8<fN;&=q9AWqfX6Ig_tojNER1}QE*tQ%m7m-jv7o1E15Uac`EUzsbkq{WBrEXiAV_Cox6TJ{*v~_#4uc}#p#yKm!R3|S%}{d;GzQUpl*||GVhiXGETf5L2iUa8&R}?*ZTf{1uu^2DKyoCM;Ch&1usmxZwQypkHo&Jd78&q#P)0(R*CFhY#w@IRV7Abn@_tD+NuA6(|CI9#``S@{s|GLwFi(-ACf+2N%^>C-h+Z-5nQXohL;YK&j}M=fi<13)=qHd~uR4hB$fqkCld<iN)yQUSCmgvePl3r#i5<b~E><L^Q2=tz!Ydz4RAGT02um5}{U~Zw+mc&2cEZDD?|iEU=BL^`C{2Ow2L4!+MJ99!FHD56Lu=&DA}40dm7)irGggly*pl6J-xA+fn}=Ni?6U~l{?R(BsjxVX5Lp{IR2Vv4-{CWT>g*wCy<_Xux^@>W8>TMRjgAf0Lt$^B&!%p7aT1WYO;;Raiid*tJ82DLM{Sz>qjt?13*jFN-I}29(Ci}<0>Vjw1bc#*K5C{uCg6cqhpx0_x=Je`t+0__deq^7HRz5MWOB(`e56DEi9`Fwp#@M%w()JWpljK6*nADVGSEe#7cxua-5$m@n&$N29v4MUM74cfvlg##PZE|~(ji#yKJ!Yu6)To$d%Y!CmF?90fOaA$FQ8<7ScqF7xrD2f*!ynaU;fyX4_psdEqWQrcO}_Cgp8BO=|@|wTHxCaTo|$25W!Yj6tuEIXo3EZ>zccb^+-wDq6PwN06P@IR*B>Yx<GhZeMH}_778O+2e3w3#Jg~(IyU;zJQk<ZqD3<aZG-~#?8FiP%SaiF@DzJ^tst>aK&X(}f@|A4z*lq*_#IMOVa(49QY-i2`h@L{Rwm3NT`YVO^?owGn)Vzy4yOdAOo=oh6cM{CB0J`5B$Nh<C|<?lSLq`<CFr#La9dDM##zt=RwSrRI<}bt%`n2ZyB)9v$j{xo0P>IT3>{Tw)d3$pl0qHXkVAc^JZ}emzrhYx&<N2J9Wo!${oq6vU}b{+x#-$Y-F)bJ+_r67hFJIl)A$CO^v8mv!Q&Q`brxQi12OOM5jYyEz=T|oW}v!?8Alx5Lb}%d7lxLbO=%E=;BW94nl|Y3l*+&OEJAMh#3rG&$)?9M&sq)bs?!VhaqF1%LXF(iKq7RAOLuJ-UHXutPC4jsna04*TOXD<)Mcokfd>?H^iU`anlw8EsaV=#>Vkg`RWt`P)RG3JO_nJ`4tSSM(C3OS_@q5hL|Fy()qx)#w%f=5d7ZNT1|N~#TK{eR@sIz!zGa)WlP>~2YB)uF)S@d24In8jTK29r(EG4WzYSKWCdt~>8^Tj4X1PgI<K%>YbkLdPqj>QXo1K%_I5fW-aEVCXQ=+pSzd^q4(&7HM^`B~(A$A`)jSsoHcmP@VebBR8nZb0Z!bV{<Nj*>EH4z^)EmTuoyKYlfK1d|lYoodp;>}Y11d=MYHiKHwC51q(1D<2j_kk5RqBb<K*JB0Nl83zM%dHkDM^Kv74UogQwzlFVrDtu^QjwC!ZP+XhaLNgJikj$5M0b!pwj@EB9B2dcfJZvpvT=>Lsi(#zPmNrYFqg4Z?b1B9CS$R>t;r-xCxfCB&Tl7f$nzZOSisA(tP$o%UEDp7AA|nWrH+Plsbn^g@-GQBELGmFgHewCfC@mx!d0tp9`boa%8`*4bMSN;<`Z=d)Qv!(p{EmXZfDxfxSk{}l1e%;UIRuE$HSI&kP3<#Uzq92VeCri3a^3Zs!(q|vQR1It2n?rLp*D-1a4l`JMrGG)4@fjv0UsgY!+w?JqC88EkbFvvE;_Z3v**j5iDR=W~vw3^=7Kx%bbDonJ4BWA1$@CEjiJ|1EIK%$3)E-lxB5=Mi;BWMx9CStu-=7N=ZICc8!e3u6!ZKuRRY`*&J?R+T%H_I#!bGICB`77K(f>q<RX92Z>N<x(oWvadLJUglO`9>n3Y6UT_<uYkDwHbz_LE7<B(zoAo<-_)})tLWR>aGZ-FS_>*=IRX|EPxvysUoIT8*vv1=T@@HxJ^YHXKR={U{za_gy9j`+z$B%E_B)n>{hwutukDXr2b;5QP(&P6-AwA?%iu2&V2Aqd5;5;&qLn1wL2|1L<jL<P2^u!1c{5Oa1pkGCB2mj6>JCdI%u!H|rBRh)e!(%&&X~V%g#74q9HmITzqdZ1fxe4ZxPcb7rifJZ%M?R$t+hIyAB0I9rLnAsWa+ISv%;^<qj!arPltWLtKQu@BY(#X(Ck@Xbe-ywRna2t=M>Jc+a%3KjNDl3}9LkZV6rdcL$0Cv=`&<BW$lo~_hxSl{<j@jy9EZ<sC>Tcu#lb%^IF97!02oIheJB`5>Ff2QIEKkOB!(mNrVPMgN;SbZ@+k)JM&@}CasyK;fE&XiHw=kopbb;%0K`Vc%Tm0CF?o2j#&G$5U3iUOPhUoj(imm!BZ6s+pwjz=W(<>ibjXYctIG(?C?pxN8Pmf;GqOn~z>G{v0hp0_90ry#D2D-*kxLjBl~JA{kIK-WikOV-vl*13CzwGQ#k6%GGAi>_ATo^U)mV)3cLPBfm9NV|80Pd}2!QbmG&%w(#s*h75QAZOGa~%OhSoR`c2W7d8gfzo&WyFFLRysJEV9ozum$}xK`r><L4X$PEoH!2<Pz2ivluGpI&c+3X1pIf#V~oZc#8D54yjPTa)1i?b0|Q?z$_J*3VOaj9K|r13wVmmV-Zi0eKuezatS3s3PYj+Op!|{fl(L|i#Uqxa}ht0eJ)}rvd@*+iPBeQ;6yR41T|quECWrLQp+$Crc@(jqL5SymoO%0@e=9pGK_>NwE`ef^1_6V$fuam5yiA3HX{3+14n2NWvB>KY7rEXeKrCj3Q1WgMEX02fY2WD_y_%|2z$^U4RD8Cf)VRbNXmm9^d|$tA(v2sa4;m6KpYH-B`60ip#X8nJemOx#k4YHgDKSjYRDy2;2BC@m@y5-v@%G8DYb}d$Uc`K8VYF@ScZ}pW-LQ7tsKo@POrc;l)NazHkeXN5e>%VBB&wzT#aWae`mlo<PwayhC<Q+R71tffslsE*8^Y;6)#J14aVehP=h(W9N1t^-*{ld#@07VP{U{{-Z)Uh#?&(cIKu{4I1(tshF7`qK!%O2Z$u!55mY)V6vHTL9UY8eH1&=U%rK&gM~P?{Rn4P@G>o$L46Y&hsev03{a<O_O3zM>lhi87!W{Ic48$S%nSdOgWQ=nHaF9<4x<N$iMK)v}^S}oEDT`@PKg;k8rc@2bAb%KO47r3~9>akD4ni*o9lelf$`1}-c+eW|55utjG7l5G@UU9iIDo>&)bp!_C;TeAwGmK+2d&}3K?x65e&k4mkybw#i%|W3ofw35WUjy-l)M-QbWrtvqj3lKUkSku!U3>@un0TA?;L#XyH&V@#|PpLe0b_D!D_qz022gQvV?@-IlUWR27W-_xfA7qCVJNhS<*2@n%EuNK|>EUktS5dnz*pOSQGov$`Slw8U;z<hPd(ySOUTSXJ!0@T)YWFYR=(zjYW0P2}p3AT2O{c(CZmx<OyIG2)pX?*Cr9-M&T!t=o9i=eUvGUKH+#xy6(?5>O+V?fo_{v3qer_W{6#tF(?S{)ce{7dT=|ar(o5O;Xf9_v%rkvd;*m&&#nwXQO5;M3lx@ZWe5r}I0VIbP<NmfD;gMp0>3SDfxazMb148tr#t{f9Y4cTL%VT3ktb$>f=NIKYjc!Fp0J0BJTc?DK;t>Y=?x4$k!fmR=n1?TTpE4iDb;KVU|}3|QQk_X02D5Rpfk}Yp05f%;TnTa?4?h;IWqc0N$?4L_Df?=sLvNx;}uF{Pbe~2o!*6GPRFkdKY`zI>F_}EAt)}GLr_STevG$bMI;K~eNDeI5XE%dRh1+#hP{$!<O5RF*Ab8+y1#%FiI;tI_W=S@a9!<8K#Ji}48A)<Sm9axa0v-at2JaSihA<ejAhtKpN^nV6ytT<v*r3VN2Bnis4R&_k$eOYx4ZPFZ%9N6`4M||bi-~BfDelqQ5};4sAaD^Bt<(Gh-vQfa`uJ@M<LR16!>jvvHo}z9+_4uD22mODcoOmREnK0s$c2gTXcQPiaqQFezb-^2=4z0BqodvWhO>zkm3_Zi*_|+lY2es(|Db}9qh{J6Ll7*-D21ZCX~Nz<S>UM4uu>U^+i@Fk`ci$BUBU88bRU7Oz9{?PY{)o9;!*v=YXn)oDB>;Q6&Gw&Z(*K$?<LX4QJ@0TCULenQ#-yXLlc3$O&HyInlL4jyVC8Aw}xG;SIzXHa7AEP<{}?VXs%nX9_>D{^%3y4L;%DPw)wrdP4`FsE9q`4~#vbC^ablL|6N)#d^RF6Y_N~_=LNT;1hKjd_t@@_(b|yBl-P)*wIRz9yS04+0EPeQ*F<qD$#YT15ki`Z{o)*(l5L{|7(an;n0`9$bt)bgG2vZ-u3D5pgJq?J81d9%R<Nrk(FQDMiz6z6*~E{@h4D1kd0{7(YkBkXE!h;MQ=$P68*xjPYf4sf+iK}c|I1c5eAx&t0xIG0VWh)0<h(HP>agyGPFljWQkx1c*A%XFOCH2V?|hrTChVzlOPR(KVc$97)zpe4TDMGcctjtS=oRRt|_2IqL)*O9ipf7_<aK&$W*c=H^A=+;c!#0nz`V%s@M`lIIe;3SPhSTnAXBd=#|K!7G`3dktO_K6d@(pWY%IzWJt+Hx8*<(d-ucB{=In=1O}Fv*xP&iz=H&qm=>%{_imsvtwoq{AoDf@3WDS9S}o~)-1YzgC6q^uT#H;_TWK_js63j)1^HcW@(0$+14<<MfI-J1=njf00al-kQKFYH#g|BXP#-G3gjTaw!VqX8+ht&rrZ^K_6=wo+)zGhQ4m8np!IsWs8XRo`GI#ZG6Lraf%8(OyIl*fPKU=ao=meWw_E145IPc7$pc9iKoUuJohh<FuB`0;~7*G`X++pevDi1!v3@`bHvYR?cN@7sZ$EiS=gH{xlA}q8I(W|`H=7tPMQ3<vf_v&r=%{EyQ-I@H=FnQup5tc&W6~oG~6ov6-hhq#;VVgr#<cQ)|1*zEQdo2uSp)%@oUmB?*`JSyAnXzBY)m>ZF2sURorcdk@f>qGx-sI_zUmC0;d6xxi<VGpKwQIy}upq#%&o%tOgxxsc%#dcM1}{qR8`^w=IwM-KFvhEB%6{Y3ve1O%(EDDm4p$+gP)L$%xs8C1!*&Oc1XCwxn!f<+pkM5WYhWA;f{7HPSCExW?8b)4qJ?fkcxd~B-DXM`uZUsM)g#TN$4I3?Ebw4nez$mF1PjXRCcbGC*dy;k2hF&}fhPt=vGA2GWsYQ_i4~Qz4EzC-N*yq{78nf<7qdNwrBNvo1e&F9Iwr?uG)L~>$QDXKnF<V~yQ$C+Gmt4}28irb{8$Z0<P6n{=ocN2G;nrzSH`~x1b-^r-iYuQ?AERijDCT7L1*~*7wR+`?QTBF#xE60;tfEGz<TnZN4nYa>+_yu!n3+G87dA&8X&-z+?94xMJNnDuAD>nxDEWr9S{p+mmT;nudFUD4<Wy5TpAE#o&#cZR6vXiBMXS3$8W$Ylnl#!W89NLFlH$ThNDHn7;zAcWUr(GO9i^9N5D*EC=AcyBQAI=&|T_qh$ZMRhrb9Z9EM|WC{$$JrQ@9p_4up&Kr3Le@(AEz#k<%gzro)SNr;Oi!i6G|6y=Zy#!O)Zk_tx_-9nyo%abqb50kl-#g)ur7z>*!;Db5~1+}Er2%=dOf>|Jaqy;5|0n8@SgG(cG(+_V(f&54~A|K}kehut<iaeWm;;7QutiNn@_>Mz-blkvp3k)~0Ea>z74>=@-;@(=lih0Wq;Hp~zN!$sXQirPgMIumOqy*S~ax*f8I51DB$&nGmGY+LZ0P4pDj!X(W#F`j~m`H^Q$DQ$jwtNZdA%~c#v!9DXOav;#1o1LQe!3buv=zv}fhBAVTIlOafHAa${OM;f7^J4_5DXc|v53O3LsPJcS|Byez@G&vF*x8v+pcE=PNWH1z=@hGwA2hRL%p<sXTkz9;4>!3zkPp!Ct|^oCmeYhtRnIRu>Y>ed^TIT3ewmU@&Z~(@Cijcz8kp#*o{Lmoi}BCxA+xvC<z6TNo<}$27(bUK%~HGZwMG+gOr<W5DIn!=fY4N!W|8}if;&1M5AywDjLN;6z-buw-}Rx{7tr(93gBBpkrV18ULhMn7Hr31eTF0ei=MRV%pYWw;O{|D0?oAMZsQut@GL)Kg(B5(cMKl^Vmo<M{0@>3O6xMM!HSPWGzOKi`V}g4Ao4V>sK9eLWC_E8L2TOKZF)&LXR^6=0Mxe2bZA39QLk&ys)3AXFM{6>4{-s(-A1uy)jsgov!RhA#Q|R=}?|7I?1~j8;R1`Cj&-koes5N5h#B3J1P$mpg~vTIZVW?lC}2sq+Y%?rBq}th`NN(s~;YT!O<WByxPro1s*gWM9ERA9t|R_#$!yF#oD@n89cY@L>V{xD8oV6(r}P=3NInP#wJ5SWDme4Cc}xUF&R!&z+~(Nl@ly6zY3G_hoLYTD0Jz%<v>V=Fe5VXS_xXwovxja27y5^;msU0@07qY;Fn{w-r+j=xDf7)tp|qSM~TOXqsTGEhH%P)LpWJ125@Qzw>GG<HeVx7gG4|>RQV8LB7_-|0Xajk4TeBtFtFDI$B=c528nSvu){jCIfp<F4sZvTVHm1BAu$3lZ}CtbM@gLt(HlN;07jvA3W34Bln4xDyRDWJd+5L6rn+5Vzd8s56#<K{^RNb75+7p9!3SKa0=ZVZ6n_D1M8YrpD)>b!1HY)oU)T)4a0q_kckQ}eg1-R81v0ZnJ2d<PD3o9#P_qS|fSCrPF9?3oa$(MEwmatx0l&yLRe`_wbL>M`oGSdqG&NcRzL*jbc@j#3Mc^8pVM`!EU`+cn0gMUwkpYA;-fR-}Bd3VLm?qXnkG)UL5DXYgH3p+Q3<kp~fnX3NFj^*<`vU+NgujS<W8?^*_-g@u5s@K}e#+A55xq|>VL)H_I{ISV)h-39o0nPG#a{0(1iKi3x|kNc3vrz?>_QBOyHEuaXElg_%H!W3_CnQ%CAf%K2mE3$=s|AWr6|yZzQC&Za)B5CzYq!f!l5}UqAv~zV1N;VFQ)l4Dk=eAVDBlhEvldw&M>eGN);*@s9FWR0Cj~dMTb4iE?(XMV+p;`ekJ~bWUAd=F94%%&q(}*Vl34F44byIG`r{}8ZheyVK~r#%Y8KIuLop$6wDaZR(bXO3Q-vQNa4y+AOppygAz-f^Zx{9sA?Llml%3f!~uw;R|!o(*6Dx@rUl7iCQcwE9s?=oY<oyiC&YF&I_wJ9R~(;%pbX$+X}#1-pR11|e{`6PNO(l5q@QYf)ND8slVQ&UFnNZVnAo%T$>|3}WYB#X2V*Jfc#Q5t#bY=+9s}=AM-El^WDBp)<th}z<1r?XPYe}oLJR}PAj#<ug~rHaGk`H7v2HX*T4bbf3?&GM1!P3x!4VmrUk%8ZXge`Q{7g9beStEvm<;z(2c))N8Ga(hAm*^|(C%Qes2&Un%g`>-Gbkffv4@C9;SeYTHEo4jz@KP=Yf5h!G-DT9aIm$~a$rv-n%ysk&_FR%cLc~Tke@^i+V2H?2KN{^q`Zy9Kn>#82~s0gKn*up8Y4kz5Gm`9tjfXY-ytbdgw8<ovW_d1G=dx=gLIW)B2YN#q*`_j6~btQ*bHq6$<g?QrAjCb9vz<AlUTIVjq{kU`3wWrph2a+erzDKkgFgYs9-a`!vST($8}wW*x;U(05;Ui61;}M8#M&i;2U;%zy_I(2E2w~HArj-TEkHg0~{&)+tvfrXxI@?l`RXi^>!aPjX9dJq!Oj-<>^0sq>7}bFl{2*IG_e7qcnJ0zZwnAD2?gE<NFVd@7P;FX&l~p;JLjA59~CBt2nr>Xcc~f(Fm1q!HChwdQgEp<e0SY8>>M#=u@x;E~*N&hQNs?xP~y|HEh0oS`O5Z8DMJbj$MJ#poS7CMUveB(2zBP#Hd1MWb2cei=YfyS=~3oF{WXHY*Kjfki|D(F-RBilh>6f3=j-mke~_vf;mbV{9+tLTZA`x*sG&Tmf|lo-z7PEIM7B307J{1cuGnU7-W&ea{VbLom`<d<1mb65(8xb8UxFuSNb%ENgj>?<YD_&Izae*q6Cf+(}ik}ye8Ni#$rJ6N-PG3vv1RCQY8_LF@;{lfFyA#5(A1124dufn)I#$hM}gmfWuJKs0Lxgo*Yl((F_Pfm{1sg%~4G{B>)VNhr+exH=4!}F=W7AkTGeO120NZ7s(7a?K-@R6mbjzGuXAza_Cll0d}zuVHd8G4A-edT>yEyj%bm?EDO1qZrW}r_aq)<h%(HD>Umu`&B{<0(+YG!6HEC^gJ`6{L(RjfN)%BS5&j}&A4vyVwQq!7sCz%aEBzA4MY;{hMW)p1QozMDYwu(+I0>_GOmK_oF8oFNud7ZBO3@Zc)+(q))>RJrM7<Jd!EB+Kw~CBl3n?xjb1B9`G6pMPOU3rY0Bpr>$FKWr%XofP@ihZ0XckD|m~syyuc^!+LTAdD5fuj#w#p+Bd196$D)1gz!oh_BPq7pECTzCI=TD(*43@(6Gh4F^Pk|QDI`9-^Mb$V5LMe304S-X?qJR|()~G^Kpc7md2*V&L5YDUK`Wn})MpM`sFa_GpQ5Bd%{vvh1Zllq}%n}>2D=-z~SxALFGDL+YQyt5v13y@p#Iw)<pyHO`yDn(26OKZR6h<+fswk>fSQ&IElgcE%R!iqqP70%d4uXWF`<Wh|%5OA+BFc~}j3szN9(+ZzEOuLJq|s>L6Vtkk$5~PsijZV(B-E{ASZZ252~9?Vosef(h?z*&4<BdYv_Nn0-quXaC4p{WOLU!RRG<k}ItQCT0|x|nP;>CpkWxC>TpBr8NQTVlKojZln~s+#2vw@t$#|KRPiutu33>i&<IdDLY-$N$Zya9w#CByBZSfGm6VS1wVxco^(q>f&=o_JB6nH{BO!Nfbj>JBoR=~TE*BXB?1n&T(f<ufLJi*%^u_d9LCtG4CNWWKeDR--b-Y%hP5DyzWLATx*Ix$AjiG+vYGHW(tP>^A+w*qOYpLT~p6}mx-l{;qegrj38SmV~f6Mv4;7tQxo@-~49Jdr>rTJm^P4`kus&lEZ_?s+j|5)^X6=?ZE+0Zur0$uM#}+kl%$-dQtJsWO5l%$N!MA^jYQXF89Y@MrLlfW9(a0-ERsth>-5f#$My42X#mzyvxpGtRjUz)XNXjL=lJFEg+Sk4vMsX)~^7{ICn3BY8js9WDVIgS@ek0WN`yDXPFq=+~w;052iZ8k};pgpYo0>A~M1z{I1rG?en!$Q_rn|8jT<X`j}qK{~R?f+bwnR<>FSm|*vM+Ie{$4}B2OilZH$Y$Q}dnbKTcp|2WHf~;)5ITFKC4S=`7_@(pmSB;Yh=~xHv8o=IS12#QR#xt-4DuMIiCVr3<FX3V$<0Tw|OQ<>V`4H2WkO@bAI8Gh?JveA$pRIK$>9hej@o3CfCPsjoh_n`am!<q=UtA*=+EtQY1~x%!8#Su!){G7I8?Vt~W!PW$QT$AxI=38%nb2=|1x_5+o%FzJy@&}q$iz$22_r1PC0Zz#oq=$PqC{IaSRxYYR2Q%Rj0`LxkD}0OP<N|vH8h(zU4h`!G2K=G-OvG{E)f&Wpc*mJ3<`*eT_9|Fm%!Ajf=vA9K*&T)kO?sdbj*V$gb_4hj$`42B^1eT-Gv-OTt`mymf%0Ifm#*eEF2-DS@bURhlDif#7-{|EeBV>7SbY{sKQ#rp#eql7yjZ<21n6blHci&FEuR1gbgz>*7YMjutm~bZz&uSOMwC?4r;=LrVw#Z8r(t^s*G--D&a&bvXOv_$=(vELUl1`VNG2h6ztv-ev={&tRk=?=5Ghe+;!Epx--^5H7_20jEh2ly`&kK;5kTvj@!@sbYDE%hQwCDB91s4NE=j1MOl0cSOM}0<N}zBh>d88GKhr_E4#OZiLr!^m18UfK`ao2<B<Qj1Y-gF34Y>7t|`bxTU154n4{`uVBM}S%7vH2o`Bsg!(1TFLR8@_h-;%80T)Ww^*goU;#}yBRR_8d0|H%4t9DDU7Kkoz$^u<X`!Q_UuE@l?=+yk)ml2UKhqIXI-GtHN$r%19i+3Tx7E4C31<;nU7G|i$!FY!5sfuc>MOnBDMGROU$I$Ozfwtgi7u3rl*n&B79&CYJ{}>Dmc(**tG~+FnkQFw0j0xVtuBT{=Nz_+E9d9woY$J=fn6Mkn?5m?(!2Ib^F2t~5F0fnyY;nJFF0iuHBg9AxOXjl%hq}NwT@oP@Y%wg>VsNO72^*cDloe0^9ZyPi6Wk({cnc{bO92<*uz(9EL0mZ1u`ckiK?S>T(r6dWDzF7>A->u&!=f$dE0ggtQW&v{!DtJS1zNN`u^ylW-HAmNJ?$ypeScJFm-v2V2n%W4s!`WLm<WZfK#wRWzYSREmdiU2Dvi-=5aD#YBoAPJCp{qo%%#ySXa}o{btr(j6G$Ui1k^1iRrt_=6&52FWL2{NG$7z+UHr7OHqx|S?j}_a3a@1Oqe4~?*<?S}%<x?N3A;xXhiEqM+BvnqcgnJ3{D2u~zz=|?KxW_RU5?~u2DL&5)5ZJ{BV5P;7a+F5WabbTahR#Dx3r%478Aq?HV#mch(~J(P=z6D5m*5nYQ4Y;t;jln71n*kxj?B`fK^y#Tm|&15>_z~RiVgL39Mk%;=y1QA`|O^d9^pg26G9pVxJR+9M1^WCZEi$3s#|BfCt%2`kAXM)x(Cnz{Kt80VrO_O;y}7T*cu4R4@LDsC)xvj?~|NK~%+3h^N6VQVc-5V^foNzUrVp))4a`rh;XVsyZfZMulk{A*AB4ETC#b9f|^5pjOJVlDZ6CCm$2Ms3*px)f53J<3qqI0v?E*RSUhmFbpv&U`1vP5wHT+W`3>OsaY(QD=8V%&689+7*@eU3UpvaBQxs3(J=g38aW^Dz~6zvFhpfA3=vd;EAW&S_kRIefo3ARk4)$a84UyeJ{Z6PT_HFxxWW`X;L+4Kw?33bH&QH*12C)~X8{@7h=L$~sMS&|wccnLvYs$$0kzT%!&!ugv*<?T^@0_nC|Mm2V|<4RXmNP&!2<@I#h;(tIULYpKYK;#(_;8W5)pHPlIf9q)r`1EJ+ENbBo55`gj~?-p^vPRgR(k6#vb4aD4i=I7o<tzu&Q7eGE)qa#A~|5V9MYZs!<7-D3&s!Fp>u9zH0^O6z(n6oia#<u?<xy3{^`egofUb0i)47g|kZx6!PHBCv(UQuNjcVmE@_wYD_T8!OUIGB@|-A6;*%@4{tlAg-XF1nlqHYw(nG-HMHDAp*3K2$2NOf)AMIof;IkJxe={VR;CRTHxRC2wds@Re($TnfDK#)6pSnJsFXuC)JG|`%n58`X&`KaTT08OxD7LG10D0|ccb0~y(>}DwX$Is#*xQt(BI4yXHXmC_^s3^Zm{zgi4#^v&xmPAkJ2Tz0k{njrp=bc&VWgSJVMqO@=aM}-30{4ET8&h`<a1p@JRL7Mlgq(eY!fw1U5i9Vmgk%kER0CG@&_qry@KTQ$&c5m7qEFDFsp+B4_~rv5C`TmH@~h$6to&zyZ_~w_F*fqj#!K_YKlH;I$&hRvuCV?-6VM)LbERTn!n#0A>hY76Bf+Q5h!&iU^Np1;9gY81l^xM0iX{BZADA)R-_KJbI_PHZu8G#daVouoUH?XHP0MB0X}BdMoVx5R@Z55^fUZO|=rRhZ3|Qm#Bt(kVL~n8Q4z9670AN_3=L<#)CO!jiZ}TQ_Bs&4<$g2IftRRx#Td^&y_R-K$K5h8<oh@xEceZSgG8AWl=TIwQs{>7aN5Haop^NE<=I{4F@6y;Xn?7QOht8w3~mc({BI_WE!u$u=&7T8BfG@88ci!4gI8Ea$EAOmVrRh)6o<L!bBc`0wFD-Yj?5F$YMikrW67~zkrmzC6xhM@kmt~0T3jXmpHNtiYDn~rSy}zm?udNvqWb!gbf*Ohz;#<DO0J)2Hl8{$;<Ge)mxI_5Y$rf_y$>9$WVxljj-VmK%_vxkeovJO@BU!NJ4DjXJ}!qJ7RPZHe`@^*AG#92~qOF2&Kt+j259*M+bwI0GURH5TQf2<ftu;uEA?6P7dQD>3_kU5(rfl?6`*o6~P-7-Iz|HY&P3qrjB99&?17DU`XMyv&U75k)cJ9IkJO`(IV1~m)4Q``*gpV^3shODnjy3a^X(z3XYX(3JEeo+cXhEy!(hx<Ffx{;%%UYOGki7ZXnvMkaH^$BjKnaBSNbXooNnlN1kXUP(ogFx!yvBqmQ`}qGCo>gKYGWG_0l_gF%MS%P18FEDIE91S4+zztayBHp2C^&^f}m5n6q;Nf0_>i6+plx3rb$9Mg&q_@IK<X^6I3NyLq8zztU7HPi@e$;E&h!WeLaoE?Gxyohpm5&S7~c#%w`4YXEZi)CVM^p+5v;Gl+O47ZVakF0bi76$AHS_gs;o7=t1bS1NhAYtE2>VeN8NYL|+rdW%Nr&1Wn!FUFPZ=j_HOB5MKL*7WxVI<S)YFr7BgsGT%9XBHO2KurC8iEN$Qb!N1wHa4v?^3K#B$=QaunWkcOzND5A_46gHc*q@LMe(wWKkrEw!0A^l2EUrh$3l7*F7H(sl$p5i@ed6mRC})ksKA+zc`jeS-^xQkw<jJ*c)K|Wn*vfMH1>f?*yORv5gpZ*4(JTB#E`|H)yR_#NEJp<~X>4M?p7yr=i@$ziu>%oP#C@=o48i2{L;$v|NcKp@VpZBk7&OBpjuj98eIpW@m*DZgH|OKoqCSL6ex>P*e$au7D{?*1inKf%ir>9#n#NXVXv|5gOigdCRGR+C=6?%|phO2xbT<Y|*~<ar<wF8fTmkSoa)RMW|2HK7ABQLth1UpN`+}CoBi9ff%HV^#I{G{8`v<#-m&<7{`EE9FsW_XRQ}l0@KPT+G4a(IOw=dKR~CIBX6DsT!(I0fM^jN;J*@Bf=41%z!LhxQ5IM-DdGqURKZIAI0#nK`>2Ng5Ny}Wp-POP60Zm<c^b9K82+CO;`)&cp5!S%K-I!CK}q&g<c$^sN^<cxx&ndlfv3gb(2^KHGS1&0$^%H4Af`AR{6+(h90D8Gn`?<??_%$~9*1MM2xW88aQG1%{o|8kPtY43KQavpyZ{P|7AvAA5DBC?!caVeA(^5YC`o18FaXJ+*gJyeFdi)h*b!}HbB=(OVWBjJHiRYnfxa@ZX25ho<d^V94jPetl-+?!hzii>BUloW=HiaE$MNRkX75gmvtUpT;ZlajrbN9Rh4h=U?)0K2npvJ1IC4Nlb9UTxd$+>aYn9+dFl`KPS=p^dD4d2cqD3g>NM$4rPCY6dSccXUlzhYh5qTo+LZ55=I6Oe4cgu^ABA5xUVS<pTw{gS6itrj$5D{Vy_~Hm*MFyfnvMp7BL-yM^(#j|t+;;DxM^1bbJOtKTJ8I!2k-!WQd6G6d%p_$<P$GLh7`ctYx(E|F0Gm~RokNKbhpXAa5#dBdj0lnUF>42G7SD_k>78vhJzh{nh{$-YgEt^Oq@Woi0*~9QWKs+W5nx<(pjkABYG9I{g^5feyMZl}M~RHbFelzop11-$WRKr=0~<CDvN|<Fg%ANY@1+otgEe}Y07P&ayevFq97YcN5w<VePy>J>e~w`u>uoT@qu~%D^!kYH%0eo~{UJostZ1%{O{+SG49BsjcgJ;!=OgK0hU`uRQ`!hbn^%GvB=Q8Mg6300RH`O@i!hPh0uL)9NP2>N`VPyj0!l>5M_@q2w2d$knF8B8=4ms7M4n4i{{WJUK20RbFd{o)z2d&IWIoSsup~F*LlT8TZI_|oA-F<?Or{zJ#p2*(uwxMKK*`R!z#&QRY67%*d^aXlXTRB`ODrx^@YjS7nH1{EE)QG;b0Tg<76}9EDWL6<-mL(5^`A%?klMOnX&I3U0Q(!bDoQZbAJ`IcG-ugIKs&Wu+R<CV@<6u+V=agtu)v*K^biAXXrr+}D^RuO$219K14(}o=%>L$sLL(lr+0v#jtm|GY%r!u>D8FtXJ9X?(x71-+_Ce3wR`9E#2%=28h&#txY-}MZ<NRmyN&aXGo|HER`x@|hmbVkx=>vPf(VZ)ob25RhpNwr4?%vgaqtk9j)RdQUM5ox6M}4MU5F69z>s(lqUO5sAgNdz9B6}>YbhRtXLA4`#M85wupn|bXj^lAcn~d-xHH~4&loIKkv1s71LYDEThM&Oe7p(@l4xb1J+^S`C@()S5a>b+WcM6ZGAPUjYTBOm4&`80kuAf5jMtiO9EM=Cki)_0BzoE}f&`hi>qk^y$mAg5L0t;fHrK}K10&*r)-c{IlCY7;Do`*y(0@h({&-H-LW&X65V#IrD&#H`(4y_uXjLPdB$43a(V!<f7TSr`$PYRbp~a`oA}vIy#u3O>Mh5`NEgmp2!SWNXr*DeKq|$;`F-bi+WKRxl0OSK-c<i``?lv>c_3pr?fO%jKP!;ZDT=#{Jk(q@~L%c{poh(2<NR%fMFq47NADRlJGUNduyQzi1dIBt>FpmHk+eyBx4Elo}P|3M(zz4AjnE3$pr-+u<4m&2ps-%nw>*2Ah4HrmiKn;)c7{?)qBE=z73eZT1HZ07;SVi=p7!TbjCI?kYuo+l}vJ{@ZA|Xf<(xD!cQ%_Djv15EH1N6XOPr|PZ%;O3C3Ch)QFc0MjkOl|LDT)<tK8Ng(K2T&F%BlFsdO;m~J*!DxLdw97LM!gH1e)uD+s%PG*wAeEZnaH_4tRD#VsS`b7Atu`2hh3RHs#5oET$B?f(ob>3-ArTX6$7vG{QEL3S|*hWge%o2Mqjdb$OV^6dqH@&7-i}*w)TNG%!Px&yg#T8S)hwJs!Ryj!_25kZA#=aHB>v#?y{>1jecR7|lQo<;wu!q-QqcF!)irXYDwwxr%)n02nf}U(4q$!Ci1N-WY4c282=>H-?V7m~y&Zyn-j1<)JY+&zucf`sPVe2P&}@oV`Yj6W)!(2<hH=5mGUYu1(mE<O&Ot9^^;E6=sHz2U74Hb=$l^G9U`}pr{d=!4v7sac)<6GxNv^ZpXE;LuS;(ZUGGNDAm$IO@;fb!zH*0)U3Em8Jq;aR0GLkB;@VJWGp#k#B)>>waF(tO*^|z6)++l=uUL=cxGJ0F7k)yvyuTtObMq=^AXz7oCynoJyD%B;vbldW0<cM^ltH)juG;Zb~u~40CnI5{|G*NMU=ySyhj*}!61U@s5~t)z#OC!OCBb<gi8?)`|+aJOkPno0UXc{3nL)rk;?EDTv3wG1Zg0@a!9fXwKmPcYz8%q^R~?z90oYUK0hx&j8F#2?h$+7wE}usg<_x-V9}bU8Fn4vmS7mPY*0f(36nAqgO>ehhQOuR1+7FaOKUS|f%~5%2aeqKB|rt4d<4JSPd3UE>f*L%04(el$j*R8azZs)A$d1;u=q_Ng;u~FawPHZ8gL3}688_%yMv($boLtg-6o`F?c0G+1(2)lfQ&KbYh>n3DKb_f6`0wfVoG{He+<1Gps-s2v%)uc+e&z2>DgQvK4G_LBAbK!hX|cO1`ZvLlz|hpbeTE|SON(U5I}L$X(@SRc{Z829qTFlusZ489(vt8Nz?rTHyYxQZ*@ooA1NT=35rBCld$G=ozq-{h64Jo-y#EbI>PZ#CqdjJQ}$fqt{VwMpwqOYG;q0}c(0P38`@qIy#c7^!E|>l^yGqqIuZoJQ@lMQVP%hJh%iTxZeCh^j0Nq8pa*z-s8tAS7SD2cDXHTfnwOer+c7ywo{HTg1eySq%^L~s;E1Y<7?5^-0qH|C1@x3SN9-H1C=bQK$lwOkbZku5XxsQlV|dspL1I1iH!;n+(pl8eS>ouB2a=V_&*x#cntTq_l2XKzY?VDZl9HZeAEN{vOgnTCUq6D}O7Uq4-}U$~XBux@cw<Dj=fJ{i+Cfd#G1^EKV67ZM-M~Q{(9>A)H2$-jFA`~M&a+sqpsTNUv88&>RqoRJIywvjb5&*u`V`}tI@X}Xz=T8_jO}BI^$=hOy8{fpjC*zrB@A!g6pJAH3#p)8z?Rq*_s(P8g1)(gXO3<}SCJZOOjC|pmqi4E$b_xX^y;iqo5dg`dVdy!a0tN%M<Tk0mq8#*cLV$&aSB10>fNayX`$Wcv{D?x(-?^(K(D%|ArYR71I$gE-YWtTo}eGrTrO7*hafwu9K8h;!nk%UfqR_l&@l)iM&fD)jTwW$39wpG!|mN_Ha$rvi9XoZyQS_F7QqKLeVrw+q-$&gkO!J86J%x0A=iuL(IpeGO-S~D^=NGdtAI6h+P>HW=%yWO7=-aS%wP|=Mf!M03Gg7RzCJki;F)K~GIxQpRS+vyE@Y1mRdj#(#vl;(pp~S3V*gIoZ4GTcH@2J3w0<EB!V}n1NQX;_y_&-y1bp8uX=(?b!qMRzdceuU%{Lp_6GqMjR6vO@2Hr;E5cZ>Ja9X9^O{&?A*SvS2b_X)Dcc<;fbkc?+)$UsUN}&kTU63;^*g9=Gf6UylLGP(c;~)njo;Cls>X_~s!I@$&AKw3iW$0~H_X6-R=!lv#Jfq^OkM=IM72khg90J$iY8@)w22c}SQP6$b8;VQNJUn_~Jgc)BV5UiZVh*$)b(7;E;u2s25cLPTjSaIBT702<yRj1NW{n60mXzH@Z#+!zQBsPA!XyMu--Yc9t3bQ=a=*}o^3z5T6iBX!OC7ACm>1Om1zi%Z3!A`)trp!6WJ_h^!3n#N@GVdcKurWnh3e`NS^CB!VwkvW$FyT62~~LBu7)Z+Zx^5nEARbn<)gpfyYfjDSmFN+0xK-fzq&mC)AIal%kv+uzH@%%<eM5~q5tD&tFPY5f)<t+UtV7LYI)(i<;D5s#m|e_h5qOB%k!7}r?2-<ew#rqEHA#dym)1K;fLkL#pT75CIG|o;%Cc?uPiTKU0(PSDqmh)!V-&jbS%Ta@4R;R=a2i>-cOMX$uq+kmgmnc&wsZ(|3wDNu=3HVm8J8mAH0~uGW5Uu>F$s3_OE@xuQV{j%Ei+wA6;HM^_hla;HFk?pIn~*xdO;=@6MIA#cM!^$0t`l{Kx9IA7mg5M7^cug^SCJCwO!w5W~G!uB^WE_453cVjUSAL#{S@mlW7AM8o5gYD_RQXO<UlEH9p-iF%8EEa9XsTu0I`yoSr^#QfdcuVLnF@0RB;^?&;E-j$zM-o3dz{~oQqbIT_dMh$jYg>K}!y7&WA3DaRk<3d}+AK0re?*05@|J6?+PygkY))p_rKvWGdinBCuy$For{PO%){WCX;RrOE3x_0g&kFf}gSYEt9nZI3L{M)@tpZ6Ef^uPb20v)luaG8oMVIN>PSP(m71WMp$MdII}CVnnOORS#zae4m5<;72UYp$KU)jxOH0GC*M^`(2K{y_w|hD%`K`{6+o&j6|aedi3YhkxHW*+2d2+KDqO@4xZyJEtnp63Yv?`<EBrq<?AEEdXD6xqo{RD*5MiE?tVANSmwxPV~RJy>jDSsIJpVsw-kAj6EqqQ7kWhMeF?{<$ZT~@$dBGQ!}KZe+CxGUspf)SqD_Cy>fba{u-{s3zt_feqTgYtX#fw_x2ad^EZl!3TC})^GhoyE)@|KM1NRg?;79~YiD2UpZOeCeE+8xt={`aNJW8MIY7nAM<@ChFO`uikFHpG<8uGY50FR;%<V4_XF0j{%9$L-;_mHJ_b$B!5^3e#>v^0-|KeGm;{wKFb?N(+o1dUOq5&&(#mcqM*FOF%fmhtU{VG2u01L>@DH_6}|I+2VKfawzNENzb<?J;mp2<1@UeW(#VfDkCTn>o)?8@2i`fvVKEy(quD^{-G?0<LTxumi`{^s95eu6o;x^i3vkC3H4(2Q2#`^yWjmm(@wzj+blVE@gN%L`{ff#{$4>fR!7k}E|ep$M@cE_oK#;>!0Q8=w`5xQ6OhZhU40R;;`Vy?b@_<~fuz^Zx*L3w<xeSFGN=esA#;Xz&k{%M0JolDt_4uShZwCB9ty;N^SYd|QgHV3mh=kG3-^u@!f3UxUR7b>DmS>(#e!Ay52#zW>Gts&EOyf@u0zVlONKKBFCW3d;Y!|JTc0c38LtKCOIsdwKqJ{}t%Udn@M_mgleXI6&5|-nzE(`uwj9ZBa%5kiN?cKT6Sya`7!zXHf>9m`}A3oLJC8Ugtdz*+4e;-}oWXMSzglNgyOhZ0rV3f0iOj$+-$`f<Acf+PClu)@%RO?<f(4{_;F*h)<X2-$l7fqJOjqjT~A2edhzLZS|eYI#FP3a@g}<6)19v34sG&{DBAl6%U-pI4Zct%8kn_FP?!8=Z28$J4}P@lp4b8YiCa(f0{oJn{?$Rn2<}_Vg`xwx~^TW56rQ8^F_!E8_Mdvr*g6~$f9vX7!D9S*fQ4!vxR;5`XW!s^5PqyZvkOsP4F6}=ie@KRlwqts+bEH034F(EdEf1;3({{AF6;HD0_({FoP9Hj)Zc0wj7p&8DLokGn^w=25F|Kks(F_)B&W<H8v!ygT-o+0b8UT+)ftP!M!U-c5o*updH$RtHO5Vri^z;%E^XAc&vfV_VWc60%-=|ZD5J^Uwil7<!hj;RiHd_y?Ex?)mtE$-&p<dOXQC~z?)O#Xt+86_+eBYQThA+i=;FClegB+y*U{C(f{bJd#~PxX<m8bEzpZl6V&wWGTaBNf539M)augBUkdU8Js~4HWrV;GfP^d8K11#X+RxHWAPVZm8Cj?8-}x{5r{BMO`-HULQz?dWN|7aFiElU{g!#_eDI_V52xjpgSJzH_z>>88^2@8&-a;m>s14oF?P3zar`Fy$3l>eb|7oAg;UfL7e(L}Hk!(s$K6Zgj{E;9<Sf|q$8_v<2uS*4s_8Ivf5^;5||LINCqfg9BWdlcdUh!+46j#*-cxC0opL0YQ04!16`ZA}VW9O2Nf(Em&0M;YO-vI~{jYnXW?<qs~<nsJ&9-|Rsg3Lf0xDjSj%#%l&X#C^~ETBBrgl$Cw+T`vJw^&uXZ@|ggiBHi)`s&60hyTE3bnB(%`IDsby_l$whO(?tn!qQS3g@pT<`k^gb%9V;&-~Q?2whd$#IVm5Iq1(gH@pfzI=>ziN?9E!J1H}cmvXbHSq~P4lW~8S(EurmTY+h(15wz|!8T_GjKUga7K^g>%IW^aOT!^i^on71$z7ux6uD02;3+vrH<V<rak1pO5G$0<PGRY|1Ug+jwQ}aeV#PV+3K;flSKl{)R#?!jes~kK3=?4G-r~)*#ml+(Icy2%!8yDNLwtATt9MLT6*7om3B8_FW(2Av*>d&efhucXoYgy)N2!1Yw0e7<q|G8&3Lqy9NR=cLkf49&EN7~~tn@E_z-$Gr_Mg6AdG|W3{NMc-a35ayCgchffZTU)-{$iIBW?vM084{CK3KKp1vcYXl(WcCz>HzRX@)7vaeYv4Zhv_1!gVv01(nFkG9{1}b|R5SM!JuH201Vb`+l&pZ@-2qE(Nr3J|=YktCwMjOzBcc3m52r_Y(S*zItc%jaQ6#mj2gY<FvnaEp0qMjHHXXVdMcVte4*X@$~A4xATaWl^dVwV>Clra+3*V*53WrfN06B63EA%Py@7O?ZnG^KI+4_z*3nUI>d$Fu6_IoC`qfAt}BnRhI8Q@$@sEB7pWwx0p@TnxgHZkyvm&};9c@m`0^V$x+3UBdi}tv(5Em1e7Sewb(*;kr1LV5d*QC=T{og%j00c?co_^PH;!D90vP7r(v8)d*J)j!M6(CC8VOnSjGii@V^%I-Sh@5*Rs1dcy-M&gMI!(N2JDMckc`pL;5jG&I@qkOLddXTTY`=0e|ZX+1p0L=&kD>ynbbyr*`w~|Au{|f5e+7M3}jh*>GbN4Uy^b3Dr96SQwosL)Z;JFCZE44&-oTUBLYL0zbgUD=tV)?uu!W&%Ve5Tgf2zOWO6H_n?W+N-^!?E23HP}>HqNk>Q|@O0l#|t3-;3Iu`vmAM9l-$aZp;{9srT)zj<oq<G<4C<fVQC`=ng?CcF%L?$H&m`Rxs`ndQav%ZsnkG3He|g_uW+37g<0{oWu5O>*L&^Ailf&k&EioJfq-PZz+@yLb6y|C84Sp=Us+049n8Q?94)h$>gh0W>R@UT5C7`o&AhL2Vg!M(35w^9x{6tekmsb^fag@J#=s>tJ@SeDf`_gU{$Z4lH(9<Vzy}(EzRP-i94<85&&q29&X@s~?|O!8v}b{}b!8^O`ujig{qQExeYjHa?-jDPWa)R9Kq+$FI<xg)d1}#0Ag00{i~{8>^pzoqA>M-1YvCU!(Dg{)vnF7GeWO9tCU=nr7wvJE;x)($z#cWfvtb$rJM$!N5p;8Mj52a_aE)2KQ~lfi?+os`fp*2#IKTbL9JrcfWrt;n2y^9uA7ln~ewIq$hqC>HgA>SNkV_P{#=8SHaZ!`s@Bbmav;AK2Gd&=<Mp%*I@g~Nv3l`DWusp++bYJ>e89zg%^3sHCyR&k=OC;qJfhv$JgIm`TM1{&(Kzr&Oly{qX6slzdXP8!H2pF6{%X{it8_&BOl6nx;AvOe-YVtazdJNWxgjg65!72w@V3OrOtc%Rb)puuajd($vI~73va0#8r0?QU&n<DRDJm}?XI5_cB{(*?*6FoJ;_ZV7zT8R?&;*ORp5g7=?!uepcA%#=iS7`cK7yT!ar8Od2{95Ep4}r2=$X(I3i(P?CjOG`6cDmKt%{9f{)sD#+S&$yFY;(xzYb>0siGh4zf|M@R4DGSe%;07TP8+-uv*CdoO*L;dJwtSHF9e*3}ihs-fI#*QE#>DMW}D^t~59K$@a=<i&d++<}j&J}obtM$WQuTJkY%d-l&<?7wuIc^zHRyh5w)b2^^9M%?EUN%}<ArLZBqxOM6uI%o(?3=J;SKk-@yE0i;c3Yek0KYrAId%pkX=`3RC-sKZ~D^>!A`Y$b_;(*-zTnZS%&5qM?Q>8LusDJX~m5<K%Ph89v$-sv0eQ}mA1Io;=pDluh=;j@ggZ=ac(2#WEfB4D0A3n>%g;vg9r#1hgZsM5{L;BqfrKDYz_bh=!orUdjMn@3wO+*uZDCe>Snr<k9h%OU>B>3Cvtq;&0hpdtB9itvX_W|EueeLh+4B>4SWr@d}QAA`XzMBCOtz160^8MKqM#QdK9Y~~W@f!gnO0K`@rLm(hD(wUWGiZe|gXyGzhj%|{A~qvsKU5E%L!aHbH|hLgaI+5&S;WqF;u!{0pWEaMP_Rm{X&4JO2|edEpr83>@7k#A#zi+Jd3G@K?GH&-m~Z856c`DWmCLW;2{l?xRil*S`%is*{nPWn9MPZu^0)odH_JNvD}^W(d`(x^J~+2__H7vD>O1F2Z+eYz2B0^;j@MQ$Ur8KftCxO&nO%G33}z+|756$J4JRVAMOpP0PdCU7+yD!2(H(P{s18e$3t^zazXE)Qj!92e-N||YY*YTy67@E>Et8u&?32oD&-pJO@1Hnbu}dEm@T4xtWP0>?|F4%}!DV|w*V%5LzIW?}T7Q|2j2QX^y2skP-=c;mub*DxmQiScYDEYCH0Sd)+vnj&?)>>IsZpQemcRJXy~}Tu?V>@zsEkxq$7;!8=X!xrdMD+nc(z`=<V73<tcu&q3zx_dbTW~Br68#a;g6ji7BmGN&~F^@a!GEWo!The6f{$PDMGuC_?=?wILU_V5GBW+*xTdBkN<z&PklQ')).decode('utf8'))  # Replaced with compressed JSON by the standalone builder.
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
# MODULE: vase_studio.schema
# ===========================================================================

"""Unified parameter schema and validation for Orca Vase Studio."""

pass  # [bundled] hoisted __future__ import

import copy
import math
from typing import Any

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


_STUDIO_UI_HTML_TEMPLATE = __import__('zlib').decompress(__import__('base64').b85decode('c-rK>Yi}e;k|6fIe}#9>P9w9Jnal^tVzH{&$0AwPoT)07NOt#h*VJ-@nUTzBW=7;hM3PMQl(4uD2MIVma3^RN2LXGxk{}$Q4+ov@7Fa<iVEdoUFW8?TGxJCIEAqjr>Y0;fx|o^%Fn2dMH#ajkH-GZ^!SVjtcW(~aFdvV0KYM~7Y!t+oPb=r=N3W00j`m)jzubHM;{3eA`cbMU9~_+=?w=hUzoxt(4;uL}9EW<5v#$<c9YQuj4ud{?jKe%&y<w1MVg9r-%?FL`3R{;Mae(!&qwr>uq<Mw)k~j}zD0ma~^WoEecpde^2K}hBD30<d7&Wq9Fbbcxn=K9~kMdEtdz|(H_Dzt5>@=VDqvXjtPyg&mme25WCry&P{@Gi-<NYALs=Q-Ae#Tg%adFuQCX*fZi}qG~yWM*%6DL6&jxagwv^rZVxfi5;NbPKPw!1AOwJ}Vt!xZy+-BveHc~Lx><_PFv`%ybo$#V3KJi*pG-OfV|pvt{SsBWjd(cV_M!zuJ3y}SsjosBx{Jgl>Bx6WG4?X8+9lcfDHZDi96KnB$Bw!2#!Ei*4qllT(yHrgB8n__@@c$+uIK@>xJ7!EoEBYm2OIQB<D(7otr8U1Js$y?#WhuaT%ast!R2zou3RLE(yg6&6JPL4uYt93C5Hr@Oz8RTM|tvUnj!Jn;79B6y9<`(Az^H<o|78SBQ$fsE&xuSM^+nZe@{U%6p?1RBYx79LodTEqX&L+&g$QcIx<VJL}#kME6tg``sWCz55&93Zi8uTLol>xf8Cbve~7%=<DN*lrSv^z3!kRVEeINM>@L0T1K$J9EjoQ9W4$i6<R)EScVC~Rc2EDy(Z_G}czSFeKJDgAy<#ZM9-tEA4pzL>`Ow9XJ}BMZ}LP}ABPCvmdFD*FMfynYn0{iGiP{QV@(l2MRhtIuCSnZ`+YIUNNl<YAR;67+z~-+yK<x>0mF%-vO|Q<=8v2J}CB)eSZW4+nvN)rCO_bK|T!3y`(y`u%Vt?3Jy$-ot*o-}9}yO(3e`PpkQ;RkHB<oBdw6;a_+c+r4gY;4Zv&uhZ#VcoyE~=2q)r%UO62FSfTl%Zmtn`_aRTc?<91qpgdD3$F_drrjY9)9x&@@U#jWo1TT&zIYUFT=*7V|Iv2Gzwr8xx~<OU5(}?Q(^6*}wD#IKGeC<Ei103w+eQ}MMTmbf9gu`T$3c3D*r&E9LBCIBT2vQz%Q}?r&j<+ZORzFqtzTl{VThDn{6^dkM#;?%8%981F{WJvy{pSKnZ|v&c=-Y#-1L%BlFD>N2$V(Za1e~6(M%RlY@jFrBMOmIG&eb~fE6D$RJWQ$e$xy|FC2wENQ;x0Z$vlY#Z{CGm}A%}hcxUU#vM0;ZM9Db*x8XKvtF8vMi)V<V?yvU*&_XX@2k|vQ$Pft2@NBV8UxozftE@u4yWS_r=mcmzOD!>B89V2;H!`3^aug((1IuduTeTDrHg5vCou{pz+!-T5>lzMF<ntS1df_pv!tbpc~>a_x|xv_0|Xw9Mg+1SWs^|=;0B|Ru#BIu@Kb0rN`PPi%5+RbHkU2|`1%9(6-Z|=&}T4z57t#{L!Rnw4#?m#ZbYzk03s0wVT#E=OtU;1%o;*++hN4@8y8`I6LONj3?|q%Ck?fr9>OY>Tbg%K&<3DSBCz5-0XEl$ny~LgeQVZ<)7BJbvSAAQomj_runqLX+a1>73%Pj#l-6%xqmz|}OM?;H^Eiqd0@W?qEOZb4A58N^Z)cQTCi*(*SPMn|w#fCNiymCjK&+Qo1Ugl1cQ^atWnGF+to6&f<mNQrgpYgAWsxOFRNF;eBoj|1hK#%z=9c)ePYCM@UM$c<l6tl(m7C}<prKCDNRyk@=T-14qg%ytz7do4kZ(&m!|f`D8|FFEBCG+vZ8Qam-wdHiN)M6i-lV~VH+2oXm3NuANEv4na*VbfmRSfEJ@H~n_N*BTvdibo*-Nw}iGeMSfjQfi<Um^jFT~g*K7*oDRGTFD3^8FNVrP)_rko~{X^v!H>{dF2Qs&&80BPc6Od^|uMlo%SOOu3#B@`~&ZSQJ*^k@z@LkV@o$@8EW#Xo1aZ_lAH6lZSbDuD%41;KH0TW6bF*Eh9t9@bJk47xE*GwjDCi6my`&t_f2fK0I`Tb~<!&z(Q90!g*GSmrYAe0j?5K>*C<nlE)4+aO8DLK+zbdH7uwaO|Nff_ZP!+Vt-tuGHu>i>rj1wd-n=-Psa5u1^XjTof4~VnmZH%I1*KO6%Y0a5f2hd@Z}XMoEJUsox_EqtfXtk5*H$b+b>ixL4Ap6=!qKwrQ+Wzf|rF*3r*ug<8@Wg{bMYU9PI=7Pr^!jD^5XanxSby95(+8LCmIiFJS>mO;{1QJR4E7FN4kEf7>J;^-&2E*3pBrJ{#kHoM7%+PUJnhBte5v3V}$HUbhUveo4TF^@jb7kPXihA@YO^cK}Nw29kL%Znf1CclEjFn9A>q@Y?1!b|;&_7h|8*udSy+F>wFr}ox%Hb=t38R0w3PMqY`9hjKlVg!t&T+*_35#Od{Ynq}RzK{4Cn!l}3Wm$pCJSaitGn61VIy%|_b|V-8+ZGx*R&7K;H&o3akcUc~g(7@mID;<JCtMyNRSPsE6{>}a97BJ1m4^3vSC*TUrTZr)jC$$m{4yPus6uPfViN!rt36&#YFWtW%NVxNulamh7F~tvO(4FRL!-efSnTZEB)y_l#$KerNHpugjmr74(1xXmBbmCn!CnFgVsh{a3}rmQb<yBD9`Lem7qv*J4uVa!yFsFBdjPZC-P$OVZg3U>0Jk69N2fG;y1+EyYo1!ieOec3Q?c7GV8Eg_mDa1PZGS;+UY#4Y7S4j~d;?G;rG3Rf<nFQp@-#yar<a4Icg0>M{gAy5uA|EUE3mWRB4bsKF4!G$?+>Bb%aDzsWQ_=_4;33Z7BuEh>3<*DUSw!@LgS;sY?N>GvWpG5<7=2!@Bo&Caj#w4;-{si(v_7(uQ>17m=O?(EV@LZZ`ZID@jaPnS4WDb*3A(c=E)ltz^109{RwgAvM$cIPQdEehf!wi3w9a`IaFh%h=KV6%15*Wjr+Bavh=s5yuk%15VAjoC3(we#j?@a!lut~M+B(JW7Ekbgz3pbzX5Mk%B|%@d_N;2_5UL1U%LHom9NrbmI_|Av?0p7NbXJf)&Ld~{F^k)!aOVFh6yD!2GIy{UTU%>vO{@(he_)|!JQG40zhvVO-w1cE2UuDB(PbI;4)->m<m-`Z|8AphXubk2DdZ^tSx6H^~!l-R<Z`lWafk{kk-<05(as-Q<oB3i%V-Y+nS1IDs}YH+B79Ok2E5sr%qwWA;M8ya+1jXC=H=cfTNX{<wHxu-YQ7v(<|78?6RV@b;Gf?Ze;exjk2RK;3%xkJ?Ff)3am9?km`b6SZik)j-?SmaTqKtNZpocLh5e$CAg1pCZ=_RT-kmsKM^zvE9335V%eNi7Qg9qC5x}tGoVttV~?8KrMsWvS|7O^{cxm&>SAGoG5~xgr-e-}J6+x}!5YLbdG2Ic65IZjykW9-pL$Vv`D}OiKUia1E+f}mRLW#-kJ;B<>>q(FEj-R$>UOt%`#~05hYbN!`g=GknQo;l>9S<zG<&92L`ldy`$0Ag=P1WkUz*7zjD13bRkS!-we(?qvEK94wd{Oqg`?LEznCJVSS~!BhL>YRWuGh5r#DgF8*-H)yqxFA@JBgJ?r2K1+O@Hx^R(qnTcUMNeC>t%v+Kj9ny(n!Y7&~?%GNnx`_mMF><966kg;dUEzNTe6B}Va%9E7D;W?turx#fY3i6uZe!+X&<3lhA^I`-V^Bgy&PN!v_6!g+0%Z5S3ry!a3hT`Z((g$f%)E@Q)8gcp52kV~3V%=WFZ%Hw?1x`yo1*M#fi!t{SfYnGr-A<++@3Y0{qrSFQ(gRDnvA{orR~trg?&`nNZN?pcKN>5A@)Yn1TiZU=Op_5ep!D)|v_O?Cw_tRYZjMl3;y$eb0~;9y7s5<!vi|O3xyxW$o2`}x^*R_8EMg@+$V5Rr9qZ!t<~+jx2z$zgrG%mNUwRN}8V$*OD?0+T7ua#$7i0c#=OcnNjibEGwo^vghFsE?CN;wC+k7^Gbq9OUWmtLFq((Eo1b)<fc!LS3;ZUfjb=sF!!hSbbb#8K;ZXJ|)%o+;@q&eu)Z%xy??=ZWTO3?in-UX7<JBrdZ4@uJ>vdzx|oI4>KhTeaf1{d>OJKEX3v8O2ln)Q<|Q&rpiA`NG&XUXN|$P_W@>&i}*OEN@dH_oZy25)T{!;WySuqBG_hBepQW#>3nlZBp8oWE;uTRKpqe&NpU*I1(%)R1yLV>!R|6@4eRGpC0;I~O5LyR_GeS*cVWmv&sP9vh<@(%*HED`}quozAk$N?RzU#BL5jpQN4MFzj7{HnhgvIautvzY0hLX+A%W-&EUM(mxQF4>0p76yNLh010^H`7)THm_p}0xSW99FF4_`g~*SjpLtC(i(PYNf16=kc&IFWwni&Ey!{jhLdI=^rQC0Q7ItTNW_Oo1N@6WKkGiMm^{`wQbv&|VdqA_-sc`;TO3En2$I?~j%=#^mV_)J$Z_#!0d!%{!VQF<&%CQ)!x!dM*XZy1)t2WJ-=!Fkd*<jr6N&69<(9-;{?g9Ho+y|uPt1bsZTdN#DEPIt<fg1`gX%O#~OH?mPd$3&xIdWOn?I;H*>z1SL8)aQ_)cm9T+Wh56SLGMndvi5?pVDs2Jnywubcbxc)CCX>@6h!GijJZQa-gDPi#OkuyDk_-BfJJ&XGQ1LjiOCSE#IO==xiAEuHrDu*ncsFZ|cnR3-%^Vqj8Az^cAYSNJuwOLz*b>clxRPg5_%AD~|xH<50iNb7R|5wz`F~W$)fU;}PhJwu{au^=DCdT+*3kiDR;54&3yXKY`av$pwj3Og`T3%{^&ePHpBZ0#{0zVQ6DXW7QIr^eOB*e&>Ud^|Z=#E_v`Ucfu^hE_B#<K1yIWi!Y1q@0i<HxflyPI8PF~JgeLt=N#C{{ayGn&UG>}`Q0+NXo{OJurKtg$k17Xbv8RBnQQ#IE$n2_`^!;~W#vNnaN1W3wx1>w;i!U}!!)gK3&0=M2TL~@h!eWvhI>tQT)SyJx91Ca)yF>f+4Nr`Y|nGJ@rdL!NY|Z5gZ}9cIOgE+Bb+4N=farqcapgIczaR-^XKp|l5I6^(_pshwZD1RTODrMK$f~cJs4~cS}oS@-sh5o?;bQVJO4#!VRdU}lPCqD9$lat7eO3{CFksO_^TA?O#WKR7`Fuf^4=-(T%hxlwiRKbYqHwTW7~zjJ7*JH;^JnRJpSH?K~U7P=t8)M-uv>eA2dcOu^sdqK93MASo3<7YybsxH-Hp2RN$Dh-Ft2ayxuAugx=|J&>O|h(F?}vaMVvr(rtcoYpLy8*F}7LY;T$`*`QxOkQXP)+F#YDPXa3IE8;ktOEG^M4i)}e3EChEAF5J;^k?v|XsxvKm->>Gt7z7Um)R8ES|9ATApw@0=9Z&i<=fBFl^QS>TtuTNpRupLK9KS_2rb&>p(TWIYkA4b<6T>sd8EZXSoKtWt7OGtXSu!f;~y+7ronsO23W=~0|zG9zY0EK`0YQOd&auxCcr~})NeP_Os@PJ0>~Vl7W~=ffxEU#y%&?Kniueby{7%}kvPljv`S%%eb56Poe$?gFZ?b$okf0^68S5;uD1s%{?oO};#d+Pj>9~SdaF5=yw|HXu2%4^l};{t{p;0Td)m$WL~oHp#u)>O&F=3>V|w~O>XbS9>n+k^FLwwsHnXj{UcC!wwcV{b(rL%qvuzn}-j-qvV0oez0W24Zkvf5gK|T&9Q1&v6`+hZHiI6rPF0+h>?tNp{ytg~<m(G>@E-%!`ZUX5GAoiw5=1KG;FAa38oyv3+po`vNzY&Z=JpZ_#y0zKS#Z_^@?LQuFYzjrvlteq6gw<jC5-vBKg4*4}edJNARuZ3ULCh*;lQGp*3UIU~)m5V@5y7$8$2WZnnY_DG8jrz3{0D1kf=?6RL6p04Z$~>EUiNaAKf34EX04pH=mpJ9)}EDR<dPM`WY`!e@%s1ow%bvH<p~Lod&Jb)^CZFZDwHkx*&XaPl=7qRy68vshFx{Pc{n#D3+zE@;yb!D2B8+B5!$VMik7kGt{%G2jIZIdF4?M^vwSzotWBNTr@D5cuSJtmxzSt(0&@blye}rGJYa<~ypy_u$E($Lv-PlMR{xObD;z>u2$s!F9d9>*4AL3i@)LBZ@2D`#Nt}vZny$gaaD+$OFci<_;KfSFl17RWsmIoL-JmiK?Q_Dze=TPKAH!B=%Wf^rSux0R_BsKwjCwr61i4sYvc9z!JNY2G4f}@SX=}BeT&E$ttHAvx42QuouK~m9rM<QIEMwfS-9M&aiQ%F&eAD8PkBiQy%%v}If~uRf^gEd$Nj!S=$g)*GYF*z5N4;Vq4N*ZMyuHG7wQ4TVFin&4@Pm&04K(-kBmNJXW&6jk-t6t4vD2f2!^Xk!{;%1q<AXz1{R=V%qmk-q1;b2K{(?bI;~+(5BmH+W_T(vhgwg(L2<v0^4ObF+NWHcDVMUOumzJ^vsagUy#!xP)>5GdhH*e(@Usl;0kZ1+Hy}Vbp>z7!0jka-vX=AhO+VP69Y36msw)UyJuN_aYxQCkkSX}Wa1FY-*<ukk7fz|tY-Pg||R;s5TDR@HnNaQ+^d=^6W+s(CGD6aWt&J2}AF_PpbNT)RyhKwaupIgF?7gcOH<?){uG|EAG<bHPv^MPKDk_#Y+c_rr}YEFISlj#S*QzW*ZR$xn-gf429>`oc9UyzHI2#&E5GqWKI7$2>N1w7uzEE)}yDVnb9_k;jH(by3s@yF?x8&gC#46ca2ocq^j`ttaYZffx497i$d1@-%axP(6;a?lSX6zIsu8m0usI~c~-;V7A`Kp}c<Io^`d{gZKs&%{)9d5#1WD(?p7_88vYV?pmWUaC=bwp&H8z|NKyEU+ak6z`#PPu9hIP*2vy3svL;t|6d!%?hP3_12Zm5uj#2x@JA}A%isSxdzB$?8)bi20J@`!@fG)J2*UHjRvKP7Z%J~JdvtF5e=&LN`c7r<>TuD6-GkV(~A8LmZ}Fev+GMPB|NRPw<<zh;oniPd6wKht+dc(Wdr`Jpw>NlTEQ8qF!U9=0`Q;%;}P&aipVmxAz*fz9hHQ}j$SZ%S|O#yNd5tIBbi=w4!So9@*(R#t-RW1-Qo7A(Qa<Cjpk;r1E2V>3;#C7_eagmM)M(lZFHJlw$Xs1S!1Kw#afNc#zwEvZfvktgO`EgF9GUZW!>N67J$Sk{yq2y5VqMvOn}dJo3->xKt9)(YAV)YF3RVHKWm^*fKx=iRbV0lh&}dzs(2nb!=grAE-gneDEQV;QglVav*c=^8@fe^E4qSQc@)N%IGNimAc|l#MUsm9LB@{L%OD07JFBoDjRJnu{j_orX3=HLUQ-(eqIBFCKlrmL)JL5a$gc2g)nTg$r}F(#^t&mBjZ6cUMR6}p;^+=U!f1>;O_o41-opr3KVgWp(^1q@E6l;M7LK~IYvYucv^(422=nxj=eYCfKrp7o&Dnhsf>0gx@cPLcp6i)zKWK`#?uX5@cK_k;FwVkHf5rc7w%B;gAg$Hh7>^wcEQb*c{$0{0<q*~IOC>;W=@f?ehky2enZTc{^Vt`ykduwW7R~tG6(3=tNe&oHqB?|9y$qGC$mnY*!K(XtI$Ha_hVLD6^B?r<Kbk#pfv4dj;3uI1{+$W@?-l}wHJ^+@&2U;kJBv-myZ`t%|Ly<bpCsD3qV{%75YDq{3KNq7=1=ik7{bbKjKg_z;2SxJa*KwJMPQ_V?*J37%LojgofNLjIyl@cW(cJaAKGLplL{H=awZRY34o@-WvJR$3A^X?nB~`dFAmR--{9Mor|0J|TxzszfaHBQe}D%;dd1e+OLEZL{lj1XCokdR7f!20#3T|F=AE;>XQxsuhyz93N^3O7$Qiy07Al1W(RHgX>9E`!E??>_1Q(qsAo*N~GtZNB99Y9BhpvNF(yt9!W$f}hu|ak(_+0k1f%DYeBhK-E`k#|~!sa@P3!SI$iVIvi@F(jqUB!&P+B<s9x{dwgmtVhn&AvT8`St0Wz5PQuwP<3s<UJ+O%2`A(FAtxeF%D#hy*W8NJv=*QYwYys<yXgFAD*2Z!Ve4$^!3R%hwSj+=<HYum9(n(iJfSth<`0L2e0^8#ERBg3U)??>I_DsFrCreW!0Jjg9}F2iYwMQG0)ry^~Pn8SfhlsGZ!&ljTwUB7Bln$Pm@92=!X;<Ym{W}KIvKH;sSUPCCtxjB{P!DM?7owxUd9?1DT4$Yyq_BWn~v8G8kP4sm%`^>BvB?74EFSua#~M)szAC!iLP@L`W+Y2Dd;P0Bx%m4wDgZv!|8U$v8yWiq~#7n}+P?!#8lxL6nZ?BAg#pI4GA9mmCZySFn-Y1Fc5fSzS)D!qHazLlVXHsIvyI?FFDz1t_g*{e{GHOxrz6`bp;N@4N<d$O#w39q2M0w1mr_{uaJ{STmPl!adKNhKd}JQIqjc{}#W0SYtq3C@wlp$@Ja*pf?OBKmDH{)CxX*=`=x!yRX7&b{`_*CM}DEMB=VhSr=y&r+r4+oU+)lFW3=|SU4oBSa63F_H7OeE{uLZD;L(9-NjK%F%;?-)ad|v@8!gW`jCufJb-k?Xo@H8?nh}4pA+_|Jr*X-F{yxvmH8}bk|qNYAxGP~M36#bMf35ZdFWi0-{rx_7SN;76a_r98**FV#dbLgUq;tyNQf+@&9a%b!v)&d5clSZg0x_L6=@>swpxXa2=qjxXI{ht<TR>9;j<dmXWtVxu42M5^LD>SpApnjfBI|oaI1+rtB<~1?29>rJ>QxGUE9z%_$_OL_ia9TB4<ia0{g>1`xl(>OK8GjC8fNj2#sf9WN1smn85o{Q086=k~XlCBx4g81boD3B@v4=nX&-gcqqTeL+6DV3oe4_Hffg76bT~&i^Y-`t4v~08gc2k#yVUTXRCM?heweW4++tzcq6FdBi)^k#|{@YnQ)K>!auqn1r%N(!-t$dLZ5uSx&UT<E*mQAoVQ{)8qGeSra(uE4lYYqy$PZ$zgMHY=Diw?!`{`s+8jlb^8s-CuyoQ(=)i$;5nhL*xuj!M!CmMw0eKyMW-HbqD>nM0dFm~*`@agaAv-Bf+ZO0q#kt(iy2)$J?()w5^uK|^4aL~2U^EO$H|TjNEP$S)wPu8S#cI`Hm&v1EFe($YoF8cTp`|ZviZ})Php*2LPn70;gunLo&yGOL?jEpj51+kw*<s%t9e(@f_~fiq<JKKR3SC><VpVJ#cN^7<IdN_D;-6`hbCygRFY!q5Rgk0lI|8W-!!#7pPzy5BX~7EGVAv81(;R$lj0NC|R#jT-bjy_NfJuJIgwP|75W+Etw4*+Xi&v(^0}{B%gpD)=iaN~r&wvc~Pu4l0Ik2I15SNoY4;;u^*6x0o{`9wFpci%~QkMY^P;wB-phsg%6GHgp<6hZ)lcc>6G?joo!{Czv&B+qLdkJ1PJHJSi_%3vS^W4hrGs=c}y#Pt@FzY4PAP+489k0PVKq+zeAOGfm_}|${0DR*&Y@NLUrrQr$^^E-Fe){`f)K6+lG$8JCIBm%E-B-bc%rY1?WC)9#RsZ4Nc>vq?SXY3%=9l_)N+h*gzwvK$<9ae@q^@}8X-}-e%x=?eMwNr6{^frMvy{V1M!|H6HWUKqH=*zegZW<-GM8%M285kO;Hk{+AO87YNoKwT+$@;ldD;TVq7?M|zxlt}8<ZpBVX^{z;4m{?D^Sf?!W}sc*p2hL=dd~FA@G(%SeMZ)t(;}rpG2|StT6uXO+k@3p?G(Ix4-%K&KZZX(-XJ;D#3oRQ*xT)5&Tt5ouhb=uxIp)lEt!#6FYu(#n$h-;K`si72j!{D9?-X^9-1pfBu){=X+)iey|ChPk;?k&JG(R$uN|Q*<_tHyRV+3g4R4ed&xlO&BIIJC9Jp3o+ZE*_by<^4(!t=2U*9{yaDR+Mc8K}G=d0cL?3qS%S44{XJ^=FW`Fos|GIqKMQuLjgJ>Ma*-!rg^rY~%2P|aF5_XO1Lx@69aq9fJ1Jj}{yq*KpBaTN)j=Z&dJdWB4>F2Wc?j9;~LCSvm*C<H_OAsQ84g8MJOGK@4kNgY9$4QUT;iYm7;Q>m=QbJLFr}`2poKby5sGr{I*S<Xm<+^q|?Vk(RhoYzbpdZdV3AgSSSM+xETiIwmKK`|P*lmiER>!$vuSCu+ZtKnywDmi|6??Q8rwi1eB!Sr#`|>(_jwjjkO=;X|cQk77x}LVKE4!WM20-gJJ6_9)U-<rbLmLA-9-a>qoXwy98U~dn#1<A0jA}Nhrhi}nZhP~OG^~C!&I}Gw9gk~^$3)fqqiMIde)=o^XRGz|4=51=2CNP#x4ru5-`p-9lB!rjecR2AfB1Jl|9JQnmdft)XcXWRI=Fk~%_WvoXs|eQF#qMoHoN@!$8wfNc$%I@Km9H0%q2&i#xQcMQbK60&8vlD@G(S$jq<g)%3aYMbF>@YE^ps`63L>*{ca`EY4@Cd(Hiu(dL7h%qg`ibfa>SK6>t+gyoHZgvXPRVVWpM_gY8~-drr#{7b*6GYub(27r}V)*kIGkY%4TFCdNJuB3r%f%`P9#AO7qAWn<I33h#lX3p^qqup66y_{)E}`OyG(`x5XMm-%BK+){jMmsbp`SBblpb%-PzQ%Kqm&;%izAlMra7Uoz}#4VPJEAx4kBPjl~5@ktc_b8jAi<H+Lq=|I~0LkY(b@w?s=Z5zIn<o<oD5mX##CWfM@>@6#Op&~c=brZ(e&iWEq=AC>yJ^r*U0(o?6#R@j!49UNj0uk_P{YtQ5)WC$vqIHxgnbbRAsIxYkbTG2K$A<OJHRz2kAO3fXDR!>HitmOb)^Mju^xY{!thY$X+@l`7=B=)yZh6e^hlF8*iIMnPLpXm(Qi6=&N<Pl0h;p+l-vL5pR#?>Q9)akxTwAfQ$Pm$uI4?GEbG8sSqFSA-=SXmFa96)JjkO!$N2ZqJbDBKZ1b1EaOjr2hlniRV7kN5Yhu_1)g$fY6seH$M^*4L!P82MTw$J8+ISwC<>3UrD&Odq>GZ62-qFR#(~^8&NU=Tc-nfM~_O#g4;!-^bV1vOTg%WW&3`T>wXPPqdo9nc+yV?5XVv9(RH1dJ#fHSyvyEHWKLM^q_pB%mTs&J9}cJJj&P+5=P9KJq!{eo4`j^ET^eV!fu=IrZ}L-um-yTcQ7pgVm1&EZQZ1z%t6ogDDeYYa{N$FEP9bfM$g?rJ`C?WP?P{tH;Kpvkb~3BMauJsgGC0lw)7LMiZBmJCDyj(s|s{Jb{T=T6>I@}32$ja9$XTpn8W6T0c)2{m<7Dzsc$B4f}r4VKWCNU;@Wt}<tl<6eT6Csc9gXn`N-F+zO+J#>`ZEbTBNitm0CWC_Dwo`l3kIWEF6qv0>(L_)1|!`osn5>d`D*Rg7wy^P{vP+P&Bgj!E-#jqR61pPce!HGXvK61HM7M}d;ZzrIPP)K{$s|uAe?+~x)O$D|W7}bCQ+i!w8(iV0G-;6B_+$0vG4Ip4{sQJ(~e84xFAXaY(&zX-6d>espe<I-RO@xkrOTjOu78U;9qLm^Y^rQcZZJ}uwk8xmqwwfD!x|eVY;G*p!8eXu>gvs5z%;=nB^<`!sBVbS#P17tQ&7h8Ca1u-voCNq79$`4E>6jTD<`NaB>6qS6N%*-yZ~8-mA=47})4yeDI8LtdOkfg@5;i~quMZ-36;BRoO+26r7>}w05;GkmWFcDDS%BL`QU_5CBM%J&7VrZG?uo#?m-wBp&sX;v5kth=iRUDeE$=-ds*1TE;Y(lHe9k4Nf(*4wP-B}&9%*ra_63&x^zWhRq^t$GFQ^y$N<8p%iIh|eW8y)4mGhpBlO!MFjiKP0?%3@o8SUG0%761+i5DIZhASE}9$a(!WJu|~;gwtlqH)16=z%u!?vhWnt$P6J!_(h!tL&EabDcW6oU@+2Y)vT(gPSb~>7mD1#09(L7P?ikwm;%@=c99cPF)EsugLY9UEs+btv>ij%*FXBCO${z7sg7=`r}XiM@Kcr{6cq4Ivl6d<Ukzc6?at$*YS1abASF|Bx45}q67b5L@<;XPqc%Km(e&P^vVMbMEW>Di^iB6%sx7bsSDbXh>hi+9lOS^H4bjivtSS^9G&;W%X|7TcABsyj4vX3JdvGF(*cHRIFlhF$~D;H-r&#Z%jn)o6utlH-&}{$g7XwEwm0bIz*0@L&Bc(VbWmX@IEgOM+hLvUqs1Y>d&9u{N5Le6)QcHx{)1pT%3)vOCWW;Ey@MzR?hMn&@*#)_$*6A{4NUCGXAtETNb&P&C8ZwB*<s|9m|9IiqWne05)dws;)Tr0q9stgHVLB8|M(yMi@@VH02R+=Zxlw?+4D5Y{3mAKRWqLfuq5sQ1HF1$p%{P73^w#PX)*~eDF|V;wwOiW_(V7V`0PQ$IR->o!Wmw!q$VFjvmZ{%1?Ob|^pa_u-@A5yn$OOAvmUw^+!I7L4AM!7H}`T7@*8rw_wv%^AWVjI$DjnlGGeLV$s%3{FpO(p6YGpe@mS0nn0y6SzLe_liW`LZL9D_D;g7~CL}yf#6S_MY{E6`i-pM~XS?xaTf`;+|+=ADa&i^!h{GRd$Kod6*&PT~bnB5l$Ipqz)G>m)U`8c}0FC6@Po?V4E_XY5Act{s{NOT#DBj6t2CD||<quPHD;UeK+K8R)bVf@jUhU$()(LofDY3fglZOCr^XDwfdL3{wqkPv#|Xq24?BKFvaK`Fg`v^<<N#C7@sQip_;<-z4;n10Z5-vBiZ28L`96_Er@d-quDJpto`7JCVhKiX<9`U5C3Fw{Nx(^~MVr~g^6csYs>Sn>))25U5&bH#8qI7;l8->1c<tmTbaY1F?A#R>X1VU%QeXuJ=)Y#y*GQDLo=m{+o3xi+j2Js-%<v4Y@v54tL$tg>aa#B3$KoQw745PWCY`m+~gj1S{}nf=`cM4^`3@*dJ0LJGsO&Bq^XE$q(^M)o?qVW$L?2ZAd(dtH8Om}~9>vG4_jYG#KbhAjJnouS@4$J8go&Hk*WKGo=M(Nl6gIZIN0Y{&<4uj|X=z;6)rOD?Q?s5F_ZRGvq~J}<W^c<1MZ3_ZNV4$>fsgG-#CQ@T($XNFY7;-7VjidJ`j1z)MRW9)cH-=O1oZ7^BcpQnuPF3WTK0&|sJyrx2)0IE-T&6k{4J(l7X_^rijRf~%^?iJaqhqW&7L6Cj<=w1j4@LWFx*9Ae=Q(jFLMx-Nt#(LppfbmY?8|Y(b(c$Oi=*_|JDekZVO(_W9QHI_H?03`fA_bW)p>QZk8Yk?hzsLAl7~xF!Zn%eMf$Vt`Z!evfTR0chToh4bPW=>?*ExSqrZkqvANh3q;U_=cjzGGeqFbD}l6-`}qg35W25}xo5(oZ^b{}{cC|Xz7rhjhP+`k&h-H2bb{zwbm2wg~kg&zm^EGl(5T6muui;1}_;{lA3hvgdIG1w1N8Tn`&W*CJaqf<G&xNABraapE1%|aOn;kZXplJN9B1O|aIhWbfXYu-;b<-Kn9Mqz-#A;ML(8BsTl#^>_`BF(A1oL}V}0OY9jK@jM=6rRXs%MIgWYEOb_Kn%y&HIp!hMK4Z%k-Zbm0K+d4Gd_wMC6)qq;ZI19T2lBgy+iYDBm%CoQ_zU7X4a#T+I1N5q>C7b@uE!mttt5?pO{cy3x&qGkD=G-?T6HJG43D#=3o6~+3j#UKr6zMfDXymhDVeS=r+9>JKnv3=3JW4NY{KA(0fNmzcyhEk=H%%jt6uN=0Ev652bjKL*<awef3=3J}keQv#8xHA5kom|GvCkDst#?1Y53MO@lQ$K;CBqiZEL|X8~!9H<bZtQ6Bd0pDwue^JJY9m~)*3e_%-FB7XCJGM+#e*g?{}G6>qB<at!g+y{*O@wt~HYWo%qy%pFpuhDe$&9{v5KQ7f<@wFFI`|6a=N!TBLetEj(1i1*xC!j(t?7O5s$vBl<q(41aDR{e{$nXB~P!;m>UvwQ()H#YbrGRF=G@9hQpH&Cbm~-DMe`5zj-Qt@oQ7^AN{*0b}jI*3QJ3c-;f3x@9%j3NR_LQBUAD`^+oqw};dU$?%_VvNh@i~?F)#>r;^K+`VzRo`CTZaIz-9$I1B<5Euc>qUPL#MD6jxl!ZYYap`ithMho>jc$hs7{L32eDTmQlgxWLEnG{o{E0)#>@c;q$$(Um~_n_FkO=viRFW7(jc6IZvY0DN_kI_@-#9+2W~o(8wJMUMlkJxRCg|Vav?b!!Y7wwA~G!>x6gQVO!g>svE%(t8Q)cTsuhP4%_a?ntB|@9k!t-%fN~|=#<Wrjo^vUgqf<sBT~ONc_xtNd2gDb^=!f~)`ChNjIvPF<!R^igep{gD^~DZL<{S}2;bF<BtQn++%(f*l&rg9rakJ^*+yGW!y&K@tV$^&!;MOa&pEc7OnDBlgU_gl*)lAGfKrJg&F%+NBvWnc9->HA5H{l-L3GeEIR_QLne@^zP)9Fmi4zm(SaYjLCd<PP>vpt~%3+G0IBpd=>O@kXHtJZ>*@C`l(xk@$jY1^9m-*zC;O#s<1LNy^R|oEQ^?(6x>7@)84(MNzWBX<7&|CIJzVf%wreN`)#M$d=bJA^U6QG|)<FmVVPC;YaT9$QajD35k4MrRV^C`9aEYBcTC8P}vzJ8o$^vpRR!?mH~vpC4ICtjS^Km`q4h@IN#$T57Tjik6#3cQ%!Tnqd1-U2Uyw;6)bO)$&!OAUIv<b+SJ5?sPs6YltW0pFz{VxpTyzH#$shnboD{)!IOQO7m>dM=P@B*Qywc(xmp=Jn|Y3@Sb(ErP}D`{%weRYGke(cChMxphp8w8XacDdS3T(X?(4v0!P&4wHoD;SQfVwe1uJ5A+!!uz-R-#(*T}_&%C+66f>wnIymWBoQf5s~?7w{ZSH!)#T!bniyCbLdBS&1l0toIt#1x6-BZ5G8)XNY>hugr~{*UeLhNpym}ps>ge(P4StT2IvYk3dNg2Fv>+q{j6Z;q535`xFf##2vA_SlN{pwYk^UPPOgI2K?(2z_N=<f`xAyomzEhwCGysX`^>lm@rr4j_W7YiUJhd5R&!ZTm(dwY)1tXGP1^KXv4>ICF_>U;A4x>67l%nA%{{IaU=m%{82*QJqJb4B~)6uaE8dPVlWlwyiV;V$J*d7#)nSIHgaiIL?jxjzTR8H!ZTCvgzml@y^$}}N&T&*?p<YjUbru(qkssgbbT*jf$`*1i>;&)sBF+*3_;%A}_80&e!5r5O`wDccwVt~V-7RAp3HUWA3S+N^AGj7gZEEJhg#E*GH5^XgNZr<dX#E+mf;A|KI36NB<6-NtcnzFG@kQnoS22)3$stFhc|JvkY6MMos`f#XCo#KgQ^`RGU-|^%DUd|nbIg22%^%y>$m>?l(ZOxu+bfAFpyx`mDotzN_baxWmFupqV<kU^Zftlk%xHb007u0|p)9zCoR3Xra2C&H6mTH>G7AU=~(%-WXW|i8aUITDJ(R>g@5f?vT)a#N)ns@ATgS~tylXt|IbEE`sN1Ca>ZVGj){2Sj@$K#TMDtkvyP)q8)F)w!-N5c`QVmv$5vQs_V%k%CAL|{&Oip&sCQlq$7i=42UlW8`rzE%8?R64~FNh1TOwR*uZw~Z2=&L;lG7T(qLm53b_O)R8zQ7%i;T(g@5b#?(0EUN@SI;_Dikb>CznqCu<F!L!Y1xC8rfd*@fa&0W9Eix2+V!q1W>LBY{1MPS3d@HccSD?|7cLh#zC@sJh>yPJ+f(&y-H{Oa*z2Ex0PjZe5tcBm6uy)wk(APpyYL^D9=dpRsAO>jCp?3S7wp7KU)WJ~mZI1R$_5e^K64rR_npXR>5-73@oC>MSvTbX@6jWt(dkzB?<8-KF4gxg#(DoBiaNdT3Rx{d3%xxq~djJp9H9m&FOg8o<rGYH|Ug!NF^q%ti0H&#)_$~k$$u>kI(*_Mvw*bu>5tp4b*k-y7+|0G1gZ^$pCwqenoF|vS=9xBVQ1VUCLhE;d%Zw86GTUwdG;*^6siM0rsGO1}RKDFtKaI7C?JK7+V`5dZZ(>!Z4H~pM4K&yBEWjes2UcWppr1)e0F8&IXig*^CG-I-ZrB>@tVREIHZ(D)sJhEq*pDLN3G3Dj&|QNkPsV&xJ|*duH>ZpY&em&XyGDrG9647sh}G$|>8Wg-q-Sn7KrOTa4Vk~)cHDghAL2I0fhKG32q<I6HFi^m8UYzbs(|V37VY<r?OXIgFfYk%xuINjNtqD})mu|}u{SEGE{x}_OMf?8@KKZXU1Pch#x79j)^^ruaeJ=;%(cGT(CiX*VV|D^&osJw0qRBS+@z2D#Ww!k-mDe&4#&c8fpbdK`56G9(Cwb@Ou!4z?%o!4ti6eUA9WNw_Y}c`W*4aQV+L>M%wq=&ke*qmGYQsclPHJ+p#h^fqwv6xnRPnAV0;QS0M==SVi$J4cCKNy;*_X!6FP6Jt+nMl1`*mm0&=tKTmdaQYaNu7sGFQu8G55KwRsLZ436s-sMBc(+X8~^Znb=n3afP)C|ROTXD4h6C!wXSBI_K*UO`57olJ)uyIVRv8HX+w2raKp2Qr@e?(vKT#4aF!G#+x!Kp#bKoD&`2nT~!i!YP3ZPEC<)Q-Eov*ZL=_$-Fw*LFJNZ>q|yE8&cCHYEyC@kBnFsYHgd9^wT3x%PP0d&z6vX(BDTU80{Rxg`zS`7m;-+<$}<rXKT*<SjRms9F-|L!8a(Pm_qL`kCd|cQ_H2+VrtQHwRmPltzu@o8Z&few(R801?VqX=Vxr3<F*})Sx0V)fCNk<8}Lu^+Qzm4!abXF`(~G^^Yc4DHE4%<E+myH7b|SHwC65C2m-{4gy1<PbV-4087r@HQB9|X&YV?loHnYt5<v7^oN8M0TRsRL{%*i1xI3V>gYugR#5uooM`V|&^D|EWgsTHj7mmm(Sdgghn<(GWs5?_!U0ZpkL^YisZ{SREX{ck5$UI_IXckb6Y>DL!9|+?t*6of{sLoH@7$=~Xz1)rSTLT|Oj)#w_!(DqIB7^$hh9Q_EpyOX>>>*-(gI9Qj|EsxXpF%(?PKlMeB{NG8hzk+SU&I<=*)ehf##_RI;y-J)Bo1GpIzNy`j!4AaY1uHX^JzmU^A&;V=QFZtLsEy?8jAEBYfPTgT1VTkN{EF)T-lK9y(i;-!O(<9EV1oq3f{AHXU>d#d$E@sw_Ba^ma6kZdDf+cwxxH>J)?J-5Vz-)Ga>!_UQM^CROCS?_$sn%mT7c41XHP_u}G!3raOE%ZUHVlrw|eIw%T5|wrlpnwtWd~ZvuS|$UtS>zA!qxX?57}J#gU|1thy{yV}D->gV9f7C;-R*6f<kyTJwMmJ+f*LEJJR`W+%%n7(p#a-0xqlL6K1MIjazhv$|MjKj3REA#g!a6#=f+3653`_R!+$Rk0HRP4gT_!4+5s~+B>U-+{qZw!*O0iT8+>YG_UOyW=HgnDrJqH{uix^({a=7_DM7RC<?c#*SjkIy0fDb5CaAj_F<Dw8CGeGkvK#+H*xwHmNrV(J?Hfp6}K183~`=*1}@C`hXzZ1gba_yN4*);fMbck`z_lQrnGRTyU}_sLT{K6<3iP;S{SFUP*5NXI+cxe39X%JG++7gld&OEtg`wo$7YrzulF4F0Raf@ckZsj0`+Vv^!jukchoZ~yB!$+PN2j*(8OgB#7->@m_5XJ2&e!X}pO1%@%vP8}z?cINn29KF)PRISd6pY3-w?HJNJ*Aho8cqdt%j>)QyIn+M!eTMc(Pc_@_Y1jJ}4TWw!#~x|ddmWOKgH_Eo6xy|3MiZS3NFC*%)(RlHk+7y9@M(Cf_!D;{CTzVcxYk>1<hlj4Ru^dUmUk_tSf0?Mm**bH)Mq`JNEnCrPNcn)r`n&1&fn*p8mhU+keG<@79LOc!~S$ahtmp9U4oo{EM0*2o=M;Rn)`&jjoxXF8DfgHyte<mn)>yY{+69pLko)zs-cMQl)41CI-yQ~eedJx^w-OrP4lMt$@JZ?sln1SX``D@bnh2=2*YmCb6zUEFn=@rttPSVr3RQ>_TJ;)B!MGL-n7ZYt~7eQ5`-vee701bHr28AeO35k8jbpI@MVb82`WF;+YAR}?mg&lbgP__6soufPZ@?dpdI*EXQ0@;z0GjS8judd04((pi6G{{S8O;C{=p`ec>6<iUJ7p*iB4M^++S&oh&7J=`r#-K78O-%>xw&FUBM(%K77@e)$r}rI~w*|WQ4NkSBg@pF<z!R(+c7Dceq^+RbhQ7eQ*DKeQTHZjngT$&sWleqC30DmGt!|&hgtylA)2U;fJxtRml#N6lGKet7Kmc9H6d21spDZUuQ<IFsn$@mYlObIXJ~mi&d$FgMJI!tI7_w_y}O{R%0h#O*t~9P4iIIOBcl3Z|OCkJT=iq&8hxqer&2n(TJ#wN8+@L1{WDXufa^HpWUY3TFq+5%++b8&v%i&xrxL$mz*vN{KN)+;<lUu@x7yAN@g~+f<|6PBF+a!Lt*TIbnqC@#bZh9UW~@27!^=zR<oWWCT?TeQ~I%W$nN7_L*iHcf>n`Sz{gO->tMwBDHrN9Vyhs|YwpE-8gJ24f@e2xGo6vmw49ldQ^JWwS>8ExByd=>a6@_-#S3NrZ!kC^XVXXqs<6Sp>s-~)WI>L-S;kizwe)~kqhyOM)2&b-VIOs3a@f-w!Uj~o;5SkGJAuVoLH1GqR;-22YU~}crrLf|uz5qIA>da9+q+1^;L0aBh;8bsn6}|tsQu1x0mB8Vnj|!05!xyYKj9o1a1O}JjnpotcI@O~tECt_6ln;mhk|Q`@0%#v#-dcHQxvkGA!}(UaBB*j38*ar$qX_3*qaA9*Elld8f{`nSMW#RrLVG}DOr^7oofWxQ=GEhl{O5rVfX89r;4Xm(G33G)ycH2E0riZRK<)DK}F-~2x_q3<AGWC;l{(QcK1;i^mMn-j2GJ4+U{&^cDDS5?s%bg=ix@Xv(<k1&{qn3CCY6+df4r5Y(Y6H1x#%hwrq|?>g<sHIsU=qcDLr_7eI$*tMlM&nQ-K60qJdY9&J3@df0ii$%(~8F+IfjI*GEddm#8(50KphWcL8s>X5<4dY<5mq8jJNL?Har>DW#kq~Y&$KTT0mPZGP{aWB`oL|e6wm^B1JRLn7GA1+6MdBNiqdw{A(w7h{wi0@CR3Hj4iv9NUS7HAW@Y-&-c<@aXZtUJuQQ(2}f|7}Z-h>VNXTT3~QW>$fjUEt0ta96Y17+|;2jsuOEbqCn%8RpFF9PIQR=G?U`a8m>~AS~S4hM$4m{VBFEAiT_+!uC+6*yw;Tb>|dzhLv$@kTY$9>a~a~Y7C-<90LE`!5^$^HQsAGHIVBps?}<H+Ywbu+iI7#wV-B;__KdpysCd}?YUzsui0w1=Z<eqo9*_(F&edv>hUd22hHOe(j3qOO;Ll=tj6NoHZR@QOSgIHwp*IeLAcalw>j*#3!9g2>!sVgbi3_#oK`ILe+}s$ic|L*l;!}RwR!2bUb@XoyTHF8rb=zB;d-IsGhTdF0O#Cy?J4om2UJaF2_DSzWFoQP2P8#k<uIky+%#=w;vyI|poxYYtdI#kHxHBXWSWQKU7Z7pMAi%Obtti^z+Q5Pp(*P4&`utRj~8|2+f^4nV-ySZBrrCcek%7A(<>fj6!QU)LSTm9@{G^WGB90w5}>}p?dj$|Kqq|KWge(PN!H||o0h&`X~hc<t{UNN%c@Gw8D<O0U&AVz3xt@Zm1h<zed4UctVgakPCey-W7M-MqES*Dd{k+kP>Ph@c)%wTZ;pr-5EMt*x;Rtejv^NKm#D&7z&094d{|eb%0iHyr@>6o<^UM3SxwxW(t%51M#M9bHD0-wWL0?*1mdn+Rm@16Hl^H|t_dCwRCz8<74}><xF#m_fq<h-NGUEvoh}sRJ>Wo%#iuT0=!8wqa0Ok%PcL0#`Xai%8F|PREBgJ{YQAYCceH}0u(si;W)&Ytw`O769nD@CSK*CWL3y3k7ST7BUV^@_Pz<Sx!#|*AAf}s9O`~VCohvjr@=-rvay6K|O0Efuq}meO84xbCx`wdU_z)lHISw&)teOp|S@RN=Iqg95f<*ZOK>Q+6;^w1LFricP5MGi-I^hZDyMpu}!Ap9WzL2Hvk#k%zSy)MTo3q7>Z-69yr6sA_<;m&Is$e<7*`&t(+sry5(cYMGMRK<HfOpMeSP{X|r1Wd6u>nH3M$Q67UB)QbtmL1>Q3b}<IP?dyzZP7qJq5U0+f%#ucs7_2@;Px-)zk^$8v)Rv&Kk3`u0@uOykwB;L|U-cDnUcmUel>uFK{gjm@w%Qyqw7gs@H3h?eZLAozS{>IhdsQpt!+r5IRtjPUzBkv7mHF@lrabFQW8pFTN~j3TqfHhc+Gso!eZwsHb@tdKt1*k)PtQnwr9FHN>@Lf~z!U;|vkK5TS$&Sb!x9&qSM~db1Hqc36Q1EGZXozF}|Yy<0gz+=RK{M-(n#Sfyt=T`erl71?!;NL!rdQ4^LoaQNtv<K;_9gqp7iQbeq1eTRu9Q>1xG)TAMoL}gfn)Ngs72089g(KLGjJ)>9!be*-%;_u<#8RE;dLZejUx%<k$8CI2;cE<R7>%JST0Fj3A1@QWzqSg*JOV$}2|HOAs#j)LxXkFz!^|Vx^JFRu)0R1hB6($<g&6(t1@M>Hv%Smxz&gk16Xi}Ltz~d)(@ts)!H-Y&jPV<mZeuoSK2}d=*4#U2qlggUzs^g0i5#RZp0Imsl95hC9;IUdbP-sgvg#i#yEWyqwI;7FPjqpt5?ph_%h<K{1&RH9F9$H*i=|;B=mP+f?MP6>8CLapi2wt%cv|yp&2abXt5Cu7W>L^fcy!`<?`vb{i2+`A@EA&1>HKxoh$+(A0rf4)a*=OYhrin*I{M*c2Fysi+KJcCRDymp&b_F0l3uOmPYNmX`n<bHIlx|<Oax_M<EalbSiFsAH*eS$f3bHo|c|D05yL214C=iT5kmjZ#D)=R<7A|<aPR;dH%WslBQIWGz0%IUsUJBF)=iC@HSN;WFRMX3w_uowFw99H2-At(HZyWh}z$$AQm!VjZmPI+1;wI120=<OKl3e%M;REESscrpe3k%ZLsFt$jAm}-z7j-yOL7&1FRdL)HNhPP2fhbFYrG#e*uJl~*pX!7kV$LBdCe+Y?3!pLbKkDWKYQfs@)8xj_e{4U$V!bH{OR*q>-Qn;wmh{+H=7lWeRT|^R#p43xAc>bxW%nK%o>yWuS<yj+XxGb=w6NJI)0$XPHNd2{nhYfx@8}9SPDyA1ue4sI@D^%%eWR<I;#n+2NG!mwF@1#={#?fJ3p<}aa-4Kq)D}|J)8!10v14_dG)wJ{uD2OOy5f6|5=H1@AIHHOktOIWsk0P_QE;XXAPla}U0^*oB}fRmv*I!dJ?>85qYG)mGPwk|2Z);fofK4a5a$(F^WLe@_5=mZ&&v2od*oXby=h8rh<wcUa)@v9B3B*wuC(?F8x+p`G{re-@bS8&O;$`%Xw5Bz_=hfG?h^o5W8w$edh~M2pGD;FQY<}Hco=!S6MYCI%ykfpyBwR1#vdDlVi5B&C<>KeP~ewiQ2Z#xpvdPKRE2d6T0rq`L{V@{XAGsdo<Dv%86X65N`9v`<fI!-zW3;867JnONNm{--_7f~v??;xHc{6Z!w&yYY3KZbC9yY^`EyDoP+Yg*x}dHH-U&8$UoCJ2ZOP->W18zFEai@WryPnjQO8v~6y$YXrLm8IenugGo>(56(%}b7;wuOaB|^ip5<T&?LW;Nd8!5@#;=65G@{1pu81G0RA0mB}Ngh6Bz>-1y`hufNeMGH6lU;>Cu3XZdN@C|ywkgUl5S69yEr6M8>f?ys60`xiME;hMvM^IgYtZCk=}fe;s*t8DGIp5Qa?y+?SwI>_S<|(riDhmkKK9o#7_e5+NVn=*9N6W_R{3wx`-NVT#Nie1D43OY>;%50xFgx|q?u)n&hPk>#d8h9^J7PS<LR!!b;pyY0z!X+`-$BqJ4=H&8_^pW8LPfIYdkw)U$Dd1HGIsIp4VcpfXMLal23L6@#XRU-pj-DgT1podM$(=3K5BK_V#~$ijRb-!h5e@e7*PL@ch-`*`BDP0cegzZ`~UBx`tERxGy3Czp5J}6zQ~=^h0^)$>{Gl@bT>HmwPAQSzWkJdcg%6SZ76@qxSY|q)L)gNCuOaj^fKHhP;DCs5)v2Bt00-D7h>eDH?t&tG`1}XBjgO+tPBLvSW&e*BqqD_%P1XD9oxNDHK0V3}zWr%xWfXu;|RW;PRG|$w^uC^KE4s?No@P@ErJB+0jz){txt47B>>r53$+ESk=DhlrO~ytF&lzH<%uecPE0=Q8tB?D~Xra1gQwwZFT*8{j$y~4Jd~)OI}@n+x#c*)@$l20tKi==;~srnzN>Od@-w5COq^Yeqt=WFs|_0H^T@v*D9~CdtZBiP$AU{(V&tDXmI$Uwb`I1DN#kzqhEMI>?rPsx5oo2g*!r};<<h$`)MG11f-0(?&Hn`Byc&3vf=XNiH{3m7vf8UK;@_u1rS(40Q9}QBi{xoKIB`y;h)yc;AEQi5IZ6l=o^8`Uz41Z!Q&6>KB-=!@4Ur#HG51VU9)w{=%-_P6bsk8Sc6yLER*nRCSiOoi)%CeW5pBqSje%#n8et(mYH-CfT*9wbd)RL3Hq-7_Q$tD<L=$sZ{OF}tpyL7LT;;s>wjKU__K8oJF=XYL#|29^SgzZCJ3>O5oll?D>|z-*S@S(9_v;ko<o(?T727lu=eGj|Jjf4tF_<1{q4Ko{`MU$&fos_&%US>_M=+!hXmB8O2x75<UJGv_&o4n09CYio`jc&x07n+&ygWX!~lo-vr5f~LrpdG;gbdtX44S`H5St>@u?XYI2K^a4+CgYVH1<<EaJP1fWp71A;Z){Pbgd_bm)Dh&PO3k7`5W!t%frW!gmov6yOMO))Rj^^Cdpw2>Myr({?>`&0{7kquOI%{jXynqAC2buKb%Isy}Ao<xb@^yhMREtJHhJc&GA`!oXDO(|D({PY)K?lU}}4Ipzn=mG`x`2$@zMH6h2qC;0Si@9b#*eDCb+<mlPgXSBO>x>tR~IN=fX<21+63%aaRl|Ak!y(xC9`MYVD&Q8M-=}>#4QMK}xo@Ilb?JdpEkRD{ipZu*f#N9jCD%`0y7`(Rlf!b1B_-`xxnQ|a!4Kn^LAXnbGRxiGjp(qTD{W8q=0A6$fdP5Z<*Gy}$*cBZ-@df&0O!10hilv0Lcj#}Ow;=@4_x9CbcQ?)jP6dipj|v29<EPyn5#V&H7%MI_#m1>Zllo%3wjlB`lI`mRmP<cD(?%BN&1MreLRG)=hEi!wVOANCgCM;EMfxQwbw>R&dJUDG4M7+4)J89;G|#?`@?o{|bqw98B6n8x&2>N}D(E{@Vb%RS9j$#|Q$UsR&ja}+Tm%_Q7?8iSAeU6+$!eN8zKOgtoxFHDClI5`d#NmnMfvjR;PB-9^v&V^sS1biBeK~cNFBwayujI_c!zac$l`8yF!(M22330p-QaPxLvbn>LNS;Hbh7@6s#j!u9tGBpJt3iYB=n8VxzNcvav<t^z}qn@R)$ZpFBUbRhjx%H@L0Xn1_tbvji8xAwKFuE;Yea91jcE~iJKu?YHuw!79NkId@OF5iefAn*jJ1NgH+5L3vXurSnOaPs}6<YdX$eu5Az{GH`EY1+GK2cDR#mzn#gm6;0G>)1S<r|ZWoX{C6G^|F?)v9UC4(0(gxkxa1jzqz;Ad>#;u&y*3<ncMYsI&Hk4`5Zl|ryZZQVCp%YczX~FeXl1*SlU}~egrDk_qH34#lY-LaQIGrd^bDNP)SgIX09U5zDsfIv;kqvz#-M6fktVM1ZMs0*`&1WD~S3D;kvgZK99gAj7T@5-C)O^skHC`=;hl&N#H{M3E9RA_o$u?dP1X$1`!W3C2JxH?ds3`A0cm1_D=dY5J=z<+!Z4aWXMtWTK6g!fHzwN=<G}ghB%*v_<VVp(zthTtJ;;M_r6I%sOY|ULY*yOhujS=LO1H4bOPmmV2s+_u4TcrB{BB$tO6aNym+xY<Mz@fRMF}F2!d%+%+#uj`{Nv`l_NG~0fQy^U?`2Yg^7V0mgK;DS|PKj(%^1F6t?kZMX=vxJ3VZ+9C6lWXSp0@xb9$!+`MGe_kSym)PTxen1Ae6p>+KZY~7h%-2QKU~PM`?|1I*m~yr&xDUEB7TqYGEP$i9019K!MLevCJ2eplnCKVPZ4Gt+~8#A8Rsx2V?1m?CrLr6oGk7DI!0M&~&gwW7fr%m3bhl2Fox(*`T<3GOrz%=1!6ub}A~)Aqjc=!b1}s#U$p_#J+sHXAxPbwu~zo_H1pmmf;cDD5Hbr<r~!Qa>zy%-M5xwguGeMbeCyW+-^`hge{8~EkQ}y)IpdB(TGWd)iQ$%!@k`Hg_m~Q`Gpdfg^d#L_It>~7p=LFFE$hfHamX#qQKlKK?1cU4!NY^j>s3t*(QpDFSUK*vJhrZlTp-X!UpJ3Bdvh7#fY{&8kk>Gh3P+&AUs;P8^&49Ota-_q*E@LKgZi-^BVKI5-K(;DSOL<xnkdV72L8@fWeLh3=c8Lu+CciWry76E!hM40M}PgpG&yzV9Z858o1mybc*vS$<#=>2Cmw1LO0v&l|LQiA?~ygG2=@n91se7f<@dE?%9ap?2KrE+JDMl8au*J#%x~#@~k7?lo94xP1JH~n`jD60cD0U(MsuJqF~K@+ikYy6S`<^(V`M9y5XVSCbyPsa^cz%ZTiATJBsk4Hu=P<RRD?!HuxFEOZ_x17#mH--B#G%WP&OXS=G^)9<nbO8jRP;`U@$&t54>EfhQ&VIo>|3K07|f2im@SdAxUk9@hHrrZ`c-X9jR{qi37v<g0i5)IH)nRIWMv!33i^y>dqe`F_&7qKE1D7c@G-gjD#{k0^}3>jxl4K?k-q`B;5C4MwsAKi$C)_ww$hUIj}KgHEHqjB`H;<36ws31Ek=+KFfGL(pi_urKqzp7ddOdWjfNAahT`-%UZIMp{&3;OW;<22;Kx{o<S+rJ@9$gUJZ!7)%_Rl4a>9N8E_Bf-luKWTZiQB~VB2Q(#PcarPW!S#%l8s9--DhnQ%$31K}%J=Q&7Z+Oj05mgxU@N?ve^w5!!I`gJd7zeVtfxsjMN-d!K?fD&YSfgH?+}(|Mw0#g}igXe^^my{Po{L=beG91Bv19v7)Cq*}<9!~6j2A)Y*F1{(0aCWZtQVq1by4b^pFU;$(P)33h*T)r|FW!@$ltNwq&60cd=j>3*II~n0f6`Rofz3P3)2O|!Xi3sUpj%5RD~(eVH`+W6=+*bY|zW2>yS5g)JN$VA9XxW)T54d`LMCiIZt(m=i?le3{vGgk4%a&3-^gr@uCBTtmHX-`v5^SnUXmi7AeW-z-Z+U_Iuc6fG1Q0OMy{F_%KlgRvn1LK-tl#SYY8b$+oZN7P|#(zaj>xbp;RRCSiIkSdd^P*c1E$j1w=xuqv>En_(Ce3<i56di_#pp=mA<UgIwvU=Xn+?S*}o#Nzo5Eom^|PDxQ34pLg~T34_o&<A3(f75*LHiCJo%mjjF6#%F-F7Y5B`>xI^cbM}PsKs}%6<{9lGju5Ih3tC{EKRa(f11DP5mQ8Pt!5JgTj7DRg83bTGOUV`q>cvz9w_jR;7~<U2BGR^QB`a7d(mQ*hcp8KY@IzvTyl}A_L+>S{US^bf;`Z<Hzq$v#Owz+e|lDw9U;>|WaCbxq3B|o&Gu+IjO1aG<tO1JNpl@cZxn@b{wmCY#cHp(^&?yhZ`&vc@;_UxciM9>$Lb}SR`CW-8Vf{9FPJpS%@k-Q)2k2$UT7(UD9@hJ`!7H{dLl=bnT|r`E8wl2f-95MhiTn{7gMn)wn|cJaBHQGVFeD4r+`@02|!cPb^^*H>5S)XZx(F~gKUq;{!Bdt0v-KKWA{@Kqey@%SQc#DMUwKdEnG*kQ@*Nz`Z(~a<>JD9!^D!{d+#0YyH%c{XcXhaxA+}=QKcY!j8N@~5f)|poD*bL)8rn&ftaj9ivl3JCj}gDar5O0v#8`u$W47%@bouNt5@O7^u+5&6qJx$Q7tz*OlyX*(FZL47J$5SUJx#Fb{KrPtzU-uv)LQa1**x#4|UQCtP4HpNI}okW2g-Bd#f}nTI5`QnG9-|-%KVL{znJIMJ#5|fEt8yOrvJ-mKH&K8@+qyal?ds&-*Cu7|B!T(+<>ggHhf(QzMYW#)%cLahv&{8xL}89!(|`<y@&<kDiaOBE#-8!4uI!2#@^AY;buR2a{|_w@a|khO^j3cp1g0Z@qv`AGnCI=swqLYq7OWnEf!E?2nQ-6iaEMUm1Jv3k5ii@+F(()KU1K{_6Djbu%Le=V&minuQVPRso|&#Rzz^;*Z=n%m8LMJz1p%%6IYcMF&(ij0SmC)#urY?aI1Oi|9I2QlJnY&!%}!K6*xwa{mNckLy7H5rQmOy$FHIg*+*T?H{z7Jfn&h<Nf}lUo`fTky}FxQ|Q+iOPPe?@0Uq3b`Pu}o7ACKnUq|=aj-E-CRJIrbSAS|+}j7)EKNq)^E4TgoujI@Bf4;S+5@Gt${(8(wR*#_KOKc%ffThD2cy|tI0r#!F7YAAM!ye1r8IGG1ZgP$V<G4hSgkgj>^SWOB;%y)+wkI>D7@*gXFLQ{^)GHB7}`w}G>rhpoq>!?S4#c@#P7dIV)^S+ylIB4{(`!35(fR*X-Gko2w9IscEB-o7L6$uon$1Kg)+Y|bezIWyvpPn#Y|xfdPOEBt&|NP=MZ%#vjHnyJED)H%N8ufF3M5Jw@)QXRM5VlAs2rd<sFoB$yByn@rf33|13eusZN5~C@BKUieMUgPqh$3=}g<qOBz=Y9k+Fq(2M9QJ#yBsf^cg4JcDG~gybZxR<IvpYMDMj%HBZ>ZkpESIKrzra>PeDm(gV$&^|m#4gN7nHR%R^m?Dk5)=)77TKN)~xPvrFo8;HeZy`y|MP7wXn`BGF+)k&3x09Ynw_(59DJeOdQ?h7K+1#jA-RkB6OXfEMySbnP$|Oey$>v5;y6Y)z8R~eQ&Vo9+`A)QARG}L0#LbW2S8Co_J(vN;qn?=Dml4QXg;Tn?zI<y$DxnL$q8oy_^U8dBY69y`E5iP41t7B$Amck7$YwbZnx~qWC>ux=gZ}=T?-VFN&&6#WdT164ZiQ#9(WDlPfZVaQIGJNR7y*X306pAzEKdipv1tL2J!`Oyn)Ps^T=0ON-|WDY)QjKW!S9(e0SFj7>YHX0`5sd5wBOQXp}uN)+=3v!XzBaY^g2A*(PH+QAsRZJP5u}ug@@(UYo)J=rQG1J?Gsgg7_kqV<`o@G?StYCY%_k98SF+YhWuR+fMIjO`RB=n!Kt_{s5qUv7e>*Z4zN6Ytr}C=6P>`zVVuJmJ>&aFOr(hB4KtJM^^eQDjtw{5U9|>^rfk>OYu`2;C)$&kT06y#F=v0)w;Q1=M`Te|w|{_P9FFM1{j=FozgiLNt%2n#h7yD+`Zk5Xn?2}q_A<)yX3&S)C;~uND%O=8Lo%rG*M#wVGR>{LqMj{HWMM9=6wln5k!!3TrQtZa4!xavkB^+U=IxrAc%Zia86D#wxbum1DkLrWC6cpoi^z~dd=jj-D0G?4LY$GsM`B5M3sB}6q8g-tq@7bOGeTCpp^A@H`)qu{WHOo^#k~X;)TJQSs=($OE;ZF*9B~2_!lS`H8hq&yZnWO-iF8X!(JLDgi;>}#UL2M|=NJ)Qi}eXe#-3!VL*hK`sdd8m<NLZ<qHguejC>m2=Bu?Xm>EYCk90%*C&MU*CPHu^-I}t&Gjv^4Dj3(zMAjQvN?#vY3K(oYFT!LTf($%YHB)m_btV$Iqv$Mc=H6*7<^qXWAGG!IO@>!BiVN?K>{qcaymO}BgGwY0T8}kE<BaZwqBj5st%(0iR;~Q>*A*H4ntVPT@fB~O{q$FEAw$HhDVRGV>g8&{3^9167WpkX5G?=U?^s29*ms^}+onq6u|icgOm5B+*ruul#{eBA$0W%V&ymtVXRB$fS-b0t`T*YX^=Jt4ti4uJ6{iTRs;SZ+a7W^kL-pC0In}uwsUPOBUXS7*$VCFRExPq+uwhd-eQN2Z1<MioAS~W}9@wUTn$Jf3n4(Zd759-UxY3B*ntjcDuJ&#DMQq+4kh-QS{ZM8UNvWil)l%TP81OlVQjD2?H;G>*lQ7L^-_UK{g+nf4rQQ@v*bl5)X*5vBZd|}FZbq~)x(1-U4bc^L48at<uCq(|<${0FA@CP`Ip%*+aW5hd!(0B2vb^JOcSBeY!dqqQd}@TvB7&r&iZlyBu*IU{ZBqJzhn_|h%}cv*TNZA+g)i*F9a*?z7uMe4)Ox%7lx@xLY!PLnQ(M?sQMd!rR&8NtMd6J)biwXySv=a}MNFI%9_(N}y}Ss%{B8BO*@Noa-}amD)@tyzUjB1EvZilbf&vQPTpbsW$XcV8`JH$Efy(^uyIOgiLLy|&n?d(^j;<hKH6^Ndk}v(q7qvOdZA9<yRa?zYyR!ufT}m&1JZx{`yONjmqxG<ZKQ1uFT4!^!2yrN*98Aab#xPWI{jKCPufn!<?nKThy7b=jo@3nS!mzZY!Mvh_f*$2&oL%w>KM>)L4E8C~`5NZuK$SA{9fw3GMl?aHHOEAEu9JjrKX+db{~Vzf>=A$YL{Cjjf+9^U&HIdVcurDJ#XNt+Vj~g%RoM3ZZhrDqh6+FRI1EZiHe;uwfJ~g1C;gB%LQfFVEIZ?#cZ|A@-_OHabmNTpw#9vJzMQkS?ii#g4p<dj&7%(^CK>5OW#$UyJr~}9s<@ZgsSewXSQ!gjQRU|^Wh^FjgTiR7r#>w?C|+5w(11E|hOsNA%Nv&VdGUGD)xnY7In!5AAjPV@Tu%(gJGUXtbx*XSS9n~8cYZ`=p<SF?&BuD#;Z^~`L9x$xW1F59YhjFQ$V9+<v2wDlYL6^~L@1F#FMJrVOApcJX>oIo*vJ!#dxD)M-;fq%?gmcGYLlBuoq%hX{2=GPYeK$$mT^-TZmT7xug8l`W18kK&%ol#<CGA;uheOy)Jja4qI8#YUfL51Htmw&^30q0yKWpc{mJloA@gI%fa|a?!LP>pzbuk>e0-Qp4^|T<SWl*a4YOuu7W0(bShBYSqoOVWE}S3#-r-i$TVKE@-s|kdHn?ePjl0a&i)FRy`VPef=ge8-CSl8&7he4;Ag(Owar!q@Gnqp(B)&h<7K?tXpk~Qvg&T`?vB4#JQJ}CqnH4Ne0s7A40-dWn9D*s}Pw1*PNO3Z99`*U?(Cdr?Z$^E)$0GFd0tO=M+bqQ2yU(58DMap?r*8f`9$%KtlN31p)j0bwo`$f7`rh7tO`L1a3hpx^a?uq8b*~`+22{eA^M|ve4`;!^^?v(FRX<Dgmry67a;T-#V764UFPWTY!DeGLxx9$71mmC+hAhg?c_cr@G*WUGw>|X=M{=<l@nWV69dWndA{s^c?5k;iRY`@!I#*CJT<DnVY3K2IypI^Uobcuo&`Q0aOoMG<r%gf2hV9@EZM5Qk#L7$`rB4G_OUv}DNc3}r-Q|dk%nFjk^rNqwA07)gv}e<7W?@wVv*~e3id;yOwz49k4;u}sxzh^N85$Ux$(8$-jDZo?>o$&o0eJkc78<zCy-CD#O=r&{dNI^@v`Fs|FLc*Z9&whl7RlC@Gn<YV*U!zArMzua9ov$A*sL9e$|KMe;p0tOx~`<{n@)5{Wp77}R5j1p@<C`vv!Y&|Z5INMFT1PWj(`6NJsh{1Y@e>@G%y|-UVsE_4cRkfKA@OYQ3Ygc#Z}=oChjY*F;FZSuF+57-dK<^OiK>p@HD>KPewdwspZ`?N%UC2;$Sr$J88-F&`Cp=dY;HHX0^zpJ`3qxRg?*7u*REnbfjWbNboKXUG`bO(CX4nZPp8}ffcNif6%(T>d)W806I=4Y!pq_@k(1Sm}u=p{adHAc!f<Q`W%Y@4?Flro{<3#cJPn<4ddUzKbj9izC(Z2gEKI=9r~-TkM?hO@Q=FD6yd!i{3}zgDSCo-y(;MU@m5<16$@5zTW2$Rh$e<_F?@~jsa0{o>ma<WQ$LP?>@)GO0Cd6?*6BTl9N$6U&91E#YZ^w*y_rQ@+HwaZ@T{VBEf-M2bG80x*%Yl=1$#a+oIKHOld`m4J2!juJc`@kx`{^W^2~b;jb~}3<1nbRi#qEWp{o10ynUJH1M@A+)@gWYOh+4V1pn^f-)#rJ!@s+Z9R!>6Ky`7lM)NLk><8dsl$N(xFgv9+d=LS2&?2itn3CZP&v?_{(BJRicQ6|4#g{;ad~NZ77M4$=dKVHv(BshQZ}9MI#=n1O`b*%OLRbp^h%)e}p+kox?bl=DidWWi9yGeZ0~2)fqb~Hc%SRWW^PSPNb?84=ZCuFX`s{aUUPWLv-Dg6L71TrdtWE=;OWAN9-@#JE>NNZ`)c1GJGi_J=y3-Xv?!brdg*L7SaL8}3oCn5I<Dq8L2qj7wk2Cv9^h3Hcgwyi?i#KR`@cXT){HiCEp@w)%d)xO^S$+~=qt$dq_#NKjV?yaI|1qoKDHcF*UoXo<J<$~^T=a$jdFqn1gf*!{n<%RgpxvjeArmP737>hh$4rp}meJw9FEItZ_da1mP|zo{?f0<)dFBmW3qkoD*47m$YG+f}fJXSlg4j3ZYJ#QuEXm>TSu(-rEGF=YF={ecdGJA;m47AAQHEz~6ih~PX>%oFLEtY)nH}Q=SI}LcIZ{EZ3NXoj^i;6|3#fxNwMB=UR$|B4)Txv7X1M_TB|y>~S=-tGoL8oyz}{$-+=TtFQVoWRQ=qNyZHXzM3-ZZU!3xYm%4Jq7-O(!-qwzd^zg|F#1^PR+8UcB@W%?lxQ<DL0Xl-*oQ_Pk=P74Y$T@!u$r6~n@$WMp$p?UJe@EX`HeAxU^%{OGLZD3QU@?9|P`7j!|V23`&B?_3_ONwIjZn%18{;H+{H0;_*cB1pKG_hZSg=sm_`4}%@6uC%p9yP~(b^@~KI=3ea1iZ3ZkfqnMnK!?Z10PS+0)t;(9{v(Tog1jg5EZJL&5%u|PPJXGZSwV!LNEY2ns+vJ{D$lbc1jQ)0a{(707)%1?Xg?otZ;io&;Jpjt|5KFW`1ioi}r0SMY%I4_m=lc0-;X&!SI5zz|85+4et*1>H#OC25<cVk&F%TW~P@XqFR&Xv9?oQbd`5mYk~jtH(^#$jT8{HVMwCoLYvwMno35m;t=c9ak(qB=)XprKBQERQmZ!olH%vVg#vZn-DMyflECNMo@DN)ay>0MAll$~vu3Mpb39C~#-&HJENJaTV^A3Rp3Hi)QG}K*#^XO?9CD#pqUx9>Oe%`_^xF++lI%APlrhjA@p;XD1@;CPbfen8El8+86SU#1+4yEwlor%OrLm?_dKqGYw(-wQqC!W)3a|*7%fNbXGUc4mDW2mjTH(qeKCdfwMx71bgTrRHs;e13Pg7&R^fFd$fS|Tj<-&WLy{oI$@-~Z&U+-!wKoCD-3*Pce$7w;XC2B#^zx5+FUE7w05%XWF&;Iow=J0|nA;nCt(X=_+R-RKiC=Ju#WL~trKw=jP6@=mz6nkJ7_y}fBf7-Rh1%U?uP?t{m8(Q8e5yA<rUcOoRcZnXYSXsiiDL@1Jp>P}Wt+gJmtRAi`oozMRbC;|De8LY$-};`GUS<WYE~U&92Fk@2pKwqvzc4wpa(-XB>(|RS_=O1eJ|=%Jd@kfk9$Hm&QkTQ$OI7_ScU0AmT)gDWJ2mK)P#{Oh{7usoj|V=PIpb>P#`ZjBp3M=JUHZ!mqz&c>07}Ivh)`F23Sz4*EgrmIeHhl14tjOyG_ha!DChxezw=ypvm!7dF--Q8(R3W|<=<ENd*$phjryGfd{}XGgyQ?%S&&|axvBQYc$Jqb$aq1DLPU9dYM2VVZ50m(a@dgamP3E%R@;@;#MA3`UHKxr0f1b(k|Nd!{^sx1Q)%O6N=R>D;a$X)Nx@?>F;^jTjb5eS-7U5W>LYawO1-1eNyJdg<HC$f{-@NuN_=lTJsud20Qfp`T?~2{y~Ed*>H8>oXTB|seUoU?3n3u`Oyk0_z!qdnOu?9N3#p16Xi4QXJjFexrrt2@UG2p)5rRwv%bJ*!k<$y~GAg(?2A4onHJ1-vgmG{&;$C#h4w&2TqtwU^y|sy!q5=Ycroa!teBQ!eU&gfeL$Dtx@WW7%&;3B0koF47XX^fviD)|g#}IxzYOeC&oZtaIzH}<?NMDE6E2WY_AS3pkof-5*l=S+JJRc3H${+>|ZPN5SAOxJOvt3ihqw->%PRrM3zCxQKo&z+wu~FWnD%II&)r@z@FUubCMs!LXsBgK^U0P#!K@*BM@6G{)aX63<^?Z7$+$n=0y(3wKemq{xM@1%`b`MK()$8oI-c;-fW9U%^8}*3p#ZR~kVBxt|$%a6eVgGzcMU3ZSDW1hw*0INSNw5Yh_(e@dzt90*N7=U&OA${-Wv9M`PB~$_VS*=3U$}oA9G$0rufcNdxNRe<fx;EqS1|(pr0EHbU-O!JH#W-vbvNooXN~6qAY0%Nt)|_=$RVG&%);ZrAPe)~kQ|q5kKc+Dc06gIWIc4Nm^h5mijJ`j=v@~z9T<)MejkbgTTKed*lHSvd2IY;G|0cdN7Eu!Y)#=C7GY^PbbNZYIVW&=fo<xc!N)Q@HNlr`=^EA626r@y&D9C=*8E~hvigBbRzILkIfqZvo}8V%{o$Q%7UgRW5(^&<Xi6)DlAc{i2+8Z~>`fZ>_+3jD-U4?soB<e*@z2>3U1CEWYaC|7^Gggw9iV(SnX&400$Mb~a2$A#7Z*w<tUpB{lq3yL%q7(&n|`OcX~j%Ay}|&cX4zJAbCdB0H1yKc+ZUW`B5nmz?@Zi}l1W%z$QN}nzO&*iisk@a*9NbtGZfL<mQE18#$fAO)E6$>Vc|8WaR2Vqm9jRaltrKlL5q6u&TcL~A;wuwT?Hx@mt2Yx)s`VG>#$k81u^Xh_h>e_ImHQ}lTcoahJ+;AkQHfENS}DFN%*kA&?J7ZW2w<K_$K|5jp_O;U9u%zn>yRjIQ#?cz#9#kYqFUK;*0J9aTMz_nxZ{W08}(vQXD!fS3n&z^lP0sb$qo#hUWM+Qt7-Wj(eV@e84*S@SMnaEUX}So=32Zg-^E?qZm2*Q9QtleKR_b!-R%Rd8`-x&Mx|0Nzo!4GPxFLN)E<E7ALE^?t_7mJ;^yfF-umu(_lQ|$EjL&Fqx#u?H&k@uf`qOl4NS_CgUeo<P=74WJt3$TJd#PD=dbXI_hWhSO{L7z`L7F=;Z6TB39)dX>wCE1L9=2Q?g2xpat{y_)nDq-HThyXB9t)(N%xIXV-HY7yG3`wN_9Jj|!?X_Mu;TaQA^s2S89*&}z|XiH#zKBLrYnxtkBC72V#A=!xlqJ~zM7_Pi#bKad-?$+6;@C@;73hAJ;0Smkkga81%-BMjX+Pk9-tIUdd?Nv=7WeS?vUK^AToSE?EIc>O6=)6!<1G-_ET8@)=dhX<j-38Z}@LdBBqqEYoH<fO7;8W2@&uAyf7DZd#Cj6~=L9|$?e92~yroa`Og4l)AbuFj`w7SrNoN^5RxqNu8vneN$VmE5F~iofY4-@CY|xhxNBI47|V8EF!_dkAY1k&{oHM!+CJ+d8Fz<{E|y@Pzh_n%q6?{KxZa6W)JQlUvP#+B4qTcQv^I-OQX41o69?+>vf()&Mv==A6W}O~b0s!%4wyk(&^!)92LOYSuVH#fI=eUr!ubU9tuOCK!(YT#0W8e3$nhJ>tP5{4@Mfzd>UKCo<u=&}z0EORc`MaWR0mX2=2l&C3&JT(EEDL|g#2Vy3j65`>0($(BFF4vQ}}FQ+X)BcL8W@Sq@V<7aJ&3hknTYlfBr#kbP66jYJ~RsGEJcE*W6GImfS+#=v~oprWNPa|3HS99v+P_NsmEz(qwDpfb^S<|HnbE$vAIT60RRsC{ZvGJGjuew!8uq|}R_5z9vNbwv{aRCeG`cA>}2HGpdhmPf66{wlJh_Ft_;~(BB6V5udp9!NLitr%0vlQ@73G|Kuz8vjxopqY>sXlIhFhqAekYZmjd>$Pi*?SgVhec+`l<Ps4;_uXbu*pS2(kv>bK38%yrS!8p`=KtZfVG;Vg;B;)|MoQJ7d*`KA2U~y6-rGU!A3qE^ayj~8u|ctYbJOlPH46hJWkbbrNAT{k{yU@l9MD0a)ydG2W^`+af-yzdzo6Zq-l$5`7NpOlK$!}5o16#U5QXac0<r=oy*V-MU+xRhDOX?D;}*N7#pK5-@A1~fFhu>byQMV_PjXtm9y(vvM8>@NNCjJ3m44syDBB+1v=mLMWrjKf*&v&!>v8`$PLDn%vFHP_1bhk1+A)PlI=yeka%QYWl++sC9YbfQ<O(TYxtEnMQOU}=8vX{scU6~m#Q+WI@*`U|G$*?9PXiY>2P$5IZ^m>tA-oU7Oodr%vmYSRBQAMQ<65-&7)XPFkU`n+KO?uFn8Ugk-B2?zT9hEtEE5jb5$aH7sa(ZFq-78=l{HNw-lpWE6ClhoNmhlxYxgoCTuT`>E&|V_e*ws>C=Zr${C62>^{G&uzW%vko^f0nQ8G{WoMfx+n00;A=R+pQbn>69c03_V67W9w_Dl7_1(BY0ST$U{P2-Zrbp4_oXX-k7@ZYv*6B8h)Na+nx4MCQ$cAw;W}W2pq4azluYf?~q`}3NpYxZNdqt-~;_4fLUNbE78ab77t5o^2du3zg_|C--bsnqpB|>)rL;Y5@TFplr+(8RxprdK}3cqtYh{G)JAkX!6u%I2Yvznin(;sbB&FRq`u5R)25`;Buj5U@;+51&Vu9Ok_+>14Gshi}3j8U7cSU<j70LQ3i{G0<sFXezRW+`48idD@@aL<*yP4<ku3>bMi>&Gvk!*L~#YiR4moqb)?vrdnZOt=GMp*J@v+)I@|%F6jd>z(}o2Q|Wbs_So^rtT_XwxAv8)k_)^VtUQEAv<Zx+Yr*b$|k65spi>N0JH!$^KMAG+p6|nvoY2p-6I3dQzJf?TZI;3zZe&K@1FPQ-eqaF=Goybgp$!Y_bh-9ysfEgC!bmJm2u%#;}+uL?WQiisHJ_4ddam=NUkG#-NHgRB>%tdz1wmdNs=h|USE+y+vx&C00O{^D6k|MMM))XQx_wtQmHgL>?DvNvXw-lkpM}sT5IzG`?zL1wlBM%uy5yWALjhYe8GOg`XwSVZkb3>Qcv5=v~`Kd%m|MN4-XFy55Ktf%CgKf%|31dOSwe-$V0!1+765cL@&jZ8SHuKB>3%N2N>!6DgtreqQr1A#MHnTERcgTOw(j}o=)yz40u=rlA67qeMhSfOQyHq(Kk9<>CG22cx#}Ayxu9N*tfIaw6qP!j7p#nv1HE?$gH5r>ez~`%ANW0y(Mi6{Y`7|6X#7OuN@tl_G03J?+n#P@q)FiCVNfOVVct?vvr6Ziholg*PH*IMDAh1u5@L3y68hK6|h#Sn+nuS>v!tA6TLMZO&baJi}JJQ3TP94V=M#vXle#}SB$pQtI0rpXAPdBNPI2uYtNz@MfElJ4fm9P0Nx$QA^m4rR*GVq`3wk_Ut#Z11liQ^ru{Ba=xjb|2QN}I%?*yp7CE5Q<{)vV=d*A+jt8joX&r>q07YLQu3<btGgEm9p)7Lm7+xv}3Mw5`bSfYRR4M4%Li!+_<}I10PtHQHwf94jQ={9Hl7)&5tvFNL-i_Z%L5>J6*OMs6Lt%tiHZTHLyejysS`HP4{jC>(zxM^6hJVo<4a;bGs~x<VqC*E#u{4g}d@AG4VR$;znh}*|X!b(ZFLcQKb<ZvFflGYg5+AhlrN;o?(K3?z1RJtj>>Z}$Rd}r*g3Hd&ic+{885=}F*$A>WWqrdi8p`D%-yy<TbduW?&cjK)%hqx7iomi<CfA<suKm`uVVt8ckG(i}u(^vusVjn>I7>H7+Q1ZsYF0S5%{Hn8_2J`~T_+HH3*xVqQuS^=exOCAr*>~c!~m2ClKDJIU;3_TmBUbyo`uQDRh-R_LM_zrw9Q{m=lJP#7@aqA+`G1$n&kq_gmrhPd&|XW=7^J}o1CiaJ=V~Y($hqVQ<BuQncoqEJpXK*w!Ed?C|_*nZO+;aD`MrO?0HPsMPvr7?ww`#GR@DBv)6N{PjU64z)YV_E_Kfh8G-0-FxM?geT)$RI-D{0{xTej|3ZG4uRXEH2BvR`$8SBGn4Tp@5#nUg_0ySc@+mkNr$Rc#rFSa)E-5Y<kNZ*J+JFWcye(Aoin6%fkl%{%@C0#zvaw-au;W1pb6vlo04VtXG5!ZLYb}?%_%U|?ZCc+O{xE3Pg@jTmGV#!zs3NHi?!5siT_I_TO9doEowel`3K)olhBj!@Lrbw6av5t9&uMZ`OfffLVqB@7_q5Hbd2AXTA6n3K3!m(!JE~>#@Tx^p&)J=bW_c7F(fBlu#|2`ez?T)=%VWK`{(7-w31_KTQiL`pHX>*S_N$5gPMC+T3S6=Zv;yOQzY2PeYXx0@r9-!hPQDH3!WO*|9?Y%r$%=!wMZ+EK|Kcdv^&h#j=PS<KE@a>KWJ<YR|G696dKC{>ZxU5$xFW}whBs&L!^?<vW1r)ryaS%5S0aF)aFkM;#4d?-un#m$8Q!^S-N6fGeQVa1e2#;amznzR<l$3VA+bL-iv$fZ_7$`A<%e70zl?*FE^@)b+@+p>u$QC$rE#lf3V;=TDR1RTu3gYu?0DEzXC<)bxw65e66<-g5{yw*8&>C&_tn<{oRsv>W@Ajjh!i+lx#H`(hYmNlOrc-4mR?&wpqlJ0Uu2?-7>w3BJ<+LY&xQ6u7m)I|O%V~<g1c9gPSfa}3-8wz@V>r7*3thJAaWf1kvyFPH8BB3zK91|5DsQ3JPIdjo+EY8&lVR{9U3{ZT_okVmlNYtB{hfvcca))MsH)IOb4Xf5?u($(F|j^<`J!pM$swKyng3)CPlTd3!;+dC7L9!g#WkeUP@oXYx?S<r>ZsTT56>$VPd7*(YK0?OUW;Zs{E9XrC|)~%5*i%Ydp%w*D!`^)Nt~8+G$qvX7kbL?JNK1J^iC-%KG@_2O~Ca#({LinF}}Sf;c<5Gp@+mfE<T2%!{NWa<%+m1$=e1V_KY7LocSgacTNm{R672av$OREN$9*SkFf201Q0xOPU;9Y$9JYUBT{Zp5z-wTX&_wKah8~)3KsjMA`g3b@pczyR;VWg5c5HGNOkplH^E5j)9FQGYohi2U{3Hp+Rvq+z2!FYZ>dt3cP|D<)2XWYnAL;51Mj|)b-K;ad;SC#PeT2=vq8)U=~U--w^5J3xc;$hIv`W;4`Cmp78+GV16*InC<N%=ll)yn$UVGJSUV@qgD+|R_K01z#zp&zVDP)UfPwN@x365!6?8t#h_rAr#B30TY(a@%_Rr48efTx>Y?Hfn7O_me3UVehd0WWT62!=>klf^MmU?i9nAY4kA3v;g&FAL0svaf0|4A}3sdwL2@`#0tHI2p2dsh#BhLDs1*OKpOR}#m&t{%!6zQukf9UUdUi#Yarp{F_`Z<$m>K-Kcg_%UtX3_opXVd1;{rsnzAY*UtThB%*wHNoTXIaYT@O|fvOqlV5o}?|C{~V>9-C9u;IePT@kD7xqzvRD7EvikQ{%vX@Z2I)C%J_o2Z=e4(?GPA!&D+Xy+v=-d2KIlmkuP_TzWSx|#>naO%%mm+_k9iu>f*5Pn%YSw-VbbxyEP}l&8`z8Z3CK>>zh<37#3~~m4Anlz?GMu%q|*vejerk<u%gFaYN7Gv!Xxf&ZVdKDKCyC8aW*dF*G$-co$DR<>TRXLr)F#wi1%Cq^hRw5X<U%E*f=AtIw|sQSO1D<6eD!Q!)u282W7FBPo~`-zfC?QQwaWCdvcAm@)PJWzp1mAn0>=POBdOElS{%(G~z~X@Aaaxqd^jby2j|;}D(?gNH63)64|URSHxsX{HwR?i{1(6~w)}IY^)zB$*VrP(f|Qa01msWB147C?KUmkTGC&s|t!!CSP6HXHU93Gh_C^F62Lmv8uw7Y~#ssn#4otdaH*26Jkl2!EnwX+mWz>|3^v|3#PLzfR&+OMZ`jKx0Masm)S9a(E2D7i<H7OU3neYVtzyrr*tphf%3PpcKRk~6TKv3enT%Nj-CV%<4450Qs)YfmM}35IXzeA*GDuv4LL_<=qGEpV3O;rQON~%^FEy=!~8v7o(<dXCZ-{?Z#*?M?DQp$wB5Nc5F}q=a*J0{IO%Ij0>l*Q2UMY#6E5SO#JnP))2MgFwIs|Iqny&P<l-9OvQPi!Z^G+7{aeIjDER4%bQa&FaIQ^$J5GR`0n@6l&0|nz7ZN&P>Ke{@n4PV5Q_DZx5OffWG43$PzlCh+Mn*8#m<u7s0z+rhcE^g9N67^Jyi>QH$`Y&nb@(D|v6aHU-mslgmb953bz_*MtrLM`#PyPt3DA&sgCHn4zqUbEjBQl1!b-oD4VHNU?Du|!;o+KLOG4;(Zd+vyqNI+`DYkI1#h$H|wPlGis-j@rsZx&fFWoe&l3i_D(H=GaPc||3Eq-xFUryHUr&i_fO+TxxSS5kQ7HMg}>}#9CDtJQ^mmB%5ce1K}rdsDTRrMTI`2<z{>_if`we@|6%)a;A!Tad!=ffTvPyP}|SCqT@+2lN)L_wYN37uS}t+!!@Sp%M;_Xy_a!VP#MI0%z?8qKork=z%F_8fOAxx>;WLneCrkTaCa_ZSxU?JPaFiet1W&uc9GWHB0H0A}-xI{B>l3`eKv+6bKKem<du<Jwn7TQP9;y#TuT-3E{6Wd>})#Sh4#9Drxh&|3lCd&|e(ZpCJ2e#q^nFQQqllUjyXee@RI*=6dV#`D1#EiyNE_{C79h3f~Kn=1AL2V3t4AM?;DyYMf1EwKhhNrM;ReCy>fn#|#(WJ!P*`k_oNvF?swI~N~2pD6YZ{MuH(y7|klc&l@z3s)S)4!l|<^BB!~G1IQu3A+6)>4sv|ES>?Y#veZgTlB*{kx@RRGfct&`^6Tz4|MexWXS_Bd)CVyzTC84ZmKIZ=%oTlFCGRV;^%Ha8I{71TlBk2zjvX?U2Fm$x;^@`>4C(7{SZ=DgS4$ddSF1>EQ8czNIebGjs~gAofVL_${=krq)iRdeH~I)hqSFjGP17%P(Lxeg(W_X_)cz=UM`P9IKzhYstJUEIS5AK%%qZ$NbYtoH{E8#9|6D+&?kB6I>Lja6$0E_gX$0?MCl_v(WvYs<(|k3(mELB&%8$J&?ZKVjc_b?p;KA`n)a3or$g_ys1hF+M|4eQS6zkJ!!-T8KmYCBv>q*^rbtvO@knvKu2ue099=7ba_}Qppp2Gzfvzmj)eGF@1$weT?~|EZzzica0;zkng#T{L7(ye8A2dq#uvPi%M*PaJ-WStfS*6p2pC9s{zwsRBhd<?yjSXRbkOvPQ<jjHVVg*rGDT%bWXBpyWgz5aSObfe%KR;;tC`6EWjTgeBYc8ynpmZSo8n1-~xL=*~tcIctP?Q0RG7Ci+p(q2yWJ~qyM*PyxwhQcdhAoZIULwN|j+T0p3+y<*$M~k%HI+3=V8{7ArkQ4F*G4nEYRnzQS})o49zPK|XG`&fED_rmk6q$ctvWTwM2H4GOYzjDryKFq`=m8OD`z1ap_R9gjXa=67OIg=Ze(FJvM?H1cpKr~!Qkm>ho6>v+Tv~j?(}6lGTIm!ZH&BaQ0IUe`RTs##QY(D^lY?VCV<B0aYB;aEWD_nCkJz&tjp|phIy{=kI7XpDfJ4LYO~tocpMI+8CPuo^6cp3*{`R^FZQ24lesPVOGd?x)5UBM)h{#Agi%CvMF70abS({+0QrT#z71y_n}I;_$AdSo-o8A1c6xlWfAa3QVQ%tpRA@)DSvsrNemM^4SHC7}DzGmnqx3L6$F_5=sI8mQ&51^(*m!=l|MRP7uTNIuW0Xl;7vp184IiVm@$q~$K1NmXG35h-juA;&#?Zp~JRFS0$gmR9!>SS^vjiMSK1<+Oz>6MHAjc1b;_rtqU;k+(dJdr(4}t_>i6QF1DjbQ|Sk|);30tq!aq2jlGa1RAxrg|^foQH)&rj~Ni}C_+ATKX~C-L$Ucmyvm0Y`6tfg)8j-p|m%RGy%%6UZQ(T!y&phUs8|PBJ(f&l2*Nd9r*ttk=$y78k1NBq8d-UMYTJy@PauPBT&iEOstBDm#VhwX5jtJm~=y{2qj`mBE2ML>qwF0wkv}nU2FgpQM`sWgX*B!56I;=Sfay+W8yH?fLYFr9HWAM*{EBU+?01LP))yN0SWZq+WaT?D#Zd9G}u5^>h(W<~1|mCNDe-mvYxY!rtuQLF><dxCCh)ry8F{1Zp6*Su}|0^*BBsPtmL)R7$gW5?n@u%^*AlvUgtsscSE(CcFju_Pj-+_Pj<)mai9+7><w^B((&K(~HZgcIx3aFZGUSZ?&G_TZVqAcSV1#_eFo7EoP%|5FKfKx=bl`Q9P;Zx<={-9=-JL1l$jLt@S71e$Z>JKY{26L(w`Em>r?-I+l<+Po)h33Q>qCv?YuNTXpJ?FBrg|4Z0Y8Bf7Zs(Z!{gE-t-vap|WE?^H<gphgy_Af^?3K}*VmG)ZR#-`PmpTY{Tk0KymNW3<UGDge7$m?ZI_==&IW?nO8)`g{#XSd3gy^nH-T(^cPp36rAF(=f}*swa3UcQOXXVy&eu{2?$SR{$bS42Qnd84CFXYfA!)W#K5=M<ZZ(KtqKd9>DLDTi@2UrdL;mpX7zRyI5>j#E!HJqwQZH3j=wRDs6|VbezIy)EDHCA5gI#RZ(gK$vR;eXb-uC_jO7&7Ndt245i7PgabO>VpG|BR8$MPQ2=kp0}lY<IGS9lB^t#@03AOR&H$o8;p#ZP9LNp>d0+q$b+Dx4Hsa@LJgZ1p9CFjixRO&Po!Ph1J~bz`;3s@%`a%jq!L-&7jru<U=C&K;M2{S#ji*>e)M#~CS5KJXgUZ}AY;Rx!{1e9nG+ln-%OIQ$i~Mi3%3UN(t9Fh9)J(NR*?U~p4^zkw#b`2zZlUfGqvLn0ixM|K>9}!*rsV^<cP}`e0^0_x(Pc-sAJ7eVkee6;zqRQ8J~-Ha8XTaTNlV^^9E4MAzO@ee=DX{k?=iY)qY42COpM_gV|wstP)pWpZ<>hYRU1zC?G?_vqu244)|f|!miPnWH@m*l2c(k5C4|jTfDTxV+*KT1Z=1|Ob~s63w`Y1>3!cdBZPgK4Q{&<SKM3Ff8j^G^r)epfRhY6~-w0--2f2}fZSt5l7~-aQ$_l0jN5K{qa&neNXGJLyFoMHaumTq+bVg1F);f^uJUk~mm1tV$AiyKccbn5dOQ!)q@>av0s4)yapDPcy@9s95YRl+ov)+UE+-pvJ>ggfL=rpMAE{&>3`L?j%ce!ratc$J*QNQX0)2Lpf2Aghl<C~~X0+JDh5C(h}4n98zi3du8G=KVh2Fn$mp;IOomgO1*wDo$=YU&rGDH4+;;_YqnuxoY;k=lZ(?omwK9gKn7-ri|A)p~9<o}Cu1Be8!wwKjdVI@>&V9Jjb(MATxM8jZT_xKkgd^ZM&1^t$0j-;!l}R@q)j*-fkLrYftiPIYs9G7BeJvOtY`z?aJRIKPOvK@M1HVy#D$Mfld^WQYMfP#Z2f@=L=*x}#Z?O(I+u=t<4{5(_0zUz0}AmZIxnt}m_)^dI5{(J!8M@Y>{8(Tawg7uNzg&0rg)6<T9k+Zw7wJJ+y6T&UOkxMcR6{Y^jTs6EDf?b&8%US8^XX3?iXq)cJE{3eBplp$l0t3+AQLjO3Bg3pumit>`62h6=e3LN&10iG6QoRMMJ+a#PsVuD_`#eK!j?w(PBhEC0kKrlw-$L5~4wJG=*>=ed_ZI)Bby+;yKF0xBf%G<k(EN$27(>1eEtyF*+o|*A&ZxiFg#kIk^A3ydQ1`PV&hS|$q;tN|lNCS0AmdtYTDuC#R!XH_~U>b07gSUe{?!_+NV=zP#0x2-}hKwaIzZeo&E_Yef^ss<#FeL!_t^}}ZVF_d8Q6LNul(T7&EH2_ny2ygTGMu!|(_~27f)B5Pf%RDMATec^ae@<>_nMI0kVwP>4i+Lb72t;=9oYEr4B8nQ=PV_kVi-|&k$zqV5n3=L!+SU&AbezGS1}C!xtKT{{&^nQUn6HKEXdhQe~*>$#nekU*zPH^Ho5!#Ee}}>6^H;>y~SRScNs~Eee)2xz0J$1;aw4VGrS@?ydrw$is-Fg5!g1(z7Rg06>)#JbUCdigsvcejS!4A*4s6YBNl_rWd#9~7{&b^n-R+c52Cr#wHM8GE{|Q4{A02MnuOj~qp8kKcZnMnEq~lq_<<wsqZ1xiER2`r$ltW_ac8uhPrO#J#i3xkv5qi4hm8ZySHYWU_}4`gynS-iI*jKLd{_+Qls0*tBd{hkIg5tqUZB%6P^+P80wVROrX+h83KpN3pr9K{7}BTdF>cCFpts#?RpU7Q{LnP@Dq`2#YB-7;txHO}H4npOqjee-v3Bk=!R<C2t&%pAEOsQ}GMb6-G}v8UO`Wbh%m~E-JZ-|6rn~(>119<bD@H-FMeP^ea+yj<RO5IOQ+Nj+(}NwN*e$Y+$Q6xlJy_*kk0jPrl9+<rAQ$v&wH=`njYUMW0jmXIt+92)0}02H+d)V|k6-;jhDSHnrHRA2qKHj;zj<GfLX(<sMm8heN-oE0qx(e-ZnNEEDYMtJ@s5}|iOoJS2axoV>t`L+px`5NdV{(g;07^lV-wg^n}E3|Y<k#wAQ&@sjQM)kUrOMLH!0S4?$TZWc(Jn2mN8~I64GhlZ<{f9gfwX}=7JR?!Qr$pBNae31}oRSak_JuGgn)61#y`j0_}d|tEu7}B)`t{Tim34-7vJP3GDGe-y1wS`Le-i6JY`J;~%epy4>+9Jq_pcS$qZ}rU&oNH|+)}|K_<MbU*6%LGIUT*M*niY>5Xv_m0Z?qIFY#@!VF~pY$%;-~N+bA+A9`|5%gqUzdsB@iMXEm7#uJreAa!I(^>8wzeu<kgd8KG{G0#3V!(yd`afH7IUt`Dqenl`O2#zQgMgphU6gU<i0pjh*Nd>;jQ}hhrdZCfL*=e-HJ_CQ0)uj99^BCEADThx38*HE>;(tie^i5?7KOm!~Z(ET0`o6Y@FR#=IwRNGP%BJr%+!c1b{WW!s^8>7T+n!pQ&CH*Fam_1?okw3@%Wjk4q^*_5!KmVC_av*KQa(4IecQ=yqux>Qkp>OM?Id_h<`n(A8BGUw>Vc-?gl~!r=pTrSmkLtUSkJb#P>(3eH1n!AA+%IQ!8Nj}CrP0j@N)*o?LCY)TN|@BoHCO*KW8<Cl*H7*e&<(>IddE1sIF3XLV_q%}HRb}(|frDIW+wYs6XS30)$&D=8cv1T*b&kspPiIG-9iNP{HO75<?su_83?B}y-HItW6=xb=h$$c>WM$Dp19*5BK@*XG8(h7##=6PZn9CI1nQPWdISXxs&j3?3X=P1SKj>>1{ES?OdUGlTbXfn_0Y@OS14VisV#11KTV=_io9cmanR(K{}>k)T$%OVP1dm{>-Eh_`?ha?<dtMtNW*T#os{=sk?;?RW@w((mBV#K(QGJA;b8#RwGx&|QYQLx$TAXFGP|9%{7Qb-le>nrb|6Po9V7UBq2_4v98<8(5~{1wC5V9~qu#|h4WC~FZAx&y9L*?ZJYx@v*Hdr;^n0flwJ_-5mwC}c+y$n=Q6*<WXKE0aC;sTH6@(Y0*{$W<Q^OJoFcGJ<PNe83@tTYSbrk238=ar}d2mGLc|@h!{8_v^~>p^MbgH@;sz<D<d-+6<OzeAWwRd@{Du<oq}yo1^<ZXKFKcvdTcNlLg_)7XTvc7;)>f2Ho+BDt6hfQMR5@*a&|OZHT&f#^k7C%7-X{=r8e_fnJg|Y+22&uci=`dd1N(bkw6lzC|!v!Io$;@VsnzogNC;5%41KDjHvxuOW--$4i~$$IG?peZ2HjJG?KYbsa^>TJnDAPi2@@pr}5Lgpq4Ls$!l}{z7?~mcLNTQ%XU$a~&JBuuBCEO0ZuwJTaO>GXR`)w<gf}UakjMfEpr16HL#hbQNpko-H<bc-lWY+W&C+<lXb<&yJe8G|<S4(=*1ka*IO?=mOS8pRtz*r%#Xe-+MOx#S}U`%;gh+2!EP+*p;S?s?yAZrZhPwN|Pg=G-W)KCfW{Nz01P$NK(?OAyI4X{J6eiOj@t<rj#R8m8Nn{!-}TVsBhU&e$l+5Aq}gyY>I-=RKp)n+b!Fn7&evK5p=P-oo9#7$m!JE9!A2+9nawjqmAgIk&ya9gi?f|Eh^Y&ceb}TH9L2w*Z$@`<h+-A2#Sy=Q2X8M<Cj0be)jbA<?E9IkGM+h$tXbG9cCM%{YLc;9KU#TbmH;eM70a>o4y>9z)mxm1B|``_Ql5+hUg)zPBlNjedj$9IOiVU$zTBWBUHE)hwd|+AE`7z=U;8J^CWU>lUf!&$5sXz*%cy+oNO~d2dWsCikr-R$~lqwUa}4IZNA1WD6}5Ucf5AYcakD=x_bKI_5Lft)_>6UvjS}3VB16s-eQ8JsMK66GT%OdXW5e!Y2iFdedM5>uziG}=vjqkjI)<`%nG5E$vGT=tf2*cYYQ{ZQmD;%RXUAYe-!e3vv=-J-MMex&h1G%w`c6!oh~(MeWHw@N^&6j6zTDm)OVho+(j1}v%~tLTG#hpE+35L4n=GQhm+KFT8>#)MUu;3M)PlNTwC8?n`pPbzOiS(hOSSB_3cQXm%xjZ{Hr-hntbSw{l)0f=PU4s0TTu1YU{H0h?3A^O33sw<7!)Xu4byXb0d<BSl#X>WXBbAs#t=p6}=TYo2$h3NyC~6vD0*(Ptw8Llw($)hc_3+kf;c!E>)AwphkMsnxP4Ty06J3V0B%P2%Wlb$ZlYDT@dn|x^LOIphBmipi^6z9;~j7OsCe+c!5CIBV%)1SN^6N(Ih-eA`WiJU0}I{ThL2hYGvN0q%aeun!zTWKAs=G**|GY4}VneJAU|Lu5QzD{ob&=<FCz<1s#V{>vbFn<u)DH%}~ob{>Cg>&~Ye5u|X?$oT&6xw2~h-RuYR<w1`@u*m|9p&I)UHUOU08>im&aw4n1?tYYVHclh~|M^=2bfAZ|;<^JL6+oNa4&rXh2j78zEaGJ%*=Y9ZEKVC<2@Wftj{kyY?>G9~|lD@G$Dq9Tnwm;#iZE;Sa8PQXK%xfr4V<-3`f-**coIyIDhkbn1nz{dg>`nOgZr5yvZAvypV|p`aIiQ;9^kg#^;d~yQLiO+>9`yBQ9(3t`n6C=&o6YdmAsZvyH=5bm@isF^r_*S5dNxZZH<8hd@V)1Lcg<!t*?d=A$s0)1o4K!=L9>H?uEEsjW-Gt)yx+6tM(e_MPj9BHBdxnFn-Le+eNQvndOQKM8Rwg728|AKq-_%kTah<$gQ6&h2T44A$2X6eaY!^{t3Tw}>RM2lksBV}in9KDaFGt9J{w$Iir(;fRogZ(IKD5~JDew+cX>E{nHS#3k^T$Ca2HoV7>Frr>**c~!?_0=+zl(LlI(v^^`Bb!Vly>?DReDASYQ?=RMA#MgFFjeb255$8DR|KEJ~8)=`iNVQj{jw{Eo@Ni$71I!Dsz5+Y0QU7f^TCOh<ti_aE4Ffzy2pOB$Idz!|ATVPo$H59YdR$PD<4@A48v=NT!3o@3~&deO<0?wIjGUO4-e6(VL6-ni0l<7<|^*OA<9%8*B#<m-Jr1j!fL*x54gCZXbsvWg<r7}VU_HERy1GyR_L3igonsy&P@kp$!GC^<s$kOC_<gPu|K%4$)&7odUMMc`)QlW}R47iJYQ@ZeEg(ZDf(!WFA-=q;}udOg-on0gg0lZIIdsu-sr+=OMAEe?i$)eJNxD}|4G6=t977(pt3&zn4MxKE$GJ$Z3@^6dCTs}*PR^TE5r!_(*c2hY4;pBz4W{ZtpYnUd$^Ye&3|Y&vU(OfpEKkj;eZ(g}1|MP114Rb0KHQL*!Y_;i=HzwYL)QS}GC1`XrQ;hQ5NPMkh@c@q3BP-D;EHVjS5AkE&&iN}jI4&vOVV9f@3poQJT;G>!_D#p>8IX0wtC8Ii{DHp=N>%d-ySB<6@PIomNyysg9r{{-b1K>dt1oNtXI!pf|;(_WheK$Gz_S0uS_m1|T0u=%W1L>Q5leT(Jau1|g0mTkrtM}H-;d(h0Ra9hY>`aq@Su+P*5d-_tLEO6`?^#*nh({i%DBajtAOC6M<n{yZ8gPd`{Y$@J(C-&b)mlGq_e-92wA&7z&cZ9<26&I17vHiWMSz#7n9nD89?ziP^{ZJtk1`JW7Mw-U*+_&4Kzr0X4YkgUo3lrj(7(u(t&n2sn$#`~qF~Br@%7f|vd#x<fgE+RmQ~?oO%__Uh7#l9$xcbKn7<i4f!+*pm$*~+<alh$<d~>vEBMR|zoCb-(;%A;H*y?XqbdU+Q?6Pg_p%k@s_>n%Gd@@1Wna~cO^$ED4#qvp1<`TL{)&b)U&kE|kFix?IRQsEG!83KFllWV3Z}L1X;+;zML#MWHbu#mDhl4ZU?ox;8FumT<?Cn1R7hV==3O?d;GS5)m=pq?z3UqR=S6P>sI<%P-g0GS$%>RR*DY40rt2zOkvYK4YM_9-At?BhyLL(edj6+qsf2%JF8(;E;qMw87x)VljAn7}`k|`h25KGAKQh!$C=%J<+WN8m)&o+O$2cr#jU@To<3}@WmH_#c2V{3t1)_4~k?`ont-(pR9|?_~Zw*Zxn-N(3jy3U$cgqQ9&Zw#YWppV8nr@W6ZU<y**aL^~z8<{vi>Wp8y}OMEtFM9xM_2>k<yXvrbUvwB*6r)U$sMY4R66^ag;UX#|4Kr?%2Y-3y;4q-zD0`2M>r&ochv%(51eu+1RF#=yY&a?bCCtm!AUSeHy3^(V&LK-<{@#rhQ2H22N`)5(LPd3&*4an-;a+DPWKPrzSyUI;?3)4r>|bVes_GT-kWvvlM^?(=WkU%AL%6qizLA~1z6_!(VN#N7IfH9M9gE_icWwDzW(_Tx1)R;Y3BExypI(%@MQnsPv07T!5Ppr-Sl0o%ez#co-6;5Ym0tj<(BDSb^G;Vhs^U6vTLHTXSQF0K;NjFKI;Kp_%K}Liw@?+2kZi|&=Y3_@lXlaI^D3f0N;knu=f;I5<^J7zzB+wKf+`<4UY6!DgQ-#x2HWo`im4qkGT;N@;JJPTNIdX8qP3?g&sRn#*4%#k$KQaV>a~MeY%d6JO)mQ$I~?M&HgFsn{h()YMwiPo=&aMo%)(no0~h^lU%%UeBIWuV)OVq0_#;HFx!k}4f=9tq3N;VFsZAYldR%GUwjD<fl4>qz|s&MK%?*DSu{cwO@Ov9Nw~BWj#uhCP=aZTAy~qlIFq&_3!xFJH~#&!CM5)Td*U;c1UjFtsxA1zT*I2wO-`?T*HTvK!ETj8oeG6|Ju0;6n5KVsRfS_6^be-1Fv#1e;9q0;irQ)ihd}qJ$Y?zZdQUlYvj{pW7FJOI!{xL!;Flr|M?>5};f<0gE=t!M-!&iSld=x~`QqZwd9VNMcKgrYBNL~(U_;$AFciuLeUcszW>GY$UtPoeEaAVKCTov#ZLyUE1zlsH1m_dHLjM<hq8xo!OYy`x1+Q+zW7o{NHdqP}T?53n0pfuLV$%e1BS7>F5IY74&LWtD*fK#}2@snGi2Ejpt_foMlXg{hMc2CRZebSj$&doc4$ygMaAkeLTh+l*`(kC;x$Xyb0&q7EPlgw@G%=#gl3e(=gBAn4tCe}7lJN`&zx5Ge*iupI8(gvn;Sg4Bdi5d-hxGyG;+n_PU+LcuaFmT_ztX?(8<@OF6ch57!jHxvah|cBeTfP6IePAv_%gq4pGD{K<ZU<~tMujY@*=&APSSeb5A7SWN%0NFkIeu~guH>>xr^6{ScAWP$iJa0-&GYjtr9pb7tSC_VIQ^zFp86;-YCTP({urRkFd@dzwS1JCH!~YgTL^fh$J=)GdN+GIH%<7*FAK;>>3x$i1j7DUz+bZyo#2{4>ODpm)hm8h=Q_}2b9^f)AkLKma&|Zu5Y;Xd<k)AhtWj8^1k2RZgOw#%1|Q;Us;IKO^&~8K1)AG$MYrGQEDFW61fGRa8lok3+ZlqXImSiKqWzs=D4vvg;({DTd=u(YE&ago+g)wc-ox)8za)&l<oPKpCpFX0zKXq%ceqSc{M>hSj$rhJ28V(R62`FDDy26E`b~1e*gy4KQ)81bT$+kWqprm2Gb-QM8hZPb);^)d=olK$;!BPzte$ZPJ4HH9sGC@W`l4Thrt2JP(L=|52is2LE8B7I66<G;N44jdy!63IO7c>!!LUp4w1#)H$2bNYc$U28HOx#WIQy5QJ5`e(Fta=q6}PYxnKc6vk<7V!42FEdRmfC!!sTO@GH_LGmIA3Zw2^ia4nyiIcqLZhJXClmI>wsS9?L(O>hF_vjQV!qo3h0ltkqC2*=w5S3<%eB|;1mLD%G28cbnAvtSZIIdW1<;8+}mgK?0~$0B4qE)SC1+HuA*qCTk&*GraEqvVxLzbMTy{xY4CvE(?O+Zn$!IG-8FXMmu!C=Acxy$Mgv5{5v@i+}w5Y0oJmMv5eI4baah4aZp<Cw2=DSM-RpgU^rfdm#+mua^X4NifEkd>COY8O95GMi@&wevaw|l$Ox!5W`3f^(9)&ondx}$7R%@cVP=d+8AVX)?RAGtr)~S5qZ`(CyR?2w+V_jg0oo^ezq@O^@$>P+uu=QL1*GV`V(LE39rpy+~=-*@p;;!Db#ie%f&vRuSGgywuP7JM<Bbh`b6?9?PA*~RcF^`?gw_F8O;19I?NM2H4L*Hd(SDpmZ;6n&%%0d8yG+jugH5G_36P@11}!=Yj>O7kwuWNPNU`%8+_Z@R?+^bF=yWvwC*7O(B0~Wy&iS>52MY|{n44$N93ItLLB>s9Q`654wJ|lgyOPIT58BloB4v#CEJ3{Nq2rk`jYFFsv=+P+u#aK3he`+mD@2nSef3@IjC7_9wi9Q^eCRZ$sV<a=alB!Q@UR34b28HBc~_D;UK&qD<H#YR<jH8SUjpKkJZmMed?nLpzKREBgg_+FMP1Ri(TaO7KV}2TUbWQq2$JqQ(+w`zi0-MQ^P{itcn%)oNvlda%x&idgWrM7S*ALP3oq83W>rQF+Vn{)Q<6*vE!XM6RRPU8b$X1b!@JglzCPyHft_Z+cj6i_4&|e&h1*rDe6(-x5PP;Jg|nqq<#SbLW%|YWafL38=@!9*fCl4p{fdAZ{g<Uge(RrcZY!YIH*IXc-CH(nv>%etrc~Wt7qZGG>HH&`(lCAWqbPa&yw{g0OZ4iaS8|1K#0A_%z_Yy50gKQ@JfW@CCyV|z{nPkGt^9hc!t@57ldG7@>h7j{fm?{KhPHd6cPmq6F(H^L{s~dbDmUT*9mNz78wPa0ZzSF=2@`R=0!IzH|&#)hS2&S$NOuGh6n5>3ud&U!X$+fu*G4YDc_s8cH(i}ah%D+$@!67iz!}V)bo~_0SC)5xCvA^j7Hw_`KY}${~{ZrLL|D>>#F^GvI<~q0^7%b3ns?#`Y)nYt1`Xy*Ue8KlzirR91{TLI<fwA;D?;=OFL5E%eJ~r>+1Om&7PRim(+fcCGFXp#rz}V>yyZ~)ATfg<|{r~a|+cDafW>APwBoZTR{wdGGY@kR?#yARx;iKz8Q_+EdOh>v?@g~%ByNa)#}|)UmU%w?q8k{;i&2m6r%Jo(8~&gFe{5usLHn*hGCzcJiDH+5I#Gd`ww=`SorJ?qX%a@#=#$8yhv9{utNaR=?DpS6rOE$Y#@}sY*kNoH+M%2WM^wM8iqCy%I35J%3x=6)V(jea=){+S<4Uc>b_7~4vZtrq(-N9=DRU(2pCskoEsX<(+j@rUcwAOJuRFH?^1RkfSZ$RJ^<Ehz{F2)PN`Zgzix(Yg|^dr?f086wWiwn+Vk`|h+)Hex8W^39n7(~5p_@Pgn8sNSG~jn8cFk*KM6b76ckddVX`;5Zd;^&dMdn{)MZOOlDWhwFePkPXK(};`LFJY%`5ng(U+U4Gq(UPMr+Q-B07h?MY%oCKExlE&}(8cSe?${T+}UfBuX9mN?8(Lfi4uF=-<zi^ejxY6k6N*SMvzjGXU!<$xTfST5u{iRG~alm`E|?#-6SaRbLq~x<0~!aU@|J`CuGL7)K5aQ^o3tMkd`k3U{-EvInxUoDfZG2;n^gHNrCrF)h~<ys9;{RdI=H0(j#Pz`lyYiN1;omjs8ll(@rVGk2<?J~1{oxRVW3HNv#X?ySFhdTo(Q@CmwYpqUMjn6r}ph=vWsE>Fhs;4|g(5#MwnwH;5$Hi~$ny>MWQUbP4FF7$G8n@zZ&?&@85<p$>5<HJafDv#tgdvQ_i3Y&4Y(P&1nG%d*NU{JbZvT)Tv`L_JKq`ybv`3RrI=G+V{iyGmS2%qeQGo}C-zLoQGQnYYNmJam~R}OWoVSZT34@<-!I?k&eX<aX0Jep;iK;V&QxA3v@0%nd2%PeADZ@C3@mfn+E!4j@*@?2xe8ZKlnU-pclZW%@%P#Q_|bP2x#I5mFG@Ic8qO8<zSS29<l2wR^O4zJtZ`I_MYhupC?74!Q>uu}lXLV*X8UBZRsL6ndqBEG&7FraF0XU|jSgC;DXkM>>(qI&BgDqk2!{=G(FND_gcR%j?q?rq`l^|$UGtpw_eTvwwz+S!=7dKFKeBC#1t8Q>ZC0p#q#MH{IL9$sCzb;Ij|y5Y4}H@tT1PST6_tdY8mGhCK>5j<OCO=2fzykJrng+k+on(@Vq;!xLBXIg4Z4T^|@!Sj)=5aY+R6~!exyXK9O>Vw8)@!jbRHV<9kx8!)@yEsCxz;6|XlQ|ZbU8z(hyyhxA5I<k{q<1YEkGpBuo%dyqa5fHJi5tQ8mY`w0T5IO5HYE$LvN1TuYfsWSoYVq7COXnnP{()|ouJ+3%+0?w^eZyFV>x7Un}x$T{@D4Hi#HhB!_W{sPiD~A3c*CcTt~7ptE?8N1QZI*QAM)>{l>J!{|No&ImjWFk0C!X3e=+%z@stMwG|F@L?1<mHf@Kma4O@@(6%IgE*myvQ4V@4%i+&u!Re~-EV+G)Zs9g+bj|J*m)fvO`61E(a)@FO-eKkts|=OXb|i;#m)3f3AN;x02bGvW4T5$~)gJb;;;FnGlU6I&S}XeA?d^n*5X2~(av--jVoO8-4cm;GUb>uGEw)O>VmT450JC0;em1oRn`#YJJo@@gp>PMEg`>A9zS7NtGF#Cul>fSbdPj7xYy_yuE1H+R2Eg3>LIB#I#1~}z%@J=@J6hs3e~(O+eYlvX$J2OX96+@D7m^b?yLvh}V;r`PhZ~AVpwDABHj3wb+kBG#!pSs#x8l(F!!TJ<kDeCCJSvZAv??T$6Z1$ktViv@%R>=%0R9=Xjq1)PqofKwqF*21*DfpI8EbawdV)rD7kGDXJCBIu;M|R=>Cf~cP>KW!tK<CKAqF<envgGo^8xQ(f6b$j%2yxw)el<8o^Uv%h7Vz^5ggWF5wl6cMKoE!y3Oem^~(XKSBbFv(`Xbfl6f5yAT?HjoU(VpFuj^MAafQV2dP^u<s+;|?Xv}lRujHeLSfo?)8jW8?(lz#a&|9KArBb8>K{I6A3j*Yj6k#yUJ(c36y^8FZRmp-%FCg)J}M0!nR(IRNu4G!(6F+gX(qsG45&uNaam=S`fx;<54S;tuI}I&a8r-KhhsEN$S;1iP(8?ex?A>XitcECRe3I~SU}#=A3VX0tipCEqZXMi-<7T1RXr`L)3xe+s89z(6p<mcThuwxXna|=L(F;G0ZtK(bavC~QY=ArH_DGj=?(4$LcG7-@Gy1{-~VD>(!sZ<Kz+zZR;*29HxeX2i{KQMMO7BdUZth7n8HF4eQH#zGC;aZjB4feuEr6S_YT;@<xIgR9L!T?!xUXlVXVU_nTH=F>38!Q#d`^+bJgc|cboPWcQtW)4bA$)H>XYD&uEexUq*eNs0!R^c$UDbAACksnA^I3;1PzIM^P5vL~qWrXoj}MX!}%KKp#dRSPpAWo~u-(Rxzu2MV><WgoVT2(}M-neKw2%51R0jV<c^-3|~)`#;f3ad4BEURf-6Ke;J|Y*KwST(?v9&M*;OW;0~kX*8rctr_UGe@!XR?P15;G+Amt<6+%YYXp3xqup)vA6u%0mQ@qtR#gN>e#~(9s(=?$P+XZu5z@BNUKMjYd@Yw8OijyJUvY?J0exBq%pWunOXBvT}b0e4|2CxO@%HZhFQNynA!mcppk|+G<iD~Z`;mp!W5J7H;CN*Owc{_Z;@!Os*Cm8is#7sMkFXFk1;3jO?qv4A%8L49<RK;cgBpUwu!Hx&2cU4gMgYDcIRf0m%v$Lb@GD>A+HlykJ3tRGbSy@}Sw#s(9&`($CGluTICnJ7|#;qNd2hs3_yXps564<yOjGIal93J-RU+v8iy*bj}oY0#S?adQ<^F+PD9`yN-{_X|8Q@(V90{ZfYe2>%9r+<~+=_LJ?uIT#OZi3gLa%hs6HsEz|kLseO7U5)1#sOwHsIFQCrd1B+2J<qUq#txJHxmsG(fo#t?uwu8^3XLP*C*+b4&Yj=pC@`WwlAXR@S3>DQ8TF5QFkKxj7jFGpV$_4yrDI=JV}4UPU{UWeGQs+VqKBT84<D+YZ)7&u{2a>R*#W5tXGY5zX&J8B+9H~?9@8O<~DOv^uj+KEV6leaXOu)qd3uI2Z`ji_;N}TN(TL(YCGQ)BaRHO%?(f(zr%aV@YCd}1iD1Awi(Rm7lyU|49CWPP~$Gt@~FyR8g90n*=ty^is?+9^=nw(%kZG06CKqB&X3qvP}~!`=+hYm%}`S-0Cn@R2+kyw0y9*Fn2_DWy#$S4T-ZGg_EiXiO)+f#?1N2TT-ci$0x<9^z#@FAdWcQ8+Lo%;6?n@x9(qA@0-H)ZiKnNdB%DR4rchAfZB0z#C%@ZX@9C>}5<dxt=TWKa9;VnmWb=X5j(R(tPVk_;Rozc73nyq`JBvrPTl?Q#N$<O^AsC#InsnPqQ_D_vSME+sIcV8;Zft!04$ekrfb27L9=d}6FoNs~S0l50siTpYF3quMTlf@7$D*F@ScFbR=p=EU0~A+xEb6XwEGqMCE$Hzd(1)luV8h2K8f}fjuka!|Lrph1{*?O-`BsN<T(G=<R=NJ@qPpevqq+R7;qP->XP>X|lY!la<x;;`?*vCEaE}2n?JJ*8&0t(!X<Q-P_@E%(_@Fr8_@FT2_~08l($J{+&$wYZm>i1s3e10X9G%bNA*>_MqQ=w_l>fZjBMo$SM_bd*itpTS7;w?&!4DT9Zr(?*n<7?k4i>**8jkJ`$Mo%(KzWTjV9_A@!F^$x-RYc-!fm4(8TcF*)E(?>Z+5q&8T5n5w#W`I<N5MAEc!~L>FgAb2EQ4RC&DDD47j&j40zK*6H$0E<X#uScJ6ba9J~pz=Cz9l&+Q%Atg&le&s`L5hdVp>g(dm!&I91Dnk6{}<t9t#0$wgCuwW11*UB?HX3y*xBb{u)U)>X1*fLXSbC7Js0U`!rdy6G{cu6OS%9ok~&S5j~URE>XY02h}>|zBMxHqpZOc$Brd>~zb&I2$2>pL6Ii1AfON)OuGASFpj$Rh|@8=5echwg!px5aL;n~rVn0UeftY<U6l>1;_0y<)fw!4nE%Pe6-XRpVVC#^sS$&9)o<!YMY+XX{C6R1Etz83vAaSZC2NK%<vM7Mw5QVMK&oqCUypg?Nft@d85|o?Z(@le!kvzAeQ!ZDW#<e`4z9bG1qNXV=nq3rna2zpUC=$C_W~29$n@_>5u(p6TnYX{RrG>r9_9fkq+E<W({UFzNT%Wtc1g;lbO37cbuiS*{KJV-Q`#VLO<Pml=5!B7?q1%rrQI<9ATsKYYLc;W)^~>DA;;W92zqZpSauBuP<#nYvLN$8cVR86Q&-gViSCGMc@xJkUUte!aLji)I!@QQ=d?JIH$$xVM!mA`{L<s!NaQyqP4Yb7=#Hj0X>?BD^Hd!zl?i*3~$ng&3IxCXoMFlei2`$kbqM>@5c;X|hB!+E=!EeSPQ{-@gzR=KoTC79a^F8R{?@ksG{IHk?uXW<&$xlwxvt_pH%q4V#cqNs7)2268tk8g$P*147ATI6|8x(Qb~y^lfzvS?=>Boo8f)7GXHiTz8LZ@~l2J`jAb<sf7|Dza5O@=`p>k6PWfjoQ(O`(v+^*-xu52HJguMv5+Umk#X&IGjXm_-r(IVl;&1p^@Kp8)OZuMcb22dGz%=-53x0N9FNNz3~mJ#ED$$cebTz3<c6o@a8}l}E}B3Ue(l(>Zj2K})B?Jz-{39{MM-;;lZRO|OQyz^>87zZ=xK-w)8S3S@}JHt2^!Pt0oq%Vpqc?a$yF{b4F5WtlM;1<x^Nf&Z8Y+$PR(KMcyWe-duGu9)*)<k#93lsek=nAC@2)~&R!8s5SCX^yTK(O7ogJgiWi7X65Rv@3!Af-6EUewopp!AuAOZV>R4r@s3?`uIu!C*l*z#LNL#v)M~W0Z+*bbai;I*T8Dt?1e_O4;8&XW6NNVv3DNP3nj`F84mYgyc)sIQ8dPj5YIv$4@vVJ4j+HMV_^H~(BfYltrnyB{)?zevw2Fk}tcvdK4I)n(#upGqx9B3(&E?@^|ljqi>V4hCDf?_rNTj*bh1A55w?@pWwQS1OC5e4W$ED4(XyOOa>q>LMrrdJUxjBB4_0*HaJ1jnHlU|<Q*eUoz|;7@DxveREpC*NZ9v_#h)JVjeDiC@equYs?aQXlb`bh}_Fd=rkNX-|sz4W=r?P$C&|7IN*{5cDujljS)GGw_woN+~4n7+H~U%-(<svkOr?10EF2VN29{7*Ea1^ChvXx7YT{l{0UYeUi@Il3I2*Yq+{j$1FiQK}}O3I?+@LkN27-C}j#2ZMRg}h7t18I0*XGQW!^&Q-5vh>Mqg~vQBWbXX&LJ)qZEMf+&G;dRlb!+k@XfvCb1i-^y1T4}<&W{fDKwLBq51Bc@(b9x&;OUDqP1w+@|FQXOo{XaJh+4eKMnwLJA7XLqtDb0uG)xJFHPIr-4p{Tg(BAAa`@hg!Og-V&b46qFv`zq)(+>b8`i?0?4I{Re!mkYXPCTOEiE%UT`fdPP&eU&L`XxA!Wpw(l*dyUWYk<8QOpWK-Yhu=0;C=Tzpso)j${av6o9)*zhHZjXN8y{DQsP!CPVS{g^?0rYC0xb(C&V)EFF&=`wRs){o952Ml9W~Wmt_SD)b)XQ$Ish2g6hcrf*3mnF3IlZ{}S}Iz0NcQC~ie<_iebVSEygVy>g^WdFx@2fRW5SB!=&d`6gRr+-GKpJ-lem40Nfbg22H)n$OBHUg(2>wvey#c2Zi}D`lvv^bq;5EkWc}cO{!8$DF-x1l+i(^QVdHtem<-b&sxB!pL$5GW(g7>7tu5=prcv~ogS+@B+A4PB3Osr_q$?`bVwjJD?(TZdw7xBBy*Nl1wRas7z>YRGZ26`i$5dFR(v+J)R4_yj-3j=z78hkJrpQ+`*;u`yt`Sz3Ro4V~tU<pRea>tHw0sn~k!*fDC|>2N)?D_-(~gEBSrlDKle6TsH!O%1lOsg;CY9Aqf>3Yyv}O2m!-67}n7Sgt5UsePko}PcBg31>I_<`t_BQaeEM;{^i@uE6bQBS~49JW`4<tHy6%TdIbiSW=+Fd%vZJP`58hayR7gm&jp^1hI!?QXK8NjKvq}UeJT}w8=qI(sk#dU<&(wqwt4^7oEPXY!pP;Z%1`K1~S+XRaoe``zmTjz7Np>Uqlpu#7`>vHMZAI?HtFeswdZn3&}+m*x5Dw6l}T*D$sdjeD{RkplFO+CxZBUX9UEGqs)fu7|n*hD<3%WLUwCl7@tI=3O)#tWwVKDJTdgf6ZgznW?6h-BO37>DVs6eB=~abgenLh1+&KL{@Ou*e3zP(vZBs#FP{Q^R<OJGUtKG5%!A%VYO&1Qpu0{$cDKim((tSS4eOZ-ZMBACpY)qrd$v;McnAkr`W}V3!SNgZdbbP~&A&H1QZPj;YqR+Ph>gVFcIpS)_6$CEQa6aF2kXo5=b^hTU?R6aQB$-q%Yb4;U`s-_>5#XPG*S!Xfg4)lgx<3|pdj&GH&WPr?H%kQI53%GQWXazofBXqy#J&JRceAuX$YGfOEZbbn_A(&h_>W#8~}o^i<1sq};RV)Swx&rbmRyugfp(kb2QY9+hbH5W5`;GIR3ld09UUq0nzP2EkoJKkdXmo0I{4YZYBvextB=8{+U^k!ly)OF)xMZ^2C9yN{<FkucAF+?+Dl{WC<p7kDAa8c$>MITtun(o^KG+62I%aJa1D?*?1kI!R&I;Yc?S|fEkrf5vAm<D~;ryR#ekAOpZC@3o8Z{yFO?EJNcrx8;KZk_qLptR&8kSw&>!4xm=;PiMr38&c@=2!=z&2SlH6i{K`B`>CKK^^oC1_}$4_$GQwZ;D#-`?U%mLD#c2_oyOkonsI&A}7afhWFx&BzlozOqMWN-b8j(l=Zx)3j;g+7xnxX_1rcr3QnIH=H!;-vfjo<nWIW*OY0q$ee^Ie5|oo*heYr*)L+buc#!sNKz)0H<4kR)PC%G7!?UaiAP`u{RDoVW$bUHrp3kBP6A}w=ezYxZ2DIR@V|c?oj)e6Cdbb8J#aR$i%mX%oMU%igPVA;aRzLyeFv8cPhx*wFBZ*a9j6WIbv+|i(!-L(rm>4AC#T1T~A>WQm|J^!KN0S4*!#R*t91nKgz%DKb^fx9FgX){)S4{sHKE)24DcNt9G7{n=T1BYBDa=0JpjF=|>r<A_=9-so*bL4zKje_2%LHfeXHSbgQOe5<HpO3vY%>^bW`)zGw9pZfPqM@$0GOY7NHk=G97WORPq_n!O2raSo}vxqg9i@^^6qsx?_M?TUzm$8H`K%^r6s^Ve*VM=(=OGNWO#!%2iRl8uk8BpW>1ao^PV?Voy|U|_;+R?#!g^_x&HF)VnBTlK0bpYLcpg5W~j9Cs03TY*RSo%(VIzL-CW|ja3Riy?pcI=aq0}^Zb3-6hNg>gP8tkAD4+p~zp&^4xtEfMCA;YS7Sv#9*oh7J^{@W}uSoFCP`tUgsCmPCn*{cgxv`1u@ntpHOKgx>`i`v#F&363g<uVR!IW-bUsi2pYq9wXo0KOK*eX8k>^Wg3hB`HQj)6F9sXw%Y4C2@rAs2Xzmet7k)cs^`HAqErgXwn4b{OHx?eB-^zuOz}LG-EX_DL1+_iU@Ta_cMXn2_*o`t|lztkA=hr{JSm31)&uutA&nwwosP=0)tSxFIUG+=@<Nfg{C|pfj5FJ+#nd2GnS*08@a;&T32+#cPADm`)UQGbR)-r0We9(;*Ofh8bjr=mC>pHnjDKwmk5TF_N6~HG}&*IFz1Fvvj9dkz%`Lop3@0751Xbi>9m_Uf_B}4ih@faZ~siu@_dSy}Mm?T)mQUInh3f$F;*8VW;x2+(07*!`h(%b!F&=io@D08I}`(sc=-gy;Y+s?ZlRkXHc*bXp%&WmbjTI?O!1d_1GuoAn0u~pjaubE=9@fZEHp$`mUEPCxc^Nj&CN((ihp*FTGhY5Mhg(;^@l)A$pjuwZ6-A4Sw0wN|e2JOhq2S1#II5$GorBW2_OhQAgssksF=5-z#q4gLd%lC7DCc(j*I>#B>+Y4BpNnI1^;S&tZ~8Gc=xj5-0Fw5hlSqX8hlwL(+#0DflQFp(OSD7c)8^&mWa|9}hu>%VSmfZVHYMUp{?ybb9>u*}-wyZ6W4*gIaoV_s%fQj9a3=E&wyfK%5wmvi{>oz)INS&OfaEh@Nl&6c+d#<C6YZ`}Cu!NJnrDx)zNmcqB7D0HXoPkq7~ZWQxLfyBj<X@anIwzwU|)aoZv=p2YKC!h{9gCri3o)LBk5?_PfN#y+)y`DEE^POMxT%x6h!rhJA)5xOCMaq{Xgc&L`ok3S9L%YZ6B<Z3{~wMT#mjp_aPQ#K7JMyUj2nAZZv9(0Lc_%QhBr+Zl20cp2;878f(S?Dy5W#h?oF*iz278kVu10X%DO~~iDhG%fCeR!hgF<6`aI=trBI1$==niu+jF5nS=5#H2dQu4za&U1rH-}Cg=LDm8Q6yo6?Ai{X*ePv)E1)d{lRw98DrF;h*NQ#uBwMd@YeMXn|NMhFNqF#U0d#J4^k)LL9QK`C^Wv4#TT@i%ZM~gr|)r{pVDmNq)>j=&$rf~hVdab5$S_@ll=QD3K$(0(SvbVu^@QJwv7RuLo&SF2RC5A_b-)Z{#^lwwnNMHVFGK%~BrzwZpmp_`KEB#fYXcB+xGne~fsL(}IMle8rwZ^4^eZN|)_pPQS`=To+i@QTaR?-pNn=S#kU<MKpEfGg6n6o}IE*5@dr)X-Ik)iRWJmp@(E&xI@Lf$k+wu<jJgUdpxzWS9?o*rs;@k_<+#vCe<Q-i6Bv5_N*pj!M=ug|B@r_l^V%^}%VW#;@AD=e*f6*4_=scd|NQ)5WJ=1gjLnFi(97gCi)-4$}{3dwba>>A`zF)OSl5?(blG^*4cjEN`vD;hdQG1)mbdD_cB7EFSSg)`!S7{e%<9waHCr;t#s1*j3+f7a!9t2JlvX@iTQ2+iT07>1#)vM<AV=DuPzufGhOWM#Gm8lIp{tuWbV*#U9a2zAXvf~^(<JLw#SNnjFTN;ua_Y^3&Z+NEiOHjWQa#O5~es;$JbhXS;DKQU_iHrV{Ns46FsJ7=q`2a8$x$-*Ktig?I%Q1`E*<eSS`?}bH7N)^f-Qo)HBXv3H5?u#{ShwZ4Br9=K=m{sX>S+A*!o0?K7acp-{+bnIXH)}pUlvTx6MpmffDEcbYv9(m*D&pQ3K6sNLF_St;*{Mpbhug23YFxb_qTNF$AevReov$AZ>VA6d&%{~eTQZD+V?QqZgxdXnV1)F=MwZ{Uk*?DS3=pPc5hllYjMVNIXoyYjL^Jq%q?;1)pGMIMrHrvVw3+K=MHT?G^B^s!GT}8x^T>kca8RL#w%WXBB4zJ~Y8Me&6vaHoLB|*J9al_qWkvz&oyNCT-a&j_2R!)?N_*hDE%5b#)#(*_-~wFH1CL_=t2*Gx)L^&oT=yC}`A4R1yG(g6Hm4F`vT<MjKYiocpUuK093ALynR!V=@0(8#y4udgv7#<D<@p$k%SJI+LvK|rDZ*;#YK|11dU}4{!d>6G#H_Tqoz22!guZK|Y75r|?y}L9&<hu(1Kktae<k#y1?K>_3;JM-1K;`wn({LO3g_~w;`uDSI7R?<C7%?W44e#&0$A};0RwNIq+vF%qZ`#6f1Lu9c{Dr~fiMksDv)I&^r#XNq!}?2KcfFn?X9fYXa;%r+|!3~e`jXlfcZc?zB$88!R^n{5^$)F2qoT9RI%*#!+YGoRcPIST&|G$v5LV@FX{BG3H<qWhiS-ly+5C$eU&`Ipb#XI5}2nNJd8^<{bTc6UoxZ1M&Y5S${|DarkR6lH~__QB0oe}N9fC(XJHxb2<<;}9!K>1U@?~jZcToi{g#W1X4C;gZk|s*lzB42_ZC!dq4{oWS!-Bzf2&;g#;hApre#&(bBki7Apo;xa+Z|UgwJkGic}0EZP0l6!U`2ffb;Y71lA;9J;R#319&ql{YI63E30JIfxc_E-jgZag*>DQc^uTXDKJ$YGlL4yfwI=^n6E8*V*qx{hrXO+95avuyfeJu>8{}{G4J8A!`jZBOENj!M-R<76r>J2vu_QObU++>NRhg0Z$_h9d3yS_LyZ^3xG?o}PRHzO8$s>A1$E7;5sn(Q3g%2jkTrC(p%P4u4;gg(>eRsA)K==2yvi+;!>7rTK9sEpEYv!~Qu=aGRc+oram*2QRc7$FK-uLf5Eh0esNe*A%xB#A=^&mBFcbkGL%kztr=yFxxixD0q83?4PvAg{4lulO++4B+eRD@|Ldj8p8{r_&{j1Uo*f_xfFJ^i4Ey{`0p2cTp(Xbs&(5)FauZ<0}z*Tq|WhLL!S$rN|#3dyLAP6qtSl}&Uj>?)9#5@-`g%72eA9yhjweXT3C5n$V9x7C+(U|au=sf<Ey{vsI7BVEbGC2bc?`1j1ykZc}hAYi0aQ3kv-zb0f8CKxu20`=ic!6dZ)RQz#qR<j<B^`YH{7KD-4|j1U0zEmVzE<3I4i$chiNLI_Rsks8Z)vY(D9&cB;=QkiAmYB85Yp=keMqlG^R09`&m0I9`T!8Pc>{vjjkyPn93kcVvM6qVkYTgb&lU233qvBJk>jMDp>I3porMLpr0rfH3-<g`5?#}_KS?KYUIif48Tqpm5Y<OO1knn_LR3VY4sD5B<Z6Wh+B4*7<9LdZL(%3I&Q&)zNfb<BW1&M?FjnzHRRWlm+!YHktvJk8)z6o+dSx*sIXJc7@~%O#{|WA?q-Bj&U45xp+5lfx08IywD*^g8cuDA`;GI+it{%o%?O6VRFkZx-_LD?fh!7%qnv{u%k6$XFWeoF*?^(p5LRCSJbeKRqrNn0oI0M)0rfa!CWz?#&H1O=@_i1u-IJBsX4Kh#bZ2OQ$WcebV%vVw$m24sL8iI|iZ{vo-Q<!o5F*2+_Z-q`tB5TD~&$j<bQ<`EYm6u1Rbun>|J7hZ!iBMACBv{p2;i`<h7NjOE*Y|7$Y%X1_wQTuHIEYZ=R}<$ET<F^=PBjZIs?P-y3{6eLTP&gVO}O{62(4&5#G(RQE7p8ArEo#32v_Wl6imk<T@8jqyyLISxMEv-!X97(L@RqQK;A91WnhEKrh05OlOsDhPsTn!G{L)G#gikls@2o003BjqF<WzQTUYGbmBVYjG9};Wb((gn771&2yWs<-&47mr#h_^Nis|s;f;JGq%1Sa_i84Q3!XOX`{LzWhSMmxFfkg#w3(ADoT!v8SgiZ8BD*YvnuBPd19=x24QcQ|4F#=)nNceSy#UP{zEM2n_$K-Hc4$z5zB`gNhiU*j1v<McS&#S{iIxtsh4k=%z`diPgc^PLhoDN)}G<Ts$j>8d(T;78Qd_E16t8kf}rqgI5<Q9!?OIyDRXA`Yy+(qt)2F>d%3*ilC3LIq!_Zno=|L_0$-~O3o(|`Lv|L<B6&=bn`sa=a%-wMIw^5gjs65%Oc)GC#N`H6z`4_yU|q-aIHzqXFTWfMbz#<0T>vw)2T5fr?L!a4d2(=23qjKEpAd@`S`I!0YiTUgR0LVR-=otM?cBCRAkk0wL2?f~#qso4RK#yWeAFRIlZ^SJHGD|#(zc{`p(3E;JKy+yzT1nTvbCQ#jwI4_e%%~gXHkW)1*XfTY1oQ2X=x*8nMM?=g@`7u-wSjNUKbsY@NOM|DURN6Lsk_&<oajZbFrjJ{oQPZE&G2gxkp5lg>YNfcg-~p4MC82cI60SJN7Ts%DS!55$qq>MudVH=eH3&wM5SM1F)&oKi-VRyK2Zv*uRDnVv;Y=9R<0t8Lsq$9&(zc}Vowd%=Yl}A^@KvHG2c@%RP7@&w3qdQ+e>@c~G(t<mK+=i@Vgr)6X(%jt6eEHXJc<#`ijWc0$Z_PTAQTwfN$8A0Wlu-5DBoeU_ZmUy38!b16?2K2t>G+;C*gVI(T)Lt*Xg{JnpABPnI=$LpGxjQL-fSKm$6JFB&oG5Q&WkKHDnJ9bT|Tm*sD_sUa4;c7R`^jmeDZ!T2#Ozlp26+=3)^(ya#Egbi3iYLdqlA$V^B%J*E;Bc1s53uYMRVSA>Z)fV2`SZ?IKDMMI#ZU_#@`AXy9}(dCk96qsp96glwfK7bhaOiHW>{VYibpMBuvup0^iWlP@ERKtbED9i;$^L<r>#1lO2w|sbUK>F_bGGjW)pa2d;AYclLznq@(+?|T|lG^hRc-vJgz0mjAsTfy%XczJ<S#@WQ7Y8jYs*@2{Z3qz7?kv?i@J-)_O{Z`}nwuYtKO2VW@vw<*d$!6VD(h`LG!7mS)Q*z&U>prTM?-CIzf=b$;gZ7bqqoOry4+D0QQmtQ`%2CaLtbI|L710zehB&9mmh|GvFC@PuFZ<TIJbW;94G=f8J<V0flx8JeDc77qgM-0n(`{h*0`6QM|C*iVxG1rl$bLt{B#PmGK$ZkW2aom*A-^e*+rVp#|5f?{^-L8Mn-61j39Im@^=A?oXR2|7;?k1YulTsr>bB^a-%3?e8!M@OMp3Z#>=er0u#c~J>jXC*oNVA;BkpDdCo=nIbx@M3^IOvd0yv>0JgQW%nUrnct+{Hzkh1rIVbDwiVQP&Swg`C-%{hXTK*d29-D8K5gF#!xUVAX`x6aeLn|_IQ4uGtnQk9;)GW(#X6IpgGeYya`i!m5k1%CXx7Y5t>6hx8o0QuKx^g$zM6(!=c2%KeLq!`$Yn9rofOf;+FsL;sP0}`{<Hgo>Fck0$4QH0c8Ds^Hs$^;W$HtYU6+jgsM&YGZ5ii2)<;S10%kzLPkRH}HJGFon^6-177F@>B707cBYaN(~P5A$g9(dr#pU8_)SS;j|m-j9BG5D=UX^$Vu<cHk{-DY=ZyV+^?dX1V0*#5Bghfe2g6mH8GEzzNFd#iTOX!0I(7ai<fE`cd<GiDSAz*o-G*|HwbqYL!hOenmHlFx7>S1(ymqD&1EDY=id)M(8$>o$Pd9*7pm0JetMK1{C=TyBQzX#|e^v%D24IS|0pID3~FqNP<ABuBQgmDQmOk~?R0{#>J*5A(x$I2%S2-<LrM7@P7Jqc6g)83pS6QSBi`@2$PXGlcUfWeq{mAh3Y1r&4I~d<tiSv3GE@Wj3!oHq&zK5r$?e97Q@i4=4H<?sx}*nrmNI4WBbfXeKRlI#m&<=4TLoED8G@UX@GOyys;tENLVQ;Hsv3CBM@npV0oJ(|>w#hE~pKP*q|m#oIp;x#)Y50RThe5Us-I8_r+x`K12)m!=EmWBjQZ{2quU(kHA1UmB}&?+HM-Vb9~qH|UZH$?g@IzU$p8?3Ze-#6AM46T@YRqMA(^&0`t6leePy={eDEqc9qeZJIWiMNnDLQoS~eFZ0WZ-0)0>(BU@7Y>hS`T2h!^=%GBcg~DkP%e^Gsjj;Wr9lh4Dx-*aGoZCZViBO3FONRq`ppvK4x%DEN2$uvl6@f-fTUV#315DN3v%(f-gQAY%w^=;JwW~wbUklhpJz57sjxwB&mGO$i9L>jzi!<82Jp#4P8KIHizfj;FUx*zSFmUv+Ru;HOl%uo$BNwK>bhbG26_$On$Y#RfaR?!Ha2CCJ`zG^jWi{-FasHohK#vP2EDh0+ahrICCGlUYB+jZ48O9I*oVcsQ$i7aq7AeP#*Uj0vig&HTr`FkgQgaGhfp!1q|KTYjR;Oh?{uHn_k38*rB44;^6fRB6{phldA>!W7(rI{(K5~<~6QSWw1{>r_ivCUY-^rP#FUNN}<jypMc-RjlKl;)z8wuP!MyZ+f?TdGQEmZhIixa*;$msPiS}}u#^Cs`?<9dNFp6Cr?Rfp3l)IAu(QM1m-bVH7C!3rq8eclF(d*?%~nyW!$ELPM6qNRqb+Ot;@=QBms42zcms}=Cjj;9lZB`inBVHPMERbCd<&(b+cYhe-y0a_Hl)9^Tz6iKum-%(R{>x5O(d;jcuifO`RmxLCC<}V9SuLGMo_ApsmD<4Y!DO%pfjNOnt<}7*4*_0h2D#2s!5B@$E=ImJZ<NT8wl4U+v)1H0q7_=)w7&u7}l&$()GggN-H8nlZeZ3YDVs-loGf;NP>MM1){K|Nm`3@~4Ykf774gX%L9}W3ahG%gS&zCP2w(viTrixc#G_s=z4MdF7>V-f2f_VuT(}MNJdcq08X5f$MrwuPLB11IEptoca*&tU%>n+GQg9{4XU}>@5T#hTWsk|e}-%P1Hfwi9-UXrqHrw}zy&GAdU7gwa-_<6l<MA<w>6M*3<S3mW4#8ZsABHGlu0TYs~*9WKpLjf^$kS->3Z~ImeY8xBU8y>~;><OLZ;G=wimg>HafGl_idjfwEJ{CU(E=0SYz9w?e9Cjp!E}qwEfE7?i8<xd7Sw5B@fX9m=8;y$`kp>~6ne2-+iB^N4qAgBOyJxMQ)wQvdSuedDudb%90F0_v=kp3fCfu17fdW=nL^82#KH?-<T@NR9k+ra})!lG5sWL^g3DALUvVzwEt4uPXP%BKL+1zW8dB(zNH2~6X@|(CpNxu?7q>kUiF?oZ_Fi#g`X8!5|S3s}5)zFf{Dq95%jBA@9k8Cg^=_$h5Z1;Q`W35w`uupwLCGkB{6OZJhN}iEB=xS>xADQ;jIYw|gj=Z0yML%};{(ZB*cHRyhI^UxY(j=WxMpDyEboH&D=5A2C3}^M0Bw!@OMon`t5T7ZEY&gIyDlN+2(Wn{f9kMzhX3!8!!NP#%W+4J5(E#Ci1%K?1-Lj7=c{#R8j3l1{dbC>R{nkS4zy3c8uUyB(sMw<)1>4&WiUzZI-axfYU6tC}E<j|CK=C^L+^9L;-o(-x%-L+h`Ck<ZTz?g@pEj6O&b5U{ysp74&oPUSGvO<amr8YdCLe9>ex*Yo$!bJs`>~i~*EgfgX?NuIiMyD#*}<cR$F>o;3R6Fm&CeYH26sjcpY4vWu@+JQZjFM`oQKm>=+Wnf9zTj%bxsZZY##qDX3ZByq7N{KIJq>pqJxhEHpRw?Oh0QrR|2+UnZ|I)_kdbCC5R0Jr1q6<nS}L;c&D|at*(4C089wBZZlQ3UMiRm*>eS`)U*_>cyuj}mGnq-z~gcOUrwXzK@`z}L_6eY4h(14noEW2fF=A`5Yly{Q3PXI6~?j{#!VF%C|BP!8h+z+-sW(R*L^4P*||v2<BJp=Dx@5+GTM_~xH!C%*lH>2N?u;mq3e>|WmWyRejhT_!d+ao>ACnOP$<RXOLs|P-&&|8q4kJxj61AYUg?=1&d7AjeLoiBAL-fUlCIU9ZWM&Zc+ZHcUl|p|tQsn*__8=eRoST)&f~y8-o3P=L(FnHi;EeO=uBWt;CrgY9{L%TUhyE<d>W`QL?*vIh-U+%E-sC198Uc+#$p}DfgpW~E%dY4#ZZ5cqC_3U9BaoG?NEaBUa#Zd)~8~PQK9XQl6>T<1>SiJkhJt~*RDR=NqS?r=uR~UJK<kvmwy_c$Ma0j8z_L>g>5!y>0Qu1z?y$VnWUtsYe9u38S7j}?bWKm21iLTuPj#|Uj(Ij&MvDh81=fw)k2<gBU=LkmA6i9ute8@U>sp`Q%X{;ac6Q4DXc3^Ccuj<_tK&|wovx3|AUk3iG?6i?%^vnPkTRD8HacvdF%Y_ZCwXgp^ahzNM4-G!#H^x&WI*IuGfZf-3qinouvbG14iUEbkKZdoU<3BV8enkijxp$a5WgSq=MtrP+Yin_(DHwO&teY;a{selk&m=DfsZcT~~K2S6<~#Re54^#6xjYq<8l(X*{Xdg1@m5S1tIrfBxU8QSzE*T0TX!?CCt7Iu^*7VI!tp3N^Ly;A9p~vV`u3q~DF&Z(yfNmM3FaD*Kb+VTh@H&T}JWwVvb;v8XUps2z4-jzE-MBRz?ZRfLl0mYhj$vnkVZaNk}5mH=6Y`>%g~xBv6A(^t<<_Mh&b>;n-1tCZuS%M|VYiS3Z2CL(VlzlW+i)ELb@jm|ta9@|iYy`4~;Nai!cmqRvkmJXNs5;R`>aEm$=g&NJY*YH)xUhu_2X(Tl$)yk-t-m|=NLjz=4l_yF+JQpM-C`|R&_Uj@tsNkZ=#G~~`R%|E`UL$_`$YRJaoP9>y{o23%%m2$BtN-%PHN$$=lB$f3PSRmiDX>S}-JO(1^dLy9!XHtgg7_WSf_abrxsg|J4pX1K;WqvqgG9>Uh$<J38Et)aW*iyL(HjgGKgyIh`S0SiH!3!yNPVNBswB-o;eA-at&`v(MOkTQ5s(vJKOt0~-L`dumd%yo|1z@d*`ib$RzF`P$?<$KjMJalSa4|t<CLlq8=x9Xl7_=qQ8qqFe}4O}4xo)udNETt#!}3zL;%;u+x919p<&0wTdd+BASkD%RJhX9YZm2ID3eknSfJk#Up*@u2ebf~hl9^DD=(Q^=e1@)hi)x|?XP7y3BmfOUt-u#7TL0X2LH(6OKZAp$>nJBv!&&=T8VXq1fZ08At?Xq$1li#w2|ihP@)H2p<|@nllX$JBql(kd&YqCsJgIZ(M$B%Y?jW<*)DZ5;!wQSO$M2|M3%8;<mffwNqzE!g~Og`ZsM|U4No1qRF|qSedAK2Zv+E?GQ;2LVy=G>d#H{lpaWUZXN+PrJ&Q1Fy3_iXX0W-_>39|wDJ{gxOroO@DEb1V!+I7)Ll9$SGdOv4(JJ1fDEkztZ<1cs@#OjFk(pUwhNc?+^hgAU&am;tBB^J=e+RGxp}XB^!f|_RXSdhe?mj^IcC)v$v$gx+LHEAVh_d_@HR14mFWBlm*m|&YzxO~Xi@z9Mni(BR(q=G@H9;^*(fl6zT}PjS`Z$K8b^>hAgfd-~a$@T7NH^0tO^xfXpq7oJ1eT5Tj+KS{cQ1yG%+wQRD$gD^t9RSGlo-|%M}FECac2rE_qg(wx3ZH<gY^;ECI%Mj!BplAm8MI8Dmy()Fy7N@lqWctdNU@>>YerjXuI3q+O<Jhxrg&X!by%&DMJ-KI8=__(mV%Kf93=P%c+bXIIv23vd!t7JKmm@=R27C6DSZ$5V<hQ9F#vB0Tyls_uJdv`8F;4AIf!tQQdmGAX<L}#P2}$X0VHM3IFvzeWVW3jcQ%3tDT0Hg=E@3PtvmxDENwcPccVK+Guq#A{6|CD|{OvY+DMd!Dm^?YHCaMzQ8*a84=ef7b&!!(1x|`RyRCDjoRG`wJo1eqkhjVZu@>3<u?n*ChS`5RSA=`qtSp}YZy&gM`5xLsI}SN@lu3^lmY;|2w=Ag06ZweXitG4qRi?4CQ?+R1WC9tS#&VN`_2dOzfNA!<Ns-JRIwL0&X1n06X*{h%!TLlNlJpRC7V{uQdG&0vdEi4O7y=6?!M!AQ;0Rgn!FMh6zPoV7x<=9YxYr0wJc7jP%+b+n8(2QzBInWY<@DXvP;r^7$&j&g_3>4#LT^^p1fPIwr_riED~#`ixAWU+r9`CQ<C%{M6KOT^z0f<6p!c8MV<AYI;EjNInlC|$(x<aFiW*)r}sYo_kX(jr&c@ov~lme$@ez1_@b_r_@|6Nomx&-+=7DnJ(G@iJMDn%v4i*Vj7<4Z@ScB%#`3h`@nrb!WkGHQI$N3X528yrp^PTqAO?bCdoDrm8L8#ci5>9)4VK*$m|75CpH;Y^kElJToL54PC$I3B6v#0jr2&vd=+iH9!Zov8?2mExgWV}Hnin|<>98-<ZO5?CDB~)~J;s%Ffl|)AJubTKG;bP7Z)6Ee-~9$qGjaATeO*hBH_*kIVy52oFj{#WA(mGoHQ0!Do2<_oDmX^*yfsf-GFy#4cLk~X8hP~T-=bNH!FVs?ETfwOX?!o7(gFdNIB9S-2C4>LC-?|1=Xr{{+hCe3&f`e{N6$N^qTO}JpaU(bj!Lt>8k+RH4smeS1*?;>p?h?wl91S>NiD!6o#@%F_zHLjoXqZ!Z?a5fQ_~EOxqve)?vWga)}?~-_1Xx=mKA!XR2+vlnk}9|kATM(J0#TLM2Z^47L{eg3FCS~i#(*D<v399s-vN}ipoVC3G!VRA>Cf55F^^m9z_{!yl>93XoeK*nPJsOGpEE=n7xRH!)StQ#m?p|E<nPwqm;9-TJ30h9vI&&jxv2v1RhzR!VbG9yvJ)sx?|ik%8or{a}&Fc=}#ou!;y)fQcIb?`Pli?9<bu<h;D^+n<4C(zg(N{L3NXuadFwPVRNSYqmacE2I}Zx_s8_h>Vk!P%cm&6Q#T5h!*H^3mynjW)-<ag^^WGfo$_4gOU0x?$)`zot#N1Ix*(}upztax$daV8c1s>bRMIRe)qJb=Y#9N{K3ee>NKojcjfX5!*L4l=YM+0h-Zld6)4xrQ`j_>K4oa5q;d=ge%CD|W+xhLhnmk*+8uhSNb%$p6=@k=H4G$~43;&nn)2Gj#@4q`dIeoi-wEybZs%ZP@8Ee4``RV;C0@R`((JZDyQunWwktxf9+OlSS(o-+x49m{=L^jFlWBC-8OkhDaz|sSrF?sqmx?e=MCG>=~5NckOu|>73dMiP_47EC0go%X2n>a0Fog2z~TViG8nYyvT)hE&QTvk5f?-n(|+6GZhmVv6j$HTq?)x;k5^Wl9_DU1A8C53#0*hURqlBFp{&4%4XMS4HCfM|+doa!Ay{!!HPoEn`~C{0&NS7Gk)Oe79nIAP-h1KEaILWz+=LdK_Pra-SMA?}MNoj*+npE+v#NqD9QvIeI2WaWJz8o7LKK~ZvVFS!pC(EJ)A@e%bs>$+B}z9RZ^Fdl0N_{vgfjqFfsrX*t-)T}h5k>iGr!M_cU1Mp`a{AbVLKij6$vge;mGpgjJhz9cEdOdLq@7D{i(LJIqkOx~X1X&2@v_FcNPMj{tBz)>?3yaB&F_nacv#>k^Kn|}3MeR@$6|zL?5X@*4<mM21LO<a389Fw=M{PDx+zjIh#zmS&M%)LpoSZc()g)k+6F$MmP)K?rNIR*ctBgU)eHASNO}mm;qm$m_cD>j@+-6l2SaEi-{*-+c(!a&5o2n`74kJ_G?y>f}zY331iRH(xPa`(b40dH4lviOqSv&NqjBJ9H8v=-$e!Z1d!8Z_HnC=6r^y%Mq#bY-F2dV1~(j1}<BFe+3sMN|Y^P5^Btp_@96JdUezC;uEiwyME7t!1FZ!5;;4ewDBmEeob4$S2&O(e`k@7L3**>J@6FQ$#4h;6ny1=t_ND&PuPAY!AmkO7zNwps)J9ak%Gn_brpc7>w63DdI$!?cPm7z6*6@0q?KIQypFWcl7{mZbgD?C-kKEZnU!zk*|V>i8<255@-5H4+9?(SWbYU0_%#-R6L|(){FW4o6kbKvoun3W)i4!iyoG|6R}`hy}Ip4syI#%9?1e^4OfDX@YxhT_v#D;M_I=2zcQv8lr>7!T!_W;zB07!8oEal7~!o(@;G#GP10^SP}ssP<?0IBk3F51s`iTCyv8uG=+hwp37;$(Hf{o7M0WrPG;wFO-10OJ_#<&UR|*IS7k%VdFJJD3N!Y~Q&TdY606w)(cPgNnO~^VSyUUPmE>j5S#xgsmlDj|=v*-e-*osY&rv0*78Vz~7+R@#R;i}$K*hap+HXlQ>&~3#&S1j9ILfm0pd)1wW#UF1p>8V~o@R0KnOw(JO<RGa$a$h{W4{$juHsomtqPVL%~(>uW4*G@AQduiP`l=V5#+<wc`H<tt9Jw6a8)q)3In#at#>@Hzjnte?xRdfQmLzEo{S2~GisC;gHm$vyNXn`&M>C&q+0Ls*7|r#=e#@SoAv36TD=8b$rc+fTUMV|tSS%-SYItPJDCx1`{GGO4*)1yYW^=k75M+~$J?v>KF4G(uEFshHZE$G=7sAak;QoS4}M1wfQ$Ar#EZxl+TrfWcT<$!aYXISojs49UppqKE5f{i(JZCN;C2&q7xwmLa2Mcid)n&UqOEy4UAv`jduwa`me>e<?Z#TrTJIJ(j2VL^_1sg~(*<loB28Ryu)rLo=(RORBK-xVWr|8EtOA1%AmzSDXYmax_uzFBP6E0i3Vv&t+Oox*lWHxipH9>r)kC_avd<(X7g-t%{W6Qpj+NMzUuFG-S6Lom%eV;J?)b$lnNcsCqUTnl5{oTSEmzyq6*_NjiO!qV=)CcuGshXnByy3aUl6)zd_<`+$RPOTWL^gdLCY=H1Z3mIelytJMv-af9|iTOhopYu1R&<&1^w_I+e%PhhBbv9^RS0@{(zNj`m6EfQdE?Vx8TTTl6_%sI`n_NFW>O^f%H8NlhIdD_iDn_-aN$h4U~xl+1Hl(cSo<EOHp6Uo_u5ErlV0cvF$e20RIlF6E?0B5utd0Fi2-Z46zXWF?hz|msyo)<Qe8Lyf30~SV>^Rz`){?j%${RZyIpF2&WbJ3NbFi#5)!!-_5Pv_nKqfYiCrb5F8m>ccLS6=HA(`q2*mLJv*J~$6f<Tv=4^~^`*jtcC`?K6MDBofp$9!raYoEH2F#M3zA-`iY1D?dfy$ZWEE&PYGb-E$aLw-``Xyin*V1$cb+tYG9-ATxU32l&Ob^@YO%ysvYq16TKc~{^tjF(?fiZ#sOlC<@v<a=RS4@FDaG;R%Cqrpt=%d)iutS=JBBr*Cqw2p89td~U>0Z8_<`)wI>6Bf@53aKr}<`Zd~z7P!NiQOFoJ7v9FC&-5_XcGDI*n{(;J(KL@7z*A{+0z_b+APdB4F;jOG69#QwdlK4?9fBLt~rmtTn>(}nxn<H+YC{(aGu#|dXjtg1+&aN&HBTq=>6ko`i5S?2a~$rXp-qoc#~Bn{_v7qUl8(T0Ne|GhT3itnO3MO#1d+-fhcG{IIKpSM4b?eCV5!Lm^I=Z*dLyHsH)gq8bK=?W>0OH<|W;^w<u$0N_14tMpSoF3Tea@XmDkxlm&Z9Ca^zy0L<UAF%ol8KcH_}dT7&XDuf6#b0`?Iba-L{j$6)pr_-OaFTA<nO?IiV`q?6%|@C;6*rF1|p2p9|QLE4n*Lmpf0uFJHZnY&r#hyPX}qz(6(xh;q>I&MSRKu`giC2`|Wq;kW@7$B+pJ93fDmM1R4tMR1Iw@Pk~EJG49~3W+j^P#nD2elk$XUMhY@vpJ}zzG|H?nV>AnkwQ|bD)mMb%%NDNZI&(9y`9^2&>!yXHm3QvVY!Dvv-h+vdf-@$uNs0lwClmG?se>Rf8HPA4Jegq5utpn&A_tLQe4ch{rXr&3)6I)f4XqLE_ps5|d@;yJ7lKS&D3600{l)2-Cp9<9_(<6Kdcr6;=D_5^-KOjv7xTUELqwwUcwJ>t5c=zd^FFrycOosTedrRK{1VRoBhej+jiWRfdf0<&hfSq<o-$d>Fh4H7t^An+8U=rfmS-s{$d1PVWU!dS>>bQ!$;NNNJ^t}Q{x}}Tqxr^ft32R8N6TS)H7PgAn};YHsqM&6&%w9XMB<N~AQ19Xd!D|VPE`!|zLj@?pd&V4zJB}egch)Rb@J@jll`M-`_9=HD?&>H7%CtI>qKo#cKRpOno|E@WWM0>=A8+fGXX}PMx$_%%<I-(5VbSJBSF<%U-e={6`BLBb2D=5t}ZKg)!Vh)p+iuT8S95*WSxxTtc|zj9M=<-R!z}pLCDX3(Fb1j8A#Mg1n>5RJ9yuH)y(1Nx9Y#qsyzs&{lYI?Z#qkH9PiUv0!!?8FpJPN!1tER11UaT0_TYb!mau+zKC(<6nto^a6RVNCm5Uqsug|VdgM^|axzFSU@eI6eec`m4}OpDzULj6EefL1FZ{ywhS3~Q^K$YR;(o{>$>XnI^nq)E#5-ic{#BG^aGvP9uLQ1CaNfT5yO{@268<$mC;>GOkOL<~CL=BHgcd46vMyc`T95=xBU4~MW%3GUVYn9@WSR7!EEsrQi>qnYz}AHeCB_GEzL8U<eRPptnR;<OHWdr;gs}IxOU>0mrHIB<2SMm~AD#VtC~ddv+J%7kX3>sBwD-eG_s`o!tSazy7Mm}knok>AP+pS=_I~)%z<+<b$N9A%!7p^L#J}VDMe^u}{~t-i7Uc')).decode('utf8')


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
