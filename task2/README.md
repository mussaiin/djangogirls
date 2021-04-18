# Frontend and Backend connected via Ingress 

```
cd backend 
scaffold run

cd ..

cd frontend && npm run-script build

cd .. && skaffold run -f skaffold-frontend.yaml

kubectl apply -f ingress-frontend.yaml

curl http://api.sa.homework/health
curl http://api.sa.homework/
curl http://api.sa.homework/kbtu/nurlybek-mussin

```
open [link](http://sa.homework/)