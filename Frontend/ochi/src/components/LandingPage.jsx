
const LandingPage = () => {
  return (
    <div className="w-full h-screen bg-zinc-900 pt-1">
      <div className="textstructure mt-40 px-20">
        {['We Create', 'Eye-Opening','Presentations'].map((text,index)=>(
            <div key={index} className="masker ">
            <h1 className="uppercase  font-light leading-[7vw] text-9xl font-grotesk">{text}</h1>
          </div>
        ))}
        
      </div>
      <div className="border-t-[1px] border-zinc-700 mt-32">

      </div>
    </div>
  )
}

export default LandingPage