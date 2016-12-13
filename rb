directory=$(pwd)
mkdir BUILD
cd BUILD
mkdir SOURCES
cp ../*gz SOURCES
cp ../*patch SOURCES
rpmbuild --define "_topdir `pwd` " -bs --nodeps  ../$1
cp SRPMS/*.rpm ../
cd ..
rm -rf BUILD
git add *.rpm
git commit -m "New SRPM for $1"
git push
srpm=$(ls *.src.rpm)
copr-cli build KOHAExtra https://raw.githubusercontent.com/FedoraKohaPackages/Copr_SCM/master/$directory/$srpm
