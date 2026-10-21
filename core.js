(function(root){
'use strict';
const names={M:'Manhattan',B:'Brooklyn',Q:'Queens',X:'Bronx',S:'Staten Island'};
function cutoff(months){const d=new Date(Date.UTC(2026,8+Number(months),23));return d.toISOString().slice(0,10);}
function scope(records,borough,query){const q=query.trim().toUpperCase();return records.filter(r=>(borough==='all'||r.borough===borough)&&(!q||`${r.street} ${r.from} ${r.to}`.includes(q)));}
function stats(records,end){return Object.keys(names).map(b=>{const all=records.filter(r=>r.borough===b);const count=all.reduce((n,r)=>n+(r.end<=end),0);return {borough:b,total:all.length,count,share:count/all.length};});}
function project(point){return [point[0]*Math.cos(40.7*Math.PI/180)*1000,-point[1]*1000];}
function distance(px,py,ax,ay,bx,by){let dx=bx-ax,dy=by-ay;let u=dx*dx+dy*dy?Math.max(0,Math.min(1,((px-ax)*dx+(py-ay)*dy)/(dx*dx+dy*dy))):0;return Math.hypot(px-ax-u*dx,py-ay-u*dy);}
const api={names,cutoff,scope,stats,project,distance};root.StreetCore=api;if(typeof module!=='undefined')module.exports=api;
})(globalThis);
