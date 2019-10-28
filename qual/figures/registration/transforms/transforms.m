sqsize = 60;
I = checkerboard(sqsize,4,4);
worldPoints = [
    0 0;
    0 480;
    480 0;
    480 480
];
% I = insertMarker(I, worldPoints, 'o','color','r','size',20);
% imshow(I);
% saveas(gcf,'/home/maksim/dev_projects/phd/qual/figures/registration/transforms/worldpoints.png')

nrows = size(I,1);
ncols = size(I,2);
fill = 1;

imshow(I)
saveas(gcf,'/home/maksim/dev_projects/phd/qual/figures/registration/transforms/original.png')
title('Original')

% Try varying these 4 parameters.
scale = 1.2;       % scale factor
angle = 40*pi/180; % rotation angle
tx = 0;            % x translation
ty = 0;            % y translation

sc = scale*cos(angle);
ss = scale*sin(angle);

T = [ sc -ss  0;
      ss  sc  0;
      tx  ty  1];

t_nonsim = affine2d(T);
I_nonreflective_similarity = imwarp(I,t_nonsim,'FillValues',fill);

imshow(I_nonreflective_similarity);
saveas(gcf,'/home/maksim/dev_projects/phd/qual/figures/registration/transforms/similarity.png')

title('Nonreflective Similarity')

% Try varying the definition of T.
T = [1  1  0;
     -0.3    1  0;
     0    0  1];
t_aff = affine2d(T);
I_affine = imwarp(I,t_aff,'FillValues',fill);

imshow(I_affine)
saveas(gcf,'/home/maksim/dev_projects/phd/qual/figures/registration/transforms/affine.png')

% T = [1  0  0.002;
%      1  1  0.0002;
%      0  0  1   ];
% t_proj = projective2d(T);
% 
% I_projective = imwarp(I,t_proj,'FillValues',fill);
% imshow(I_projective)
% saveas(gcf,'/home/maksim/dev_projects/phd/qual/figures/registration/transforms/projective.png')
% 
% [xi,yi] = meshgrid(1:ncols,1:nrows);
% xt = xi - ncols/2;
% yt = yi - nrows/2;
% [theta,r] = cart2pol(xt,yt);
% a = 1; % Try varying the amplitude of the cubic term.
% rmax = max(r(:));
% s1 = r + r.^3*(a/rmax.^2);
% [ut,vt] = pol2cart(theta,s1);
% ui = ut + ncols/2;
% vi = vt + nrows/2;
% ifcn = @(c) [ui(:) vi(:)];
% tform = geometricTransform2d(ifcn);
% 
% I_barrel = imwarp(I,tform,'FillValues',fill);
% imshow(I_barrel)
% saveas(gcf,'/home/maksim/dev_projects/phd/qual/figures/registration/transforms/barrel.png')
