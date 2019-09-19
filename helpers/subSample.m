
function [outRD, outTR] = subSample(RD,TR,factor,nSpokes)

    outTR = TR(:,:,1:factor:nSpokes);
    outRD = RD(:,:,1:factor:nSpokes,:);

end