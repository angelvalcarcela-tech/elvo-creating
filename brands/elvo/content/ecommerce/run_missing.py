import sys,threading
sys.path.insert(0,'.')
import gen_ml_nativo_v2 as g
miss=[j for j in g.J if j[0] in ('v2-6b','n2-3','n2-6','n2-7','n2-8')]
ths=[threading.Thread(target=g.call,args=j) for j in miss]; [t.start() for t in ths]; [t.join() for t in ths]
import os
print([j[0] for j in miss if not os.path.exists(g.F+j[0]+'.png')])
